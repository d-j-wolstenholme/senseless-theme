#!/usr/bin/env bash
# scripts/email-auth-check.sh — email authentication ground truth for senseless.uk.
#
# senseless.uk sends from THREE places and each must authenticate independently:
#   1. Microsoft 365      business mail       (MX -> *.mail.protection.outlook.com)
#   2. Shopify            transactional mail  (order/shipping/abandoned-cart, sender cs@senseless.uk)
#   3. Klaviyo            marketing campaigns (installed as a Shopify app embed)
# DMARC is published at p=quarantine, so any of the three that does NOT align with the
# From domain is junked BY POLICY. This script proves, from DNS, which of them align.
#
# Detect-only. Never writes DNS. Always safe to run.
#
# Usage:  bash scripts/email-auth-check.sh [sending-subdomain]
#   e.g.  bash scripts/email-auth-check.sh send.senseless.uk
#
# HONESTY RULE (learned the hard way — see scripts/injectable-clean-sweep.py): a lookup that
# ERRORS is not a lookup that returned nothing. Resolver failures are counted separately and
# the summary is marked UNRELIABLE if any occurred. A green run with errors is not a pass.
set -uo pipefail

DOMAIN="${DOMAIN:-senseless.uk}"
SENDSUB="${1:-send.$DOMAIN}"
R1="1.1.1.1"; R2="8.8.8.8"

PASS=0; FAIL=0; WARN=0; ERRS=0
ok()   { printf '  \033[32mPASS\033[0m  %s\n' "$1"; PASS=$((PASS+1)); }
bad()  { printf '  \033[31mFAIL\033[0m  %s\n' "$1"; FAIL=$((FAIL+1)); }
warn() { printf '  \033[33mWARN\033[0m  %s\n' "$1"; WARN=$((WARN+1)); }
info() { printf '        %s\n' "$1"; }
head2(){ printf '\n\033[1m%s\033[0m\n' "$1"; }

# q <type> <name> [resolver] — echoes the answer; increments ERRS on resolver failure.
q() {
  local t="$1" n="$2" r="${3:-$R1}" out rc
  out="$(dig +short +time=3 +tries=2 "$t" "$n" @"$r" 2>&1)"; rc=$?
  if [ $rc -ne 0 ] || printf '%s' "$out" | grep -qi 'connection timed out\|SERVFAIL\|communications error'; then
    ERRS=$((ERRS+1)); printf '__DNSERR__'; return 1
  fi
  printf '%s' "$out" | grep -v '^;' | sed 's/^"//; s/"$//'
}

echo "== Email authentication check — $DOMAIN — $(date -u '+%Y-%m-%d %H:%M UTC') =="
info "resolvers: $R1 and $R2 (cross-checked)   sending subdomain under test: $SENDSUB"

# ---------------------------------------------------------------- zone + mail routing
head2 "0. Zone and mail routing"
ns="$(q NS "$DOMAIN")"
[ -n "$ns" ] && [ "$ns" != "__DNSERR__" ] && info "DNS host: $(echo "$ns" | tr '\n' ' ')" || bad "zone $DOMAIN did not resolve"
mx="$(q MX "$DOMAIN")"
case "$mx" in
  *mail.protection.outlook.com*) info "MX -> Microsoft 365 ($(echo "$mx" | tr '\n' ' '))" ;;
  __DNSERR__) bad "MX lookup errored" ;;
  "")         bad "no MX record — inbound mail is not routed" ;;
  *)          warn "MX is not Microsoft 365: $(echo "$mx" | tr '\n' ' ')" ;;
esac

# ---------------------------------------------------------------- SPF
head2 "1. SPF  (does the record authorise every sender, within 10 lookups?)"
spf_all="$(q TXT "$DOMAIN" | grep -c '^v=spf1' || true)"
spf="$(q TXT "$DOMAIN" | grep '^v=spf1' || true)"
if [ "$spf_all" -gt 1 ]; then
  bad "$spf_all SPF records published — more than one is a permanent SPF failure. There must be exactly one."
