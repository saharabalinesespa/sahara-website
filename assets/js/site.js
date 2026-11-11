/* Sahara site behaviour — no dependencies */
(function(){
'use strict';
var S=window.SAHARA||{};
var $=function(s,c){return (c||document).querySelector(s)};
var $$=function(s,c){return Array.prototype.slice.call((c||document).querySelectorAll(s))};
var wa=function(msg){return 'https://wa.me/'+S.phone+'?text='+encodeURIComponent(msg)};
var aed=function(n){return 'AED '+n.toLocaleString('en-US')};

/* mobile drawer */
var burger=$('.burger'),drawer=$('.drawer');
function setDrawer(open){
  if(!burger||!drawer)return;
  drawer.classList.toggle('open',open);
  burger.setAttribute('aria-expanded',open?'true':'false');
  document.body.style.overflow=open?'hidden':'';
}
if(burger){
  burger.addEventListener('click',function(){setDrawer(burger.getAttribute('aria-expanded')!=='true')});
  $$('a',drawer).forEach(function(a){a.addEventListener('click',function(){setDrawer(false)})});
  document.addEventListener('keydown',function(e){if(e.key==='Escape')setDrawer(false)});
  window.addEventListener('resize',function(){if(window.innerWidth>1100)setDrawer(false)});
}

/* scroll reveal */
var rv=$$('.rv');
if('IntersectionObserver' in window){
  var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}})},{threshold:.08,rootMargin:'0px 0px -40px 0px'});
  rv.forEach(function(el){io.observe(el)});
}else{rv.forEach(function(el){el.classList.add('in')})}

/* helpers */
function itemById(id){return S.items.filter(function(i){return i.id===id})[0]}
function today(){var d=new Date();d.setMinutes(d.getMinutes()-d.getTimezoneOffset());return d.toISOString().slice(0,10)}
function timeOptions(sel){
  if(!sel)return;
  var h,m,out='<option value="">Choose a time</option>';
  for(h=10;h<=23;h++){for(m=0;m<60;m+=30){
    if(h===23&&m>0)continue;
    var ap=h>=12?'pm':'am',hh=h>12?h-12:h;
    out+='<option>'+hh+':'+(m?'30':'00')+' '+ap+'</option>';
  }}
  sel.innerHTML=out;
}
function fmtDate(v){if(!v)return '';var d=new Date(v+'T00:00:00');return d.toLocaleDateString('en-GB',{weekday:'long',day:'numeric',month:'long',year:'numeric'})}
function showResult(box,url,fallbackText){
  box.className='ok';
  box.innerHTML='<b>One last step:</b> WhatsApp has opened with your request — press <b>Send</b> so it reaches us. <br><a href="'+url+'" target="_blank" rel="noopener">WhatsApp didn’t open? Tap here</a>';
  box.scrollIntoView({behavior:'smooth',block:'center'});
}

