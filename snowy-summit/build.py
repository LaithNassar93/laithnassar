#!/usr/bin/env python3
"""Generates the Snowy Summit static site. Edit CONFIG/content, then run: python3 build.py"""
import os, html
OUT = os.path.dirname(os.path.abspath(__file__))
DOMAIN = "https://snowysummitgaragedoor.com"
NAME = "Snowy Summit Garage Door Repair"
PHONE = "(612) 555-0100"          # PLACEHOLDER - replace
PHONE_TEL = "+16125550100"        # PLACEHOLDER - replace
EMAIL = "info@snowysummitgaragedoor.com"  # PLACEHOLDER - replace

SERVICES = [
 ("garage-door-repair","Garage Door Repair","Fast, reliable repair for broken springs, off-track doors, damaged cables, rollers and panels.",
  ["Broken torsion and extension springs","Off-track or crooked doors","Snapped cables and worn rollers","Dented or damaged panels","Noisy or jerky operation"]),
 ("garage-door-installation","Garage Door Installation","New garage door installation, from steel and insulated models to carriage-house styles.",
  ["Free in-home estimate","Help choosing style, material and insulation","Professional installation and haul-away of the old door","Hardware and weather seal included","Final safety and balance check"]),
 ("garage-door-opener-installation","Garage Door Opener Installation","Quiet, smart-ready opener installation with safety sensors and remotes set up and tested.",
  ["Belt, chain and direct-drive options","Wi-Fi and smartphone-ready models","Battery backup options","Keypads and remotes programmed","Safety sensors aligned and tested"]),
 ("garage-door-opener-repair","Garage Door Opener Repair","Opener won't open, close or respond? We diagnose and repair most brands.",
  ["Remote and keypad troubleshooting","Gear, sprocket and belt replacement","Limit and force adjustments","Safety sensor repair","Circuit board and motor diagnosis"]),
 ("garage-door-maintenance","Garage Door Maintenance","Seasonal tune-ups that prevent breakdowns and extend the life of your door.",
  ["Lubrication of moving parts","Spring, cable and roller inspection","Balance and auto-reverse test","Weather seal check","Tightening of hardware"]),
]
CITIES = ["Minneapolis","St. Paul","Woodbury","Eagan","Lakeville","Eden Prairie"]
def slug(s): return s.lower().replace(". ","").replace(" ","-")

EXTRA = [  # additional SEO pages
 ("garage-door-spring-repair","Garage Door Spring Repair","Broken garage door spring? Same-day spring replacement across the Twin Cities metro.",
  ["Springs are under extreme tension. Never attempt to replace one yourself.","Signs of a broken spring: a loud bang, a door that won't lift, or a visible gap in the coil.","Torsion springs usually last about 10,000 cycles; we replace them in matched pairs when appropriate.","We inspect cables, drums and rollers at the same visit so the repair lasts."]),
 ("emergency-garage-door-repair","Emergency Garage Door Repair","Door stuck open or closed? Call for urgent garage door repair in the Twin Cities.",
  ["A door stuck open is a security risk; a door stuck closed can trap your car.","Call us and we'll dispatch the next available technician.","We carry common springs, cables, rollers and opener parts on the truck.","Temporary securing of the door if a full repair needs a part order."]),
 ("winter-garage-door-care","Winter Garage Door Care in Minnesota","Cold weather is hard on springs, seals and openers. Here's how to protect your door.",
  ["Cold makes metal contract and lubricants stiffen, which can strain springs and openers.","Replace cracked bottom seals to keep snow, drafts and pests out.","Lubricate rollers and hinges with a garage-door-specific lubricant each fall.","Schedule a pre-winter tune-up before the first deep freeze."]),
]
POSTS = [
 ("signs-your-garage-door-spring-is-broken","5 Signs Your Garage Door Spring Is Broken","Know the warning signs before you get stuck with a door that won't open.",
  ["A loud bang from the garage.","The door feels heavy or won't lift.","The door opens a few inches then stops.","A visible gap in the torsion spring.","The opener strains or the door is crooked."]),
 ("how-often-should-you-service-your-garage-door","How Often Should You Service Your Garage Door?","Once a year is the usual rule; here's why and what a tune-up includes.",
  ["Annual maintenance catches worn parts early.","Homes with heavy daily use may benefit from twice-yearly checks.","A tune-up includes lubrication, balance testing, and safety checks.","Prevention is cheaper than emergency repair."]),
 ("garage-door-opener-buying-guide","Garage Door Opener Buying Guide","Belt, chain or direct drive? Choosing the right opener for your home.",
  ["Chain drive: durable and budget-friendly, but louder.","Belt drive: quiet, good for attached garages.","Direct drive: fewest moving parts and very quiet.","Look for battery backup and smartphone connectivity."]),
]

