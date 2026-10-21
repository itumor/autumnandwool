import csv, re
B='https://www.autumnandwool.com'
P='https://images.squarespace-cdn.com/content/v1/6908755e4a17f81b7629f4bc/'
SHIP='Free shipping. Ships from Riga within 2–5 working days. 14-day returns.'
HAND='Knitted on a manually operated knitting machine and hand-sewn in Latvia.'
# id, title, url, color, gender, category, product_type, desc, images, variants[(sku, price, attrs)]
D=[
("6915d24b03d8727c4c8380ea","Oversized Merino Wool V-Neck Sweater Vest","/shop/p/oversized-merino-wool-v-neck-sweater-vest","","female","vest",
 "Oversized V-neck vest with ribbed edging and Japanese-style shoulder shaping. Easy to layer over shirts and dresses. 100% extra-fine merino wool. Relaxed, oversized fit. Width 59 cm, length 68 cm.",
 ["62180209-cc63-4af8-bbc1-ae0a19636fba/IMG_3336.JPEG","d81ded9d-57d8-48b5-870a-0d94c4915ef6/IMG_3328.JPEG","8718b530-a760-4428-89e7-f33cc93163ce/IMG_3333.JPEG","f37dbcf0-94ea-4d51-82b5-3b6bd6491a74/IMG_3331.JPEG"],
 [("SQ2078364","126.00",{})]),
("691050bcb0c4a7226c535650","Merino Wool Raglan Cardigan","/shop/p/p/black-merino-wool-cardigan-100-merino-wool-raglan-sweater-minimalist-knitwear-sustainable-handmade-womens-cardigan-1","","female","cardigan",
 "A relaxed raglan cardigan in 100% merino wool. Relaxed, slightly oversized fit. Width 61 cm, front length 67 cm, sleeve from neck 82 cm. Hand wash cold or gentle wool cycle; dry flat.",
 ["1762677080229-61UOLLY9NEB98MTXF359/image_1.jpg","1762677092877-O17XWBVIXP9MU9JUKH8Z/image_2.jpg","1762677102877-8LAAND9MCWAJPTX82X0U/image_3.jpg","1762677114303-8E871ZOXVZEDC76749OC/image_4.jpg"],
 [("SQ9088173","160.00",{"Primary color":"Black"}),("SQ7601591","160.00",{"Primary color":"Brown"}),("SQ1988154","160.00",{"Primary color":"Blue"})]),
("6910544d03d8727c4c7e8c2e","Oversized Wool V-Neck Vest - Beige Melange","/shop/p/p/wool-sweater-vest-knitted-wool-vest-oversized-vest-womens-woolen-pullover-vest-top-sleeveless-wool-knit-vest-soft-v-neck-vest","Beige","female","vest",
 "Oversized V-neck sweater vest in beige melange with a minimalist ribbed finish. Easy to layer over shirts, dresses and long sleeves. Wool. Width 57 cm, length 69 cm.",
 ["1762677841592-KZ36KWM82YPV0Y2QMPIN/image_1.jpg","1762677849092-9VFTI2AZSVZHYHV1D8VS/image_2.jpg","1762677855853-NUXMX3QMZL2SH65ME1Y5/image_3.jpg","1762677862631-I08WP9MX3C79KUB3KPSL/image_4.jpg"],
 [("SQ7004700","126.00",{})]),
("691055d8dc1bc40ece1f451a","Oversized Wool Raglan Sweater — Beige Melange","/shop/p/p/wool-sweater-sweater-for-women-knit-cozy-pullover-sweater-sustainable-knitwear-oversized-wool-jumper-relaxed-fit-wool-pullover-1","Beige","female","sweater",
 "Oversized raglan sweater in beige melange with a round ribbed neck and ribbed cuffs. "+HAND+" 100% pure wool. Width 59 cm, front length 60 cm, back length 69 cm.",
 ["1762678236514-ISG5HGL1TIN2JE3M6EIP/image_1.jpg","1762678243583-BI5P02ULM0W1REN622ZO/image_2.jpg","1762678250542-2CBREZJPPXJ9FZG0U4MP/image_3.jpg","1762678257300-EI6KVLVET5AALMTF0CMW/image_4.jpg"],
 [("SQ9326369","155.00",{})]),
("69105624c6bfa9183a014d2a","Merino Wool Hat & Scarf Set","/shop/p/p/merino-wool-hat-scarf-set-extra-fine-rib-knit-soft-on-skin-warm-not-bulky-unisex-gift","","unisex","hat",
 "Matching rib-knit beanie and scarf, soft on the skin and warm without bulk. 100% extra-fine merino wool, Italian-spun yarn. Beanie fits 54–58 cm heads; scarf approx. 190 × 36 cm. Ships in kraft gift packaging.",
 ["1762678311409-26KFX7XKIYQW97QLAA9Q/image_1.jpg","1762678317830-7XLX255QXEKTL22EIZ2Z/image_2.jpg","1762678323532-C9R3IPOWS7CYGHVXQWCW/image_3.jpg","1762678329491-I0WZRF7LKLKSJPAOSEQH/image_4.jpg"],
 [("SQ9379546","110.00",{"Primary color":"Black"}),("SQ2239941","110.00",{"Primary color":"Gray"}),("SQ7476378","110.00",{"Primary color":"Brown"})]),
("69105690dc1bc40ece1f4561","Rib-Knit Merino Beanie — Unisex","/shop/p/p/merino-beanie-100-wool-soft-warm-breathable-rib-knit-hat-for-men-women-1","","unisex","hat",
 "Unisex rib-knit beanie with a fold-over cuff and a smooth forehead band that won't press or leave lines. 100% extra-fine merino wool, Italian-spun yarn. One size, fits 54–58 cm heads. Available in 11 colours. Ships in kraft gift packaging.",
 ["1762678420385-G1VV1T2IJJKRDALKRTXK/image_1.jpg","1762678425659-24CLPKNCIHPP3EBUHGOZ/image_2.jpg","1762678431875-S6SGFZYLM9O2PCULIHM9/image_3.jpg","1762678438631-WHKO0C8XX4ATTNE7AE15/image_4.jpg"],
 [(s,"45.00",{"Primary color":c}) for s,c in [("SQ0189633","Black"),("SQ6735209","Brown"),("SQ6830651","Navy"),("SQ5766994","Blue"),("SQ1398008","Gray"),("SQ9891810","Light grey"),("SQ6240622","Beige"),("SQ2122502","Camel"),("SQ3845006","Bordeaux"),("SQ3314835","Pink"),("SQ1599152","Melange grey")]]),
("691059dc03d8727c4c7e8dd6","Pure Wool Side-Slit Sweater — Camel","/shop/p/p/hand-knitted-wool-sweater-womens-organic-knit-jumper-1","Camel","female","sweater",
 "Round-neck sweater with ribbed collar and cuffs, side slits and an asymmetric hem (front shorter than back). "+HAND+" 100% pure new wool. Relaxed fit. Sizes S–XL.",
 ["1762679264631-ZZ35NHN41UYSDTS4FUDX/image_1.jpg","1762679273579-4L6P4GBY1U3DOVMF2QTZ/image_2.jpg","1762679283213-IL8ASAT5IPUN88BKQTRS/image_3.jpg","1762679292623-H4EX989HU75R4DWT6HO0/image_4.jpg"],
 [("SQ4565277","136.00",{"Size":"S"}),("SQ0850514","136.00",{"Size":"M"}),("SQ3934346","136.00",{"Size":"L"}),("SQ4975266","136.00",{"Size":"XL"})]),
("691059dd03d8727c4c7e8dd8","Pure Wool Side-Slit Sweater — Light Grey","/shop/p/p/hand-knitted-wool-sweater-organic-knitwear-asymmetrical-design-1","Light Grey","female","sweater",
 "Round-neck sweater with ribbed collar and cuffs, side slits and an asymmetric hem (front shorter than back). "+HAND+" 100% pure new wool. Relaxed fit. Sizes S–XL.",
 ["1762679265516-FR2E87LDR61AZ8PII1KG/image_1.jpg","1762679276177-WLZ3OPQX2BULMU23TKLH/image_2.jpg","1762679285506-84RTLKY334JAU64F4XXT/image_3.jpg","1762679294073-5AMS666IAC9NA2R5RL3L/image_4.jpg"],
 [("SQ0554332","136.00",{"Size":"S"}),("SQ8772441","136.00",{"Size":"M"}),("SQ5710264","136.00",{"Size":"L"}),("SQ5327787","136.00",{"Size":"XL"})]),
("691059de03d8727c4c7e8dd9","Lambswool Raglan Crew — Brown","/shop/p/p/cozy-and-sustainable-hand-knitted-lambswool-sweater-for-women","Brown","female","sweater",
 "Lambswool sweater with a round ribbed neck, raglan sleeves, ribbed cuffs and a gently curved hem. "+HAND+" 100% lambswool. Relaxed fit. Sizes S–XL.",
 ["1762679266401-VQPKD3S701V2NN08ALVN/image_1.jpg","1762679273575-CHMJLY4WKLGRPK3J8ZV1/image_2.jpg","1762679282737-QWWHBB4SFQDUAXV4SJT5/image_3.jpg","1762679289924-HSMOX1C2M4AGXRZDARVR/image_4.jpg"],
 [("SQ6061536","136.00",{"Size":"S"}),("SQ9265885","136.00",{"Size":"M"}),("SQ0851295","136.00",{"Size":"L"}),("SQ7867996","136.00",{"Size":"XL"})]),
("691059deb0c4a7226c535904","Lambswool Raglan Crew — Green","/shop/p/p/hand-knitted-lambswool-sweater-womens-winter-knitwear-1","Green","female","sweater",
 "Lambswool sweater with a round ribbed neck, raglan sleeves, ribbed cuffs and a gently curved hem. "+HAND+" 100% lambswool. Relaxed fit. Sizes S–XL.",
 ["1762679266856-UZISE2P2FOPO9FRBY6TK/image_1.jpg","1762679277008-GCDPUIZ2H0T5H7P63AU9/image_2.jpg","1762679286441-89RET5WLC75KG8VRFAFN/image_3.jpg","1762679296003-VZSOP8LVMYBADPRAN6HT/image_4.jpg"],
 [("SQ1183187","136.00",{"Size":"S"}),("SQ2462373","136.00",{"Size":"M"}),("SQ5891265","136.00",{"Size":"L"}),("SQ2323221","136.00",{"Size":"XL"})]),
("691059dfdc1bc40ece1f4648","Women’s Classic Lambswool Crew Sweater","/shop/p/p/hand-knitted-lambswool-sweater-womens-grey-knit-jumper","Grey","female","sweater",
 "Classic lambswool crew-neck sweater with raglan sleeves, ribbed cuffs and a gently curved hem. "+HAND+" 100% lambswool. Relaxed fit. Sizes S–XL.",
 ["1762679267905-YNLWU1MOBROWJXGM7SSH/image_1.jpg","1762679277067-DUDVFKWRPGW8PLV0B2L6/image_2.jpg","1762679287053-MNLYGJVNQHYF5SRX57T8/image_3.jpg","1762679295857-XUZ2C77E74RJJAOMGS0F/image_4.jpg"],
 [("SQ8973335","136.00",{"Size":"S"}),("SQ4628527","136.00",{"Size":"M"}),("SQ5713917","136.00",{"Size":"L"}),("SQ3869977","136.00",{"Size":"XL"})]),
("69105a20b0c4a7226c53591c","Distressed Wool Raglan Sweater — Oversized","/shop/p/p/hand-knitted-distressed-wool-sweater-oversized-raglan-jumper-1","","female","sweater",
 "Oversized raglan sweater with distressed details, a round ribbed neck, ribbed cuffs and a curved hem. "+HAND+" Wool. Width 57 cm, front length 66 cm, back length 71 cm.",
 ["1762679333780-YWGP2NQJE5WFG32ZY5GG/image_1.jpg","1762679342937-Y19PQ3G1ISA02CW9SCTJ/image_2.jpg","1762679353137-VYZBTAWTV0D71JL0KCTT/image_3.jpg","1762679364637-MQFMOBS4P77OMD0IRQMS/image_4.jpg"],
 [("SQ3807672","155.00",{})]),
("69105a2694cd8c749255d65d","Merino Striped Oversized Sweater — Women’s Jumper","/shop/p/p/hand-knitted-merino-wool-striped-sweater-oversized-jumper","","female","sweater",
 "Oversized striped sweater with fully fashioned (Japanese) shoulder shaping. "+HAND+" 100% merino wool. Width 59 cm, front length 67 cm, sleeve from neck 74 cm.",
 ["1762679338414-QH60NQHB7FJHOD744SW4/image_1.jpg","1762679348428-RY56DGBGF3JRDVBDV0MF/image_2.jpg","1762679354529-KC5YSOBPPQ39MW0755NR/image_3.jpg","1762679363688-FN4L2V0KP7XPYNJGC5BR/image_4.jpg"],
 [("SQ9502706","165.00",{})]),
("69105a2903d8727c4c7e8dfa","100% Wool Long Shawl Cardigan – Warm Knit","/shop/p/p/hand-knitted-wool-cardigan-minimalist-open-front-sweater-1","","female","cardigan",
 "Long open-front cardigan with a straight cut, dropped shoulders, a draped collar and double-folded cuffs and hem. "+HAND+" 100% pure new wool. Sizes S–XL.",
 ["1762679341580-721KIL0CS050U4032IVA/image_1.jpg","1762679352038-Q1N9C4P2GLTZ991ATJKE/image_2.jpg","1762679361259-7JDHQV4743M356TM0WZB/image_3.jpg","1762679369740-00PDHPU6VN7Q344USHOJ/image_4.jpg"],
 [("SQ7145776","145.00",{"Size":"S"}),("SQ7776260","145.00",{"Size":"M"}),("SQ7845957","145.00",{"Size":"L"}),("SQ2037965","145.00",{"Size":"XL"})]),
("69105a2ab0c4a7226c53591f","Long Wool Cardigan — Women’s Shawl Collar","/shop/p/p/wool-cardigan-warm-cardigan-organic-wool-wrap-winter-sweater-cardigan-women-cardigan-sweater-minimalist-style-sweater","","female","cardigan",
 "Knee-length open-front cardigan with a straight cut, dropped shoulders and a draped shawl collar. "+HAND+" 100% pure new wool. Sizes S–XL.",
 ["1762679342615-6S4AVCS6KE3TOH9YO18X/image_1.jpg","1762679349551-NMY94WJ6KWX2STYTXJCW/image_2.jpg","1762679358872-2FKO6O7ICEZXBDQQSMVN/image_3.jpg","1762679368266-D9G1Z3DYVS75U9NAFMI3/image_4.jpg"],
 [("SQ5142555","145.00",{"Size":"S"}),("SQ0742548","145.00",{"Size":"M"}),("SQ8362078","145.00",{"Size":"L"}),("SQ8241965","145.00",{"Size":"XL"})]),
("69105a8403d8727c4c7e8e1c","Open-Front Wool Cardigan — Women’s Side-Slit Knit","/shop/p/p/hand-knitted-wool-cardigan-open-front-winter-sweater-679428","","female","cardigan",
 "Straight-cut open-front cardigan with dropped shoulders, ribbed cuffs and hem, and side slits framed by ribbed panels. "+HAND+" 100% pure new wool. Width 56 cm, length 70 cm.",
 ["1762679432282-2GSLAI41DBEVMU9486FZ/image_1.jpg","1762679440003-R1HKA0M0FUWAZ1NPPXVE/image_2.jpg","1762679453888-5MBM3FJGY3833GZTFHVV/image_3.jpg","1762679463706-MJZU19F3JJSBNQOZNL1X/image_4.jpg"],
 [("SQ3776585","155.00",{})]),
("69105a8503d8727c4c7e8e1d","Merino Turtleneck — Women’s Lightweight Knit","/shop/p/p/merino-wool-turtleneck-sweater-womens-knit-pullover-soft-warm-lightweight-minimalist-sustainable-knitwear-sizes-sl-12-679428","","female","sweater",
 "Lightweight turtleneck that layers easily under jackets or over skirts and trousers. Available in 12 colours. "+HAND+" 100% merino wool. Close to the body fit.",
 ["1762679433178-LVOBS3HEOEBCUBKCRYX8/image_1.jpg","1762679439909-TRVNE0Y1JSETVLRH14JE/image_2.jpg","1762679448112-8PQXXI1GX7DFV3SM5L4T/image_3.jpg","1762679453760-NC8JFQWN01BKGI744CAZ/image_4.jpg"],
 []),
("69105acfb0c4a7226c53596e","Pure Wool Stand-Collar Sweater — Beige","/shop/p/p/hand-knitted-wool-sweater-stand-collar-knit-679503","Beige","female","sweater",
 "Stand-collar sweater with a clean, timeless shape. "+HAND+" 100% pure new wool. Relaxed fit. Sizes S–XL.",
 ["1762679508020-9LNAG6RTPH1N8SVJAFS1/image_1.jpg"],
 [("SQ4863473","136.00",{"Size":"S"}),("SQ4591024","136.00",{"Size":"M"}),("SQ1844551","136.00",{"Size":"L"}),("SQ3898906","136.00",{"Size":"XL"})]),
("69105ad603d8727c4c7e8e4e","Pure Wool Stand-Collar Sweater — Blue","/shop/p/p/hand-knitted-wool-stand-collar-sweater-womens-knitwear-679510","Blue","female","sweater",
 "Stand-collar sweater with a clean, timeless shape. "+HAND+" 100% pure new wool. Relaxed fit. Sizes S–XL.",
 ["1762679514469-GOWSKQOMVJGA3U1V62VL/image_1.jpg"],
 [("SQ8867279","136.00",{"Size":"S"}),("SQ3434719","136.00",{"Size":"M"}),("SQ8666979","136.00",{"Size":"L"}),("SQ6566202","136.00",{"Size":"XL"})]),
("69105adfb0c4a7226c535976","Oversized Merino Turtleneck — Dusty Pink Raglan","/shop/p/p/merino-wool-sweater-oversize-sweater-knitted-wool-jumper-stand-up-collar-jumper-relaxed-fit-wool-pullover-warm-pink-jumper-679519","Pink","female","sweater",
 "Oversized raglan sweater in dusty pink with a ribbed turtleneck collar, ribbed cuffs and a curved hem. "+HAND+" Merino wool. Width 53 cm, front length 63 cm, back length 70 cm.",
 ["1762680780169-3LFZS4V3HLAT1KDK5YGX/image_1.jpg","1762680790430-WCDKU3Z9AGHDVML4EO9M/image_2.jpg","1762680799979-15UPUXQM00BI22P5DB0I/image_3.jpg","1762680810149-9DV2SDIIKX54QIYWGEJO/image_4.jpg"],
 [("SQ3600486","155.00",{})]),
("69105bd9b0c4a7226c5359f0","Merino Wool Raglan Sweater — Dusty Pink Oversized Jumper","/shop/p/p/hand-knitted-merino-wool-raglan-sweater-dusty-pink-oversized-jumper","Pink","female","sweater",
 "Oversized raglan sweater in dusty pink with a round ribbed neck, ribbed cuffs and a curved hem. "+HAND+" Merino wool. Sizes S/M and L/XL.",
 ["1762679774296-BNIENHKIPCSRY0OCCB9S/image_1.jpg","1762679782725-ULZEAQJ4CYCXVW3KX39L/image_2.jpg","1762679791713-3NRNRQGIKK0TDBL7ODED/image_3.jpg","1762679800161-SPT2OFS8191HLNZ1YGV2/image_4.jpg"],
 [("SQ9956956","155.00",{"Size":"S/M"}),("SQ6945548","155.00",{"Size":"L/XL"})]),
]
TN=[("SQ3433178","SQ4483570","SQ5350409","Melange Grey"),("SQ9035687","SQ6470056","SQ0376525","Classic Grey"),("SQ5958509","SQ1481398","SQ0199503","Chestnut Brown"),("SQ8005265","SQ8421560","SQ2134916","Melange Brown"),("SQ9790760","SQ7638948","SQ0831840","Melange Taupe"),("SQ2914675","SQ8708276","SQ8111036","Melange Beige"),("SQ8096733","SQ5264360","SQ9486312","Dusty Rose"),("SQ9044699","SQ7358699","SQ2898392","Rose Pink"),("SQ6384123","SQ1480313","SQ4599687","Berry Purple"),("SQ5869324","SQ0111040","SQ4784604","Purple Brown"),("SQ5989399","SQ1919240","SQ4155762","Royal Blue"),("SQ1526199","SQ1652750","SQ2272298","Sky Blue")]
for p in D:
    if p[0]=="69105a8503d8727c4c7e8e1d":
        for xs,s,m,c in TN:
            for sku,sz in ((xs,"XS"),(s,"S"),(m,"M")): p[8].append((sku,"110.00",{"Size":sz,"Primary color":c}))
