# Sahara v2 – status & open items

Built from the client brief (SAHARA BALINESE SPA WEBSITE PROJECT.docx, Nov 2026).

## Applied from the brief
- Official menu prices (massage 250/350 etc., facial 200/250, body scrub 200/250, nails 200/200/350, corporate AED 300/hour)
- Contacts: +971 50 205 2017 (primary, WhatsApp) and +971 50 684 7716; saharabalinesespa@gmail.com
- Hours: 10 AM – 12 AM, 7 days
- 8 therapist profiles + photos; leadership (Arif, Neny, Sahara Wibowo) on About
- Dark (default) and light (white & black) mode switch in the header
- Note: assets/staff/ holds the original WhatsApp staff photos; the site uses optimised copies in assets/img/team-*.webp

## Please confirm with client
| Item | Detail |
|---|---|
| Removed services | Hair, waxing, aromatherapy, shiatsu, gel nails, body wraps/facial types are NOT on the new menu so were removed |
| Packages I–IV, Bridal | Prices/contents come from the OLD site (facials, hair, mani-pedi items no longer on menu) – need updating or approval |
| Minimum booking | Old rule was AED 250; menu has AED 200 items so it is set to AED 200 |
| Modero Therapy | Description is generic – confirm what it is |
| Prenatal "after 12 weeks", postnatal | Old-site/assumed wording – confirm |
| "Travel included" | Carried over from old site – confirm still true |
| Therapist name | "Sugiriana" (list) vs "Sugiariana" (photo caption) |
| Kadek Juli photo | Photo has no name tag; matched by elimination – confirm |
| Fresha URL, domain, reviews, Terms/Privacy legal check | Still open |

## Rebuild
`cd _generator && python3 build.py` (edit data.py for prices/contacts).