CSS = """:root{--navy:#12324f;--blue:#2b7bbb;--ice:#eaf4fb;--accent:#f2a900;--text:#1d2a36;--muted:#5b6b7a}
*{box-sizing:border-box}body{margin:0;font-family:system-ui,-apple-system,Segoe UI,Roboto,sans-serif;color:var(--text);line-height:1.6;background:#fff}
a{color:var(--blue)}img{max-width:100%}.wrap{max-width:1100px;margin:0 auto;padding:0 20px}
header.site{background:var(--navy);color:#fff;position:sticky;top:0;z-index:10}
header.site .wrap{display:flex;align-items:center;justify-content:space-between;gap:16px;flex-wrap:wrap;padding-top:12px;padding-bottom:12px}
.logo{color:#fff;text-decoration:none;font-weight:800;font-size:1.15rem}.logo span{color:var(--accent)}
nav ul{list-style:none;display:flex;gap:4px;margin:0;padding:0;flex-wrap:wrap;align-items:center}
nav li{position:relative}nav a{color:#fff;text-decoration:none;padding:8px 10px;display:block;border-radius:6px;font-size:.95rem}
nav a:hover{background:rgba(255,255,255,.12)}
nav li ul{display:none;position:absolute;left:0;top:100%;background:var(--navy);min-width:260px;flex-direction:column;padding:6px;border-radius:8px;box-shadow:0 8px 24px rgba(0,0,0,.25)}
nav li:hover>ul,nav li:focus-within>ul{display:flex}
.btn{display:inline-block;background:var(--accent);color:#1b1b1b!important;font-weight:700;padding:12px 22px;border-radius:8px;text-decoration:none;border:0;cursor:pointer;font-size:1rem}
.btn.alt{background:#fff}.btn:hover{filter:brightness(.95)}
.hero{background:linear-gradient(135deg,var(--navy),#1d5a8c);color:#fff;padding:72px 0}
.hero h1{font-size:clamp(2rem,5vw,3.2rem);line-height:1.15;margin:0 0 14px}.hero p{font-size:1.15rem;max-width:640px;margin:0 0 24px}
.hero.small{padding:44px 0}.hero.small h1{font-size:clamp(1.7rem,4vw,2.4rem)}
section{padding:56px 0}section.alt{background:var(--ice)}h2{color:var(--navy);margin-top:0}
.grid{display:grid;gap:20px;grid-template-columns:repeat(auto-fit,minmax(240px,1fr))}
.card{background:#fff;border:1px solid #d8e4ee;border-radius:12px;padding:22px}.card h3{margin-top:0;color:var(--navy)}
ul.check{list-style:none;padding:0}ul.check li{padding-left:28px;position:relative;margin:8px 0}ul.check li:before{content:"\\2713";position:absolute;left:0;color:var(--blue);font-weight:800}
.cta{background:var(--navy);color:#fff;text-align:center}.cta h2{color:#fff}
.crumbs{font-size:.9rem;color:#cfe3f3;margin-bottom:10px}.crumbs a{color:#cfe3f3}
form{display:grid;gap:14px;max-width:560px}label{font-weight:600;display:grid;gap:4px}
input,select,textarea{font:inherit;padding:10px;border:1px solid #b9c9d6;border-radius:8px;width:100%}
.coupon{border:3px dashed var(--accent);border-radius:12px;padding:22px;background:#fffbea}.coupon strong{font-size:1.6rem;color:var(--navy)}
.ph{background:repeating-linear-gradient(45deg,#dce9f3,#dce9f3 10px,#eaf4fb 10px,#eaf4fb 20px);height:180px;border-radius:12px;display:grid;place-items:center;color:var(--muted);font-weight:600}
footer{background:#0c2338;color:#cfe0ee;padding:44px 0 24px;font-size:.95rem}footer a{color:#cfe0ee}footer h4{color:#fff;margin:0 0 8px}
footer .grid{margin-bottom:20px}footer ul{list-style:none;padding:0;margin:0}.fine{border-top:1px solid #234;padding-top:16px;font-size:.85rem}
.callbar{display:none}@media(max-width:700px){.callbar{display:block;position:fixed;bottom:0;left:0;right:0;background:var(--accent);text-align:center;padding:14px;font-weight:800;z-index:20}.callbar a{color:#1b1b1b;text-decoration:none}body{padding-bottom:52px}nav li ul{position:static;box-shadow:none;display:flex;padding-left:12px}}
"""

