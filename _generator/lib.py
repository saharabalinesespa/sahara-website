import json, os, html as H
from data import *

def esc(s): return H.escape(s, quote=True)
WA = lambda msg="": f"https://wa.me/{PHONE}" + (f"?text={msg}" if msg else "")
WA_HELLO = f"https://wa.me/{PHONE}?text=Hi%20Sahara%2C%20I%27d%20like%20to%20book%20a%20treatment."
SLUG = {"balinese":"balinese-massage","deep-tissue":"deep-tissue-massage","swedish":"swedish-massage","thai":"thai-massage","prenatal":"prenatal-massage","postnatal":"postnatal-massage","sports":"sports-massage","ayurvedic":"ayurvedic-massage","reflexology":"foot-massage-reflexology","lymphatic":"lymphatic-drainage-massage","modero":"modero-therapy","hot-stone":"hot-stone-massage","cupping":"cupping-therapy","four-hands":"four-hands-massage","couple":"couple-massage"}
WA_SVG='<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5.1-1.3A10 10 0 1 0 12 2zm0 18.2a8.2 8.2 0 0 1-4.2-1.2l-.3-.2-3 .8.8-3-.2-.3A8.2 8.2 0 1 1 12 20.2zm4.6-6.1c-.3-.1-1.5-.7-1.7-.8-.2-.1-.4-.1-.6.1-.2.3-.7.8-.8 1-.1.2-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.2-.4.6-1.3.1-.2 0-.4 0-.5l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5c-.2 0-.5.1-.7.3-.2.3-.9.9-.9 2.2s1 2.5 1.1 2.7c.1.2 1.9 3 4.7 4.2.7.3 1.2.5 1.6.6.7.2 1.3.2 1.8.1.6-.1 1.5-.6 1.7-1.2.2-.6.2-1.1.1-1.2 0-.1-.2-.2-.5-.3z"/></svg>'
BADGE = '''<a href="https://realplannet.com" class="rp-badge" target="_blank" rel="noopener" title="Built by Real Plannet">
        <div class="rp-badge-orb">
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" fill="none">
            <defs><linearGradient id="rpBG" x1="20" y1="16" x2="44" y2="48" gradientUnits="userSpaceOnUse"><stop stop-color="#e8c97a"/><stop offset="1" stop-color="#c9a84c"/></linearGradient></defs>
            <ellipse cx="32" cy="33" rx="27" ry="9.5" transform="rotate(-20 32 33)" stroke="#c9a84c" stroke-width="1.4" opacity="0.45"/>
            <circle cx="32" cy="30" r="13" fill="url(#rpBG)"/>
            <path d="M5.5 38 A27 9.5 0 0 0 58.5 28" transform="rotate(-20 32 33)" stroke="#c9a84c" stroke-width="1.8" fill="none"/>
          </svg>
        </div>
        <div class="rp-badge-text">
          <span>Built by</span>
          <span>Real <em>Plannet</em></span>
        </div>
</a>'''

NAV = [("Price List","price-list.html"),("Services",None),("Packages","packages.html"),("Bridal","bridal.html"),("Gift Vouchers","gift-vouchers.html"),("About",None)]
def services_dd():
    out=[(CATS[c][0],CATS[c][2]+".html") for c in CATS]
    return out
ABOUT_DD=[("Our Story","about.html"),("Meet Our Therapists","meet-our-therapists.html"),("Areas We Serve","areas-we-serve.html"),("Reviews","reviews.html"),("FAQs","faqs.html"),("Contact","contact.html")]

