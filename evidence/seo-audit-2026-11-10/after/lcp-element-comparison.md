# LCP element comparison: saved PageSpeed Insights reports (mobile)

Read-only extraction from saved PSI permalinks. No new analyses run. Times are as shown in each report (Lighthouse 13.6.0, Moto G Power emulated, Slow 4G). Timestamps are GMT+2 as displayed.

Labels A-D are the user's names. The report timestamps show A and C ran about 14:21-14:22, and B and D ran about 17:18-17:19. The "morning"/"afternoon" labels are not what the timestamps say, so they are recorded here as given.

## Summary table

| report | perf | LCP | LCP element (text or image, label, snippet first 150 chars) | LCP request discovery (insight / passed / absent) |
|---|---|---|---|---|
| A product, morning (Report from Nov 10, 2026, 2:22:02 PM) | 72 | 3.9 s | Text. Label: "Oversized Merino Wool V-Neck Sweater Vest". Snippet: `<h1 class="product-title">` | Passed (under PASSED AUDITS (10)). No checklist shown. |
| B product, afternoon (Report from Nov 10, 2026, 5:19:53 PM) | 52 | 21.1 s | Image. Label: "Oversized merino vest in grey, relaxed silhouette on a hanger". Snippet: `<img aria-describedby="product-gallery-slides-item-10" class="product-gallery-slides-item-image" data-load="false" data-src="https://images.squarespace-cdn.com/content/v1/6908755e4a17f81b7629f4bc/885…" data-image="https://images.squarespace-cdn.com/content/v1/6908755e4a17f81b7629f4bc/885…" data-image-dimensions="1536x2048" data-image-focal-point="0.5,0.5" alt="Oversized merino vest in grey, relaxed silhouette on a hanger" elementtiming="nbf-products-gallery" style="width: 100%; height: 100%; object-position: 50% 50%; object-fit: cover;" data-parent-ratio="0.8" …>` | INSIGHTS (failing). Checklist: "LCP resources shouldn't use loading=lazy"; "fetchpriority=high should be applied"; "Request is discoverable in initial document". Items are listed as shown; the page did not show pass or fail marks in the text. |
| C /shop, morning (Report from Nov 10, 2026, 2:21:28 PM) | 52 | 13.2 s | Text. Label: "We use essential cookies to operate our store. With your permission, we also us…". Snippet: `<p data-rte-preserve-empty="true" style="white-space:pre-wrap;">` | Passed (under PASSED AUDITS (10)). No checklist shown. |
| D /shop, afternoon (Report from Nov 10, 2026, 5:18:53 PM) | 42 | 17.5 s | Text. Label: "We use essential cookies to operate our store. With your permission, we also us…". Snippet: `<p data-rte-preserve-empty="true" style="white-space:pre-wrap;">` | Passed (under PASSED AUDITS (11)). No checklist shown. |

## Metrics (mobile tab, METRICS block)

| report | FCP | LCP | TBT | CLS | Speed Index | captured |
|---|---|---|---|---|---|---|
| A | 2.6 s | 3.9 s | 340 ms | 0.011 | 5.7 s | 2:22 PM GMT+2 |
| B | 2.6 s | 21.1 s | 580 ms | 0.011 | 6.0 s | 5:19 PM GMT+2 |
| C | 2.9 s | 13.2 s | 490 ms | 0 | 6.3 s | 2:21 PM GMT+2 |
| D | 2.9 s | 17.5 s | 970 ms | 0 | 7.6 s | 5:18 PM GMT+2 |

## A. product, morning

URL: https://pagespeed.web.dev/analysis/https-www-autumnandwool-com-shop-p-oversized-merino-wool-v-neck-sweater-vest/95zu6bg56c?form_factor=mobile

- Report timestamp: "Report from Nov 10, 2026, 2:22:02 PM"
- Performance score: 72
- Metrics: FCP 2.6 s; LCP 3.9 s; TBT 340 ms; CLS 0.011; Speed Index 5.7 s
- LCP breakdown (INSIGHTS, unscored), raw text:

```
LCP breakdown
Each subpart has specific improvement strategies. Ideally, most of the LCP time should be spent on loading the resources, not within delays.LCPUnscored
Subpart
	
Duration


Time to first byte
	
10 ms


Element render delay
	
200 ms
Oversized Merino Wool V-Neck Sweater Vest
<h1 class="product-title">
```

- Subparts: Time to first byte 10 ms; Resource load delay: not shown; Resource load duration: not shown; Element render delay 200 ms. The element is text, so there are no resource rows.
- LCP request discovery: present under PASSED AUDITS (10). The audit has no checklist (the expandable body is empty).

## B. product, afternoon

URL: https://pagespeed.web.dev/analysis/https-www-autumnandwool-com-shop-p-oversized-merino-wool-v-neck-sweater-vest/jjp2xohs2h?form_factor=mobile

