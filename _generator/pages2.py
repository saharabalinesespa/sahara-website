from lib import *

def packages():
    cards=""
    for r,n,t,inc,d,p in PACKAGES:
        li="".join(f"<li>{esc(x)}</li>" for x in inc)
        wl=WA("Hi%20Sahara%2C%20I%27d%20like%20to%20book%20the%20"+n.replace(" ","%20")+"%20package.")
        cards+=f'<div class="card rv"><span class="num">Package {r}</span><h3>{esc(n)}</h3><p>{esc(t)}</p><ul class="ticks" style="margin:16px 0">{li}</ul><p style="font-size:12px;letter-spacing:.2em;text-transform:uppercase;color:var(--gold)">{esc(d)}</p><span class="from" style="font-size:30px">AED {p}</span><div class="btns" style="margin-top:18px"><a class="btn sm" href="{wl}" target="_blank" rel="noopener">Book Now</a></div></div>'
    body=pagehero("Packages",'Signature <em>packages</em>',"Curated combinations for the ultimate Sahara experience.",crumbs(("Packages",None)))+f'''
<section class="sec" style="padding-top:48px"><div class="wrap"><div class="grid g2">{cards}</div>
<div class="grid g2" style="margin-top:32px"><div class="card rv"><span class="eyebrow">Special Occasion</span><h3 style="margin:14px 0 8px">Bridal Packages</h3><p>From pre-wedding pampering to day-of beauty, Sahara takes care of the entire bridal party.</p><a class="more" href="bridal.html">See Bridal Packages →</a></div><div class="card rv"><span class="eyebrow">Corporate &amp; Hotel</span><h3 style="margin:14px 0 8px">Group &amp; Event Wellness</h3><p>On-site wellness for hotel pool decks, corporate events and VIP gatherings. Multiple therapists, any scale.</p><a class="more" href="{WA("Hi%20Sahara%2C%20I%27d%20like%20to%20enquire%20about%20a%20group%20or%20corporate%20event.")}" target="_blank" rel="noopener">Enquire via WhatsApp →</a></div></div></div></section>{cta_band("Book your package.")}'''
    return page("packages.html","Signature Packages | Sahara Balinese Spa Dubai","Sahara signature spa packages in Dubai: The Sahara Ritual, Bali Serenity, Couples Sanctuary and The Royal Indulgence. Delivered to your home or hotel.",body,"packages",[crumb_schema("packages.html",("Packages",None))])

def bridal():
    cards=""
    for tag,n,t,inc,d,p in BRIDAL:
        li="".join(f"<li>{esc(x)}</li>" for x in inc)
        wl=WA("Hi%20Sahara%2C%20I%27d%20like%20to%20enquire%20about%20the%20"+n.replace(" ","%20")+"%20bridal%20package.")
        cards+=f'<div class="card rv"><span class="eyebrow">{esc(tag)}</span><h3 style="margin:14px 0 8px">{esc(n)}</h3><p>{esc(t)}</p><ul class="ticks" style="margin:16px 0">{li}</ul><p style="font-size:12px;letter-spacing:.2em;text-transform:uppercase;color:var(--gold)">{esc(d)}</p><span class="from" style="font-size:28px">From AED {p}</span><div class="btns" style="margin-top:18px"><a class="btn sm" href="{wl}" target="_blank" rel="noopener">Enquire</a></div></div>'
    body=pagehero("For Your Special Day",'Bridal <em>wellness</em>',"From engagement to wedding morning, Sahara takes care of the bride, bridesmaids and everyone in between — at your villa, hotel or home.",crumbs(("Bridal",None)))+f'''
<section class="sec" style="padding-top:48px"><div class="wrap split"><div class="rv"><span class="eyebrow">Our Promise</span><h2 style="margin:18px 0 20px">Your wedding day, <em>perfectly pampered</em></h2><p>Therapists arrive at your chosen location with all equipment, products and setup. You focus on the moment; we handle the rest.</p><p>Every bridal package includes a pre-consultation with Neny’s team to personalise each treatment to the bride’s skin type, preferences and timeline. Bridal bookings need at least 1 week’s notice and 48 hours’ notice for a full refund on cancellation.</p></div><div class="photo wide rv"><img src="assets/img/image6.webp" alt="Two Sahara therapists giving a poolside massage" loading="lazy"></div></div></section>
<section class="sec alt"><div class="wrap"><div class="sechead rv"><span class="eyebrow">Bridal Packages</span><h2>Choose your <em>experience</em></h2><p>All packages include consultation, full setup and cleanup, and premium Balinese products.</p></div><div class="grid g2">{cards}</div></div></section>{cta_band("Start planning today.","WhatsApp us for a custom bridal package tailored to your date, venue and party size.")}'''
    return page("bridal.html","Bridal Spa Packages Dubai | Sahara Balinese Spa","Bridal wellness packages in Dubai: facials, massage, nails and hair for the bride and bridal party, delivered to your villa, hotel or home.",body,"bridal",[crumb_schema("bridal.html",("Bridal",None))])

