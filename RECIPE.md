# Recipe: turn one design page into a live Squarespace page (proven on Home, About, Contact)

Site admin: https://rose-tarpon-ld9w.squarespace.com/config/pages  (already signed in, in Claude in Chrome; tools are
mcp__claude-in-chrome__* — load with ToolSearch "select:mcp__claude-in-chrome__tabs_context_mcp,...navigate,computer,javascript_tool,get_page_text,tabs_create_mcp").
Public site: https://www.autumnandwool.com/   Backup copy already exists (do not touch it).
Squarespace allows ONE editing session per site: never run two agents on the site at once. Use ONE tab; close extra tabs.

## Design source (do not publish this file anywhere)
Design pages live as .dc.html in
/private/tmp/claude-502/-Users-eramadan-autumnandwool/6f228d1b-6c4a-4df1-9565-f586575e4e85/scratchpad/artifact-files/26421a77-b015-446f-81c4-e711bb0d69e8/project/
(SizeGuide, Shipping, FAQ, Privacy ...). Read it for COPY, structure and styling. Ignore its header, footer, nav and the `<script type="text/x-dc">` block:
the live site keeps Squarespace's native header and footer. Convert the body into STATIC HTML + one <style> block + (only if needed, e.g. cm/in toggle,
FAQ is fine with <details>) a small vanilla <script>. No {{holes}}, no <sc-if>/<sc-for> (expand loops by hand or generate strings in the JS that pastes).
Palette: oat #F2EDE6, sand #E7E0D6, rust #8E3B1F, ink #24201C, mid text #4A423B/#5E554D, lines #CFC6BA. Fonts: headings 'Instrument Serif', body 'DM Sans'.
Internal links: /shop /about /contact /size-guide /shipping-returns /faq /privacy-policy (verify exact slugs in Pages > page settings).
Images: only https://images.squarespace-cdn.com/content/v1/6908755e4a17f81b7629f4bc/<path>?format=1000w (paths are in the .dc.html files / earlier pages).
No announcement bar, no header, no footer in the code.

## Shared breakout CSS (put FIRST in every page's <style>; every page's root element is <div class="aw">)
.fluid-engine:has(.aw){display:block!important}
.fe-block:has(.aw){grid-area:auto!important;width:100%!important}
.page-section:has(.aw){min-height:0!important}
.page-section:has(.aw) .content-wrapper{padding:0!important}
.page-section:has(.aw) .content{max-width:none!important;padding:0!important}
.sqs-block:has(.aw),.sqs-block:has(.aw) .sqs-block-content{padding:0!important}
.aw{font-family:'DM Sans',sans-serif;color:#24201C;line-height:1.55;font-size:16px;background:#F2EDE6}
.aw *{box-sizing:border-box}.aw a{color:inherit;text-decoration:none}
.aw h1,.aw h2,.aw h3{font-family:'Instrument Serif',serif;font-weight:400;margin:0;letter-spacing:-.02em}
.aw em{font-style:italic}.aw-w{max-width:1360px;margin:0 auto;padding:0 32px}
.aw-k{font-size:13px;font-weight:600;letter-spacing:.14em;text-transform:uppercase;color:#8E3B1F}
.aw-b{display:inline-flex;align-items:center;min-height:52px;padding:0 28px;border-radius:999px;font-weight:500;background:#24201C;color:#F2EDE6!important}
.aw-b.o{background:transparent;color:#24201C!important;border:1px solid #24201C}
(Prefix ALL other classes with aw- to avoid clashes. Use responsive grids with auto-fit/minmax and flex-wrap; must work at 390px width.)

## Steps in the Squarespace editor (coordinates are for the 1512x728 Chrome window; always screenshot to confirm)
1. Navigate to /config/pages. Click the page in the left Pages list (Main Navigation or Not Linked). Wait 3s. Click "Edit" (377,43).
2. The page has old sections. Add a NEW blank section at the top: click the first section's background, click blue "ADD SECTION" bar at the section's top edge
   (~(747,109)), in the modal click "Add Blank" (228,154). A blank section appears with an "ADD BLOCK" button (147,154).
3. ADD BLOCK (147,154) -> type "code" -> click the "Code" result (88,246). Wait 2s. The block shows "Hello, World!".
   Click that text (~(90,220)) to select the block, click the pencil in its toolbar (~(72,170)) -> code editor (CodeMirror 6) opens, mode HTML.
4. Paste the page via javascript_tool (typing is too slow/auto-indents). Build the full HTML string `html` (style + markup) and run:
   const c=document.querySelector('.cm-content');c.focus();document.execCommand('selectAll');
   const dt=new DataTransfer();dt.setData('text/plain',html);
   c.dispatchEvent(new ClipboardEvent('paste',{clipboardData:dt,bubbles:true,cancelable:true}));html.length
   (Return values containing cookies/query strings are blocked; return html.length only. Avoid backticks and ${ inside the HTML itself.)
5. Press Escape to close the editor; wait 3s; screenshot: the design should render full width. Fix by re-pasting if needed.
6. Remove the OLD sections below: click empty background inside an old section (not inside your code block!), click REMOVE in the floating menu
   (~(1370,370) or (1370,431) — read it from a screenshot), confirm "Remove" in the dialog (866,408). Repeat until only your section + the global footer remain.
   NEVER remove the footer ("EDIT SITE FOOTER" label) and never remove your code section.
7. Click Save (38,27). Wait 3s (button greys out = saved).
8. Verify on the public URL in the same tab group: screenshot top + a scroll or two. Check no leftover old content, no double headings.
9. Report: page, what was built, any deviation, anything not verified. Do not touch other pages. Do not change Site Styles.

## Lessons added after the build (2026-10-18)
- Headings inside dark boxes need explicit `!important` colour rules; Squarespace's heading colour wins otherwise. Check every dark box after Save.
- Palette editor resets to HSL when you switch swatch; choose Hex before typing.
- Delete old blocks via the section's layers panel (select layer, press Delete); remove old sections with REMOVE + confirm. Screenshot before each removal; never remove the footer or your own code section.
- Use real product URLs from category pages (`/shop/p/p/<slug>`), not category links, for cards.
- Site-wide settings (SEO title format `%p`, Custom CSS) live outside pages; read existing Custom CSS and append, never overwrite.
- Not editable via UI: Shop H1 tag, cart heading. Contact form is mailto-based.
- Open owner decisions are listed in the project memory (redesign-state-2026-10-18); ask before editing policy text.
