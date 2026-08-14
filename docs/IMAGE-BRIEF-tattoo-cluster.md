# Image brief — tattoo cluster (for Peter)

**12 images needed. All 12 slots are currently empty**, so the new pages render with a grey
placeholder SVG on `/pages/articles` and `/blogs/guides`, and their `og:image` falls back to the
site default when anyone shares them. Every one of the five pre-existing guides has an image;
none of the seven new ones do.

Raised 2026-08-14. Source of truth for the copy these sit alongside: `docs/tattoo-cluster-content.json`.

---

## Specs

| Slot | Size | Format | Where it appears |
|---|---|---|---|
| Collection hero | **1254 × 1254** (square) | `.webp` | Top of the collection page, `image_ratio: 1 / 1` |
| Page hero | **1254 × 1254** (square) | `.webp` | Top of the guide page, same ratio |
| Article featured | **1600 × 900** (16:9) | `.webp` | Article header, the two hubs, and `og:image` on share |

**Naming:** `senseless-[context]-[descriptor].webp` — the existing convention. Exact filenames are
given per image below; please keep them, the templates reference them by name.

**Delivery:** drop finals into `assets/images/inbox/` and the pipeline handles compression,
upload and alt text (`scripts/image-pipeline.mjs`). Alt text is written for you below — please
use it verbatim, it is part of the compliance surface.

---

## Compliance rules for imagery — these are not stylistic preferences

Senseless is a UK **cosmetic** product, not a medicine. Imagery is a claim surface exactly like
copy is, and MHRA Guidance Note 8 treats *presentation* as the thing that can reclassify a
cosmetic as a medicine. So:

1. **No one in pain, and no one visibly relieved of pain.** No wincing, gritted teeth, gripping
   the chair, comforting hands, exhaling-with-relief. GN8 App.10 specifically warns against
   imagery showing apparent areas of pain. This is the rule most likely to be broken by accident,
   because "tattoo" briefs default to it.
2. **No before/after pairings** of any kind. They imply a medicinal outcome.
3. **No product shown on broken, healing, freshly-tattooed or reddened skin.** The safety warning
   on the numbing range says *"Apply to clean, unbroken skin"* and the imagery must not contradict
   it. The two aftercare products are the exception — they are *for* freshly treated skin — but
   even there, keep the skin calm and healthy-looking, never raw or inflamed.
4. **No needle-in-skin close-ups** that read as a medical procedure. Tattoo machines in a studio
   context are fine; hypodermic needles are not.
5. **No clinical or medical settings** (`docs/BRAND.md:109`). Tattoo studio, yes — warm, considered,
   premium. Treatment room with a paper-covered bed, no.
6. **Products must be shown truthfully.** Correct sizes, correct labels, correct tier colours. Do
   not invent packaging that does not exist. If in doubt, shoot the real thing rather than
   generating it.
7. **No claims rendered as graphics** — no "works in 30 minutes", no percentages, no comparison
   badges, no "strongest".

---

## House style

Editorial, premium, soft warm tones. Natural, unmedicated, female-leaning where people appear —
but the tattoo cluster should skew broader than the rest of the site, because the audience does.
Warm off-white ground `#f7f7f5`. Brand purple `#6B3FA0` for anything that needs an accent; the
asterisk mark is violet `#984AE8`, not the purple — do not swap them.

Visual benchmark: Augustinus Bader, Dieux, Wildsmith Skin, 111SKIN, The Inkey List. Then imagine
those brands photographing a tattoo studio rather than a clinic.

**Negative prompt to append to every generation:**

> `no text, no watermark, no logos, no packaging text, no before/after split, no grimacing, no
> pained expression, no red or inflamed skin, no blood, no hypodermic needles, no medical setting,
> no clinical bed, no gloves-and-mask surgical framing, no stock-photo smiling to camera`

---

# The 12 prompts

## Collection heroes — 1254 × 1254

### 1. `senseless-tattoo-collection-hero.webp`
**Page:** `/collections/numbing-cream-for-tattoos`

