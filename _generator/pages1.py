from lib import *

def home():
    cat_cards=""
    for c in CATS:
        its=items(c); fr=min(frm(i) for i in its)
        cat_cards+=f'<a class="card link svc rv" href="{CATS[c][2]}.html">{cat_img(c)}<h3>{esc(CATS[c][0])}</h3><p>{esc(CATS[c][1])}</p><span class="from" data-from-cat="{c}">From AED {fr}</span><span class="more">Explore →</span></a>'
    pk="".join(f'<div class="card rv"><span class="num">{r}</span><h3>{esc(n)}</h3><p>{esc(t)}</p><span class="from">AED {p} · {esc(d)}</span><a class="more" href="packages.html">View package →</a></div>' for r,n,t,inc,d,p in PACKAGES)
    gal=''.join(f'<div class="photo rv"><img src="assets/img/{f}" alt="{a}" loading="lazy"></div>' for f,a in [("spa-massage-2.webp","Therapist giving a shoulder massage with Balinese oil"),("image6.webp","Two Sahara therapists giving a poolside massage"),("image10.webp","Sahara therapists giving a treatment by the pool"),("image8.webp","Treatment room set up with Balinese textiles"),("spa-massage-1.webp","Relaxing head and ear massage surrounded by tropical plants")])
    ritual=[("Two hours · seven movements","An uninterrupted sequence, opened with a footbath of warm water and flower petals."),("Frangipani-infused coconut oil","Cold-pressed virgin coconut oil, steeped with frangipani and a trace of lemongrass."),("Warmed volcanic basalt","Stones gathered from the island's rivers, warmed to the temperature of resting skin."),("Balinese palm-pressure lineage","Long, unbroken strokes drawn from a technique passed down within healing families."),("One therapist, uninterrupted","A single certified Balinese therapist attends the full two hours. No handovers."),("Jasmine steam finish","Closed with warm towels infused with jasmine, and a moment of stillness.")]
    rit="".join(f'<div class="rv"><span class="num">0{i+1}</span><h3 style="font-size:20px">{esc(t)}</h3><p style="font-size:14.5px;margin-top:6px">{esc(d)}</p></div>' for i,(t,d) in enumerate(ritual))
    body=f'''
<section class="hero"><div class="bg" style="background-image:url(assets/img/spa-massage-1.webp)" role="img" aria-label="Relaxing head massage surrounded by tropical plants"></div>
<div class="wrap"><span class="eyebrow">Est. Bali · Practised in Dubai</span>
<h1>Balinese spa, <em>brought to your door.</em></h1>
<p class="lead">Certified Balinese therapists, luxury ritual products and in-room treatments at your home, hotel or villa across Dubai.</p>
<p class="price">Massage from <b data-from-cat="massage">AED 250</b> · Facials from <b data-from-cat="facial" data-bare="1">AED 200</b> · Travel included</p>
<div class="btns"><a class="btn" href="book.html">Book a Treatment</a><a class="btn ghost" href="price-list.html">View Price List</a></div></div><div class="scrollcue" aria-hidden="true"></div></section>
<section class="trust"><div class="wrap"><ul><li><b>20+</b><span>Years of experience</span></li><li><b data-staff-count="1">8</b><span>Balinese therapists</span></li><li><b>10 AM–12 AM</b><span>Open 7 days</span></li><li><b>Same-day</b><span>Bookings accepted</span></li></ul></div></section>

<section class="sec"><div class="wrap split">
<div class="rv"><span class="eyebrow">About Us</span><h2 style="margin:18px 0 20px">Rooted in Bali. <em>Refined in Dubai.</em></h2>
<p>Sahara Balinese Spa &amp; Salon is a mobile spa service. Every therapist is certified, background-verified, fully insured and personally trained by our founder Neny Trisnayanti, who brings 20+ years of five-star hotel wellness experience.</p>
<p>No traffic and no waiting room. We bring a professional massage table, fresh linens and towels, Balinese oils and all equipment, and set everything up in your home, villa or hotel room.</p>
<p style="font-family:var(--cg);font-style:italic;font-size:22px;color:var(--cream)">Your space. Your therapist. Your calm.</p>
<div class="btns"><a class="btn ghost" href="about.html">Our Story</a><a class="btn ghost" href="meet-our-therapists.html">Meet the Therapists</a></div></div>
<div class="photo tall rv"><img src="assets/img/spa-massage-2.webp" alt="Therapist giving a shoulder massage with Balinese oil" loading="lazy"></div></div></section>

<section class="sec alt"><div class="wrap"><div class="sechead center rv"><span class="eyebrow">Our Services</span><h2>The complete <em>Sahara menu</em></h2><p>Massage, facials, body scrubs, nails and corporate wellness — all delivered to you.</p></div>
<div class="grid g3">{cat_cards}</div></div></section>

<section class="sec"><div class="wrap"><div class="sechead center rv"><span class="eyebrow">The Sahara Ritual</span><h2>The Ritual, <em>unfolded.</em></h2><p>In Bali, healing is not a service. It is a sequence — pressure, warmth, oil, breath — kept within families and taught by touch.</p></div>
<div class="grid g3">{rit}</div><div class="btns rv" style="justify-content:center"><a class="btn" href="packages.html">View Signature Packages</a></div></div></section>

<section class="sec alt"><div class="wrap split rev">
<div class="rv"><span class="eyebrow">How It Works</span><h2 style="margin:18px 0 26px">Simple, <em>from first message.</em></h2>
<ol class="steps"><li><h3>Choose your treatment</h3><p>Browse the menu and use our guided booking page, or just message us on WhatsApp.</p></li><li><h3>We confirm personally</h3><p>Book via Fresha or WhatsApp. Same-day appointments are accepted; for weekends and evenings we suggest 24–48 hours ahead.</p></li><li><h3>We arrive with everything</h3><p>Table, linens, towels, oils and equipment. You only need a clear space of about 2 m × 2 m.</p></li><li><h3>Relax</h3><p>Your treatment ends where you want to be — at home, free to keep relaxing.</p></li></ol>
<div class="btns"><a class="btn" href="book.html">Start Booking</a></div></div>
<div class="photo tall rv"><img src="assets/img/image8.webp" alt="Treatment room set up with Balinese textiles" loading="lazy"></div></div></section>

<section class="sec"><div class="wrap"><div class="sechead center rv"><span class="eyebrow">Signature Packages</span><h2>Curated <em>combinations</em></h2></div><div class="grid g4">{pk}</div></div></section>

<section class="sec alt"><div class="wrap"><div class="sechead center rv"><span class="eyebrow">Gallery</span><h2>Sahara <em>in practice</em></h2></div><div class="gal">{gal}</div></div></section>

<section class="sec"><div class="wrap split"><div class="rv"><span class="eyebrow">Areas We Serve</span><h2 style="margin:18px 0 18px">All of Dubai — <em>we come to you.</em></h2><p>Homes, apartments, villas, hotels and serviced residences, including gated communities. Not sure we cover your area? WhatsApp us your location.</p><div class="btns"><a class="btn ghost" href="areas-we-serve.html">See Areas</a></div></div>
<ul class="areas rv">{"".join(f"<li>{esc(a)}</li>" for a in AREAS[:12])}</ul></div></section>

<section class="sec alt"><div class="wrap"><div class="sechead center rv"><span class="eyebrow">Good to know</span><h2>Frequently asked <em>questions</em></h2></div><div class="rv" style="max-width:860px;margin:0 auto">{faq_html(FAQS[:5])}<div class="btns" style="justify-content:center"><a class="btn ghost" href="faqs.html">All FAQs</a></div></div></div></section>
{review_band()}{cta_band("Reserve your Sahara treatment.","A message is all it takes. Book on WhatsApp or choose your treatment online.")}'''
    dayspa={"@context":"https://schema.org","@type":"DaySpa","name":"Sahara Balinese Spa & Salon","description":"Balinese spa and salon treatments delivered to your home, hotel or villa in Dubai.","url":BASE+"/","telephone":"+"+PHONE,"email":EMAIL,"areaServed":{"@type":"City","name":"Dubai"},"address":{"@type":"PostalAddress","addressLocality":"Dubai","addressCountry":"AE"},"openingHoursSpecification":{"@type":"OpeningHoursSpecification","dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"],"opens":"10:00","closes":"00:00"},"sameAs":[INSTAGRAM,FACEBOOK,TIKTOK]}
    return page("index.html","Home Spa & Massage in Dubai | Sahara Balinese Spa & Salon","Balinese massage, facials, body scrubs and nails at your home, hotel or villa across Dubai. Certified therapists, travel included, open 10 AM–12 AM.",body,"index",[dayspa])