def vouchers():
    occ="".join(f"<option>{o}</option>" for o in ["Happy Birthday","Happy Mother's Day","Happy Father's Day","Happy Anniversary","Happy Valentine's Day","Congratulations","Eid Mubarak","Merry Christmas","Thank You","A Gift for You"])
    body=pagehero("Gift Vouchers",'Spa <em>gift vouchers</em>',"Give someone a real Balinese spa treatment in the comfort of their own home. Request a voucher below — we send a digital certificate.",crumbs(("Gift Vouchers",None)))+f'''
<section class="sec" style="padding-top:48px"><div class="wrap" id="voucher"><div class="split" style="align-items:start;grid-template-columns:1.15fr .85fr">
<form id="v-form" novalidate>
<div class="panel"><h2><span class="stn">1</span>What would you like to gift?</h2><p class="sub">&nbsp;</p>
<div class="chips"><button type="button" class="chip on" data-k="treatment">A treatment</button><button type="button" class="chip" data-k="amount">An amount</button></div>
<div id="v-tx-wrap"><label for="v-tx">Treatment</label><select id="v-tx"></select><label for="v-dur">Duration</label><select id="v-dur"></select></div>
<div id="v-amt-wrap" class="hide"><label for="v-amt">Amount (AED)</label><input id="v-amt" type="number" min="100" step="50" inputmode="numeric" placeholder="e.g. 500"></div></div>
<div class="panel"><h2><span class="stn">2</span>Personal touch</h2><p class="sub">&nbsp;</p>
<label for="v-occ">Occasion</label><select id="v-occ">{occ}</select>
<div class="frow"><div><label for="v-to">Recipient’s name</label><input id="v-to"></div><div><label for="v-from">From</label><input id="v-from"></div></div>
<label for="v-msg">Message on the voucher (optional)</label><textarea id="v-msg" maxlength="140"></textarea>
<label for="v-del">Delivery</label><select id="v-del"><option>Send it to me on WhatsApp</option><option>Send it to the recipient on WhatsApp</option></select></div>
<div class="panel"><h2><span class="stn">3</span>Your details</h2><p class="sub">&nbsp;</p>
<div class="frow"><div><label for="v-name">Your name</label><input id="v-name" autocomplete="name"></div><div><label for="v-phone">WhatsApp number</label><input id="v-phone" type="tel" inputmode="tel" autocomplete="tel"></div></div>
<label for="v-email">Email (optional)</label><input id="v-email" type="email" autocomplete="email"></div>
<div class="est"><div><small>Voucher value</small><span class="t" id="v-total">—</span></div><button class="btn wa" type="submit">Request on WhatsApp</button></div>
<p class="err" id="v-err" role="alert"></p><div id="v-ok"></div></form>
<div class="stickyside"><div class="vcard"><img src="assets/img/logo-full.webp" alt="Sahara Balinese Spa &amp; Salon"><div class="occ" id="vp-occ">Happy Birthday</div><div class="for" id="vp-for">For your loved one</div><div class="what" id="vp-what">—</div><div class="msg" id="vp-msg"></div><div class="for" id="vp-from"></div><div class="code">GIFT CODE · ISSUED ON CONFIRMATION</div></div><p style="font-size:13.5px;margin-top:14px;text-align:center">Live preview. We confirm the voucher, payment method and validity with you on WhatsApp.</p></div></div>
<div style="margin-top:64px" class="split"><div class="rv"><span class="eyebrow">A gift for every occasion</span><h2 style="margin:18px 0 18px">Birthdays, Mother’s Day, <em>Eid and more</em></h2><p>Sahara gift vouchers are available for any amount or a specific treatment — a thoughtful alternative to flowers or perfume. For couples, see <a href="packages.html">Couples Sanctuary</a>; for brides, see <a href="bridal.html">bridal packages</a>.</p></div><div class="rv"><span class="eyebrow">Voucher terms</span><ul class="ticks" style="margin-top:14px"><li>Treatments take place in Dubai only (home, villa or hotel).</li><li>Vouchers are issued as a digital certificate after confirmation.</li><li>Validity, refunds and redemption are confirmed when you order.</li><li>A minimum booking value of AED {MIN_ORDER} applies per session.</li></ul></div></div></div></section>'''
    return page("gift-vouchers.html","Spa Gift Vouchers Dubai | Sahara Balinese Spa & Salon","Buy a Sahara spa gift voucher in Dubai: massage, facial, body ritual or any amount. Digital certificate for birthdays, Mother's Day, Eid and more.",body,"gift-vouchers",[crumb_schema("gift-vouchers.html",("Gift Vouchers",None))])