CAT={'sweater':('212','Apparel > Knitwear > Sweaters'),'cardigan':('212','Apparel > Knitwear > Cardigans'),'vest':('212','Apparel > Knitwear > Sweater vests'),'hat':('173','Apparel > Accessories > Hats & beanies')}
cols=['id','item_group_id','title','description','link','image_link','additional_image_link','availability','price','brand','condition','identifier_exists','google_product_category','product_type','gender','age_group','color','size','material','shipping(country:service:price)']
rows=[]
for pid,title,url,color,gender,kind,desc,imgs,vars_ in D:
    mat='Merino wool' if 'erino' in title+desc else ('Lambswool' if 'ambswool' in title else 'Wool')
    for sku,price,a in vars_:
        c=a.get('Primary color') or color
        sz=a.get('Size') or "One size"
        vt=', '.join(x for x in (a.get('Primary color'),a.get('Size')) if x)
        rows.append([sku, pid if len(vars_)>1 else '', (title+(f' ({vt})' if vt else ''))[:150], desc+' '+SHIP, B+url, P+imgs[0]+'?format=1500w', ','.join(P+i+'?format=1500w' for i in imgs[1:]),
            'in_stock', price+' EUR','Autumn & Wool','new','no',CAT[kind][0],CAT[kind][1],gender,'adult',c,sz,mat,''])
out='/mnt/user-data/outputs/autumnandwool-google-feed.tsv'
with open(out,'w',newline='') as f:
    w=csv.writer(f,delimiter='\t'); w.writerow(cols[:-1]); [w.writerow(r[:-1]) for r in rows]
print(len(rows),'rows', sum(1 for r in rows if not r[16]),'no color')
