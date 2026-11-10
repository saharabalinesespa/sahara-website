# Sahara catalogue — prices/services taken from the existing Sahara site. Descriptive copy is draft, flagged for review.
PHONE = "971502052017"            # Sahara duty mobile (primary / WhatsApp)
PHONE_DISPLAY = "+971 50 205 2017"
PHONE2 = "971506847716"
PHONE2_DISPLAY = "+971 50 684 7716"
EMAIL = "saharabalinesespa@gmail.com"
FRESHA = "https://www.fresha.com/book-now/palma-spa-ru273iq3/all-offer?id=31958&pId=29721"
INSTAGRAM = "https://www.instagram.com/saharabalinesehomespa/"
FACEBOOK = "https://www.facebook.com/saharabalinesespa"
import os as _os
API_BASE = _os.environ.get("SAHARA_API", "").rstrip("/")   # set at build time to switch on live booking (see backend README)
BASE = "https://saharabalinesespas.com"   # change when custom domain is attached
HOURS = "10:00 AM – 12:00 AM, 7 days"
MIN_ORDER = 200   # menu now has AED 200 items; old site rule was 250 - confirm with client

# Official Sahara menu (client brief, Nov 2026). id, name, blurb, [(minutes, price)], cat, optional duration label
ITEMS = [
 # Massages
 ("balinese","Balinese Massage","Deep rhythmic strokes with warm Balinese oil",[(60,250),(90,350)],"massage"),
 ("deep-tissue","Deep Tissue Massage","Targets deep muscle layers, relieves chronic tension",[(60,250),(90,350)],"massage"),
 ("swedish","Swedish Massage","Long, flowing strokes for relaxation and easing muscle tension",[(60,250),(90,350)],"massage"),
 ("thai","Thai Massage","Stretch-based therapy to improve flexibility and energy",[(60,250),(90,350)],"massage"),
 ("prenatal","Prenatal Massage","Gentle, supportive massage for expecting mothers",[(60,250),(90,350)],"massage"),
 ("postnatal","Postnatal Massage","Restorative massage for new mums as the body recovers",[(60,250),(90,350)],"massage"),
 ("sports","Sports Massage","Performance recovery and injury prevention",[(60,250),(90,350)],"massage"),
 ("ayurvedic","Ayurvedic Massage","Warm-oil massage inspired by Ayurvedic tradition",[(60,250),(90,350)],"massage"),
 ("reflexology","Foot Massage & Reflexology","Targeted pressure points to rebalance the whole body",[(60,250),(90,350)],"massage"),
 ("lymphatic","Lymphatic Drainage Massage","Light, rhythmic strokes to support circulation and ease heaviness",[(60,300),(90,400)],"massage"),
 ("modero","Modero Therapy","Sculpting body massage using smooth wooden tools",[(60,300),(90,400)],"massage"),
 ("hot-stone","Hot Stone Massage","Heated basalt stones melt away deep muscle stress",[(90,400)],"massage"),
 ("cupping","Cupping Therapy","Promotes circulation and deep muscle recovery",[(90,400)],"massage"),
 ("four-hands","Four Hands Massage","Two therapists working in synchrony for a deeply immersive treatment",[(60,450),(90,650)],"massage"),
 ("couple","Couple Massage","Side-by-side massage for two, with two therapists",[(60,450),(90,650)],"massage"),
 # Facial
 ("rejuvenating-facial","Rejuvenating Facial","Cleanse, nourish and revive tired skin",[(60,250)],"facial"),
 ("express-facial","Express Facial","A quick refresh when time is short",[(30,200)],"facial"),
 # Body scrub
 ("body-scrub","Refresh Body Scrub","Full-body exfoliation to leave skin smooth and refreshed",[(60,250)],"body"),
 ("express-body-scrub","Express Body Scrub","A shorter scrub for a quick skin reset",[(30,200)],"body"),
 # Nails (single price, no duration)
 ("manicure","Classic Manicure","Shape, cuticle care and polish",[(0,200)],"nails"),
 ("pedicure","Classic Pedicure","Foot care, cuticle care and polish",[(0,200)],"nails"),
 ("mani-pedi","Classic Manicure & Pedicure","Manicure and pedicure together",[(0,350)],"nails"),
 # Corporate
 ("corporate","Corporate Wellness","On-site massage for teams and events, priced per therapist per hour",[(60,300)],"corporate","Per hour"),
]
CATS = {
 "massage":("Massage Therapy","From the ancient healing traditions of Bali to modern therapeutic techniques. All treatments use premium Balinese oils and are performed by certified therapists.","massage"),
 "facial":("Facial Treatments","Facials tailored to your skin after a brief consultation — a full rejuvenating session or a quick express refresh.","facials"),
 "body":("Body Scrub","Full-body scrubs that exfoliate and refresh, in a full or express session.","body-scrub"),
 "nails":("Nail Care","Perfectly polished nails wherever you are. Our technicians arrive with professional equipment and sanitised tools.","nail-care"),
 "corporate":("Corporate Wellness","On-site wellness for offices, hotels and events — multiple therapists, any scale.","corporate-wellness"),
}
def items(cat): return [i for i in ITEMS if i[4]==cat]
def item(id_): return next(i for i in ITEMS if i[0]==id_)
def frm(it):
    return min(p for _,p in it[3])