def price_list():
    chips="".join(f'<a class="chip" href="#{c}">{esc(CATS[c][0])}</a>' for c in CATS)
    groups=""
    for c in CATS:
        groups+=f'<section class="pgroup" id="{c}"><h2>{esc(CATS[c][0])}</h2><p>{esc(CATS[c][1])}</p>{price_rows(c)}</section>'
    body=pagehero("Price List",'Home spa prices <em>in Dubai</em>',"All prices include therapist travel within Dubai. Minimum booking value AED 200.",crumbs(("Price List",None)))+f'''
<section class="sec" style="padding-top:40px"><div class="wrap"><div class="ptabs" role="navigation" aria-label="Price categories">{chips}</div>{groups}
<div class="note"><b style="color:var(--cream)">Pricing note.</b> All prices are inclusive of therapist travel to your location within Dubai. A minimum order of AED {MIN_ORDER} applies per booking. Prices shown are indicative and may vary based on location and session requirements — please confirm final pricing at booking. Contact us for custom group or event packages.</div>
<div class="btns"><a class="btn" href="book.html">Book a Treatment</a><a class="btn ghost" href="packages.html">Signature Packages</a><a class="btn ghost" href="gift-vouchers.html">Gift Vouchers</a></div></div></section>'''
    return page("price-list.html","Price List | Home Spa & Massage Dubai | Sahara Balinese Spa","Sahara Balinese Spa price list: massage from AED 250, facials from AED 200, body scrubs, nails and corporate wellness. Travel within Dubai included.",body,"price-list",[crumb_schema("price-list.html",("Price List",None))])

