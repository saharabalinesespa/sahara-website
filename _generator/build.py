import sys, os
from lib import *
import pages1 as p1, pages2 as p2
import os as _o; OUT=_o.path.abspath(_o.path.join(_o.path.dirname(__file__),'..'))
pages={}
def add(fn,html): pages[fn]=html
add("index.html",p1.home()); add("price-list.html",p1.price_list()); add("services.html",p1.services()); add("book.html",p1.book())
for c in CATS: add(CATS[c][2]+".html",p1.category(c))
for it in items("massage"): add(SLUG[it[0]]+".html",p1.treatment(it))
for f in ["packages","bridal","vouchers","therapists","areas","faqs","reviews","about","contact","terms","privacy","notfound"]:
    h=getattr(p2,f)()
    fn={"vouchers":"gift-vouchers.html","therapists":"meet-our-therapists.html","areas":"areas-we-serve.html","terms":"terms-conditions.html","privacy":"privacy-policy.html","notfound":"404.html"}.get(f,f+".html")
    add(fn,h)
LIVE_ONLY=[]
if API_BASE:
    add("booking-confirmed.html",p2.booking_confirmed()); add("booking-manage.html",p2.booking_manage()); LIVE_ONLY=["booking-confirmed.html","booking-manage.html"]
    import shutil; [shutil.copy(os.path.join(os.path.dirname(os.path.abspath(__file__)),f),os.path.join(OUT,"assets/js/"+f)) for f in ("live.js","menu-sync.js")]
import shutil as _sh; _sh.copy(os.path.join(os.path.dirname(os.path.abspath(__file__)),'analytics.js'),os.path.join(OUT,'assets/js/analytics.js'))
for fn,h in pages.items():
    open(os.path.join(OUT,fn),'w',encoding='utf-8').write(h)
open(os.path.join(OUT,'assets/js/data.js'),'w',encoding='utf-8').write(data_js())
# sitemap + robots
urls=[fn for fn in pages if fn not in ("404.html",)+tuple(LIVE_ONLY)]+["ar.html"]
sm='<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+"".join(f'<url><loc>{BASE}/{"" if u=="index.html" else u}</loc></url>\n' for u in sorted(urls))+'</urlset>\n'
open(os.path.join(OUT,'sitemap.xml'),'w').write(sm)
open(os.path.join(OUT,'robots.txt'),'w').write(f"User-agent: *\nAllow: /\n\nSitemap: {BASE}/sitemap.xml\n")

# ---- post-process every page: link safety, Arabic page head tags, heading structure ----
import re as _re, glob as _g
SR_TITLE={"services.html":"Treatment categories","massage.html":"Massage treatments","facials.html":"Facial treatments","body-scrub.html":"Body scrub treatments","nail-care.html":"Nail treatments","corporate-wellness.html":"Corporate wellness options","packages.html":"Packages","bridal.html":"Bridal packages"}
def _fix(fn,h):
    # 1) every new-tab link gets rel="noopener"
    def _a(m):
        tag=m.group(0)
        if 'target="_blank"' in tag and 'noopener' not in tag:
            tag=tag[:-1]+' rel="noopener">' if 'rel=' not in tag else _re.sub(r'rel="([^"]*)"',lambda r:'rel="'+r.group(1)+' noopener"',tag,1)
        return tag
    h=_re.sub(r'<a\s[^>]*>',_a,h)
    # 2) Arabic page: live address, social/icon tags, structured data
    if fn=="ar.html":
        h=h.replace("https://saharabalinesespas.com",BASE)
        h=_re.sub(r'<h4( style="[^"]*")>(.*?)</h4>',r'<p\1>\2</p>',h)
        if 'og:image' not in h:
            add=(f'<meta property="og:image" content="{BASE}/assets/img/spa-massage-1.webp"><meta name="twitter:card" content="summary_large_image">'
                 f'<link rel="apple-touch-icon" href="apple-touch-icon.png"><link rel="manifest" href="manifest.webmanifest">')
            h=h.replace('</head>',add+'\n</head>',1)
        if 'ld+json' not in h:
            ld={"@context":"https://schema.org","@type":"DaySpa","name":"سبا سهارا البالينيزي","alternateName":"Sahara Balinese Spa & Salon","url":f"{BASE}/ar.html","telephone":"+"+PHONE,"inLanguage":"ar","areaServed":"Dubai","image":f"{BASE}/assets/img/spa-massage-1.webp","priceRange":"AED 200 - AED 650"}
            h=h.replace('</head>','<script type="application/ld+json">'+json.dumps(ld,ensure_ascii=False)+'</script>\n</head>',1)
    # 3) heading outline: a card heading (h3) straight after the page h1 gets a hidden h2 above its group
    i1=h.find('<h1'); i3=h.find('<h3',i1) if i1>-1 else -1; i2=h.find('<h2',i1) if i1>-1 else -1
    if i1>-1 and i3>-1 and (i2==-1 or i3<i2):
        pre=h[:i3]; pos=max(pre.rfind('<div class="grid'),pre.rfind('<div class="wrap'))
        if pos>i1: h=h[:pos]+f'<h2 class="sr">{SR_TITLE.get(fn,"Details")}</h2>'+h[pos:]
    return h
for _f in _g.glob(os.path.join(OUT,'*.html')):
    _fn=os.path.basename(_f); _h=open(_f,encoding='utf-8').read(); _n=_fix(_fn,_h)
    if _n!=_h: open(_f,'w',encoding='utf-8').write(_n)
print(len(pages),"pages built")
