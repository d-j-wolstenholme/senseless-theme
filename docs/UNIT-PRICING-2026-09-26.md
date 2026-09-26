# Unit pricing for small products: is there a caveat? (26 Sep 2026)

**Question (founder, 26 Sep 2026):** big sellers show per 100 g or per gram on Google Shopping. Surely there's a caveat that lets us show a
sensible unit price in Merchant Center for 10 g–35 ml products, instead of "£1,999.00/kg"?

**Method:** a research workflow on 26 Sep 2026 (Claude Code, Mac mini) with four independent angles:
- the full revised law text on legislation.gov.uk;
- official guidance, industry bodies and enforcement;
- 30+ live retailer displays, on their own sites and on Google Shopping;
- Google and Shopify mechanics.

Then an advocate (building the strongest lawful case *for* a smaller unit) and a skeptic (refuting every claim) each re-read the primary
sources themselves. The skeptic re-observed 14 retailer displays.

**Verdict:** confidence high. No caveat allows a smaller unit instead of per kg / litre. The only flexibility is an **additional**
friendlier figure on our own website. Decisions log: `DECISIONS-LOG.md` 2026-09-26.

## 1) The straight answer

Yes, this has been researched properly. Two separate checks re-read the law, the government guidance and Google's rules, and looked at more than 30 live retailer pages. There is **no caveat that lets us show per 100 g, per 10 g or per gram instead of per kg / per litre** for our 10 g–35 ml products. Cosmetics did have one (per 100 g), but it was removed on 6 April 2026.

There is one real, smaller caveat. On our own website we may show a friendlier figure such as "£2.00/g" **next to** the per-kg figure. Google only accepts one figure per product, though, so on Shopping it has to be per kg / per litre.

The big retailers do exactly what we do. Boots shows EMLA 30 g as "£933.00 per 1KG", and Tesco shows 1 g of chives as "£2,000.00/kg". The per-gram cards you saw come from smaller pharmacies' Google feeds, and those same sellers show no unit price on their own sites. EMLA's manufacturer doesn't sell to the public, so it isn't the one choosing those figures.

## 2) The evidence

**The law (Great Britain, from 6 April 2026).** Source: Price Marking Order 2004 as amended, https://www.legislation.gov.uk/uksi/2004/102/data.xml (revised text, updated 18 May 2026).
- For weight-marked goods the unit price is: *"for one kilogram of the product, where the product is permitted to be sold either by weight or by volume, and the product is marked to show only its weight"*. Volume-marked goods use per litre in the same way.
- The old cosmetics rule ("Cosmetic products other than make-up products 100") is recorded as *"Sch. 1 omitted (6.4.2026)"*.
- A small-item exception was floated in January 2024 (*"for example, for low weight/volume products"*) but never adopted. No later Price Marking order exists as at 26 Sep 2026.
- The government knew smaller units read better and chose per kg anyway. Its Impact Assessment (para 108) gives herbs moving from per 10 g to per kg as an example.
- None of the escape routes applies to our single products:
  - Every pack from 5 g/ml to 25 kg/l must be quantity-marked, which switches the duty on.
  - There is no medicines carve-out, so EMLA sellers are in the same position as us.
  - The "small shop" exemption depends on a physical shop's floor area (280 m² or less), and the government says online sales are in scope.

**Official guidance.** DBT guidance, 22 Sep 2025: https://www.gov.uk/government/publications/price-marking-order-2004-government-guidance/price-marking-order-2004-government-guidance
- Para 16: *"Whether displayed in weight or volume, the label must show the unit price per kilogram or litre as applicable."*
- Para 34: selling and unit prices are *"always required (notwithstanding any other exemptions) when the advertisement is actually inviting consumers to conclude a distance contract"*. Its examples include goods sold direct from the Internet, so a priced Shopping card that links to buy is covered.
- Para 47(d): the unit price *"may be a smaller size than the selling price"*.
- Trading Standards' Business Companion (April 2026) says the per 100 g and per 10 g units ended on 6 April 2026.

