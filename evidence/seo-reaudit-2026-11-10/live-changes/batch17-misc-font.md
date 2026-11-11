# Batch 17: Miscellaneous font group to DM Sans (2026-11-11)

Site: rose-tarpon-ld9w.squarespace.com (admin), www.autumnandwool.com (public)
Task space: aw-batch17-font-2026-11-11 (id 37), finished with keep: []

## Path
Site Styles > Fonts > Miscellaneous (opened from the Fonts section, after Headings / Paragraphs / Buttons / Assign Styles rows).

## Before (recorded before any change)
- Font: Pragmatica Extended
- Style: Normal
- Weight: 700
- Line Height: 1em
- Letter Spacing: 0.01em
- Text Transform: Uppercase
- Size: 0.9rem
- Screenshot: screenshots/b17-font-before.jpg

## Change
- Font family changed to DM Sans via the picker search (selected row labelled "DM Sans").
- Weight shown as 700 after the change (no reset).

## After (re-read before Save)
- Font: DM SANS
- Style: Normal
- Weight: 700
- Line Height: 1em
- Letter Spacing: 0.01em
- Text Transform: Uppercase
- Size: 0.9rem
- Only the family differs from before. Nothing else touched.
- Screenshot: screenshots/b17-font-after.jpg

Headings (Instrument Serif), Paragraphs (DM Sans), Buttons and Forms were not opened or edited. The Fonts "Recommended Font Packs" popover was opened by an early click and closed with Escape without choosing a pack.

## Save
- Saved: yes. Save button went disabled after the click.
- Exit: clean exit from the editor, no "Exit Without Saving" prompt, no dialog.

## Public check (curl, browser User-Agent)
- use.typekit.net count in homepage HTML: 0 (checked on 7 polls over ~2 min, plus a separate fetch).
- --meta-font-font-family in linked site.css (versioned-site-css ... 1851/site.css?nocustom=true): "DM Sans".
- --heading-font-font-family in same file: "Instrument Serif" (unchanged).
- Note: the typekit substring appears once in the page as the JSON key "typekitId":"" (empty). It is not a script load.

## Unexpected
- The first click on the Fonts row opened the "Recommended Font Packs" popover instead of the group list. Closed with Escape; no pack applied.
- The first "EDIT SITE" click landed on config/website; the Site Styles editing toggle then opened the editor on the Home page.

## Not verified
- Visual rendering of the live site in DM Sans bold was not screenshot on the public site (only CSS variable checked).
- Whether any other Typekit-dependent asset remains beyond the homepage HTML (only the homepage was checked).