def header(active):
    nav=""
    for label,href in NAV:
        if label=="Services":
            dd="".join(f'<a href="{h}">{esc(n)}</a>' for n,h in services_dd())
            dd+='<a href="services.html">All services</a>'
            nav+=f'<li><a class="nl{" on" if active=="services" else ""}" href="services.html">Services ▾</a><div class="dd">{dd}</div></li>'
        elif label=="About":
            dd="".join(f'<a href="{h}">{esc(n)}</a>' for n,h in ABOUT_DD)
            nav+=f'<li><a class="nl{" on" if active=="about" else ""}" href="about.html">About ▾</a><div class="dd">{dd}</div></li>'
        else:
            on=" on" if active==href.replace(".html","") else ""
            nav+=f'<li><a class="nl{on}" href="{href}">{label}</a></li>'
    dr='<a href="price-list.html">Price List</a><a href="services.html">Services</a>'
    dr+="".join(f'<a class="sub" href="{h}">{esc(n)}</a>' for n,h in services_dd())
    dr+='<a href="packages.html">Packages</a><a href="bridal.html">Bridal</a><a href="gift-vouchers.html">Gift Vouchers</a><a href="about.html">About</a><a href="meet-our-therapists.html">Our Therapists</a><a href="areas-we-serve.html">Areas We Serve</a><a href="reviews.html">Reviews</a><a href="faqs.html">FAQs</a><a href="contact.html">Contact</a><a href="ar.html" lang="ar">عربي</a>'
    dr+=f'<a class="btn" href="book.html">Book a Treatment</a>'
    return f'''<a class="skip" href="#main">Skip to content</a>
<header class="hdr"><div class="in">
<a class="brand" href="index.html" aria-label="Sahara Balinese Spa &amp; Salon — home"><img src="assets/img/logo-mark.webp" alt="" width="38" height="44"><span><b>SAHARA BALINESE</b><small>SPA &amp; SALON · DUBAI</small></span></a>
<ul class="nav">{nav}</ul>
<div class="cta"><button class="themebtn" type="button" aria-label="Switch to light mode" title="Light / dark mode"><svg class="i-sun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg><svg class="i-moon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><path d="M21 13A9 9 0 1 1 11 3a7 7 0 0 0 10 10z"/></svg></button><a class="btn sm ghost" href="ar.html" lang="ar">عربي</a><a class="btn sm" href="book.html">Book Now</a><button class="burger" type="button" aria-label="Menu" aria-expanded="false" aria-controls="drawer"><i></i></button></div>
</div></header>
<nav class="drawer" id="drawer" aria-label="Mobile">{dr}</nav>'''

def footer():
    svc="".join(f'<li><a href="{h}">{esc(n)}</a></li>' for n,h in services_dd())
    return f'''<footer class="ftr"><div class="wrap">
<div class="fcols">
<div><a class="brand" href="index.html"><img src="assets/img/logo-mark.webp" alt="" width="38" height="44"><span><b>SAHARA BALINESE</b><small>SPA &amp; SALON · DUBAI</small></span></a>
<p style="font-size:14.5px;max-width:300px">Balinese spa &amp; salon treatments delivered to your home, hotel or villa across Dubai.</p>
<p style="margin-top:14px"><a href="{INSTAGRAM}" target="_blank" rel="noopener">Instagram</a> · <a href="{FACEBOOK}" target="_blank" rel="noopener">Facebook</a> · <a href="{GOOGLE_REVIEW}" target="_blank" rel="noopener" data-track="review_click">★ Review us on Google</a></p></div>
<div><h4>Explore</h4><ul><li><a href="price-list.html">Price List</a></li><li><a href="packages.html">Packages</a></li><li><a href="bridal.html">Bridal</a></li><li><a href="gift-vouchers.html">Gift Vouchers</a></li><li><a href="meet-our-therapists.html">Our Therapists</a></li><li><a href="areas-we-serve.html">Areas We Serve</a></li><li><a href="reviews.html">Reviews</a></li><li><a href="faqs.html">FAQs</a></li><li><a href="about.html">About</a></li></ul></div>
<div><h4>Services</h4><ul>{svc}<li><a href="book.html">Book a Treatment</a></li></ul></div>
<div><h4>Contact</h4><ul><li>Mobile service across Dubai</li><li>Open {HOURS}</li><li><a href="mailto:{EMAIL}">{EMAIL}</a></li><li><a href="tel:+{PHONE}">{PHONE_DISPLAY}</a></li><li><a href="tel:+{PHONE2}">{PHONE2_DISPLAY}</a></li><li><a href="{WA_HELLO}" target="_blank" rel="noopener">Chat on WhatsApp</a></li></ul></div>
</div>
<div class="fine"><span>© 2026 Sahara Balinese Spa &amp; Salon · Dubai, UAE</span><span><a href="terms-conditions.html">Terms &amp; Cancellation</a> · <a href="privacy-policy.html">Privacy</a></span></div>
</div></footer>
<div class="mbar"><a class="a" href="{WA_HELLO}" target="_blank" rel="noopener">WhatsApp</a><a class="b" href="book.html">Book Now</a></div>
<a class="wafab" href="{WA_HELLO}" target="_blank" rel="noopener" aria-label="Chat on WhatsApp">{WA_SVG}</a>
{BADGE}'''

