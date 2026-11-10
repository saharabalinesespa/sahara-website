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
for fn,h in pages.items():
    open(os.path.join(OUT,fn),'w',encoding='utf-8').write(h)
open(os.path.join(OUT,'assets/js/data.js'),'w',encoding='utf-8').write(data_js())
# sitemap + robots
urls=[fn for fn in pages if fn not in ("404.html",)]+["ar.html"]
sm='<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+"".join(f'<url><loc>{BASE}/{"" if u=="index.html" else u}</loc></url>\n' for u in sorted(urls))+'</urlset>\n'
open(os.path.join(OUT,'sitemap.xml'),'w').write(sm)
open(os.path.join(OUT,'robots.txt'),'w').write(f"User-agent: *\nAllow: /\n\nSitemap: {BASE}/sitemap.xml\n")
print(len(pages),"pages built")