def therapists():
    cards="".join(f'<div class="thc rv"><div class="ph"><img src="assets/img/{ph}" alt="{esc(n)}, Sahara therapist" loading="lazy" width="600" height="750"></div><h3>{esc(n)}</h3><span class="role">{esc(sp)}</span><p style="font-size:14.5px">{esc(d)}</p></div>' for n,sp,d,ph in THERAPISTS)
    body=pagehero("Our Therapists",'Meet our <em>professional therapists</em>',"Experienced Balinese wellness professionals with international exposure across Indonesia, Bali, Turkey and Dubai.",crumbs(("About","about.html"),("Our Therapists",None)))+f'''
<section class="sec" style="padding-top:48px"><div class="wrap"><p class="rv" style="max-width:760px;margin-bottom:40px">Each therapist brings individual skills, traditional knowledge and a passion for delivering authentic Balinese spa experiences.</p><div class="grid g4" id="th-grid">{cards}</div>
<div class="note rv"><b style="color:var(--cream)">Who will come to you?</b> We match each booking to the best available therapist for your treatment. Prefer someone in particular? Mention their name when booking and we will try to send them, subject to availability.</div>
<div class="btns"><a class="btn" href="book.html">Book a Treatment</a><a class="btn wa" href="{WA_HELLO}" target="_blank" rel="noopener">Ask on WhatsApp</a></div></div></section>'''
    return page("meet-our-therapists.html","Meet Our Therapists | Sahara Balinese Spa & Salon Dubai","Meet the Sahara team: experienced Balinese wellness professionals delivering massage, body scrubs and spa rituals at your home in Dubai.",body,"about",[crumb_schema("meet-our-therapists.html",("About","about.html"),("Our Therapists",None))])

def areas():
    li="".join(f"<li>{esc(a)}</li>" for a in AREAS)
    body=pagehero("Areas We Serve",'All of Dubai, <em>we come to you</em>',"Homes, apartments, villas, hotels and gated communities across Dubai.",crumbs(("Areas We Serve",None)))+f'''
<section class="sec" style="padding-top:48px"><div class="wrap"><ul class="areas rv">{li}<li>All gated communities &amp; hotels</li></ul>
<div class="split" style="margin-top:64px"><div class="rv"><span class="eyebrow">Wherever you are</span><h2 style="margin:18px 0 18px">Home, hotel &amp; villa <em>treatments</em></h2><p>Our therapists arrive fully equipped with a professional massage table, fresh towels, premium oils and everything required. We serve:</p><ul class="ticks"><li>Private homes &amp; apartments</li><li>Villas</li><li>Hotels &amp; serviced residences</li><li>Poolside and cabana sessions at many properties — enquire first</li></ul></div>
<div class="panel rv"><h3>Can’t find your area?</h3><p style="margin:10px 0 20px">Message us your location and we’ll confirm within minutes.</p><a class="btn wa" href="{WA("Hi%20Sahara%2C%20do%20you%20cover%20my%20area%3F")}" target="_blank" rel="noopener">Check My Area</a></div></div></div></section>{cta_band()}'''
    return page("areas-we-serve.html","Areas We Serve | Home Spa Across Dubai | Sahara Balinese Spa","Sahara covers all of Dubai: Marina, JBR, Palm Jumeirah, Downtown, Business Bay, DIFC, Jumeirah, Dubai Hills, Arabian Ranches, JVC, JLT, Mirdif and more.",body,"about",[crumb_schema("areas-we-serve.html",("Areas We Serve",None))])