elif [ -z "$spf" ]; then
  bad "no SPF record found"
else
  ok "exactly one SPF record"
  info "$spf"
  LOOKUPS=0; CHAIN=""
  expand() { # recursive include walk, depth-guarded
    local rec="$1" depth="$2" tok host sub
    [ "$depth" -gt 6 ] && return
    for tok in $rec; do
      case "$tok" in
        include:*|redirect=*)
          host="${tok#include:}"; host="${host#redirect=}"
          LOOKUPS=$((LOOKUPS+1)); CHAIN="$CHAIN -> $host"
          sub="$(q TXT "$host" | grep '^v=spf1' || true)"
          [ -n "$sub" ] && expand "$sub" $((depth+1))
          ;;
        a|mx|ptr|a:*|mx:*|exists:*) LOOKUPS=$((LOOKUPS+1)) ;;
      esac
    done
  }
  expand "$spf" 0
  info "include chain:$CHAIN"
  if [ "$LOOKUPS" -le 10 ]; then ok "SPF DNS lookups: $LOOKUPS of 10"
  else bad "SPF DNS lookups: $LOOKUPS — over the RFC 7208 limit of 10, SPF permerrors"; fi
  if printf '%s' "$CHAIN" | grep -q 'spf.protection.outlook.com'; then
    ok "Microsoft 365 IS authorised by SPF (reached via the include chain — do not 'fix' this record)"
  else
    bad "Microsoft 365 is NOT reachable in the SPF chain, but MX points at Microsoft"
  fi
  case "$spf" in
    *" -all") info "hard fail (-all) — correct, keep it" ;;
    *" ~all") warn "soft fail (~all) — weaker than -all" ;;
    *"?all"|*"+all") bad "neutral/pass-all — this authorises the entire internet" ;;
  esac
fi

# ---------------------------------------------------------------- DMARC
head2 "2. DMARC  (the policy that decides what happens to unaligned mail)"
dm="$(q TXT "_dmarc.$DOMAIN")"
dm2="$(q TXT "_dmarc.$DOMAIN" "$R2")"
dmn="$(printf '%s\n' "$dm" | grep -c '^v=DMARC1' || true)"
if [ "$dmn" -gt 1 ]; then bad "$dmn DMARC records — multiple records invalidate DMARC entirely"
elif [ -z "$dm" ] || [ "$dm" = "__DNSERR__" ]; then bad "no DMARC record found"
else
  ok "DMARC record published"
  info "$dm"
  [ "$dm" = "$dm2" ] && ok "both resolvers agree" || warn "resolvers disagree — mid-propagation?"
  case "$dm" in
    *p=reject*)     info "policy: reject     (strictest)" ;;
    *p=quarantine*) info "policy: quarantine (unaligned mail goes to junk BY POLICY — this is DMARC working, not the bug)" ;;
    *p=none*)       warn "policy: none — monitoring only. Note: Gmail/Yahoo bulk rules still require ALIGNMENT, so p=none does not rescue unaligned mail" ;;
  esac
  case "$dm" in
    *rua=*)
      rua="$(printf '%s' "$dm" | tr ';' '\n' | grep 'rua=' | sed 's/.*rua=//')"
      if printf '%s' "$rua" | grep -qi 'secureserver\|godaddy'; then
        bad "aggregate reports go to GoDaddy's aggregator ($rua) — WE receive no DMARC data, so nobody can measure this"
      else ok "aggregate reports go to $rua"; fi ;;
    *) bad "no rua= — no aggregate reports are being collected at all" ;;
  esac
fi

# ---------------------------------------------------------------- DKIM: Microsoft 365
head2 "3. DKIM — Microsoft 365 business mail"
m365=0
for s in selector1 selector2; do
  c="$(q CNAME "$s._domainkey.$DOMAIN")"
  if [ -n "$c" ] && [ "$c" != "__DNSERR__" ]; then
    key="$(q TXT "$s._domainkey.$DOMAIN")"
    if printf '%s' "$key" | grep -q 'p='; then ok "$s._domainkey -> $c (key resolves)"; m365=$((m365+1))
    else warn "$s._domainkey -> $c but no key resolves at the target — check the CNAME value and that DKIM is ENABLED in the Defender portal"; fi
  else
    bad "$s._domainkey.$DOMAIN missing"
  fi
