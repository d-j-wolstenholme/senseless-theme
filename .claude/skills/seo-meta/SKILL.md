---
name: seo-meta
description: Use this skill when generating SEO meta title and meta description for a page. Produces meta title under 60 characters and meta description under 155 characters, using the primary keyword for the page and complying with UK compliance rules (no "numbing" used as a claim, only as a category term). Trigger phrases include "write meta for [page]", "SEO meta for [page]", or as part of /build-page.
---

# SEO Meta

## When to Use

- Brief is loaded for a page and meta needs to be generated
- User asks for meta title or description
- /build-page workflow reaches the SEO step

## Inputs

- **Primary keyword** (required) — from the page brief
- **Page purpose** (required) — what the page is for
- **Brand** (defaults to "Senseless")

## Process

1. Generate meta title:
   - Format: `[Primary keyword] · [Differentiator] | Senseless`
   - Max 60 characters
   - Front-load the keyword
   - Use "·" or "|" separator
2. Generate meta description:
   - Format: opens with the value proposition, mentions the primary keyword once, ends with a soft CTA
   - Max 155 characters
   - Compliance: no banned phrases
3. Run output through `compliance-check`
4. Return both with character counts shown

## Outputs

- Meta title (with char count)
- Meta description (with char count)
- Build report line: "Generated meta for [page]"

## Examples

Page: Homepage
Primary keyword: numbing cream

→ Meta title: `UK Numbing Cream, Gel & Spray — Three Strengths | Senseless` (58 chars)
→ Meta description: `UK-formulated numbing cream, gel and spray. Three strengths matched to your appointment. CPSR-assessed cosmetic products, not a medicine.` (136 chars)

> **Do not treat the example as the house pattern.** The previous example baked an
> aesthetics-only procedure list ("lip fillers, Botox, microneedling, laser") into the one
> artefact every future meta gets modelled on, so a scope decision propagated as a formatting
> convention. Two live constraints it also contradicted: the three injectable collections are
> **organic-only** and must not be named on ad-facing meta (`.claude/rules/ad-facing.md`), and
> the procedure scope is under review. Derive each page's meta from that page's own primary
> keyword and its own audience — never from this example. Replaced 2026-08-13.

## Constraints

- Hard limits: 60 chars title, 155 chars description
- "Numbing" allowed in meta (SEO context), but never paired with a claim
- Must pass compliance-check
