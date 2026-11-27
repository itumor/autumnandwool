# Header EN/LV toggle — live 2026-11-27

- Header Button `LV` -> `https://autumnandwool.com/lv`; URL mapping `/lv -> https://lv.autumnandwool.com/ 301` (Squarespace > Settings > Developer Tools > URL Mappings, line 8).
- Weglot (Latvian): string `LV` translated to `EN` (manually edited); external link translation `https://autumnandwool.com/lv` -> `https://www.autumnandwool.com/`.
- Excluded from Weglot (delete translations): `/shop*`, `/sitemap*` (sitemap.xml was 2,872 words and re-broke the limit).
- Verified with real clicks (ego-browser): www -> LV click lands on lv (html lang lv, title Latvian, button `EN`); EN click lands on www (button `LV`).
- listbox count 0 on www, lv and lv/cart. Nav EN/LV link items deleted.
- Mobile 375px: button hidden in the top bar (Squarespace), visible in the burger menu.
- Not done: PageSpeed re-run; same-page language switch (links go to each home page).
- Rollback: Header > Add Elements > Button off; delete the `/lv` URL mapping line; Weglot: delete the external link translation and set `LV` translation back to `LV`.