**The one genuine caveat.** Impact Assessment 2024/154, para 49, signed 21 Oct 2024 (https://www.legislation.gov.uk/ukia/2024/154/pdfs/ukia_20240154_en.pdf): retailers *"will be free to use alternative unit pricing metrics in addition to their legal requirement to unit price by kilogram or litre."*
- It is not law, but it states the government's intent. Nothing in the Order forbids an extra figure.
- It works only as an addition, and only where there is room for two figures: our website.

**What big retailers show now** (own websites, 26 Sep 2026):

| Retailer | Product | Unit price shown |
|---|---|---|
| Boots | EMLA 30 g, £27.99 | "£933.00 per 1KG" |
| Tesco | Saffron 0.4 g, £4.50 | "£11,250.00/kg" |
| Tesco | Chives 1 g, £2.00 | "£2,000.00/kg" |
| Sainsbury's | Nivea eye cream 15 ml | "£1,000.00 / ltr" |
| Superdrug | Own-brand eye cream 15 ml | "£333.33 per 1l" |
| Holland & Barrett (own stock) | Carmex 10 g | "£359.00/1 kg" |

ASDA, Ocado and Iceland also price small items per kg on their own sites. Amazon is inconsistent, even on items it sells itself (Nivea 15 ml per 100 ml, INKEY 15 ml per litre). In 2023 the competition regulator (CMA) recorded that supermarkets used per 100 g where the law required per kg. Big firms do get this wrong.

**Why the Shopping results look so messy:**
- The per-kg rule for cosmetics is under six months old. Until 5 April, per 100 g was lawful for cosmetics, and many feeds haven't been updated.
- Most sellers show no unit price at all. That is non-compliance, not an exemption.
- Some cards are simply wrong:
  - Amazon's TKXK card reads "£14,990.00/100g".
  - PillSorted's "6 x Emla 5g £22.49" card reads "£4.50/1g"; the true figure is about £0.75/g.

One earlier theory was that packaged cosmetics fell outside the duty from 2013 to 2026. The second check found that Trading Standards guidance treated cosmetics as in scope in December 2025, so the evidence points against that theory. It doesn't matter now either way.

**How Google handles it:**
- **Any base is accepted.** Google takes a base of 1, 10, 100, 2, 4 or 8 with g, ml, kg or l. Its only UK rule is to use metric units (https://support.google.com/merchants/answer/6324490).
- **Only one base per product** ("Repeated field: No").
- **The legal risk is ours.** Google says *"you, as the merchant, are legally liable"* (answer 10009686).
- **No workaround through the text fields.** Google bans price information in the title, description, highlights and product details, so we can't add "£2/g" there.
- **Google won't fix it for us.** Google says a product *"might show a different base measure"*, but it did not do that for us.
- **Correction to our own record.** On 26 Sep our **sponsored** cards *did* show a unit price: "Clinical Strength Cream 10g £19.99 … £1,999.00/1kg" and "Advanced Strength Cream 10g £24.99 … £2,499.00/1kg". Free (unpaid) listings showed no unit price for any seller, us included; that is Google's choice. So the line in the 26 Sep decisions log saying our cards show no unit price is wrong and needs correcting.

## 3) The options

| Option | What a shopper sees | Legal position | Realistic risk | Who decides |
|---|---|---|---|---|
| **A. Keep per kg / litre in the feed** (current) | Ad card: "£19.99 · £1,999.00/1kg" | Lawful. It is the required unit. High confidence. | No legal risk. It looks odd, but the same as Boots and Tesco. | Already in place. **Recommended.** |
| **B. A plus a per-gram figure next to per kg on senseless.uk** | Product page: "£19.99", then smaller "£1,999.00/kg (£2.00/g)". The 30 g cream would read £1,499.67/kg (£1.50/g). | Not barred by the Order, and the Impact Assessment says it is intended to be allowed. Medium confidence. Keep per kg at least as prominent, on the same line. | Low. It also closes a bigger gap: the site hides unit prices today (22 Sep Decision 5), and the rules apply to our product pages directly. | **Founder** (reverses 22 Sep Decision 5). **Recommended.** |
| **C. Switch the feed base to 100 g / 100 ml** | Card: "£199.90/100g" | Not the required unit in Great Britain since 6 Apr 2026. High confidence it is non-compliant. | Criminal offence (unlimited fine) and civil fines up to £300k or 10% of turnover. No unit-pricing enforcement found since April, but that is not permission. Choosing it after this advice likely weakens any "due diligence" defence (my interpretation). | **Founder/legal**. Not recommended. |
| **D. Drop unit pricing from the feed for single products** | Card: price only, like most competitors | Not compliant for a priced listing (order art. 5(4); DBT para 34). High confidence on the text; untested whether a Google card counts as our own price display. | Same legal exposure as C. Google's "Missing unit pricing measure" warning returns on every product; Google calls it advisory. | **Founder/legal**. Not recommended. |
| **E. Kits and the bag: no unit price** | Kit price only | Lawful. Mixed kits (g + ml, bundle price) are exempt under Schedule 2 para 3, and the bag isn't quantity-marked. High confidence. The live kit data already carries no unit price. | None. If the per-kg figure hurts clicks, ad spend could lean towards kits. | Marketing call (founder). |
| **F. A "cream + dressings" pack** (how Boots' EMLA 5 g packs appear to avoid a unit price) | No unit price on that pack | Might count as an exempt assortment. Boots' reasoning is our inference. Low confidence, and it could look like a sham. | Product, CPSR and SKU work. Untested. | **Founder/legal**. Only with Trading Standards advice. |

**Ruled out:**
- Northern Ireland's order (still per 100 g), because it covers NI only.
- The small-shop exemption, because it depends on floor area.
- Pricing "per tube", because our packs are sold by weight or volume.
- Putting "£2/g" in the Google title or description, because Google bans prices there.
- Hoping Google rescales our figure, because it hasn't.

**One loose end:** the Vitamin A&D 4-pack is set to 50p per item. That is fine if each tube is sold by number or is under 5 g. The tube size hasn't been checked.

## 4) What would settle the remaining doubt

Only option B's fine print is uncertain (the per-gram figure next to per kg, and how prominent each should be). DBT guidance para 68 says *"Enquiries about provisions of the PMO 2004 may be addressed to your local trading standards department"*. For us that is Lancashire Trading Standards. A short email would do:

> "We sell cosmetic creams (10 g, 30 g) and gels/sprays (15–35 ml) online only. Since 6 April 2026 we unit-price per kg / per litre. Please confirm: (1) we may also show a per-gram figure beside it on product pages, e.g. '£1,999.00/kg (£2.00/g)', with per kg at least as prominent; (2) our kits, which mix g and ml items at a bundle price, are exempt under Schedule 2 para 3; (3) our Google Shopping listings should carry per kg / per litre."

Other routes:
- **Primary Authority.** For advice other councils must respect, a Primary Authority partnership gives *"assured and tailored advice … that other local regulators must respect"* (Regulatory Enforcement and Sanctions Act 2008 s.28; it is usually paid).
- **CTPA.** If Matrix Health Group is a member of the CTPA (the cosmetics trade body), its members-only price-marking guidance is worth a read.
- **No point asking** whether per 100 g alone is allowed. Nothing short of a new Order would make it lawful.

## Sources fetched (26 Sep 2026)

```
Fetched 26 Sep 2026 (curl, HTTP 200 for all). Local raw file -> URL
pmo-2004-102-current.xml/.txt        https://www.legislation.gov.uk/uksi/2004/102/data.xml  (revised text, dc:modified 2026-05-18)
pmo-2004-102-asat-2026-04-05.xml/.txt https://www.legislation.gov.uk/uksi/2004/102/2026-04-05/data.xml
pgr-2006-659-current.xml/.txt        https://www.legislation.gov.uk/uksi/2006/659/data.xml
prices-act-1974.xml/.txt             https://www.legislation.gov.uk/ukpga/1974/24/data.xml
tda-1968-s24.xml/.txt                https://www.legislation.gov.uk/ukpga/1968/29/section/24/data.xml
wma-1985-sch6.xml/.txt               https://www.legislation.gov.uk/ukpga/1985/72/schedule/6/data.xml
ni-pmo-2004-368.xml/.txt             https://www.legislation.gov.uk/nisr/2004/368/data.xml
ni-wm-order-1981-partVI.xml          https://www.legislation.gov.uk/nisi/1981/231/part/VI/data.xml
resa-2008-s27.xml, s28.xml           https://www.legislation.gov.uk/ukpga/2008/13/section/27|28/data.xml
lg-search-price-marking.html         https://www.legislation.gov.uk/all?title=price%20marking&sort=year&results-count=50
lg-search-ukdsi-price.html           https://www.legislation.gov.uk/ukdsi?title=price&sort=year
ia-2024-154.pdf/.txt                 https://www.legislation.gov.uk/ukia/2024/154/pdfs/ukia_20240154_en.pdf
em-2024-1055.pdf/.txt                https://www.legislation.gov.uk/uksi/2024/1055/pdfs/uksiem_20241055_en_001.pdf
em-2025-592.pdf/.txt                 https://www.legislation.gov.uk/uksi/2025/592/pdfs/uksiem_20250592_en_001.pdf
dbt-pmo-guidance.html/.txt           https://www.gov.uk/government/publications/price-marking-order-2004-government-guidance/price-marking-order-2004-government-guidance
gov-response-2024-01.html/.txt       https://www.gov.uk/government/consultations/smarter-regulation-improving-price-transparency-and-product-information-for-consumers/outcome/government-response-to-consultation-on-smarter-regulation-improving-consumer-price-transparency-and-product-information-for-consumers
gov-primary-authority.html/.txt      https://www.gov.uk/guidance/local-regulation-primary-authority
cma-unit-pricing-2023.pdf/.txt       https://assets.publishing.service.gov.uk/media/64b80ab1ef5371000d7aeefa/CMA_Review_of_unit_pricing_in_the_groceries_sector.pdf
bc-providing-price-information.html/.txt https://www.businesscompanion.info/en/quick-guides/pricing-and-payment/providing-price-information
liverpool-ts-price-advice.html/.txt  https://liverpool.gov.uk/business/trading-standards/trading-and-consumer-advice/trade-advice-document?Id=15452&DocId=122626&CatId=4
freeths-horizon.html/.txt            https://www.freeths.co.uk/horizon-scanner/commercial/
gmc_<id>_en-GB.html/.txt             https://support.google.com/merchants/answer/<id>?hl=en-GB  (6324490, 6324455, 10009686, 9216100, 6324415, 6324468, 7052112, 9218260)
```