def svc_card(i, href=None, more=""):
    id_=i[0]; href=href or (SLUG[id_]+".html" if id_ in SLUG and id_ in TX else f"book.html?treatment={id_}")
    m=f'<span class="more">{more}</span>' if more else ""
    return (f'<a class="card link svc rv" data-svc="{id_}" href="{href}"><div class="cimg"><img data-svc-img src="assets/services/{id_}.webp" alt="{esc(i[1])} at home in Dubai" loading="lazy" width="960" height="640"></div>'
            f'<h3 style="font-size:21px">{esc(i[1])}</h3><p>{esc(i[2])}</p><span class="from" data-price-svc="{id_}">{esc(price_label(i))}</span>{m}</a>')

def services():
    cards=""
    for c in CATS:
        its=items(c); fr=min(frm(i) for i in its)
        cards+=f'<a class="card link svc rv" href="{CATS[c][2]}.html">{cat_img(c)}<h3>{esc(CATS[c][0])}</h3><p>{esc(CATS[c][1])}</p><span class="from" data-from-cat="{c}" data-count="1">From AED {fr} · {len(its)} treatments</span><span class="more">Explore →</span></a>'
    mcards="".join(svc_card(i) for i in items("massage"))
    body=pagehero("Services",'Our <em>services</em>',"The complete Sahara menu — all prices inclusive, all services mobile.",crumbs(("Services",None)))+f'''
<section class="sec"><div class="wrap"><div class="grid g3">{cards}</div></div></section>
<section class="sec alt"><div class="wrap"><div class="sechead rv"><span class="eyebrow">Massage Therapy</span><h2>Massage <em>treatments</em></h2></div><div class="grid g3" data-svc-grid="massage">{mcards}</div></div></section>{cta_band()}'''
    return page("services.html","Services | Massage, Facials, Body Scrub & Nails | Sahara Dubai","Explore Sahara's home spa menu in Dubai: Balinese, deep tissue, hot stone and Thai massage, facials, body scrubs, nails and corporate wellness.",body,"services",[crumb_schema("services.html",("Services",None))])

def category(c):
    name,desc,slug=CATS[c]
    extra=""
    extra=f'<div class="grid g3" data-svc-grid="{c}" style="margin-bottom:56px">'+"".join(svc_card(i,more=("Learn more →" if i[0] in SLUG and i[0] in TX else "Book →")) for i in items(c))+'</div>'+price_rows(c)
    body=pagehero(name,f'{esc(name)} <em>at home in Dubai</em>',desc,crumbs(("Services","services.html"),(name,None)))+f'<section class="sec" style="padding-top:48px"><div class="wrap">{extra}<div class="btns"><a class="btn" href="book.html">Book a Treatment</a><a class="btn ghost" href="price-list.html">Full Price List</a></div></div></section>{cta_band()}'
    return page(f"{slug}.html",f"{name} at Home in Dubai | Sahara Balinese Spa",f"{desc} Travel included across Dubai.",body,"services",[crumb_schema(f"{slug}.html",("Services","services.html"),(name,None))])