def dur_label(it):
    if len(it)>5: return it[5]
    o=it[3]
    if o[0][0]==0: return ""
    return " / ".join(str(m) for m,_ in o)+" min"
def price_label(it):
    o=it[3]
    s=" / ".join(f"AED {p}" for _,p in o)
    return s

PACKAGES = [
 ("I","The Sahara Ritual","Our most comprehensive single-guest experience",["60-min Balinese Massage with premium Balinese oil blend","45-min Signature Facial (personalised to your skin type)","45-min Full Body Scrub with lava salt or coffee","All premium products, towels and equipment included"],"150 minutes",600),
 ("II","Bali Serenity","The perfect 90-minute escape from daily life",["60-min Aromatherapy Massage with mood-blended essential oils","30-min Signature Facial Treatment","All premium products and equipment included"],"90 minutes",350),
 ("III","Couples Sanctuary","Side-by-side luxury for you and the one you love",["Dual 90-min Balinese or Hot Stone Massage (your choice)","Two therapists arrive simultaneously","Full set of premium products and equipment for both","Can be upgraded to include facials (+AED 250)"],"90 minutes · 2 guests",600),
 ("IV","The Royal Indulgence","The pinnacle of the Sahara experience",["60-min Deep Tissue Massage targeting key tension areas","45-min Full Body Lava Salt Scrub","45-min Anti-Ageing or Brightening Facial","All products, towels and professional setup included"],"150 minutes",750),
]
BRIDAL = [
 ("The Essential","Bridal Glow","Perfect for the bride in the days before the wedding",["Brightening Facial Treatment","Classic Manicure & Pedicure","Professional Blow Dry & Finish"],"2.5 hours · 1 guest",450),
 ("Day Before","Calm & Radiant","Relaxation and radiance the evening before your wedding",["60-min Aromatherapy Relaxation Massage","Full Body Lava Salt Scrub","Gel Manicure in your chosen shade"],"3 hours · 1 guest",550),
 ("For the Bridal Party","Bride & Tribe","Celebrate together with the whole bridal squad",["Full bridal facial for the bride","Mini relaxation massage for up to 3 bridesmaids","Mani-Pedi for bride, manicure for party"],"3 hours · up to 4 guests",800),
 ("The Ultimate","The Full Bridal Experience","Everything a bride could want, from head to toe",["Aromatherapy Massage & Full Body Scrub","Brightening Facial with LED mask","Gel Mani & Pedi · Bridal Hair Styling"],"4+ hours · 1 guest",900),
]
THERAPISTS = [
 # name, specialist line, bio, photo
 ("Kadek Yosi Pratiwi","Traditional Balinese Massage","An experienced therapist specialising in authentic traditional Balinese massage. Skilled in combining flowing massage strokes, acupressure and gentle stretching techniques to release tension, improve relaxation and restore body balance.","team-kadek-yosi.webp"),
 ("Putu Desi Arsita Dewi","Therapeutic & Deep Tissue Massage","A dedicated massage professional with expertise in deep tissue techniques and targeted muscle relaxation. Specialises in focusing on tension areas, relieving muscle stiffness and providing personalised treatments based on individual guest needs.","team-putu-desi.webp"),
 ("Wayan Sriyani","Relaxation & Stress Relief Massage","A passionate wellness therapist specialising in relaxation treatments. Her gentle yet effective techniques help reduce everyday stress, ease muscle tension and create a deeply relaxing spa experience.","team-wayan-sriyani.webp"),
 ("Komang Lisa Sugiantari","Aromatherapy & Holistic Massage","An experienced therapist with a passion for holistic wellness and aromatherapy treatments. Skilled in combining soothing massage movements with essential oils to promote relaxation, improve comfort and enhance overall well-being.","team-komang-lisa.webp"),
 ("Waryunah Ratna","Muscle Tension & Therapeutic Healing Massage","A knowledgeable therapist specialising in targeted massage techniques and muscle tension relief. Experienced in adapting pressure and treatment methods to individual guest preferences, helping promote physical comfort and relaxation.","team-waryunah-ratna.webp"),
 ("Ketut Agus Niawati","Balinese Traditional & Body Relaxation","Specialising in traditional Balinese massage and full-body relaxation treatments. Combines traditional massage knowledge with professional techniques to deliver a personalised and rejuvenating wellness experience.","team-ketut-agus.webp"),
 ("Kadek Juli Purnami","Body Scrub & Traditional Spa Rituals","A wellness professional with a passion for traditional spa rituals and body treatments. Specialises in body scrubs, exfoliation and relaxing spa experiences designed to leave the skin feeling refreshed and revitalised.","team-kadek-juli.webp"),
 ("Made Sugiriana","Therapeutic & Full Body Massage","An experienced massage professional specialising in full-body massage and therapeutic relaxation techniques. Focuses on individual guest requirements, combining professional massage skills with attentive care to provide a comfortable and memorable experience.","team-made-sugiriana.webp"),
]
BOARD = [
 ("Arif Wibowo","Founder & Director of Operations","team-arif-wibowo.webp"),
 ("Neny Trisnayanti Wibowo","Founder & Managing Director","team-neny-wibowo.webp"),
 ("Sahara Zalifunnafsi Surya Wibowo","Chief Executive Officer","team-sahara-wibowo.webp"),
]
AREAS = ["Dubai Marina","JBR","Palm Jumeirah","Bluewaters","Downtown Dubai","Business Bay","DIFC","City Walk","Jumeirah","Umm Suqeim","Al Barsha","Dubai Hills","Arabian Ranches","Meydan","JVC","JLT","Mirdif","Al Quoz"]
FAQS = [
 ("What areas of Dubai do you cover?","We cover all of Dubai — Dubai Marina, JBR, Palm Jumeirah, Bluewaters, Downtown, Business Bay, DIFC, City Walk, Jumeirah, Umm Suqeim, Al Barsha, Dubai Hills, Arabian Ranches, Meydan, JVC, JLT, Mirdif, Al Quoz, and all gated communities and hotels. If you're unsure, WhatsApp us your location and we'll confirm within minutes."),
 ("How far in advance do I need to book?","We accept same-day bookings — simply book via Fresha or WhatsApp us directly. For peak times (weekends, evenings and holidays) we recommend booking 24–48 hours ahead to secure your preferred time slot. Bridal and group bookings require at least 1 week's notice."),
 ("What do I need to prepare at home?","Very little. We bring everything — our own professional massage table, fresh towels and linens, all Balinese oils and products, and any specialist equipment for the booked treatments. All we ask is a clear space of approximately 2m × 2m for the massage table, and access to your space a few minutes before the session starts."),
 ("Are your therapists male or female? Can men book?","Our team is mostly female, with one male therapist. Everyone is welcome to book — please mention any therapist preference when booking so we can match you appropriately. For couples bookings both guests can be treated at the same time."),
 ("Are your therapists certified?","Yes. Every Sahara therapist holds professional certifications in their respective disciplines and has been personally trained and approved by our founder Neny Trisnayanti — who brings 20+ years of five-star hotel wellness experience. All therapists are background-verified and fully insured."),
 ("Can I book for a hotel room or villa?","Absolutely — this is one of our most popular setups. We regularly serve guests at hotels across Dubai. Simply provide your hotel name, room number and check-in status when booking. Poolside and cabana sessions are available at many properties — enquire via WhatsApp for arrangements."),
 ("How do I pay?","Payment is accepted via Fresha (card on booking), cash on the day, or bank transfer for group/bridal packages. All prices are inclusive of therapist travel within Dubai. A minimum booking value of AED 250 applies per session."),
 ("What is your cancellation policy?","We ask for a minimum of 3 hours' notice for cancellations or reschedules. Cancellations with less than 3 hours' notice may incur a 50% charge. Bridal and group bookings require 48 hours' notice for a full refund. We understand emergencies happen — please contact us as soon as possible and we will always do our best to accommodate you."),
 ("Can I request the same therapist each time?","Yes — we always try to honour therapist preferences. When booking via WhatsApp, simply mention your preferred therapist by name. Availability cannot be guaranteed but we will always try our best. Many of our regular clients build a wonderful long-term relationship with their preferred Sahara therapist."),
 ("Do you offer gift vouchers?","Yes. Sahara gift vouchers are available for any amount or specific treatment. They make the perfect gift for birthdays, Mother's Day, Eid, and other special occasions. Request one on our gift voucher page or via WhatsApp — we can provide a beautifully designed digital certificate within 24 hours."),
]
# Per-treatment page copy (draft — review before publishing)
TX = {
 "balinese":dict(what="Balinese massage is the signature healing massage of Bali. Long, flowing strokes are combined with gentle stretching, acupressure and kneading, all with warm Balinese oil. Pressure is medium — firm enough to release tension, soft enough to switch off completely.",best=["First-time clients","Stress and general tension","Couples and special occasions","A full-body reset"],pressure="Medium",faq=[("What is the difference between Balinese and Thai massage?","Balinese massage is done on a table with oil and long flowing strokes plus acupressure. Thai massage is traditionally clothed and stretch-based, so it is more active."),("How firm is it?","Medium, and your therapist adjusts it to you. For firmer work on knots choose Deep Tissue.")]),
 "deep-tissue":dict(what="Slow, firm pressure targeting the deeper layers of muscle and connective tissue to ease chronic tension, knots and stiffness in the back, neck and shoulders.",best=["Desk-related tension","Knots and stiffness","Active people","Chronic tightness"],pressure="Firm",faq=[("Will it hurt?","Deep tissue is firm but should never be painful. Tell your therapist at any time if you want it lighter.")]),
 "hot-stone":dict(what="Smooth heated basalt stones are placed on and glided over the body to warm tight muscles, allowing the therapist to work more deeply and the body to let go.",best=["Cold-sensitive muscles","Deep relaxation","Tension in back and shoulders","Cooler evenings"],pressure="Medium",faq=[("Is it suitable for everyone?","Heat is not suitable for everyone — please mention any medical condition, circulation issue or skin sensitivity when booking.")]),
 "thai":dict(what="A stretch-based therapy combining compression, rhythmic pressure and assisted stretching to improve flexibility, release tension and restore energy flow.",best=["Stiff, tight bodies","Flexibility","Active people","Those who prefer less oil"],pressure="Medium to firm",faq=[("Do I undress?","Please let us know your preference when booking; the therapist will arrange the session accordingly.")]),
 "prenatal":dict(what="A gentle, supportive massage for mums-to-be, designed to ease the common aches of pregnancy. Sahara offers prenatal massage after 12 weeks of pregnancy.",best=["Back, hip and leg aches","Swelling and heavy legs","Relaxation before birth"],pressure="Soft to medium",faq=[("When can I have a prenatal massage?","Sahara offers prenatal massage after 12 weeks. Please consult your doctor first if you have any complications or concerns.")]),
 "cupping":dict(what="Cupping uses gentle suction to lift tissue and encourage circulation, helping to release stubborn tightness in the back and shoulders.",best=["Back and shoulder tightness","Muscle recovery","Circulation support"],pressure="Targeted",faq=[("Does it leave marks?","Cupping can leave temporary round marks on the skin. They typically fade within days.")]),
 "sports":dict(what="Firm techniques and stretching to support recovery, ease sore muscles and help prevent injury for runners, gym-goers and weekend athletes.",best=["Post-training recovery","Muscle soreness","Injury prevention"],pressure="Firm",faq=[("When should I book?","Many clients book 24–48 hours after intense training. Tell us about any injury when booking.")]),
 "reflexology":dict(what="Targeted pressure on points of the feet linked to the rest of the body, to rebalance and relax. A calming treatment after a long day on your feet.",best=["Tired, heavy legs","Quick reset","Those who want a lighter treatment"],pressure="Medium",faq=[("Which duration should I choose?","45 minutes is a focused reset; 60 minutes allows a more complete treatment.")]),
 "swedish":dict(what="A classic relaxation massage using long, flowing strokes, kneading and gentle rhythm to ease muscle tension and calm the mind. Warm oil is used throughout.",best=["First-time massage clients","Stress and general tension","Light to medium pressure lovers"],pressure="Light to medium",faq=[("How is Swedish different from Balinese massage?","Swedish massage focuses on flowing strokes and kneading. Balinese massage adds acupressure and gentle stretching. Both are relaxing; choose Balinese if you want a little more depth.")]),
 "postnatal":dict(what="A restorative, supportive massage for new mums, easing the aches that come with carrying, feeding and caring for a newborn. Pressure is adjusted to how your body is recovering.",best=["New mums","Back, neck and shoulder tension","Deep relaxation at home"],pressure="Light to medium",faq=[("When can I book after birth?","Please check with your doctor first. Tell us about your delivery and any concerns when booking so we can tailor the session.")]),
 "ayurvedic":dict(what="A warm-oil massage inspired by Ayurvedic tradition, using rhythmic strokes to relax the body and balance the senses. A grounding, unhurried treatment.",best=["Deep relaxation","Tired, tense muscles","Those who enjoy warm oil massage"],pressure="Medium",faq=[("Will I be covered in oil?","Yes, warm oil is used generously. We bring towels and linens to protect your space.")]),
 "lymphatic":dict(what="A very light, slow and rhythmic technique that works with the body's natural circulation to ease heaviness and puffiness. Pressure is gentle by design.",best=["Heavy or tired legs","Gentle, light-pressure treatment","A calm, restorative session"],pressure="Very light",faq=[("Is it a deep massage?","No — lymphatic drainage uses very light pressure. If you want firmer work, choose Deep Tissue.")]),
 "modero":dict(what="A sculpting body massage using smooth shaped wooden tools to work through the muscles with rolling and gliding movements. Please ask us about suitability when booking.",best=["Muscle tension","Those curious about tool-based massage","A firmer, active treatment"],pressure="Medium to firm",faq=[("Is it suitable for everyone?","Tell us about any medical condition or sensitive areas when booking, and we will advise.")]),
 "four-hands":dict(what="Two therapists work in perfect synchrony, one on each side of the body, for a deeply immersive massage that feels like nothing else. Available in 60 or 90 minutes.",best=["Special occasions","Complete switch-off","Gifts and celebrations"],pressure="Medium",faq=[("How many therapists come?","Two therapists arrive together and work at the same time on one guest.")]),
 "couple":dict(what="Two guests, two therapists, side by side. Each guest receives their own full massage at the same time in the same room, a lovely way to share an experience at home or in a hotel suite.",best=["Couples and anniversaries","Friends or family sharing a treatment","Honeymoons and special occasions"],pressure="Medium",faq=[("Do we choose the same massage?","Usually yes for simplicity, but tell us if you would like different treatments and we will arrange it.")]),
}