- Report timestamp: "Report from Nov 10, 2026, 5:19:53 PM"
- Performance score: 52
- Metrics: FCP 2.6 s; LCP 21.1 s; TBT 580 ms; CLS 0.011; Speed Index 6.0 s
- LCP breakdown (INSIGHTS, unscored), raw text:

```
LCP breakdown
Each subpart has specific improvement strategies. Ideally, most of the LCP time should be spent on loading the resources, not within delays.LCPUnscored
Subpart
	
Duration


Time to first byte
	
10 ms


Resource load delay
	
1,350 ms


Resource load duration
	
700 ms


Element render delay
	
70 ms
Oversized merino vest in grey, relaxed silhouette on a hanger
<img aria-describedby="product-gallery-slides-item-10" class="product-gallery-slides-item-image" data-load="false" data-src="https://images.squarespace-cdn.com/content/v1/6908755e4a17f81b7629f4bc/885…" data-image="https://images.squarespace-cdn.com/content/v1/6908755e4a17f81b7629f4bc/885…" data-image-dimensions="1536x2048" data-image-focal-point="0.5,0.5" alt="Oversized merino vest in grey, relaxed silhouette on a hanger" elementtiming="nbf-products-gallery" style="width: 100%; height: 100%; object-position: 50% 50%; object-fit: cover;" data-parent-ratio="0.8" …>
```

- Subparts: Time to first byte 10 ms; Resource load delay 1,350 ms; Resource load duration 700 ms; Element render delay 70 ms.
- LCP request discovery: INSIGHTS (failing). Raw text:

```
LCP request discovery
Optimize LCP by making the LCP image discoverable from the HTML immediately, and avoiding lazy-loadingLCPUnscored
LCP resources shouldn't use loading=lazy
fetchpriority=high should be applied
Request is discoverable in initial document
Oversized merino vest in grey, relaxed silhouette on a hanger
<img aria-describedby="product-gallery-slides-item-10" ...>
```

## C. /shop, morning

URL: https://pagespeed.web.dev/analysis/https-www-autumnandwool-com-shop/unpz1xerxm?form_factor=mobile

- Report timestamp: "Report from Nov 10, 2026, 2:21:28 PM"
- Performance score: 52
- Metrics: FCP 2.9 s; LCP 13.2 s; TBT 490 ms; CLS 0; Speed Index 6.3 s
- LCP breakdown (INSIGHTS, unscored), raw text:

```
LCP breakdown
Each subpart has specific improvement strategies. Ideally, most of the LCP time should be spent on loading the resources, not within delays.LCPUnscored
Subpart
	
Duration


Time to first byte
	
30 ms


Element render delay
	
1,530 ms
We use essential cookies to operate our store. With your permission, we also us…
<p data-rte-preserve-empty="true" style="white-space:pre-wrap;">
```

- Subparts: Time to first byte 30 ms; Resource load delay: not shown; Resource load duration: not shown; Element render delay 1,530 ms. The element is text, so there are no resource rows.
- LCP request discovery: present under PASSED AUDITS (10). The audit has no checklist.

## D. /shop, afternoon

URL: https://pagespeed.web.dev/analysis/https-www-autumnandwool-com-shop/qvuc87erq9?form_factor=mobile

- Report timestamp: "Report from Nov 10, 2026, 5:18:53 PM"
- Performance score: 42
- Metrics: FCP 2.9 s; LCP 17.5 s; TBT 970 ms; CLS 0; Speed Index 7.6 s
- LCP breakdown (INSIGHTS, unscored), raw text:

```
LCP breakdown
Each subpart has specific improvement strategies. Ideally, most of the LCP time should be spent on loading the resources, not within delays.LCPUnscored
Subpart
	
Duration


Time to first byte
	
30 ms


Element render delay
	
2,700 ms
We use essential cookies to operate our store. With your permission, we also us…
<p data-rte-preserve-empty="true" style="white-space:pre-wrap;">
```

- Subparts: Time to first byte 30 ms; Resource load delay: not shown; Resource load duration: not shown; Element render delay 2,700 ms. The element is text, so there are no resource rows.
- LCP request discovery: present under PASSED AUDITS (11). The audit has no checklist.

## Notes

- The LCP element on the product pages changed between runs: A (text h1, 3.9 s) vs B (product image, 21.1 s, resource load delay 1,350 ms). Both product runs were otherwise similar in FCP and CLS. Only these two runs were compared; no cause is inferred here.
- On /shop, C and D both show a text `<p>` as the LCP element (cookie-consent text, "We use essential cookies..."). The cost is almost all element render delay (1,530 ms and 2,700 ms). The LCP element is a text node, so the resource-load rows do not apply.
- LCP request discovery is failing only on B (product image). It passes on A, C and D, where it shows no checklist.
- Extraction method: opened the audit by id (`#lcp-breakdown-insight`, `#lcp-discovery-insight`) on the visible mobile copy. The PASSED AUDITS section was expanded where needed. Values are copied from the rendered text.