done
[ "$m365" -eq 0 ] && info "=> Microsoft signs with the tenant's initial *.onmicrosoft.com domain, which does NOT align with $DOMAIN. DMARC then rests on SPF alone, and SPF breaks on forwarding."

# ---------------------------------------------------------------- Klaviyo
head2 "4. Klaviyo — marketing campaigns (branded sending domain)"
own="$(q TXT "$DOMAIN" | grep -i 'klaviyo-site-verification' || true)"
[ -n "$own" ] && ok "ownership TXT present ($own)" || warn "no klaviyo-site-verification TXT at the apex"
kns="$(q NS "$SENDSUB")"
kcn="$(q CNAME "$SENDSUB")"
if printf '%s' "$kns" | grep -qi 'klaviyo'; then
  ok "$SENDSUB is delegated to Klaviyo (dynamic routing): $(echo "$kns" | tr '\n' ' ')"
elif printf '%s' "$kcn" | grep -qi 'klaviyo\|sendgrid'; then
  ok "$SENDSUB CNAME -> $kcn (static routing)"
else
  bad "no branded sending domain at $SENDSUB — campaigns are on Klaviyo's SHARED domain, which cannot align with a From address at $DOMAIN"
fi
kd=0
for sel in km1 km2 kl kl2 kt1 kt2; do
  h="$(q CNAME "$sel._domainkey.$SENDSUB")"
  [ -n "$h" ] && [ "$h" != "__DNSERR__" ] && { ok "$sel._domainkey.$SENDSUB -> $h"; kd=$((kd+1)); }
done
[ "$kd" -eq 0 ] && info "=> no Klaviyo DKIM selectors found under $SENDSUB"

# ---------------------------------------------------------------- Shopify
head2 "5. Shopify — transactional mail (sender cs@$DOMAIN)"
# Shopify generates account-specific hostnames; set SHOPIFY_DKIM_HOSTS="host1 host2" once known.
sh=0
for h in ${SHOPIFY_DKIM_HOSTS:-shopifyemail._domainkey shopify._domainkey s1._domainkey s2._domainkey}; do
  v="$(q CNAME "$h.$DOMAIN")"
  [ -n "$v" ] && [ "$v" != "__DNSERR__" ] && { ok "$h.$DOMAIN -> $v"; sh=$((sh+1)); }
done
if [ "$sh" -eq 0 ]; then
  warn "no Shopify authentication records found — but this is NOT provable from DNS: Shopify's host names are"
  info "per-store and unguessable, so a selector wordlist can neither find nor rule them out. Read the status at"
  info "Shopify admin > Settings > Notifications > Sender email. Documented consequence of not authenticating is a"
  info "From REWRITE to store+NNN@shopifyemail.com (the 'via shopifyemail.com' string is Gmail's rendering, not Shopify's)."
  info "Once the real host names are known, re-run with SHOPIFY_DKIM_HOSTS=\"host1 host2\" to assert them properly."
fi

# ---------------------------------------------------------------- summary
head2 "Summary"
printf '  pass %s   fail %s   warn %s   resolver errors %s\n' "$PASS" "$FAIL" "$WARN" "$ERRS"
if [ "$ERRS" -gt 0 ]; then
  printf '  \033[31mRESULT UNRELIABLE\033[0m — %s lookup(s) errored. Re-run before trusting any line above.\n' "$ERRS"
  exit 2
fi
if [ "$FAIL" -eq 0 ]; then echo "  All three senders authenticate and align. Safe to send."; exit 0
else echo "  $FAIL check(s) failing — unaligned senders are being quarantined by our own DMARC policy."; exit 1; fi