/* ---------- BOOKING ---------- */
var bk=$('#booking');
if(bk){
  var st={id:'',guests:1,group:3,dur:0};
  var optsEl=$('#tx-opts'),durEl=$('#dur-opts'),estT=$('#est-total'),estN=$('#est-note');
  function buildOpts(){
  var cats=S.cats,html='';
  Object.keys(cats).forEach(function(c){
    html+='<div class="cathead">'+cats[c].name+'</div>';
    S.items.filter(function(i){return i.cat===c}).forEach(function(i){
      html+='<button type="button" class="opt" data-id="'+i.id+'"><b>'+i.name+'</b><span>'+i.blurb+'</span><em>'+(i.cat==='hair'?'From ':'')+aed(i.opts[0][1])+(i.opts.length>1||i.cat==='hair'?'+':'')+'</em></button>';
    });
  });
  optsEl.innerHTML=html;
  }
  buildOpts();
  function render(){
    $$('.opt',optsEl).forEach(function(b){b.classList.toggle('on',b.dataset.id===st.id)});
    var it=st.id?itemById(st.id):null,dh='';
    if(it){
      if(it.opts[0][0]===0){dh='<p class="sub" style="margin:0">Single price — no duration needed.</p>';st.dur=0}
      else it.opts.forEach(function(o,idx){dh+='<button type="button" class="opt'+(idx===st.dur?' on':'')+'" data-d="'+idx+'"><b>'+o[0]+' minutes</b><em>'+aed(o[1])+(it.cat==='hair'?' from':'')+'</em></button>'});
    }else dh='<p class="sub" style="margin:0">Choose a treatment first.</p>';
    durEl.innerHTML=dh;
    $$('.opt',durEl).forEach(function(b){b.addEventListener('click',function(){st.dur=+b.dataset.d;render()})});
    var n=st.guests===1?1:(st.guests===2?2:st.group);
    $('#grp-wrap').classList.toggle('hide',st.guests!==3);
    $$('[data-g]').forEach(function(b){b.classList.toggle('on',+b.dataset.g===st.guests)});
    if(it){
      var base=it.opts[Math.min(st.dur,it.opts.length-1)][1],total=base*n;
      estT.textContent=aed(total)+(it.cat==='hair'?' +':'');
      estN.textContent=(it.name+(it.opts[0][0]?' · '+it.opts[Math.min(st.dur,it.opts.length-1)][0]+' min':'')+' · '+n+' guest'+(n>1?'s':''));
      var extra='';
      if(total<S.minOrder)extra=' — minimum booking value AED '+S.minOrder+' applies';
      estN.textContent+=extra;
    }else{estT.textContent='—';estN.textContent='Choose a treatment to see an estimate'}
  }
  optsEl.addEventListener('click',function(e){
    var b=e.target.closest('.opt');if(!b)return;
    st.id=b.dataset.id;st.dur=0;render();
    $('#step2').scrollIntoView({behavior:'smooth',block:'start'});
  });
  $$('[data-g]').forEach(function(b){b.addEventListener('click',function(){st.guests=+b.dataset.g;render()})});
  $('#grp').addEventListener('input',function(){st.group=Math.max(3,Math.min(20,+this.value||3));render()});
  /* help me choose */
  $$('[data-goal]').forEach(function(b){b.addEventListener('click',function(){
    $$('[data-goal]').forEach(function(x){x.classList.remove('on')});b.classList.add('on');
    var ids=b.dataset.goal.split(',');
    $$('.opt',optsEl).forEach(function(o){o.style.opacity=ids.indexOf(o.dataset.id)>-1?'1':'.35'});
    $('#goal-note').textContent=b.dataset.note;
    var f=$('.opt[data-id="'+ids[0]+'"]',optsEl);if(f)f.scrollIntoView({behavior:'smooth',block:'center'});
  })});
  $('#goal-clear').addEventListener('click',function(){$$('.opt',optsEl).forEach(function(o){o.style.opacity='1'});$$('[data-goal]').forEach(function(x){x.classList.remove('on')});$('#goal-note').textContent=''});
  var dt=$('#date');dt.min=today();timeOptions($('#time'));
  var q=new URLSearchParams(location.search).get('treatment');
  if(q&&itemById(q))st.id=q;
  render();
  (window.sahHooks=window.sahHooks||[]).push(function(){buildOpts();if(st.id&&!itemById(st.id))st.id='';render()});
  $('#bk-form').addEventListener('submit',function(e){
    e.preventDefault();
    var err=$('#bk-err'),it=st.id?itemById(st.id):null;
    var v=function(id){return ($('#'+id).value||'').trim()};
    if(!it){err.textContent='Please choose a treatment.';return}
    if(!dt.value||!v('time')){err.textContent='Please choose a date and preferred time.';return}
    if(!v('fn')||!v('wnum')){err.textContent='Please add your name and WhatsApp number.';return}
    if(!v('bldg')&&!v('pin')){err.textContent='Please add your building/community or a Google Maps pin.';return}
    err.textContent='';
    var n=st.guests===1?1:(st.guests===2?2:st.group),o=it.opts[Math.min(st.dur,it.opts.length-1)];
    var msg='Hi Sahara, I would like to book:\n\n'+
      'Treatment: '+it.name+(o[0]?' ('+o[0]+' min)':'')+'\n'+
      'Guests: '+n+(st.guests===2?' (couple, 2 therapists)':'')+'\n'+
      'Estimated price: '+aed(o[1]*n)+(it.cat==='hair'?' (from)':'')+'\n'+
      'Date: '+fmtDate(dt.value)+'\nTime: '+v('time')+'\n\n'+
      'Name: '+v('fn')+' '+v('ln')+'\nWhatsApp: '+v('wnum')+'\n'+
      'Location: '+[v('bldg'),v('apt')].filter(Boolean).join(', ')+'\n'+
      (v('pin')?'Maps pin: '+v('pin')+'\n':'')+
      (v('notes')?'Notes: '+v('notes')+'\n':'')+
      (v('heard')?'Heard about Sahara: '+v('heard'):'');
    var url=wa(msg);
    window.open(url,'_blank');
    showResult($('#bk-ok'),url);
  });
  $('#geo').addEventListener('click',function(){
    if(!navigator.geolocation){alert('Location is not available on this device.');return}
    navigator.geolocation.getCurrentPosition(function(p){$('#pin').value='https://maps.google.com/?q='+p.coords.latitude+','+p.coords.longitude},function(){alert('Could not read your location — please paste a Google Maps link instead.')});
  });
}