def faqs():
    body=pagehero("FAQ",'Everything you need to know <em>before your first session</em>',"Quick answers about booking, preparation, therapists, payment and cancellations.",crumbs(("FAQs",None)))+f'''
<section class="sec" style="padding-top:48px"><div class="wrap" style="max-width:900px">{faq_html(FAQS)}
<div class="btns"><a class="btn wa" href="{WA_HELLO}" target="_blank" rel="noopener">Still have questions? WhatsApp us</a><a class="btn ghost" href="mailto:{EMAIL}">Send an email</a></div></div></section>'''
    return page("faqs.html","FAQs | Sahara Balinese Spa & Salon Dubai","Answers about Sahara's home spa service in Dubai: areas, booking, preparation, therapists, payment and cancellation policy.",body,"about",[crumb_schema("faqs.html",("FAQs",None)),faq_schema(FAQS)])

def reviews():
    body=pagehero("Reviews",'What our <em>clients say</em>',"Read and share experiences of Sahara’s home spa service in Dubai.",crumbs(("Reviews",None)))+f'''
<!-- Google review link is live; add verified client testimonials here when the owner supplies them. -->
<section class="sec" style="padding-top:48px"><div class="wrap center"><div class="rv" style="max-width:640px;margin:0 auto"><span class="eyebrow">Share your experience</span><h2 style="margin:18px 0 16px">Tried <em>Sahara?</em></h2><p>Your feedback helps other clients choose with confidence. Review us on Google, or send us a message — we read every one.</p><div class="btns"><a class="btn" href="{GOOGLE_REVIEW}" target="_blank" rel="noopener">Review us on Google</a><a class="btn ghost" href="{WA("Hi%20Sahara%2C%20I%27d%20like%20to%20share%20feedback.")}" target="_blank" rel="noopener">Send Feedback</a></div></div></div></section>{cta_band()}'''
    return page("reviews.html","Reviews | Sahara Balinese Spa & Salon Dubai","Read and share client reviews of Sahara Balinese Spa & Salon, Dubai's mobile Balinese spa.",body,"about",[crumb_schema("reviews.html",("Reviews",None))])

def about():
    vals=[("I","Authenticity","Every technique we practise traces back to real Balinese tradition. We use genuine Balinese ritual products — volcanic ash, ylang-ylang, coconut oil, turmeric — not generic imitations."),("II","Excellence","Every therapist undergoes Neny's personal certification programme. Protocols, timing, pressure and product application are held to the standard of the finest spa floors in the world."),("III","Discretion","Uniformed, background-verified professionals with full liability insurance. Privacy is a core operating principle, not an afterthought.")]
    lead="".join(f'<div class="thc rv"><div class="ph"><img src="assets/img/{ph}" alt="{esc(n)}" loading="lazy" width="600" height="750"></div><h3>{esc(n)}</h3><span class="role">{esc(r)}</span></div>' for n,r,ph in BOARD)
    v="".join(f'<div class="card rv"><span class="num">{a}</span><h3>{b}</h3><p>{c}</p></div>' for a,b,c in vals)
    body=pagehero("Our Story",'Rooted in Bali. <em>Refined in Dubai.</em>',"20+ years · 3 continents.",crumbs(("About",None)))+f'''
<section class="sec" style="padding-top:48px"><div class="wrap split"><div class="photo tall rv"><img src="assets/img/team-neny-wibowo.webp" alt="Neny Trisnayanti Wibowo, Founder and Managing Director of Sahara" loading="lazy"></div><div class="rv"><span class="eyebrow">The Founder</span><h2 style="margin:18px 0 6px">Neny Trisnayanti Wibowo</h2><p style="color:var(--gold);letter-spacing:.2em;text-transform:uppercase;font-size:12px">Founder &amp; Managing Director</p>
<p style="margin-top:20px">Born in Ubud, Bali — the spiritual and healing heartland of Balinese culture — Neny grew up immersed in the ancient traditions of Balinese wellness. From age sixteen she apprenticed under master healers, learning the art of touch, the language of the body and the power of botanical medicine.</p>
<p>At twenty-two her career took her to luxury resorts in Bali, then to five-star properties across Europe and Asia. In 2008 she arrived in the UAE, where she spent the next decade and a half serving guests at Dubai’s finest hotels.</p>
<p>In 2018, Neny founded Sahara Balinese Spa with a single vision: to bring that same immaculate, intimate wellness experience directly to clients in their own space. Every Sahara therapist is personally trained and certified by Neny using her five-star protocol.</p></div></div></section>
<section class="sec alt"><div class="wrap"><div class="sechead center rv"><span class="eyebrow">What drives us</span><h2>The Sahara <em>philosophy</em></h2></div><div class="grid g3">{v}</div></div></section>
<section class="sec"><div class="wrap"><div class="sechead center rv"><span class="eyebrow">Leadership</span><h2>The people <em>behind Sahara</em></h2></div><div class="grid g3" style="max-width:900px;margin:0 auto">{lead}</div></div></section>{cta_band("Book your first session.")}'''
    return page("about.html","About Sahara | Founder Neny Trisnayanti | Balinese Spa Dubai","Sahara Balinese Spa & Salon was founded in 2018 by Neny Trisnayanti, bringing 20+ years of five-star hotel wellness experience to your home in Dubai.",body,"about",[crumb_schema("about.html",("About",None))])

