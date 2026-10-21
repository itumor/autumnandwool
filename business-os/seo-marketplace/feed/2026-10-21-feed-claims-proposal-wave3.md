# Feed claims clean-up proposal (SEO-25), wave 3, 2026-10-21 — DRAFT for owner

Author: aw-seo-marketplace. **ASSUMPTION MODE:** the wording rules are GM's assumed answer to decision 16 / G8
(A-GM-10, `head-of-ecommerce/assumptions-wave3.md`), not owner evidence. The live feed and `build_google_feed.py` are
unchanged. The text lives in the generator's `D` list, so the fix is applied there by whoever runs the generator, in the
same pass as SEO-04 and SEO-24 (one re-upload).

## Phrase replacements (counts from Grep on the live TSV, 21 Oct)
| # | Current phrase | Feed lines | Rows | Proposed | Rule |
|---|---|---|---|---|---|
| R1 | "Knitted on a manually operated knitting machine and hand-sewn in Latvia." | 7, 22–99 | 79 | "Knitted on manual machines and finished by hand in Riga." | A-GM-10 allows this phrase (brand-voice precise wording); "hand-sewn in Latvia" is on its not-allowed list |
| R2 | "100% extra-fine merino wool, Italian-spun yarn." | 8–21 (hat & scarf set 3, beanie 11) | 14 | "Merino wool." | A-GM-10: "extra-fine" and "Italian-spun" not allowed; fibre name only, **no % in feed text** until the spec sheet is seen |
| R3 | "100% extra-fine merino wool." | 2 (vest SQ2078364) | 1 | "Merino wool." | as R2 |
| R4 | "Ships in kraft gift packaging." | 8–21 (hat & scarf set 3, beanie 11) | 14 | delete the sentence (or "Add a handwritten gift note." if the owner wants a gift line) | GM ruling W3-7 / A-GM-22: no gift wrap; allowed perks are a handwritten gift note and prices left off the packing slip |

Totals: 94 rows change (79 + 14 + 1). R2/R3 overlap R1 on no row. R4 hits the same 14 rows as R2, so the total stays 94.

## Not changed, and why
- The hat & scarf set **URL slug** contains "extra-fine" (`/merino-wool-hat-scarf-set-extra-fine-…`). Slugs are not
  changed without an owner-approved redirect list (skill guardrail); a URL isn't shown as a claim in listings.
- Other rows that state "100% merino wool", "100% lambswool" or "100% pure new wool" stay as they are. They copy the live
  PDP wording, and A-GM-10's "no %" applies to new text. If the owner wants the feed stricter than the PDP, the same
  rule applies there too (CRO's PDP packs). `[OWNER: confirm]`
- Titles: no claim words found in titles. "Hand-Knitted" appears in some live PDP **slugs** (e.g. the Dusty Pink and
  Lambswool crew URLs), not in feed titles: slugs stay (redirect rule).

## When the owner's evidence arrives (decision 16, spec sheets decision 34 by 30 Nov)
- Origin evidence confirms Latvia → R1 may keep "in Latvia"; "hand-sewn" only if that is the actual process.
- Spec sheet shows the fibre % → R2/R3 get "100% merino wool" back. "Extra-fine" / "Italian-spun" return only if the
  spec sheet says so.

CLAIM-CHECK: R1 still says "finished by hand in Riga". That is the A-GM-10 allowed phrase, which is an assumption until
the owner confirms (31 Oct).
ASSUMPTION: A-GM-10, A-GM-19, A-GM-22 (GM rulings W3-7, W3-8); register: business-os/head-of-ecommerce/assumptions-wave3.md. DRAFT, nothing applied.