> Editorial square still life in a premium tattoo studio at golden hour. A warm off-white
> (#f7f7f5) surface with a soft linen texture, holding a single unbranded cosmetic cream tube and
> a small glass jar, arranged with generous negative space. Behind and softly out of focus: the
> warm brass and dark wood of a considered tattoo studio — a leather chair edge, a rolled towel,
> the suggestion of framed flash art on a wall. Low warm side light, long soft shadows, shallow
> depth of field. Calm, adult, unhurried. Muted palette of bone, warm grey and deep umber with a
> single restrained violet accent. Shot on medium format, 80mm, f/2.8. No people.

**Alt:** `Senseless topical preparation on a warm surface in a tattoo studio setting`

### 2. `senseless-piercing-collection-hero.webp`
**Page:** `/collections/numbing-cream-for-piercings`

> Editorial square still life, quieter and smaller in scale than its tattoo counterpart. A single
> small cosmetic gel tube standing on a warm off-white (#f7f7f5) plinth, with a shallow ceramic
> dish beside it. Background softly blurred: the clean steel and warm wood of a modern piercing
> studio, a hint of a mirror edge, brushed metal jewellery displayed out of focus. Precise,
> minimal, a lot of air around the product — the composition should feel *small and exact* rather
> than dramatic, matching a procedure that lasts seconds. Soft diffused daylight from the left.
> Bone, warm grey, brushed steel, one restrained violet accent. 100mm macro, f/4. No people.

**Alt:** `Senseless gel beside brushed steel in a modern piercing studio setting`

### 3. `senseless-tattoo-aftercare-collection-hero.webp`
**Page:** `/collections/tattoo-aftercare`

> Editorial square still life of an aftercare routine, at home rather than in a studio. On a warm
> off-white (#f7f7f5) bathroom shelf: an unbranded pump-top foaming cleanser bottle and a small
> ointment tube, with a folded clean white cotton cloth and a glass of water. Soft morning
> daylight through frosted glass, gentle steam haze, everything calm and clean. The mood is
> *routine and uneventful* — this is the boring, careful part of getting a tattoo, and it should
> look reassuring rather than clinical. Warm neutrals, soft white, pale wood. 50mm, f/2.8.
> No people, no visible tattoo, no skin.

**Alt:** `Senseless Foaming Cleanser and Vitamin A and D Ointment on a bathroom shelf`

---

## Page heroes — 1254 × 1254

### 4. `senseless-delivery-hero.webp`
**Page:** `/pages/delivery`

> Editorial square still life of a parcel about to be sent. A plain, unbranded kraft or white
> mailer lying flat on a warm off-white (#f7f7f5) surface, with a small cosmetic tube resting
> beside it, and a strip of paper tape. Deliberately anonymous packaging — the page's whole point
> is that parcels are plain and discreet. Soft directional daylight, clean long shadow, generous
> negative space at the top for the headline. Restrained, quiet, premium. Bone, warm grey, kraft.
> 50mm, f/4. No people, no branding, no address label text.

**Alt:** `A plain unbranded Senseless parcel ready for UK delivery`

### 5. `senseless-tktx-hero.webp`
**Page:** `/pages/tktx-numbing-cream-uk`

> Editorial square still life about scrutiny and provenance. On a warm off-white (#f7f7f5)
> surface: a single unbranded cosmetic tube photographed straight on, beside a folded document
> and a pair of reading glasses, as though someone has sat down to check what they are buying.
> Soft even daylight, minimal shadow, very clean and factual — this page is a checklist, not a
> mood piece. No competitor product may appear, and no packaging text of any kind. Bone, warm
> grey, paper white. 60mm, f/5.6. No people.

**Alt:** `A Senseless tube beside paperwork, illustrating what to check before buying`

---

## Article featured images — 1600 × 900

These are the ones that show on `/pages/articles`, on `/blogs/guides`, and as the share image
whenever anyone posts the link. They matter more than their slot suggests.

### 6. `senseless-guide-affect-a-tattoo.webp`
**Article:** *Does Numbing Cream Affect a Tattoo?*

> Wide editorial photograph, 16:9, of a tattoo artist's hands at a workstation between clients —
> arranging equipment on a clean covered tray, unhurried. Warm studio light, dark wood and brass,
> a soft-focus background of the studio. Hands and forearms only, no faces, no client, no skin
> being worked on. The mood is *professional judgement* — this article is about the artist's
> opinion, so the image should centre their craft and their workspace, not a client's experience.
> Shallow depth of field, 35mm, f/2. Muted warm palette.

**Alt:** `A tattoo artist preparing their workstation between clients`

### 7. `senseless-guide-before-a-tattoo.webp`
**Article:** *Can You Use Numbing Cream Before a Tattoo?*

> Wide editorial photograph, 16:9, of a calm studio reception moment before an appointment — a
> booking diary open on a warm wooden counter, a phone face down beside it, a cup of tea, soft
> daylight through a window. No people, or at most an out-of-focus figure in the far background.
> The feeling is *the conversation you have before the day*, which is what the article is about.
> Warm, quiet, adult. 35mm, f/2.8.

**Alt:** `A tattoo studio counter with an open booking diary before an appointment`

### 8. `senseless-guide-artists-use.webp`
**Article:** *Do Tattoo Artists Use Numbing Cream?*

> Wide editorial photograph, 16:9, of two tattoo artists in conversation across a studio — mid
> discussion, relaxed, professional, one gesturing. Shot from a respectful distance, faces soft or
> turned, no client present, no tattooing in progress. Warm studio interior, dark wood, plants,
> framed flash art out of focus. The article is about a profession disagreeing with itself, so the
> image should read as *two practitioners talking shop*. 50mm, f/2.

**Alt:** `Two tattoo artists in conversation in a studio`

### 9. `senseless-guide-tell-your-artist.webp`
**Article:** *What to Tell Your Artist About Numbing Cream*

> Wide editorial photograph, 16:9, of a phone on a warm off-white surface showing a blank message
> compose screen — screen readable as an interface but with no legible text — beside a studio
> business card and a set of keys. Soft daylight. The article is literally a script for a message
> you send at booking, so the image should be *the moment before you send it*. Clean, modern,
> minimal. 50mm, f/4. No people.

**Alt:** `A phone on a desk ready to message a tattoo studio before an appointment`

### 10. `senseless-guide-where-to-buy.webp`
**Article:** *Where to Buy Numbing Cream for Tattoos in the UK*

> Wide editorial photograph, 16:9, of a considered online purchase — a laptop at an angle on a
> warm wooden table with the screen out of focus and unreadable, a plain unbranded parcel beside
> it, a cup of coffee, soft morning light. The article is about checking who you are buying from,
> so the mood is *diligence, not urgency*. No visible brand names, no readable screen content,
> no logos. 35mm, f/2.8.

**Alt:** `Checking a numbing cream order at home before buying`

### 11. `senseless-guide-aftercare-48-hours.webp`
**Article:** *Tattoo Aftercare: The First 48 Hours*

> Wide editorial photograph, 16:9, of clean aftercare supplies laid out on a warm off-white
> surface: folded white cotton cloth, an unbranded pump bottle, a small tube, a fresh roll of
> paper towel. Soft even daylight, calm and hygienic without being clinical. **No skin and no
> tattoo visible** — the article covers a wound-care window and the imagery must stay away from
> it entirely. Warm neutrals, soft white. 50mm, f/4.

**Alt:** `Clean tattoo aftercare supplies laid out on a warm surface`

### 12. `senseless-guide-healing-stages.webp`
**Article:** *Tattoo Healing Stages, Day by Day*

> Wide editorial photograph, 16:9, suggesting the passage of time without showing healing skin.
> A warm off-white surface with soft daylight moving across it, a small unbranded ointment tube,
> and a simple open notebook or wall calendar softly out of focus — days passing, quietly. The
> article is a timeline, so the image should express *patience*. **Absolutely no skin, no tattoo,
> no scabbing, no redness** — this is the highest-risk brief in the set for accidentally producing
> something that reads as a medical image. 50mm, f/2.8. No people.

**Alt:** `A calendar and aftercare ointment, illustrating tattoo healing over time`

---

## Two notes for whoever generates these

**Consistency matters more than individual quality.** These twelve will be seen next to each
other on `/pages/articles` and in the collection nav. One image in a different colour temperature
or focal length will look like a mistake. Generate them as a set, in one session, with the same
lighting and palette language.

**The three highest-risk briefs are 11, 12 and 3** — anything touching aftercare. The default
output for "tattoo healing" is inflamed skin, and that is exactly the image we cannot publish.
If a generation drifts that way, do not try to correct it in post; re-prompt away from skin
entirely.
