#!/usr/bin/env python3
"""Generates the Snowy Summit static site. Edit CONFIG/content, then run: python3 build.py"""
import os, html
OUT = os.path.dirname(os.path.abspath(__file__))
DOMAIN = "https://snowysummitgaragedoor.com"
NAME = "Snowy Summit Garage Door Repair"
PHONE = "(612) 555-0100"          # PLACEHOLDER - replace
PHONE_TEL = "+16125550100"        # PLACEHOLDER - replace
GA_ID = ""            # e.g. "G-XXXXXXXXXX" - Google Analytics 4 measurement ID
GSC_TOKEN = ""        # Google Search Console HTML-tag verification code
BING_TOKEN = ""       # Bing Webmaster Tools verification code
LASTMOD = "2026-11-02"
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
.skip{position:absolute;left:-999px;top:0;background:#fff;color:#000;padding:10px 16px;z-index:100}.skip:focus{left:8px;top:8px}
:focus-visible{outline:3px solid var(--accent);outline-offset:2px}
.menu-btn{display:none;background:transparent;border:2px solid #fff;color:#fff;border-radius:8px;padding:8px 14px;font:inherit;font-weight:700;cursor:pointer}
.trust{background:#fff;border-bottom:1px solid #d8e4ee;padding:18px 0}.trust ul{list-style:none;margin:0;padding:0;display:grid;gap:12px;grid-template-columns:repeat(auto-fit,minmax(190px,1fr));text-align:center;font-weight:700;color:var(--navy)}
.trust li span{display:block;font-size:1.6rem}
.steps{counter-reset:s;display:grid;gap:20px;grid-template-columns:repeat(auto-fit,minmax(220px,1fr))}.steps div{background:#fff;border-radius:12px;padding:22px;border:1px solid #d8e4ee}
.steps div:before{counter-increment:s;content:counter(s);display:grid;place-items:center;width:38px;height:38px;border-radius:50%;background:var(--navy);color:#fff;font-weight:800;margin-bottom:10px}
.card{transition:transform .2s,box-shadow .2s}.card:hover{transform:translateY(-4px);box-shadow:0 10px 24px rgba(18,50,79,.12)}
details{background:#fff;border:1px solid #d8e4ee;border-radius:10px;padding:14px 18px;margin:10px 0}summary{cursor:pointer;font-weight:700;color:var(--navy)}
.quote{font-style:italic}.stars{color:var(--accent);letter-spacing:2px}
.js .reveal{opacity:0;transform:translateY(18px);transition:opacity .6s,transform .6s}.js .reveal.in{opacity:1;transform:none}
@media(prefers-reduced-motion:reduce){.js .reveal{opacity:1;transform:none;transition:none}.card{transition:none}}
.gal{border:0;padding:0;cursor:zoom-in;width:100%;font:inherit}
.lb{position:fixed;inset:0;background:rgba(0,0,0,.85);display:none;place-items:center;z-index:50;padding:20px}.lb.open{display:grid}.lb div{background:#fff;border-radius:12px;padding:20px;max-width:640px;width:100%;text-align:center}
.map{width:100%;height:320px;border:0;border-radius:12px}
.msg{padding:12px 16px;border-radius:8px;background:#e6f6ea;border:1px solid #9bd3a8;display:none}.msg.show{display:block}
input:invalid:not(:placeholder-shown){border-color:#c0392b}
.row2{display:grid;gap:14px;grid-template-columns:1fr 1fr}@media(max-width:560px){.row2{grid-template-columns:1fr}}
@media(max-width:900px){.menu-btn{display:block}nav{display:none;width:100%}nav.open{display:block}nav ul{flex-direction:column;align-items:stretch}nav li ul{display:flex}}
footer{background:#0c2338;color:#cfe0ee;padding:44px 0 24px;font-size:.95rem}footer a{color:#cfe0ee}footer h4{color:#fff;margin:0 0 8px}
footer .grid{margin-bottom:20px}footer ul{list-style:none;padding:0;margin:0}.fine{border-top:1px solid #234;padding-top:16px;font-size:.85rem}
.callbar{display:none}@media(max-width:700px){.callbar{display:block;position:fixed;bottom:0;left:0;right:0;background:var(--accent);text-align:center;padding:14px;font-weight:800;z-index:20}.callbar a{color:#1b1b1b;text-decoration:none}body{padding-bottom:52px}nav li ul{position:static;box-shadow:none;display:flex;padding-left:12px}}
"""

JS = r"""(function(){
var d=document;
var mb=d.querySelector('.menu-btn'),nav=d.getElementById('nav');
if(mb)mb.addEventListener('click',function(){var o=nav.classList.toggle('open');mb.setAttribute('aria-expanded',o)});
if('IntersectionObserver' in window){var io=new IntersectionObserver(function(e){e.forEach(function(x){if(x.isIntersecting){x.target.classList.add('in');io.unobserve(x.target)}})},{threshold:.1});d.querySelectorAll('.reveal').forEach(function(el){io.observe(el)})}else{d.querySelectorAll('.reveal').forEach(function(el){el.classList.add('in')})}
var lb=d.querySelector('.lb');
if(lb){d.querySelectorAll('[data-lb]').forEach(function(b){b.addEventListener('click',function(){lb.querySelector('.lbt').textContent=b.dataset.lb;lb.classList.add('open');lb.querySelector('[data-close]').focus()})});
lb.addEventListener('click',function(e){if(e.target===lb||e.target.hasAttribute('data-close'))lb.classList.remove('open')});
d.addEventListener('keydown',function(e){if(e.key==='Escape')lb.classList.remove('open')})}
var md=d.querySelector('[data-mindate]');if(md){md.min=new Date().toISOString().split('T')[0]}
d.querySelectorAll('form[data-ajax]').forEach(function(f){f.addEventListener('submit',function(e){e.preventDefault();var btn=f.querySelector('button');btn.disabled=true;btn.textContent='Sending...';
fetch(f.action,{method:'POST',body:new FormData(f),headers:{Accept:'application/json'}}).then(function(r){if(!r.ok)throw 0;f.reset();var m=d.querySelector('.msg');m.classList.add('show');m.scrollIntoView({behavior:'smooth',block:'center'})}).catch(function(){alert('Sorry, something went wrong. Please call us instead.')}).finally(function(){btn.disabled=false;btn.textContent='Send Request'})})});
})();"""
def esc(s): return html.escape(s, quote=True)

def nav(depth):
    p = "../"*depth
    svc = "".join(f'<li><a href="{p}services/{s[0]}.html">{s[1]}</a></li>' for s in SERVICES)
    area = "".join(f'<li><a href="{p}service-areas/{slug(c)}.html">{c}</a></li>' for c in CITIES)
    return f'''<button class="menu-btn" aria-expanded="false" aria-controls="nav">&#9776; Menu</button><nav id="nav" aria-label="Main"><ul>
<li><a href="{p}index.html">Home</a></li>
<li><a href="{p}about.html">About</a><ul><li><a href="{p}why-choose-us.html">Why Choose Us</a></li><li><a href="{p}meet-the-team.html">Meet the Team</a></li><li><a href="{p}gallery.html">Gallery</a></li><li><a href="{p}blog/index.html">Blog</a></li></ul></li>
<li><a href="{p}services/index.html">Services</a><ul>{svc}</ul></li>
<li><a href="{p}service-areas/index.html">Service Areas</a><ul>{area}</ul></li>
<li><a href="{p}coupons.html">Coupons</a></li>
<li><a href="{p}contact.html">Contact</a></li>
<li><a href="{p}booking.html">Book Online</a></li>
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

import json
LOCAL_SCHEMA = json.dumps({"@context":"https://schema.org","@type":"GarageDoorContractor","@id":DOMAIN+"/#business","name":NAME,"url":DOMAIN+"/","telephone":PHONE,"email":EMAIL,"image":DOMAIN+"/assets/og-image.svg","priceRange":"$$",
 "address":{"@type":"PostalAddress","streetAddress":"[PLACEHOLDER]","addressLocality":"Minneapolis","addressRegion":"MN","postalCode":"[PLACEHOLDER]","addressCountry":"US"},
 "areaServed":[{"@type":"City","name":c+", MN"} for c in CITIES],
 "openingHoursSpecification":[{"@type":"OpeningHoursSpecification","dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday"],"opens":"08:00","closes":"18:00"}],
 "hasOfferCatalog":{"@type":"OfferCatalog","name":"Garage door services","itemListElement":[{"@type":"Offer","itemOffered":{"@type":"Service","name":x[1]}} for x in SERVICES]},
 "sameAs":[]})

pages = []  # (path, priority)
def page(path, title, desc, body, h1=None, sub=None, crumbs=None, schema=None, hero=True, small=True, hero_extra="", trust=False):
    depth = path.count("/")
    hero_extra_after = TRUST if trust else ""
    p = "../"*depth
    cr = ""
    if crumbs:
        cr = '<div class="crumbs">'+" / ".join(f'<a href="{p}{u}">{esc(t)}</a>' for t,u in crumbs)+'</div>'
    heroh = ""
    if hero and h1:
        heroh = f'<div class="hero{" small" if small else ""}"><div class="wrap">{cr}<h1>{esc(h1)}</h1>{"<p>"+esc(sub)+"</p>" if sub else ""}{hero_extra}</div></div>{hero_extra_after}'
    sch = f'<script type="application/ld+json">{schema}</script>' if schema else ""
    verif = (f'<meta name="google-site-verification" content="{GSC_TOKEN}">' if GSC_TOKEN else "")+(f'<meta name="msvalidate.01" content="{BING_TOKEN}">' if BING_TOKEN else "")
    ga = (f'<script async src="https://www.googletagmanager.com/gtag/js?id={GA_ID}"></script><script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments)}}gtag("js",new Date());gtag("config","{GA_ID}")</script>' if GA_ID else "")
    bc = ""
    if crumbs:
        items = [(t,u) for t,u in crumbs]+[(h1 or title, path)]
        li = ",".join(f'{{"@type":"ListItem","position":{i+1},"name":"{t}","item":"{DOMAIN}/{u}"}}' for i,(t,u) in enumerate(items))
        bc = f'<script type="application/ld+json">{{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{li}]}}</script>'

    doc = f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(title)}</title><meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{DOMAIN}/{path}"><meta property="og:title" content="{esc(title)}"><meta property="og:description" content="{esc(desc)}"><meta property="og:type" content="website"><meta property="og:url" content="{DOMAIN}/{path}"><meta property="og:site_name" content="{NAME}"><meta property="og:locale" content="en_US"><meta property="og:image" content="{DOMAIN}/assets/og-image.svg"><meta name="twitter:card" content="summary_large_image"><meta name="robots" content="index,follow,max-image-preview:large">{verif}
<link rel="icon" href="{p}assets/favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="{p}assets/style.css">{sch}{bc}{ga}
<!-- TODO: add Google Analytics / Search Console verification tag here -->
</head><body><script>document.documentElement.className+=" js"</script><a class="skip" href="#main">Skip to content</a><header class="site"><div class="wrap"><a class="logo" href="{p}index.html">Snowy <span>Summit</span> Garage Door</a>{nav(depth)}</div></header>
<main id="main">{heroh}{body}
<section class="cta"><div class="wrap"><h2>Need garage door help today?</h2><p>Call us or request a free quote.</p><a class="btn" href="tel:{PHONE_TEL}">Call {PHONE}</a> <a class="btn alt" href="{p}contact.html">Request a Quote</a></div></section></main>
{footer(depth)}<script src="{p}assets/site.js" defer></script></body></html>'''
    full = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    open(full,"w").write(doc)
    pages.append(path)

def sec(inner, alt=False): return f'<section class="reveal {"alt" if alt else ""}"><div class="wrap">{inner}</div></section>'
def lst(items): return '<ul class="check">'+"".join(f"<li>{esc(i)}</li>" for i in items)+"</ul>"
def cards(items, p=""):
    return '<div class="grid">'+"".join(f'<div class="card"><h3>{esc(t)}</h3><p>{esc(d)}</p><a href="{p}{u}">Learn more &rarr;</a></div>' for t,d,u in items)+"</div>"

TRUST = '<div class="trust"><div class="wrap"><ul><li><span>&#9889;</span>Fast scheduling</li><li><span>&#128176;</span>Upfront pricing</li><li><span>&#128737;</span>Safety-tested repairs</li><li><span>&#128205;</span>Serving 6 Twin Cities areas</li></ul></div></div>'
FAQS = [("Do you offer same-day garage door repair?","Often, yes. Call us and we will schedule the soonest available visit. [PLACEHOLDER: confirm your policy]"),
 ("How much does garage door repair cost?","Cost depends on the part and the door. We give a clear quote before any work begins."),
 ("How long does a new garage door installation take?","Most installations take a few hours to a day. [PLACEHOLDER: confirm]"),
 ("Which areas do you serve?","Minneapolis, St. Paul, Woodbury, Eagan, Lakeville and Eden Prairie, MN.")]
def faq(items=FAQS):
    return "<h2>Frequently Asked Questions</h2>"+"".join(f"<details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>" for q,a in items)
def faq_schema(items=FAQS):
    e=",".join(f'{{"@type":"Question","name":"{q}","acceptedAnswer":{{"@type":"Answer","text":"{a}"}}}}' for q,a in items)
    return f'{{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{e}]}}'
MAP = '<iframe class="map" title="Service area map" loading="lazy" src="https://www.google.com/maps?q=Minneapolis,+MN&output=embed"></iframe>'
svc_cards = [(s[1],s[2],f"services/{s[0]}.html") for s in SERVICES]
area_cards = [(c,f"Garage door repair, installation and maintenance in {c}, MN.",f"service-areas/{slug(c)}.html") for c in CITIES]

# Home
page("index.html", f"Garage Door Repair & Installation in Minneapolis-St. Paul, MN | {NAME}",
 "Snowy Summit Garage Door Repair: garage door repair, installation, openers and maintenance across the Twin Cities. Call for a free quote.",
 sec("<h2>Our Services</h2>"+cards(svc_cards))+
 sec("<h2>Why homeowners call us</h2>"+lst(["Upfront, honest pricing","Technicians who explain the problem before the repair","Repairs, installs and openers from one local team","Serving Minneapolis, St. Paul, Woodbury, Eagan, Lakeville and Eden Prairie"])+'<p><a href="why-choose-us.html">See why choose us &rarr;</a></p>',True)+
 sec("<h2>How it works</h2><div class='steps'><div><h3>Call or book</h3><p>Phone us or book online in under a minute.</p></div><div><h3>Get a clear quote</h3><p>We diagnose the problem and quote before starting.</p></div><div><h3>Fixed right</h3><p>We repair, test for safety and clean up.</p></div></div>",True)+
 sec("<h2>What customers say</h2><div class='grid'>"+"".join("<div class='card'><div class='stars'>&#9733;&#9733;&#9733;&#9733;&#9733;</div><p class='quote'>&ldquo;[PLACEHOLDER: add a real customer review here.]&rdquo;</p><strong>[Customer name], [City]</strong></div>" for _ in range(3))+"</div>")+
 sec(faq(),True)+
 sec("<h2>Service Areas</h2>"+cards(area_cards)+"<br>"+MAP),
 h1="Garage Door Repair You Can Count On", sub="Repair, installation, openers and maintenance for Twin Cities homes. Fast scheduling and fair pricing.", small=False,
 hero_extra=f'<a class="btn" href="tel:{PHONE_TEL}">Call {PHONE}</a> <a class="btn alt" href="booking.html">Book Online</a>', trust=True,
 schema=LOCAL_SCHEMA+'</script><script type="application/ld+json">'+faq_schema())
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
 sec('<p>[PLACEHOLDER: replace these boxes with your job photos (use &lt;img&gt; with descriptive alt text). Click a photo to enlarge.]</p><div class="grid">'+"".join(f'<button class="gal ph" data-lb="Job photo {i}" type="button">Job photo {i}</button>' for i in range(1,10))+'</div><div class="lb" role="dialog" aria-modal="true" aria-label="Photo preview"><div><p class="lbt"></p><button class="btn" type="button" data-close>Close</button></div></div>'),
 h1="Gallery", crumbs=[("Home","index.html"),("About","about.html")])

# Services
page("services/index.html", f"Garage Door Services | {NAME}", "Garage door repair, installation, opener installation, opener repair and maintenance in the Twin Cities.",
 sec(cards([(a,b,f"{c}.html") for c,a,b,_ in SERVICES]).replace('href="','href="')), h1="Our Garage Door Services", crumbs=[("Home","index.html")])
for sl,t,d,items in SERVICES:
    others = [(s[1],s[2],f"{s[0]}.html") for s in SERVICES if s[0]!=sl]
    page(f"services/{sl}.html", f"{t} in Minneapolis-St. Paul, MN | {NAME}", d,
     sec(f"<h2>{esc(t)}</h2><p>{esc(d)}</p><h3>What's included</h3>"+lst(items)+f'<p><a class="btn" href="../contact.html">Request a Quote</a></p>')+
     sec("<h2>Related services</h2>"+cards(others),True)+
     sec(faq([(f"How quickly can you handle {t.lower()}?","Call us and we will schedule the soonest available visit. [PLACEHOLDER]"),("Do you give a quote first?","Yes. You approve the price before work begins.")]),True)+
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
     sec(faq([(f"Do you offer garage door repair in {c}, MN?",f"Yes. Snowy Summit serves {c} and nearby communities with repair, installation, opener service and maintenance."),(f"How fast can a technician reach {c}?","[PLACEHOLDER: add typical response time for this city]"),(f"What does garage door spring repair cost in {c}?","We quote a clear price before work begins. Call for an estimate.")]),True)+
     sec(f"<h2>Nearby areas we serve</h2><p>"+", ".join(f'<a href="{slug(o)}.html">Garage door repair in {o}</a>' for o in CITIES if o!=c)+"</p><p><a class='btn' href='../contact.html'>Get a quote in "+c+"</a></p>"),
     h1=f"Garage Door Repair in {c}, MN", sub=f"Local garage door service for {c} homes.", crumbs=[("Home","index.html"),("Service Areas","service-areas/index.html")],
     schema=json.dumps({"@context":"https://schema.org","@type":"GarageDoorContractor","name":NAME,"url":DOMAIN+"/","telephone":PHONE,"areaServed":{"@type":"City","name":c+", MN"}})+'</script><script type="application/ld+json">'+faq_schema([(f"Do you offer garage door repair in {c}, MN?",f"Yes. Snowy Summit serves {c} and nearby communities with repair, installation, opener service and maintenance."),(f"How fast can a technician reach {c}?","[PLACEHOLDER: add typical response time for this city]"),(f"What does garage door spring repair cost in {c}?","We quote a clear price before work begins. Call for an estimate.")]))

# Coupons
page("coupons.html", f"Garage Door Coupons & Specials | {NAME}", "Save on garage door repair, installation and maintenance with Snowy Summit coupons.",
 sec('<p>[PLACEHOLDER: replace with your real offers.]</p><div class="grid">'+"".join(f'<div class="coupon"><strong>{a}</strong><p>{b}</p><p><small>Mention this coupon when booking. Terms apply.</small></p></div>' for a,b in [("$XX OFF","Any garage door repair"),("FREE","Estimate on new door installation"),("$XX OFF","Opener installation"),("$XX","Seasonal tune-up special")])+"</div>"),
 h1="Coupons & Specials", crumbs=[("Home","index.html")])

# Contact
page("contact.html", f"Contact & Free Quote | {NAME}", "Contact Snowy Summit Garage Door Repair for a free quote or to book a service call.",
 sec(f'''<div class="grid"><div><h2>Request a Free Quote</h2>
<form data-ajax action="https://formsubmit.co/ajax/{EMAIL}" method="POST"><!-- PLACEHOLDER form handler: swap for your form service -->
<label>Name<input name="name" required></label><label>Phone<input name="phone" type="tel" required></label><label>Email<input name="email" type="email"></label>
<label>City<select name="city">{"".join(f"<option>{c}</option>" for c in CITIES)}<option>Other</option></select></label>
<label>Service<select name="service">{"".join(f"<option>{s[1]}</option>" for s in SERVICES)}</select></label>
<label>Describe the problem<textarea name="message" rows="4"></textarea></label><button class="btn" type="submit">Send Request</button></form></div>
<div><h2>Call or Email</h2><p><strong><a href="tel:{PHONE_TEL}">{PHONE}</a></strong><br><a href="mailto:{EMAIL}">{EMAIL}</a></p><p>Hours: [PLACEHOLDER]</p><p>Address: [PLACEHOLDER]</p>
{MAP}</div></div><p class="msg" role="status">Thanks! We received your request and will call you shortly.</p>'''),
 h1="Contact Us", sub="Call, request a quote, or book a service visit.", crumbs=[("Home","index.html")])

page("booking.html", f"Book a Service Appointment | {NAME}", "Book a garage door repair, installation or maintenance appointment online with Snowy Summit.",
 sec(f'''<div class="grid"><div><h2>Book an Appointment</h2>
<form data-ajax action="https://formsubmit.co/ajax/{EMAIL}" method="POST"><!-- PLACEHOLDER form handler -->
<div class="row2"><label>Name<input name="name" required autocomplete="name"></label><label>Phone<input name="phone" type="tel" required autocomplete="tel"></label></div>
<label>Email<input name="email" type="email" autocomplete="email"></label>
<label>Service address<input name="address" required autocomplete="street-address"></label>
<div class="row2"><label>Service<select name="service">{"".join(f"<option>{s[1]}</option>" for s in SERVICES)}</select></label>
<label>City<select name="city">{"".join(f"<option>{c}</option>" for c in CITIES)}<option>Other</option></select></label></div>
<div class="row2"><label>Preferred date<input name="date" type="date" data-mindate required></label>
<label>Time window<select name="window"><option>Morning (8-12)</option><option>Afternoon (12-4)</option><option>Evening (4-7)</option></select></label></div>
<label>Notes<textarea name="message" rows="3"></textarea></label><button class="btn" type="submit">Request Appointment</button></form>
<p class="msg" role="status">Thanks! We received your booking request and will confirm by phone.</p></div>
<div><h2>Need it now?</h2><p>For urgent repairs call <a href="tel:{PHONE_TEL}"><strong>{PHONE}</strong></a>.</p>{MAP}</div></div>'''),
 h1="Book Online", sub="Pick a day and time window. We'll confirm by phone.", crumbs=[("Home","index.html")])
page("404.html", f"Page Not Found | {NAME}", "Page not found.", sec('<p><a class="btn" href="index.html">Back to home</a> <a class="btn alt" href="contact.html">Contact us</a></p>'), h1="Page not found")
pages.remove("404.html")

# Extra SEO pages
for sl,t,d,pts in EXTRA:
    page(f"{sl}.html", f"{t} | {NAME}", d, sec(f"<h2>{esc(t)}</h2><p>{esc(d)}</p>"+lst(pts)+'<p><a class="btn" href="contact.html">Request a Quote</a></p>'), h1=t, sub=d, crumbs=[("Home","index.html")])

# Blog
page("blog/index.html", f"Garage Door Blog | {NAME}", "Garage door tips, buying guides and maintenance advice from Snowy Summit.",
 sec(cards([(t,d,f"{s}.html") for s,t,d,_ in POSTS]).replace('href="','href="')), h1="Garage Door Tips & Guides", crumbs=[("Home","index.html")])
for sl,t,d,pts in POSTS:
    page(f"blog/{sl}.html", f"{t} | {NAME}", d, sec(f"<p>{esc(d)}</p>"+lst(pts)+'<p><a href="../contact.html">Need help? Request a quote.</a></p>'), h1=t, crumbs=[("Home","index.html"),("Blog","blog/index.html")])

open(os.path.join(OUT,"assets/style.css"),"w").write(CSS)
open(os.path.join(OUT,"assets/og-image.svg"),"w").write('<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="630"><rect width="1200" height="630" fill="#12324f"/><text x="600" y="290" font-family="Arial" font-size="72" font-weight="700" fill="#fff" text-anchor="middle">Snowy Summit</text><text x="600" y="380" font-family="Arial" font-size="48" fill="#f2a900" text-anchor="middle">Garage Door Repair</text><text x="600" y="460" font-family="Arial" font-size="30" fill="#cfe3f3" text-anchor="middle">Minneapolis - St. Paul, MN</text></svg>')
open(os.path.join(OUT,"assets/favicon.svg"),"w").write('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="12" fill="#12324f"/><path d="M8 52 32 16l24 36z" fill="#fff"/><rect x="22" y="36" width="20" height="16" fill="#f2a900"/></svg>')
open(os.path.join(OUT,"assets/site.js"),"w").write(JS)
sm = ['<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for pth in pages: pr = "1.0" if pth=="index.html" else "0.8" if pth.startswith(("services/","service-areas/")) or pth in("contact.html","booking.html") else "0.6"
    sm.append(f"<url><loc>{DOMAIN}/{pth if pth!='index.html' else ''}</loc><lastmod>{LASTMOD}</lastmod><priority>{pr}</priority></url>")
sm.append("</urlset>")
open(os.path.join(OUT,"sitemap.xml"),"w").write("\n".join(sm))
open(os.path.join(OUT,"robots.txt"),"w").write(f"User-agent: *\nAllow: /\nSitemap: {DOMAIN}/sitemap.xml\n")
print(len(pages),"pages")