def treatment(it):
    id_=it[0]; t=TX[id_]; slug=SLUG[id_]
    rows="".join(f'<tr><td class="n"><b>{o[0]} minutes</b></td><td class="p">AED {o[1]}</td><td class="b"><a class="btn sm ghost" href="book.html?treatment={id_}">Book</a></td></tr>' for o in it[3])
    best="".join(f"<li>{esc(b)}</li>" for b in t["best"])
    others=[i for i in items("massage") if i[0]!=id_][:3]
    rel="".join(svc_card(i) for i in others)
    img=f"services/{id_}.webp"
    note="<p class=\"note\">Pregnant, injured or managing a medical condition? Tell us before you book so we can tailor the treatment or advise if it isn’t suitable.</p>"
    faq=t["faq"]+[("What do you bring?","Everything: a professional massage table, fresh linens and towels, and Balinese oils. You only need a clear space of about 2 m × 2 m."),("Can I request a specific therapist?","Yes — mention your preferred therapist when booking and we will try to send her, subject to availability.")]
    body=pagehero(it[1],f'{esc(it[1])} <em>at home in Dubai</em>',it[2]+". Delivered by certified Balinese therapists.",crumbs(("Services","services.html"),(it[1],None)))+f'''
<section class="sec"><div class="wrap split"><div class="rv"><span class="eyebrow">The treatment</span><h2 style="margin:18px 0 20px">What is <em>{esc(it[1].lower())}?</em></h2><p data-svc-desc>{esc(t["what"])}</p><p><b style="color:var(--cream)">Pressure:</b> {esc(t["pressure"])}</p><div class="btns"><a class="btn" href="book.html?treatment={id_}">Book This Treatment</a><a class="btn wa" href="{WA_HELLO}" target="_blank" rel="noopener">WhatsApp</a></div></div>
<div class="photo tall rv"><img data-svc-img data-svc-hero="{id_}" src="assets/{img}" alt="{esc(it[1])} by a Sahara therapist at home in Dubai" loading="eager"></div></div></section>
<section class="sec alt"><div class="wrap split"><div class="rv"><span class="eyebrow">Is it right for you?</span><h2 style="margin:18px 0 20px">Who <em>loves it</em></h2><ul class="ticks" data-svc-benefits>{best}</ul>{note}</div>
<div class="rv"><span class="eyebrow">Prices</span><h2 style="margin:18px 0 10px">{esc(it[1])} <em>prices</em></h2><table class="ptable"><thead><tr><th>Duration</th><th>Price</th><th></th></tr></thead><tbody data-svc-rows="{id_}">{rows}</tbody></table><p style="font-size:14px;margin-top:14px">Prices include travel within Dubai. Minimum booking value AED {MIN_ORDER}.</p></div></div></section>
<section class="sec"><div class="wrap split rev"><div class="rv"><span class="eyebrow">Your appointment</span><h2 style="margin:18px 0 26px">What <em>happens</em></h2><ol class="steps"><li><h3>Your therapist arrives</h3><p>She arrives on time with the table, linens, towels and oils, and sets up quietly.</p></li><li><h3>A short consultation</h3><p>Tell her about sensitive areas, health conditions and your preferred pressure.</p></li><li><h3>Your treatment</h3><p>Relax while she works, adapting pressure as she goes.</p></li><li><h3>Aftercare</h3><p>Drink some water and take it easy — no traffic to face.</p></li></ol></div>
<div class="rv"><span class="eyebrow">Good to know</span><h2 style="margin:18px 0 20px">Frequently asked <em>questions</em></h2>{faq_html(faq)}</div></div></section>
<section class="sec alt"><div class="wrap"><div class="sechead rv"><span class="eyebrow">You may also like</span><h2>Related <em>treatments</em></h2></div><div class="grid g3">{rel}</div></div></section>{cta_band()}'''
    svc={"@context":"https://schema.org","@type":"Service","name":it[1],"description":it[2],"provider":{"@type":"DaySpa","name":"Sahara Balinese Spa & Salon"},"areaServed":"Dubai","offers":[{"@type":"Offer","priceCurrency":"AED","price":str(o[1])} for o in it[3]]}
    return page(f"{slug}.html",f"{it[1]} at Home in Dubai | From AED {frm(it)} | Sahara",f"{it[1]} at home in Dubai by certified Balinese therapists. From AED {frm(it)}, travel included. Book on WhatsApp or online.",body,"services",[crumb_schema(f"{slug}.html",("Services","services.html"),(it[1],None)),svc,faq_schema(faq)])