def esc(s): return html.escape(s, quote=True)

def nav(depth):
    p = "../"*depth
    svc = "".join(f'<li><a href="{p}services/{s[0]}.html">{s[1]}</a></li>' for s in SERVICES)
    area = "".join(f'<li><a href="{p}service-areas/{slug(c)}.html">{c}</a></li>' for c in CITIES)
    return f'''<nav aria-label="Main"><ul>
<li><a href="{p}index.html">Home</a></li>
<li><a href="{p}about.html">About</a><ul><li><a href="{p}why-choose-us.html">Why Choose Us</a></li><li><a href="{p}meet-the-team.html">Meet the Team</a></li><li><a href="{p}gallery.html">Gallery</a></li><li><a href="{p}blog/index.html">Blog</a></li></ul></li>
<li><a href="{p}services/index.html">Services</a><ul>{svc}</ul></li>
<li><a href="{p}service-areas/index.html">Service Areas</a><ul>{area}</ul></li>
<li><a href="{p}coupons.html">Coupons</a></li>
<li><a href="{p}contact.html">Contact</a></li>
<li><a class="btn" href="tel:{PHONE_TEL}">{PHONE}</a></li></ul></nav>'''

def footer(depth):
    p = "../"*depth
    svc = "".join(f'<li><a href="{p}services/{s[0]}.html">{s[1]}</a></li>' for s in SERVICES)
    area = "".join(f'<li><a href="{p}service-areas/{slug(c)}.html">{c}</a></li>' for c in CITIES)
    return f'''<footer><div class="wrap"><div class="grid">
<div><h4>{NAME}</h4><p>Professional garage door repair, installation and maintenance across the Twin Cities.</p><p><a href="tel:{PHONE_TEL}">{PHONE}</a><br><a href="mailto:{EMAIL}">{EMAIL}</a></p></div>
<div><h4>Services</h4><ul>{svc}</ul></div><div><h4>Service Areas</h4><ul>{area}</ul></div>
<div><h4>More</h4><ul><li><a href="{p}garage-door-spring-repair.html">Spring Repair</a></li><li><a href="{p}emergency-garage-door-repair.html">Emergency Repair</a></li><li><a href="{p}winter-garage-door-care.html">Winter Care</a></li><li><a href="{p}blog/index.html">Blog</a></li><li><a href="{p}coupons.html">Coupons</a></li></ul></div>
</div><div class="fine">&copy; 2026 {NAME}. All rights reserved.</div></div></footer>
<div class="callbar"><a href="tel:{PHONE_TEL}">Call now: {PHONE}</a></div>'''

LOCAL_SCHEMA = f'''{{"@context":"https://schema.org","@type":"GarageDoorContractor","name":"{NAME}","url":"{DOMAIN}/","telephone":"{PHONE}","email":"{EMAIL}","areaServed":{[c for c in CITIES]!r},"address":{{"@type":"PostalAddress","addressRegion":"MN","addressCountry":"US"}}}}'''.replace("'",'"')

