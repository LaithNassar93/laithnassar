(function(){
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
})();