/* ---------- VOUCHER ---------- */
var vf=$('#voucher');
if(vf){
  var vs={kind:'treatment'};
  var tsel=$('#v-tx');
  function vlist(){var keep=tsel.value;tsel.innerHTML=S.items.filter(function(i){return i.cat==='massage'||i.cat==='facial'||i.cat==='body'}).map(function(i){return '<option value="'+i.id+'">'+i.name+'</option>'}).join('');if(keep&&itemById(keep))tsel.value=keep}
  vlist();
  function vdur(){
    var it=itemById(tsel.value),h='';
    it.opts.forEach(function(o,idx){h+='<option value="'+idx+'">'+o[0]+' min — '+aed(o[1])+'</option>'});
    $('#v-dur').innerHTML=h;
  }
  function vprev(){
    var occ=$('#v-occ').value||'A Gift for You',what='';
    if(vs.kind==='treatment'){var it=itemById(tsel.value),o=it.opts[+$('#v-dur').value||0];what=o[0]+' min '+it.name;var amount=o[1]}
    else{var a=+$('#v-amt').value||0;what=a?aed(a):'Gift amount';amount=a}
    $('#vp-occ').textContent=occ;
    $('#vp-for').textContent=$('#v-to').value?('For '+$('#v-to').value):'For your loved one';
    $('#vp-what').textContent=what;
    $('#vp-msg').textContent=$('#v-msg').value?('“'+$('#v-msg').value+'”'):'';
    $('#vp-from').textContent=$('#v-from').value?('With love from '+$('#v-from').value):'';
    $('#v-total').textContent=amount?aed(amount):'—';
    vs.what=what;vs.amount=amount;
  }
  $$('[data-k]').forEach(function(b){b.addEventListener('click',function(){
    vs.kind=b.dataset.k;$$('[data-k]').forEach(function(x){x.classList.toggle('on',x===b)});
    $('#v-tx-wrap').classList.toggle('hide',vs.kind!=='treatment');$('#v-amt-wrap').classList.toggle('hide',vs.kind!=='amount');vprev();
  })});
  tsel.addEventListener('change',function(){vdur();vprev()});
  $$('input,select,textarea',vf).forEach(function(el){el.addEventListener('input',vprev);el.addEventListener('change',vprev)});
  vdur();vprev();
  (window.sahHooks=window.sahHooks||[]).push(function(){vlist();vdur();vprev()});
  $('#v-form').addEventListener('submit',function(e){
    e.preventDefault();
    var v=function(id){return ($('#'+id).value||'').trim()},err=$('#v-err');
    if(!vs.amount){err.textContent='Please choose a treatment or enter an amount.';return}
    if(!v('v-name')||!v('v-phone')){err.textContent='Please add your name and WhatsApp number.';return}
    err.textContent='';
    var msg='Hi Sahara, I would like to buy a gift voucher:\n\n'+
      'Gift: '+vs.what+' ('+aed(vs.amount)+')\n'+
      'Occasion: '+($('#v-occ').value||'—')+'\n'+
      'For: '+(v('v-to')||'—')+'\nFrom: '+(v('v-from')||v('v-name'))+'\n'+
      (v('v-msg')?'Card message: '+v('v-msg')+'\n':'')+
      'Delivery: '+$('#v-del').value+'\n\n'+
      'My name: '+v('v-name')+'\nWhatsApp: '+v('v-phone')+(v('v-email')?'\nEmail: '+v('v-email'):'');
    var url=wa(msg);window.open(url,'_blank');showResult($('#v-ok'),url);
  });
}

/* ---------- CONTACT ---------- */
var cf=$('#contact-form');
if(cf){
  timeOptions($('#c-time'));
  var cs=$('#c-svc');
  cs.innerHTML='<option value="">Select a service…</option>'+Object.keys(S.cats).map(function(c){return '<option>'+S.cats[c].name+'</option>'}).join('')+'<option>Signature Package</option><option>Bridal Package</option><option>Corporate / Group Event</option>';
  cf.addEventListener('submit',function(e){
    e.preventDefault();
    var v=function(id){return ($('#'+id).value||'').trim()};
    if(!v('c-name')||!v('c-phone')){$('#c-err').textContent='Please add your name and phone.';return}
    $('#c-err').textContent='';
    var msg='Hi Sahara, enquiry from the website:\n\nName: '+v('c-name')+'\nPhone: '+v('c-phone')+'\nService: '+(v('c-svc')||'—')+'\nPreferred: '+(v('c-date')||'—')+' '+(v('c-time')||'')+'\nLocation / notes: '+(v('c-notes')||'—');
    var url=wa(msg);window.open(url,'_blank');showResult($('#c-ok'),url);
  });
}
})();

/* theme switch: dark (default) / light (white & black) */
(function(){
  var root=document.documentElement;
  function sync(){var l=root.getAttribute('data-theme')==='light';document.querySelectorAll('.themebtn').forEach(function(b){b.setAttribute('aria-label',l?'Switch to dark mode':'Switch to light mode');b.setAttribute('aria-pressed',l?'true':'false')});var m=document.querySelector('meta[name="theme-color"]');if(m)m.setAttribute('content',l?'#FFFFFF':'#0A0602')}
  document.addEventListener('click',function(e){var b=e.target.closest&&e.target.closest('.themebtn');if(!b)return;
    var l=root.getAttribute('data-theme')==='light';
    if(l)root.removeAttribute('data-theme');else root.setAttribute('data-theme','light');
    try{localStorage.setItem('sahara-theme',l?'dark':'light')}catch(x){}
    sync()});
  sync();
})();