pages = []  # (path, priority)
def page(path, title, desc, body, h1=None, sub=None, crumbs=None, schema=None, hero=True, small=True):
    depth = path.count("/")
    p = "../"*depth
    cr = ""
    if crumbs:
        cr = '<div class="crumbs">'+" / ".join(f'<a href="{p}{u}">{esc(t)}</a>' for t,u in crumbs)+'</div>'
    heroh = ""
    if hero and h1:
        heroh = f'<div class="hero{" small" if small else ""}"><div class="wrap">{cr}<h1>{esc(h1)}</h1>{"<p>"+esc(sub)+"</p>" if sub else ""}</div></div>'
    sch = f'<script type="application/ld+json">{schema}</script>' if schema else ""
    doc = f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(title)}</title><meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{DOMAIN}/{path}"><meta property="og:title" content="{esc(title)}"><meta property="og:description" content="{esc(desc)}"><meta property="og:type" content="website">
<link rel="stylesheet" href="{p}assets/style.css">{sch}
<!-- TODO: add Google Analytics / Search Console verification tag here -->
</head><body><header class="site"><div class="wrap"><a class="logo" href="{p}index.html">Snowy <span>Summit</span> Garage Door</a>{nav(depth)}</div></header>
<main>{heroh}{body}
<section class="cta"><div class="wrap"><h2>Need garage door help today?</h2><p>Call us or request a free quote.</p><a class="btn" href="tel:{PHONE_TEL}">Call {PHONE}</a> <a class="btn alt" href="{p}contact.html">Request a Quote</a></div></section></main>
{footer(depth)}</body></html>'''
    full = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    open(full,"w").write(doc)
    pages.append(path)

def sec(inner, alt=False): return f'<section class="{"alt" if alt else ""}"><div class="wrap">{inner}</div></section>'
def lst(items): return '<ul class="check">'+"".join(f"<li>{esc(i)}</li>" for i in items)+"</ul>"
def cards(items, p=""):
    return '<div class="grid">'+"".join(f'<div class="card"><h3>{esc(t)}</h3><p>{esc(d)}</p><a href="{p}{u}">Learn more &rarr;</a></div>' for t,d,u in items)+"</div>"

svc_cards = [(s[1],s[2],f"services/{s[0]}.html") for s in SERVICES]
area_cards = [(c,f"Garage door repair, installation and maintenance in {c}, MN.",f"service-areas/{slug(c)}.html") for c in CITIES]

# Home
page("index.html", f"Garage Door Repair & Installation in Minneapolis-St. Paul, MN | {NAME}",
 "Snowy Summit Garage Door Repair: garage door repair, installation, openers and maintenance across the Twin Cities. Call for a free quote.",
 sec("<h2>Our Services</h2>"+cards(svc_cards))+
 sec("<h2>Why homeowners call us</h2>"+lst(["Upfront, honest pricing","Technicians who explain the problem before the repair","Repairs, installs and openers from one local team","Serving Minneapolis, St. Paul, Woodbury, Eagan, Lakeville and Eden Prairie"])+'<p><a href="why-choose-us.html">See why choose us &rarr;</a></p>',True)+
 sec("<h2>Service Areas</h2>"+cards(area_cards)),
 h1="Garage Door Repair You Can Count On", sub="Repair, installation, openers and maintenance for Twin Cities homes. Fast scheduling and fair pricing.", small=False, schema=LOCAL_SCHEMA)
# fix hero CTA on home
f=os.path.join(OUT,"index.html"); t=open(f).read()
t=t.replace("</p></div></div><section",f'</p><a class="btn" href="tel:{PHONE_TEL}">Call {PHONE}</a> <a class="btn alt" href="contact.html">Free Quote</a></div></div><section',1)
open(f,"w").write(t)

page("about.html", f"About Us | {NAME}", "Learn about Snowy Summit Garage Door Repair, our mission and our commitment to Twin Cities homeowners.",
 sec("<h2>Our Story</h2><p>[PLACEHOLDER: Add your company background, years in business and mission here.]</p><p>Snowy Summit Garage Door Repair helps Twin Cities homeowners keep their garage doors safe, quiet and working every day of the year.</p>")+
 sec(cards([("Why Choose Us","What sets us apart.","why-choose-us.html"),("Meet the Team","The people behind the work.","meet-the-team.html"),("Gallery","Photos of our recent jobs.","gallery.html"),("Blog","Tips and guides.","blog/index.html")]),True),
 h1="About Snowy Summit Garage Door Repair", crumbs=[("Home","index.html")])
page("why-choose-us.html", f"Why Choose Us | {NAME}", "Honest pricing, skilled technicians and reliable garage door service in the Twin Cities.",
 sec("<h2>What you can expect</h2>"+lst(["Clear, upfront quotes before work begins","Trained technicians and quality parts","Same-day service when available","Work cleaned up and tested for safety","[PLACEHOLDER: add warranty, licensing and insurance details]"])),
 h1="Why Choose Us", crumbs=[("Home","index.html"),("About","about.html")])
page("meet-the-team.html", f"Meet the Team | {NAME}", "Meet the Snowy Summit Garage Door Repair team.",
 sec('<div class="grid">'+"".join(f'<div class="card"><div class="ph">Photo</div><h3>[Name {i}]</h3><p>[Role / short bio]</p></div>' for i in (1,2,3))+"</div>"),
 h1="Meet the Team", crumbs=[("Home","index.html"),("About","about.html")])
page("gallery.html", f"Photo Gallery | {NAME}", "Photos of garage door repairs and installations by Snowy Summit Garage Door Repair.",
 sec('<p>[PLACEHOLDER: replace these boxes with your job photos. Use descriptive alt text.]</p><div class="grid">'+"".join('<div class="ph">Job photo</div>' for _ in range(9))+"</div>"),
 h1="Gallery", crumbs=[("Home","index.html"),("About","about.html")])

# Services
page("services/index.html", f"Garage Door Services | {NAME}", "Garage door repair, installation, opener installation, opener repair and maintenance in the Twin Cities.",
 sec(cards([(a,b,f"{c}.html") for c,a,b,_ in SERVICES]).replace('href="','href="')), h1="Our Garage Door Services", crumbs=[("Home","index.html")])
for sl,t,d,items in SERVICES:
    others = [(s[1],s[2],f"{s[0]}.html") for s in SERVICES if s[0]!=sl]
    page(f"services/{sl}.html", f"{t} in Minneapolis-St. Paul, MN | {NAME}", d,
     sec(f"<h2>{esc(t)}</h2><p>{esc(d)}</p><h3>What's included</h3>"+lst(items)+f'<p><a class="btn" href="../contact.html">Request a Quote</a></p>')+
     sec("<h2>Related services</h2>"+cards(others),True)+
     sec("<h2>Where we work</h2><p>"+", ".join(f'<a href="../service-areas/{slug(c)}.html">{c}</a>' for c in CITIES)+"</p>"),
     h1=t, sub=d, crumbs=[("Home","index.html"),("Services","services/index.html")],
     schema=f'{{"@context":"https://schema.org","@type":"Service","name":"{t}","provider":{{"@type":"GarageDoorContractor","name":"{NAME}"}},"areaServed":"Minneapolis-St. Paul, MN"}}')

# Areas
page("service-areas/index.html", f"Service Areas | {NAME}", "We serve Minneapolis, St. Paul, Woodbury, Eagan, Lakeville and Eden Prairie, MN.",
 sec("<p>[Adjust to the areas you actually serve.]</p>"+cards([(a,b,c.split('/')[1]) for a,b,c in area_cards])), h1="Areas We Serve", crumbs=[("Home","index.html")])
for c in CITIES:
    page(f"service-areas/{slug(c)}.html", f"Garage Door Repair in {c}, MN | {NAME}",
     f"Garage door repair, installation, opener service and maintenance in {c}, MN. Call Snowy Summit for a free quote.",
     sec(f"<h2>Garage Door Service in {c}, MN</h2><p>Snowy Summit Garage Door Repair serves {c} homeowners with dependable repair, installation and maintenance. [PLACEHOLDER: add local details, neighborhoods and landmarks to make this page unique.]</p><h3>Services in {c}</h3>"+
         '<ul class="check">'+"".join(f'<li><a href="../services/{s[0]}.html">{s[1]}</a></li>' for s in SERVICES)+"</ul>")+
     sec(f"<h2>Get a quote in {c}</h2><p><a class='btn' href='../contact.html'>Request a Quote</a></p>",True),
     h1=f"Garage Door Repair in {c}, MN", sub=f"Local garage door service for {c} homes.", crumbs=[("Home","index.html"),("Service Areas","service-areas/index.html")])

# Coupons
page("coupons.html", f"Garage Door Coupons & Specials | {NAME}", "Save on garage door repair, installation and maintenance with Snowy Summit coupons.",
 sec('<p>[PLACEHOLDER: replace with your real offers.]</p><div class="grid">'+"".join(f'<div class="coupon"><strong>{a}</strong><p>{b}</p><p><small>Mention this coupon when booking. Terms apply.</small></p></div>' for a,b in [("$XX OFF","Any garage door repair"),("FREE","Estimate on new door installation"),("$XX OFF","Opener installation"),("$XX","Seasonal tune-up special")])+"</div>"),
 h1="Coupons & Specials", crumbs=[("Home","index.html")])

# Contact
page("contact.html", f"Contact & Free Quote | {NAME}", "Contact Snowy Summit Garage Door Repair for a free quote or to book a service call.",
 sec(f'''<div class="grid"><div><h2>Request a Free Quote</h2>