def contact():
    body=pagehero("Contact",'Book &amp; <em>contact</em>',"Open 10 AM – 12 AM, 7 days a week, across all of Dubai.",crumbs(("Contact",None)))+f'''
<section class="sec" style="padding-top:48px"><div class="wrap"><div class="grid g3" style="margin-bottom:56px">
<div class="card rv"><h3>Book online</h3><p>Real-time slot availability and instant confirmation.</p><a class="btn sm" style="margin-top:18px" href="book.html">Book now</a></div>
<div class="card rv"><h3>Review us on Google</h3><p>Had a treatment with us? Your feedback takes under a minute and means a lot.</p><a class="btn sm" style="margin-top:18px" href="{GOOGLE_REVIEW}" target="_blank" rel="noopener" data-track="review_click">Leave a review</a></div>
<div class="card rv"><h3>WhatsApp us</h3><p>Same-day bookings, group requests or custom packages.</p><a class="btn sm wa" style="margin-top:18px" href="{WA_HELLO}" target="_blank" rel="noopener">Chat Now</a></div>
<div class="card rv"><h3>Call us</h3><p>Speak directly with our team for recommendations.</p><a class="btn sm ghost" style="margin-top:18px" href="tel:+{PHONE}">{PHONE_DISPLAY}</a> <a class="btn sm ghost" style="margin-top:18px" href="tel:+{PHONE2}">{PHONE2_DISPLAY}</a></div></div>
<div class="split" style="align-items:start"><form class="panel rv" id="contact-form" novalidate><h2>Make an enquiry</h2>
<label for="c-name">Full name</label><input id="c-name" autocomplete="name"><label for="c-phone">WhatsApp / phone</label><input id="c-phone" type="tel" inputmode="tel" autocomplete="tel"><label for="c-svc">Service interested in</label><select id="c-svc"></select>
<div class="frow"><div><label for="c-date">Preferred date</label><input id="c-date" type="date"></div><div><label for="c-time">Preferred time</label><select id="c-time"></select></div></div>
<label for="c-notes">Your location / notes</label><textarea id="c-notes"></textarea><div style="margin-top:20px"><button class="btn wa" type="submit">Send on WhatsApp</button></div><p class="err" id="c-err" role="alert"></p><div id="c-ok"></div></form>
<div class="rv"><span class="eyebrow">Details</span><h2 style="margin:18px 0 20px">Get in <em>touch</em></h2>
<p><b style="color:var(--cream)">Sahara duty mobile</b><br><a href="tel:+{PHONE}">{PHONE_DISPLAY}</a><br><a href="tel:+{PHONE2}">{PHONE2_DISPLAY}</a></p><p><b style="color:var(--cream)">Email</b><br><a href="mailto:{EMAIL}">{EMAIL}</a></p><p><b style="color:var(--cream)">Hours</b><br>Monday – Sunday, 10:00 AM – 12:00 AM<br>Same-day bookings accepted</p><p><b style="color:var(--cream)">Service area</b><br>All of Dubai — we are a mobile service and come to you. <a href="areas-we-serve.html">See areas</a></p></div></div></div></section>'''
    return page("contact.html","Contact & Booking | Sahara Balinese Spa & Salon Dubai","Contact Sahara Balinese Spa & Salon: book on Fresha, WhatsApp or phone. Open 10 AM–12 AM, 7 days across Dubai.",body,"about",[crumb_schema("contact.html",("Contact",None))])