GA4_ID="G-HD07N96RGX"; GTM_ID="GTM-W9GSDCS7"
TRACK_HEAD=f"""<script async src="https://www.googletagmanager.com/gtag/js?id={GA4_ID}"></script>
<script src="assets/js/analytics.js"></script>
<script>(function(w,d,s,l,i){{w[l]=w[l]||[];w[l].push({{'gtm.start':new Date().getTime(),event:'gtm.js'}});var f=d.getElementsByTagName(s)[0],j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src='https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);}})(window,document,'script','dataLayer','{GTM_ID}');</script>
"""
TRACK_BODY=f'<noscript><iframe src="https://www.googletagmanager.com/ns.html?id={GTM_ID}" height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>'

def page(fname, title, desc, body, active="", schema=None, hero_img=None, extra_head=""):
    LIVE=(f'<script>window.SAHARA_API="{API_BASE}"</script>\n<script src="assets/js/live.js" defer></script>\n' if API_BASE else "")
    SYNC=(f'<script>window.SAHARA_API="{API_BASE}"</script>\n<script src="assets/js/menu-sync.js"></script>\n' if API_BASE else "")
    canon=f"{BASE}/{'' if fname=='index.html' else fname}"
    sch="".join(f'<script type="application/ld+json">{json.dumps(s,ensure_ascii=False)}</script>' for s in (schema or []))
    return f'''<!DOCTYPE html>
<html lang="en" class="nojs">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{canon}">
<meta property="og:type" content="website"><meta property="og:site_name" content="Sahara Balinese Spa &amp; Salon"><meta property="og:title" content="{esc(title)}"><meta property="og:description" content="{esc(desc)}"><meta property="og:url" content="{canon}"><meta property="og:image" content="{BASE}/assets/img/spa-massage-1.webp">
<meta name="theme-color" content="#0A0602">
{TRACK_HEAD}<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;1,300;1,400&family=Playfair+Display:ital,wght@0,400;0,500;0,700;1,400&family=Raleway:wght@200;300;400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/site.css">
<script>document.documentElement.classList.remove('nojs');try{{var t=localStorage.getItem('sahara-theme');if(t==='light')document.documentElement.setAttribute('data-theme','light')}}catch(e){{}}</script>
{sch}{extra_head}
</head>
<body>
{TRACK_BODY}
{header(active)}
<main id="main">
{body}
</main>
{footer()}
<script src="assets/js/data.js"></script>
{SYNC}<script src="assets/js/site.js"></script>
{LIVE}<script src="assets/js/gold-dust.js" defer></script>
</body>
</html>
'''

def crumbs(*items):
    out='<div class="crumbs"><a href="index.html">Home</a>'
    for label,href in items:
        out+=f'<span>/</span>'+(f'<a href="{href}">{esc(label)}</a>' if href else esc(label))
    return out+'</div>'

