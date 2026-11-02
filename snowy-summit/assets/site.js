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

var W=d.getElementById('wiz');
if(W){(function(){
var step=1,titles=['How can we help you?','When do you need service?',"Let's get you into our system.","You're all set!"];
var st={service:'',zip:'',date:null,slot:'',vm:new Date()};st.vm.setDate(1);
var $=function(i){return d.getElementById(i)},err=$('wizErr'),next=$('wizNext'),back=$('wizBack');
var today=new Date();today.setHours(0,0,0,0);var maxM=new Date(today.getFullYear(),today.getMonth()+3,1);
var MN=['January','February','March','April','May','June','July','August','September','October','November','December'],DN=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'];
function fmt(h){var s=h>=12?'PM':'AM',x=h%12||12;return x+':00 '+s}
function slotsFor(dt){var dow=dt.getDay();if(dow===0)return[];var hrs=dow===6?[9,11,13]:[8,10,12,14,16],out=[],now=new Date();
hrs.forEach(function(h){var e=dow===6?h+2:h+2;var start=new Date(dt);start.setHours(h);if(dt.getTime()===today.getTime()&&start<=now)return;out.push(fmt(h)+' - '+fmt(e))});return out}
function hasSlots(dt){return dt>=today&&slotsFor(dt).length>0}
function cal(){var y=st.vm.getFullYear(),m=st.vm.getMonth(),first=new Date(y,m,1).getDay(),n=new Date(y,m+1,0).getDate();
var h='<div class="cal-h"><button type="button" id="cp" aria-label="Previous month"'+(new Date(y,m,1)<=new Date(today.getFullYear(),today.getMonth(),1)?' disabled':'')+'>&#8249;</button><span>'+MN[m]+' '+y+'</span><button type="button" id="cn" aria-label="Next month"'+(new Date(y,m+1,1)>=maxM?' disabled':'')+'>&#8250;</button></div><div class="cal-g">';
['S','M','T','W','T','F','S'].forEach(function(x){h+='<span>'+x+'</span>'});for(var i=0;i<first;i++)h+='<i></i>';
for(var k=1;k<=n;k++){var dt=new Date(y,m,k),sel=st.date&&st.date.getTime()===dt.getTime();h+='<button type="button" data-d="'+k+'" aria-pressed="'+(sel?'true':'false')+'"'+(hasSlots(dt)?'':' disabled')+'>'+k+'</button>'}
$('cal').innerHTML=h+'</div>';
$('cp').onclick=function(){st.vm=new Date(y,m-1,1);cal()};$('cn').onclick=function(){st.vm=new Date(y,m+1,1);cal()};
$('cal').querySelectorAll('[data-d]').forEach(function(b){b.onclick=function(){st.date=new Date(y,m,+b.dataset.d);st.slot='';err.textContent='';cal();slots()}})}
function slots(){var el=$('slots');if(!st.date){el.innerHTML='<p>Select a date to see available time windows.</p>';return}
var h='<h3>'+DN[st.date.getDay()]+', '+MN[st.date.getMonth()]+' '+st.date.getDate()+', '+st.date.getFullYear()+'</h3><div class="slot-row">';
slotsFor(st.date).forEach(function(s){h+='<button type="button" class="slot" aria-pressed="'+(st.slot===s)+'">'+s+'</button>'});el.innerHTML=h+'</div>';
el.querySelectorAll('.slot').forEach(function(b){b.onclick=function(){st.slot=b.textContent;err.textContent='';slots()}})}
function show(n){step=n;W.querySelectorAll('[data-step]').forEach(function(x){x.hidden=+x.dataset.step!==n});$('wizTitle').textContent=titles[n-1];$('wizProg').style.width=(n*25)+'%';err.textContent='';
back.hidden=n===1||n===4;next.hidden=n===4;next.textContent=n===3?'Book appointment':'Next';if(n===2){if(!st.date){var t=new Date(today);for(var i=0;i<60&&!hasSlots(t);i++)t.setDate(t.getDate()+1);st.date=hasSlots(t)?t:null;if(st.date){st.vm=new Date(t.getFullYear(),t.getMonth(),1)}}cal();slots()}
$('wizTitle').focus({preventScroll:true});W.scrollIntoView({behavior:'smooth',block:'start'})}
W.querySelectorAll('input[name=service]').forEach(function(r){r.addEventListener('change',function(){st.service=r.value;err.textContent=''})});
$('ph').addEventListener('input',function(e){var v=e.target.value.replace(/\D/g,'').slice(0,10);e.target.value=v.length>6?'('+v.slice(0,3)+') '+v.slice(3,6)+'-'+v.slice(6):v.length>3?'('+v.slice(0,3)+') '+v.slice(3):v});
back.onclick=function(){show(step-1)};
next.onclick=function(){
if(step===1){var z=$('zip').value.trim();if(!st.service){err.textContent='Please choose what you need help with.';return}if(!/^\d{5}$/.test(z)){err.textContent='Enter a valid 5-digit zip code.';$('zip').focus();return}st.zip=z;show(2)}
else if(step===2){if(!st.date||!st.slot){err.textContent='Pick a date and a time window.';return}show(3)}
else if(step===3){var fn=$('fn').value.trim(),ln=$('ln').value.trim(),ph=$('ph').value.replace(/\D/g,''),em=$('em').value.trim();
if(!fn||!ln){err.textContent='Enter your first and last name.';return}if(ph.length!==10){err.textContent='Enter a 10-digit phone number.';$('ph').focus();return}if(!/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(em)){err.textContent='Enter a valid email address.';$('em').focus();return}
var dtxt=DN[st.date.getDay()]+', '+MN[st.date.getMonth()]+' '+st.date.getDate()+', '+st.date.getFullYear()+' ('+st.slot+')';
next.disabled=true;next.textContent='Booking...';
fetch(W.dataset.endpoint,{method:'POST',headers:{'Content-Type':'application/json',Accept:'application/json'},body:JSON.stringify({_subject:'New appointment request',service:st.service,zip:st.zip,appointment:dtxt,name:fn+' '+ln,phone:$('ph').value,email:em,notes:$('nt').value})})
.then(function(r){if(!r.ok)throw 0;$('sum').textContent=fn+', your request for '+st.service+' on '+dtxt+' was received.';show(4)})
.catch(function(){err.textContent='We could not send your request. Please call us to book.'}).finally(function(){next.disabled=false;if(step===3)next.textContent='Book appointment'})}};
show(1)})()}
})();