def terms():
    body=pagehero("Terms","Terms &amp; <em>cancellation policy</em>","The essentials of booking with Sahara.",crumbs(("Terms &amp; Cancellation",None)))+f'''
<!-- TODO(owner/legal): review wording before publishing. Built from the cancellation/payment rules on the existing Sahara site. -->
<section class="sec" style="padding-top:48px"><div class="wrap" style="max-width:820px"><div class="rv">
<h3 id="cancellation">Cancellation &amp; rescheduling</h3><p>We ask for a minimum of 3 hours’ notice for cancellations or reschedules. Cancellations with less than 3 hours’ notice may incur a 50% charge. Bridal and group bookings require 48 hours’ notice for a full refund.</p>
<h3 style="margin-top:34px">Payment &amp; pricing</h3><p>Payment is accepted via Fresha (card on booking), cash on the day, or bank transfer for group and bridal packages. Prices include therapist travel within Dubai. A minimum booking value of AED {MIN_ORDER} applies per session. Prices are indicative and may vary by location and session requirements.</p>
<h3 style="margin-top:34px">Your space</h3><p>Please provide a clear space of about 2 m × 2 m and access a few minutes before the session. For hotel bookings, please confirm that outside service providers are permitted in your room.</p>
<h3 style="margin-top:34px">Health &amp; safety</h3><p>Please tell us about any medical condition, injury, pregnancy or allergy before your booking. We may advise against a treatment that is not suitable.</p>
<h3 style="margin-top:34px">Contact</h3><p>Questions? <a href="mailto:{EMAIL}">{EMAIL}</a> or <a href="{WA_HELLO}" target="_blank" rel="noopener">WhatsApp</a>.</p></div></div></section>'''
    return page("terms-conditions.html","Terms & Cancellation Policy | Sahara Balinese Spa & Salon","Sahara's booking terms: cancellation policy, payment, minimum order and preparation for your home spa treatment in Dubai.",body,"")

def privacy():
    body=pagehero("Privacy","Privacy <em>policy</em>","How Sahara handles your information.",crumbs(("Privacy",None)))+f'''
<!-- TODO(owner/legal): this is a plain-language draft — have it reviewed before publishing. -->
<section class="sec" style="padding-top:48px"><div class="wrap" style="max-width:820px"><div class="rv">
<p>This website does not store your booking details. When you use our booking, voucher or enquiry forms, the details you enter (such as name, phone number, address and preferences) are placed into a WhatsApp message that you send to Sahara. WhatsApp’s own privacy terms apply to that message.</p>
<h3 style="margin-top:34px">What we collect</h3><p>Only what you choose to send us when booking or enquiring: name, contact number, location and treatment preferences, and any health notes you share so we can keep you safe.</p>
<h3 style="margin-top:34px">How we use it</h3><p>To confirm and deliver your appointment, handle payment and follow up on your booking. We do not sell your information.</p>
<h3 style="margin-top:34px">Third parties</h3><p>This site loads fonts from Google Fonts. Bookings made on Fresha are governed by Fresha’s privacy policy.</p>
<h3 style="margin-top:34px">Contact</h3><p>Questions or requests about your information: <a href="mailto:{EMAIL}">{EMAIL}</a>.</p></div></div></section>'''
    return page("privacy-policy.html","Privacy Policy | Sahara Balinese Spa & Salon","How Sahara Balinese Spa & Salon handles the information you share when booking.",body,"")

def notfound():
    body=f'<section class="sec center" style="min-height:60vh;display:flex;align-items:center"><div class="wrap"><span class="eyebrow">404</span><h1 style="margin:18px 0">Page not <em>found</em></h1><p class="lead" style="margin:0 auto">The page you’re looking for has moved or doesn’t exist.</p><div class="btns"><a class="btn" href="index.html">Home</a><a class="btn ghost" href="book.html">Book a Treatment</a></div></div></section>'
    return page("404.html","Page not found | Sahara Balinese Spa & Salon","Page not found.",body,"")


def booking_confirmed():
    body=pagehero("Booking",'Your <em>booking</em>',"Thank you for choosing Sahara.",crumbs(("Booking",None)))+'<section class="sec" style="padding-top:48px"><div class="wrap" style="max-width:760px"><div id="bk-confirm"><p>Loading your booking…</p></div></div></section>'
    return page("booking-confirmed.html","Booking | Sahara Balinese Spa","Your Sahara booking.",body,"book",None,None,'<meta name="robots" content="noindex">')

def booking_manage():
    body=pagehero("Booking",'Manage your <em>booking</em>',"View or cancel your appointment.",crumbs(("Booking",None)))+'<section class="sec" style="padding-top:48px"><div class="wrap" style="max-width:760px"><div id="bk-manage"><p>Loading your booking…</p></div></div></section>'
    return page("booking-manage.html","Manage Booking | Sahara Balinese Spa","Manage your Sahara booking.",body,"book",None,None,'<meta name="robots" content="noindex">')