<form action="https://formsubmit.co/{EMAIL}" method="POST"><!-- PLACEHOLDER form handler: swap for your form service -->
<label>Name<input name="name" required></label><label>Phone<input name="phone" type="tel" required></label><label>Email<input name="email" type="email"></label>
<label>City<select name="city">{"".join(f"<option>{c}</option>" for c in CITIES)}<option>Other</option></select></label>
<label>Service<select name="service">{"".join(f"<option>{s[1]}</option>" for s in SERVICES)}</select></label>
<label>Describe the problem<textarea name="message" rows="4"></textarea></label><button class="btn" type="submit">Send Request</button></form></div>
<div><h2>Call or Email</h2><p><strong><a href="tel:{PHONE_TEL}">{PHONE}</a></strong><br><a href="mailto:{EMAIL}">{EMAIL}</a></p><p>Hours: [PLACEHOLDER]</p><p>Address: [PLACEHOLDER]</p>
<div class="ph" style="height:260px">[Embed Google Map here]</div></div></div>'''),
 h1="Contact Us", sub="Call, request a quote, or book a service visit.", crumbs=[("Home","index.html")])

# Extra SEO pages
for sl,t,d,pts in EXTRA:
    page(f"{sl}.html", f"{t} | {NAME}", d, sec(f"<h2>{esc(t)}</h2><p>{esc(d)}</p>"+lst(pts)+'<p><a class="btn" href="contact.html">Request a Quote</a></p>'), h1=t, sub=d, crumbs=[("Home","index.html")])

# Blog
page("blog/index.html", f"Garage Door Blog | {NAME}", "Garage door tips, buying guides and maintenance advice from Snowy Summit.",
 sec(cards([(t,d,f"{s}.html") for s,t,d,_ in POSTS]).replace('href="','href="')), h1="Garage Door Tips & Guides", crumbs=[("Home","index.html")])
for sl,t,d,pts in POSTS:
    page(f"blog/{sl}.html", f"{t} | {NAME}", d, sec(f"<p>{esc(d)}</p>"+lst(pts)+'<p><a href="../contact.html">Need help? Request a quote.</a></p>'), h1=t, crumbs=[("Home","index.html"),("Blog","blog/index.html")])

open(os.path.join(OUT,"assets/style.css"),"w").write(CSS)
sm = ['<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for pth in pages: sm.append(f"<url><loc>{DOMAIN}/{pth if pth!='index.html' else ''}</loc></url>")
sm.append("</urlset>")
open(os.path.join(OUT,"sitemap.xml"),"w").write("\n".join(sm))
open(os.path.join(OUT,"robots.txt"),"w").write(f"User-agent: *\nAllow: /\nSitemap: {DOMAIN}/sitemap.xml\n")
print(len(pages),"pages")