def crumb_schema(fname, *items):
    el=[{"@type":"ListItem","position":1,"name":"Home","item":BASE+"/"}]
    for i,(label,href) in enumerate(items,2):
        el.append({"@type":"ListItem","position":i,"name":label,"item":f"{BASE}/{href or fname}"})
    return {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":el}

def pagehero(eyebrow,h1,lead,crumb_html=""):
    return f'<section class="pagehero"><div class="wrap">{crumb_html}<span class="eyebrow">{esc(eyebrow)}</span><h1>{h1}</h1><p class="lead">{esc(lead)}</p></div></section>'

def cta_band(h="Ready when you are.",p="Choose your treatment and we confirm personally on WhatsApp.",extra=""):
    return f'''<section class="sec band"><div class="wrap rv"><span class="eyebrow">Book</span><h2 style="margin:18px 0 12px">{h}</h2><p style="max-width:520px;margin:0 auto">{p}</p><div class="btns"><a class="btn" href="book.html">Book a Treatment</a><a class="btn wa" href="{WA_HELLO}" target="_blank" rel="noopener">WhatsApp Us</a></div>{extra}</div></section>'''

def review_band(h="Loved your Sahara experience?", p="Your Google review helps other families and professionals in Dubai find a trusted home spa. It takes under a minute."):
    return f'''<section class="sec"><div class="wrap center"><div class="rv panel" style="max-width:680px;margin:0 auto;text-align:center"><div aria-hidden="true" style="color:var(--gold);font-size:24px;letter-spacing:6px">★★★★★</div><h2 style="margin:12px 0 10px;font-size:clamp(24px,4vw,32px)">{h}</h2><p style="max-width:520px;margin:0 auto">{p}</p><div class="btns"><a class="btn" href="{GOOGLE_REVIEW}" target="_blank" rel="noopener" data-track="review_click">Leave a Google review</a></div></div></div></section>'''

def faq_html(faqs, schema_out=None):
    rows="".join(f'<details><summary>{esc(q)}</summary><div class="ans"><p>{esc(a)}</p></div></details>' for q,a in faqs)
    return f'<div class="acc">{rows}</div>'
def faq_schema(faqs):
    return {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faqs]}

CAT_COVER={"massage":"balinese","facial":"rejuvenating-facial","body":"body-scrub","nails":"manicure","corporate":"corporate"}
def cat_img(c):
    return f'<div class="cimg"><img src="assets/services/{CAT_COVER.get(c,"balinese")}.webp" alt="{esc(CATS[c][0])} at home in Dubai" loading="lazy" width="960" height="640"></div>'

def price_rows(cat, with_book=True):
    rows=""
    for it in items(cat):
        d=dur_label(it)
        rows+=f'<tr><td class="n"><div class="rw"><img class="rimg" data-svc-img data-rid="{it[0]}" src="assets/services/{it[0]}.webp" alt="{esc(it[1])}" loading="lazy" width="96" height="64"><div><b>{esc(it[1])}</b><span>{esc(it[2])}</span></div></div></td><td>{esc(d) if d else "—"}</td><td class="p">{esc(price_label(it))}</td><td class="b"><a class="btn sm ghost" href="book.html?treatment={it[0]}">Book</a></td></tr>'
    return f'<table class="ptable" data-menu-cat="{cat}"><thead><tr><th>Treatment</th><th>Duration</th><th>Price</th><th></th></tr></thead><tbody>{rows}</tbody></table>'

def data_js():
    d={"slug":SLUG,"treatmentPages":[k for k in TX if k in SLUG],"stock":[i[0] for i in ITEMS if os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)),"..","assets","services",i[0]+".webp"))],"phone":PHONE,"minOrder":MIN_ORDER,"cats":{c:{"name":CATS[c][0]} for c in CATS},
       "items":[{"id":i[0],"name":i[1],"blurb":i[2],"opts":[list(o) for o in i[3]],"cat":i[4]} for i in ITEMS]}
    return "window.SAHARA="+json.dumps(d,ensure_ascii=False)+";"