def book():
    goals=[("Relax & unwind","balinese,swedish,reflexology,ayurvedic","Balinese and Swedish are our calming, full-body favourites."),("Muscle pain & tension","deep-tissue,hot-stone,cupping,sports","Firmer treatments for knots, stiffness and recovery."),("Pregnancy & new mums","prenatal,postnatal","Gentle, supportive massage before and after birth."),("Glow & skin","rejuvenating-facial,express-facial","Facials tailored to your skin."),("Body renewal","body-scrub,express-body-scrub","Scrubs to exfoliate and refresh."),("Nails & more","manicure,pedicure,mani-pedi,couple,four-hands","Polish, plus treatments for two.")]
    gb="".join(f'<button type="button" class="chip" data-goal="{g[1]}" data-note="{esc(g[2])}">{esc(g[0])}</button>' for g in goals)
    body=pagehero("Book",'Book a treatment <em>at home</em>',("Choose your treatment, pick a free time and confirm online. Your therapist arrives at your door." if API_BASE else "Choose your treatment, pick a time and send your request on WhatsApp. We confirm personally."),crumbs(("Book",None)))+f'''
<section class="sec" style="padding-top:48px"><div class="wrap" id="booking" style="max-width:960px">
<form id="bk-form" novalidate>
<div class="panel"><h2><span class="stn">1</span>Choose your treatment</h2><p class="sub">Not sure? Tell us what you’re after.</p>
<div class="chips" style="margin-bottom:8px">{gb}<button type="button" class="chip" id="goal-clear">Show all</button></div><p id="goal-note" style="font-size:14px;margin:10px 0 18px;color:var(--gold2)"></p>
<div class="opts" id="tx-opts"></div></div>
<div class="panel" id="step2"><h2><span class="stn">2</span>Guests &amp; duration</h2><p class="sub">Who is it for?</p>
<div class="chips"><button type="button" class="chip on" data-g="1">Just me</button><button type="button" class="chip" data-g="2">Couple · 2 therapists</button><button type="button" class="chip" data-g="3">Group (3 or more)</button></div>
<div id="grp-wrap" class="hide"><label for="grp">Number of guests</label><input id="grp" type="number" min="3" max="20" value="3" inputmode="numeric"></div>
<p class="lab">Duration</p><div class="opts" id="dur-opts"></div>
<p style="font-size:13.5px;margin-top:16px">Couples and groups are an estimate (price × guests). See <a href="packages.html">Couples Sanctuary</a> for the package rate. Final price confirmed on WhatsApp.</p></div>
<div class="panel"><h2><span class="stn">3</span>Date &amp; time</h2><p class="sub">Same-day bookings accepted. Open 10 AM – 12 AM.</p>
<div class="frow"><div><label for="date">Date</label><input id="date" type="date"></div><div><label for="time">Preferred start time</label><select id="time"></select></div></div></div>
<div class="panel"><h2><span class="stn">4</span>Your details</h2><p class="sub">&nbsp;</p>
<div class="frow"><div><label for="fn">First name</label><input id="fn" autocomplete="given-name"></div><div><label for="ln">Last name</label><input id="ln" autocomplete="family-name"></div></div>
<label for="wnum">WhatsApp number</label><input id="wnum" type="tel" inputmode="tel" autocomplete="tel" placeholder="+971 5X XXX XXXX"></div>
<div class="panel"><h2><span class="stn">5</span>Where should we come?</h2><p class="sub">An exact pin helps our therapist find you, especially for villas.</p>
<button type="button" class="btn sm ghost" id="geo">Use my current location</button>
<label for="pin">Google Maps pin (optional)</label><input id="pin" inputmode="url" placeholder="Paste a Google Maps link">
<div class="frow"><div><label for="bldg">Building or villa community</label><input id="bldg"></div><div><label for="apt">Apartment or villa no.</label><input id="apt"></div></div>
<label for="notes">Anything we should know? (optional)</label><textarea id="notes" placeholder="Preferred therapist, health notes, hotel room details…"></textarea>
<label for="heard">How did you hear about us?</label><select id="heard"><option value="">Choose one</option><option>Google search</option><option>Instagram</option><option>Facebook</option><option>TikTok</option><option>Friend or family</option><option>I’ve booked with Sahara before</option><option>Other</option></select></div>
<div class="est"><div><small id="est-note">Choose a treatment to see an estimate</small><span class="t" id="est-total">—</span></div><button class="btn wa" type="submit">Send on WhatsApp</button></div>
<p class="err" id="bk-err" role="alert"></p><div id="bk-ok"></div>
</form>
<p style="font-size:14px;margin-top:22px">{"" if API_BASE else f'Prefer to book instantly? <a href="{FRESHA}" target="_blank" rel="noopener">Book on Fresha</a> · '}Cancellation: 3 hours’ notice — see <a href="terms-conditions.html">terms</a>.</p>
</div></section>'''
    return page("book.html","Book a Home Spa Treatment in Dubai | Sahara Balinese Spa","Book Balinese massage, facials, body scrubs and nails at home in Dubai. Choose your treatment and time; we confirm on WhatsApp.",body,"book",[crumb_schema("book.html",("Book",None))])
