#!/usr/bin/env python3
"""Senseless: Google Merchant API client (Merchant Center account 5805726847).

READ-ONLY except `register` (one-time developer registration). Shipping writes will be a separate,
reviewed --apply step, because the Shopify Google & YouTube app also writes these shipping settings.

Setup (once): a Google Cloud project with the Merchant API enabled, a service account with a JSON
key saved at .secrets/merchant-service-account.json (git-ignored), and that service account's email
added in Merchant Center > Settings > Access and services > People and access, with ADMIN access.

Usage (the repo's git-ignored venv has google-auth):
  .venv/bin/python scripts/merchant-api.py check                  # key loads, account reachable?
  .venv/bin/python scripts/merchant-api.py register you@gmail.com  # one-time: register GCP project
  .venv/bin/python scripts/merchant-api.py shipping [--json]      # delivery policies: rates, cut-off, handling
  .venv/bin/python scripts/merchant-api.py products [--json]      # items: price, GTIN, status, issues
"""
import json
import os
import sys

ACCOUNT = "5805726847"
KEY = os.path.join(os.path.dirname(__file__), "..", ".secrets", "merchant-service-account.json")
SCOPES = ["https://www.googleapis.com/auth/content"]
BASE = "https://merchantapi.googleapis.com"
VERSIONS = ("v1", "v1beta")  # v1 first; fall back if a sub-API is still beta-only


def session():
    try:
        from google.oauth2 import service_account
        from google.auth.transport.requests import AuthorizedSession
    except ImportError:
        sys.exit("Run with the repo venv: .venv/bin/python scripts/merchant-api.py …")
    if not os.path.exists(KEY):
        sys.exit(f"No key at {os.path.normpath(KEY)}. Save the service-account JSON key there.")
    creds = service_account.Credentials.from_service_account_file(KEY, scopes=SCOPES)
    return AuthorizedSession(creds), creds.service_account_email


def call(s, method, api, path, body=None):
    last = None
    for v in VERSIONS:
        url = f"{BASE}/{api}/{v}/{path}"
        r = s.request(method, url, json=body, timeout=60)
        if r.status_code == 404 and v != VERSIONS[-1]:
            last = r
            continue
        if not r.ok:
            try:
                err = r.json().get("error", {})
            except ValueError:
                err = {"message": r.text[:300]}
            sys.exit(f"{method} {api}/{v}/{path} -> HTTP {r.status_code}: {err.get('status', '')} {err.get('message', '')}")
        return r.json() if r.text else {}
    sys.exit(f"{method} {path}: not found in {VERSIONS} (last HTTP {last.status_code if last else '?'})")


def money(m):
    if not m:
        return None
    units = int(m.get("amountMicros", 0)) / 1_000_000
    return f"£{units:.2f}" if m.get("currencyCode", "GBP") == "GBP" else f"{units:.2f} {m.get('currencyCode')}"


def cmd_check(s, sa):
    acc = call(s, "GET", "accounts", f"accounts/{ACCOUNT}")
    print(f"service account: {sa}")
    print(f"account: {acc.get('accountName')} ({acc.get('name')}) | time zone: {acc.get('timeZone', {}).get('id')} | language: {acc.get('languageCode')}")


def cmd_register(s, sa, email):
    out = call(s, "POST", "accounts", f"accounts/{ACCOUNT}/developerRegistration:registerGcp", {"developerEmail": email})
    print("registered:", json.dumps(out, indent=1))


def cmd_shipping(s, sa, as_json):
    ss = call(s, "GET", "accounts", f"accounts/{ACCOUNT}/shippingSettings")
    if as_json:
        print(json.dumps(ss, indent=1))
        return
    print(f"etag: {ss.get('etag')}")
    for svc in ss.get("services", []):
        dt = svc.get("deliveryTime", {})
        cut = dt.get("cutoffTime") or {}
        cut_s = f"{cut.get('hour', 0):02d}:{cut.get('minute', 0):02d} {cut.get('timeZone', '(no tz)')}" if cut else "none"
        print(f"\n- {svc.get('serviceName')} | active={svc.get('active')} | {svc.get('deliveryCountries')} {svc.get('currencyCode')}")
        print(f"    handling {dt.get('minHandlingDays')}-{dt.get('maxHandlingDays')} d, transit {dt.get('minTransitDays')}-{dt.get('maxTransitDays')} d, cut-off {cut_s}")
        if svc.get("minimumOrderValue"):
            print(f"    minimum order value: {money(svc['minimumOrderValue'])}")
        for rg in svc.get("rateGroups", []):
            if rg.get("singleValue"):
                v = rg["singleValue"]
                print(f"    rate: {money(v.get('flatRate')) or ('no delivery' if v.get('noShipping') else v)}")
            if rg.get("mainTable"):
                t = rg["mainTable"]
                heads = [h for h in (t.get("rowHeaders", {}).get("prices") or [])]
                rows = t.get("rows", [])
                for h, row in zip(heads, rows):
                    cell = (row.get("cells") or [{}])[0]
                    val = money(cell.get("flatRate")) or ("no delivery" if cell.get("noShipping") else cell)
                    print(f"    up to {money(h) if h.get('amountMicros') else 'infinity'}: {val}")


def cmd_products(s, sa, as_json):
    items, token = [], None
    while True:
        q = "pageSize=250" + (f"&pageToken={token}" if token else "")
        page = call(s, "GET", "products", f"accounts/{ACCOUNT}/products?{q}")
        items += page.get("products", [])
        token = page.get("nextPageToken")
        if not token:
            break
    if as_json:
        print(json.dumps(items, indent=1))
        return
    print(f"{len(items)} items")
    for p in items:
        a = p.get("productAttributes") or p.get("attributes") or {}
        st = p.get("productStatus") or {}
        dests = ",".join(f"{d.get('reportingContext')}:{'ok' if d.get('approvedCountries') else 'x'}" for d in st.get("destinationStatuses", []))
        issues = "; ".join(sorted({i.get("description") or i.get("code", "") for i in st.get("itemLevelIssues", [])}))
        gtin = a.get("gtins") or a.get("gtin")
        print(f"- {p.get('offerId'):<28} {str(a.get('title'))[:40]:<40} {money(a.get('price'))} "
              f"gtin={gtin} unit={a.get('unitPricingMeasure')} | {dests} | {issues}")


def main():
    if len(sys.argv) < 2 or sys.argv[1] not in ("check", "register", "shipping", "products"):
        sys.exit(__doc__)
    s, sa = session()
    cmd, as_json = sys.argv[1], "--json" in sys.argv
    if cmd == "check":
        cmd_check(s, sa)
    elif cmd == "register":
        if len(sys.argv) < 3 or "@" not in sys.argv[2]:
            sys.exit("usage: register you@example.com  (a Google account email that can sign in to Merchant Center)")
        cmd_register(s, sa, sys.argv[2])
    elif cmd == "shipping":
        cmd_shipping(s, sa, as_json)
    else:
        cmd_products(s, sa, as_json)


if __name__ == "__main__":
    main()
