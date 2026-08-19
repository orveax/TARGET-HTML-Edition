/* ORIGEX — ORX-P01 | PG19 Become Partner runtime | Copyright © ORVEAX */
(() => {
  'use strict';
  const root=document.querySelector('[data-pg19-root]'); if(!root) return;
  const form=root.querySelector('[data-orx-partner-form]'); if(!form) return;
  const isArabic=document.documentElement.lang.toLowerCase().startsWith('ar');
  const marketsUrl=root.dataset.marketsUrl||'../assets/data/markets.json';
  const marketSelect=form.querySelector('[name="marketId"]');
  const marketSummary=root.querySelector('[data-orx-partner-market-summary]');
  const queryNotice=root.querySelector('[data-orx-partner-query-notice]');
  const channelGroup=form.querySelector('[data-orx-partner-channels]');
  const categoryGroup=form.querySelector('[data-orx-partner-categories]');
  const channelError=form.querySelector('[data-orx-partner-channels-error]');
  const categoryError=form.querySelector('[data-orx-partner-categories-error]');
  const fileInput=form.querySelector('[data-orx-partner-file]');
  const fileName=form.querySelector('[data-orx-partner-file-name]');
  const errorBox=form.querySelector('[data-orx-partner-error]');
  const successBox=form.querySelector('[data-orx-partner-success]');
  const languageLinks=[...document.querySelectorAll('.orx-lang-switch,.orx-mobile-nav a[lang][href*="become-partner.html"]')];
  const maxBytes=10*1024*1024;
  const allowed=['pdf','jpg','jpeg','png','doc','docx'];
  let markets=[];

  const text=isArabic?{
    select:'اختر سوق Demo رئيسيًا',
    loadError:'تعذر تحميل قائمة الأسواق التجريبية. أعد المحاولة بعد تشغيل القالب من خادم ويب محلي.',
    invalidQuery:'Market ID الموجود في الرابط غير صالح؛ اختر السوق أو النطاق المطلوب من القائمة.',
    fileError:'اختر ملف PDF أو JPG أو PNG أو DOC/DOCX بحجم لا يتجاوز 10 MB.',
    channelError:'اختر قناة بيع أو توزيع واحدة على الأقل.',
    categoryError:'اختر فئة منتجات واحدة على الأقل.',
    success:'تم التحقق من نموذج الشراكة داخل العرض التوضيحي. لم يتم إرسال أو حفظ أي بيانات أو ملفات، ولم يتم إنشاء تعيين أو حصرية أو حقوق توزيع. اربط النموذج بخدمة معالجة فعلية قبل النشر.',
    demo:'سجل سوق Demo من البيانات المحلية',
    channels:'قنوات توضيحية في هذا السوق'
  }:{
    select:'Select a primary Demo market',
    loadError:'The illustrative market list could not be loaded. Retry after running the template from a local web server.',
    invalidQuery:'The Market ID in the URL is not valid; select the required market or territory from the list.',
    fileError:'Choose a PDF, JPG, PNG or DOC/DOCX file no larger than 10 MB.',
    channelError:'Select at least one sales or distribution channel.',
    categoryError:'Select at least one product category of interest.',
    success:'The demo partnership profile has been validated. No data or files were transmitted or stored, and no appointment, exclusivity or distribution rights were created. Connect the form to a real processing service before publication.',
    demo:'Demo market record from the local dataset',
    channels:'Illustrative channels in this market'
  };

  const hideStatuses=()=>{ if(errorBox) errorBox.hidden=true; if(successBox) successBox.hidden=true; };
  const showError=(msg)=>{ if(!errorBox) return; errorBox.textContent=msg; errorBox.hidden=false; errorBox.focus?.(); };
  const displayName=(m)=>isArabic?m.nameAr:m.nameEn;
  const displaySummary=(m)=>isArabic?m.summaryAr:m.summaryEn;
  const displayTags=(m)=>isArabic?m.channelTagsAr:m.channelTagsEn;
  const syncLanguage=(id)=>languageLinks.forEach(link=>{ const u=new URL(link.href,window.location.href); if(id) u.searchParams.set('market',id); else u.searchParams.delete('market'); link.href=`${u.pathname}${u.search}`; });
  const updateCounts=()=>{
    root.dataset.pg19ChannelCount=String(channelGroup?.querySelectorAll('input[type="checkbox"]:checked').length||0);
    root.dataset.pg19CategoryCount=String(categoryGroup?.querySelectorAll('input[type="checkbox"]:checked').length||0);
  };
  const renderMarket=(market)=>{
    if(!marketSummary) return;
    if(!market){ marketSummary.hidden=true; marketSummary.replaceChildren(); return; }
    const head=document.createElement('div'); head.className='orx-partner-market-summary__head';
    const title=document.createElement('div'); const strong=document.createElement('strong'); strong.textContent=displayName(market); const small=document.createElement('div'); small.className='orx-muted'; small.textContent=text.demo; title.append(strong,small); head.append(title);
    const p=document.createElement('p'); p.className='orx-muted'; p.textContent=displaySummary(market)||'';
    const tagWrap=document.createElement('div'); tagWrap.className='orx-partner-market-summary__tags'; tagWrap.setAttribute('aria-label',text.channels);
    (displayTags(market)||[]).forEach(tag=>{ const span=document.createElement('span'); span.textContent=tag; tagWrap.append(span); });
    marketSummary.replaceChildren(head,p,tagWrap); marketSummary.hidden=false;
  };
  const applyMarket=(id,{fromQuery=false}={})=>{
    const market=markets.find(x=>x.id===id);
    if(!market){ marketSelect.value=''; renderMarket(null); syncLanguage(''); if(fromQuery&&queryNotice){ queryNotice.textContent=text.invalidQuery; queryNotice.hidden=false; } return false; }
    marketSelect.value=market.id; renderMarket(market); syncLanguage(market.id); if(queryNotice) queryNotice.hidden=true; root.dataset.pg19MarketId=market.id; return true;
  };
  const clearGroupError=(group,error)=>{ if(group) group.setAttribute('aria-invalid','false'); if(error) error.hidden=true; };
  const validateGroup=(group,error,msg)=>{
    const valid=!!group?.querySelector('input[type="checkbox"]:checked');
    if(group) group.setAttribute('aria-invalid',valid?'false':'true');
    if(error){ error.textContent=msg; error.hidden=valid; }
    if(!valid) group?.querySelector('input[type="checkbox"]')?.focus();
    return valid;
  };
  const loadMarkets=async()=>{
    try{
      const res=await fetch(marketsUrl,{credentials:'same-origin'}); if(!res.ok) throw new Error('markets');
      markets=await res.json();
      marketSelect.replaceChildren(new Option(text.select,''));
      markets.forEach(m=>marketSelect.add(new Option(displayName(m),m.id)));
      const requested=new URLSearchParams(location.search).get('market');
      if(requested) applyMarket(requested,{fromQuery:true}); else renderMarket(null);
      root.dataset.pg19Markets='ready'; root.dataset.pg19MarketCount=String(markets.length);
    }catch(e){ root.dataset.pg19Markets='error'; marketSelect.disabled=true; showError(text.loadError); }
  };

  marketSelect.addEventListener('change',()=>{ hideStatuses(); applyMarket(marketSelect.value); });
  channelGroup?.addEventListener('change',()=>{ hideStatuses(); clearGroupError(channelGroup,channelError); updateCounts(); });
  categoryGroup?.addEventListener('change',()=>{ hideStatuses(); clearGroupError(categoryGroup,categoryError); updateCounts(); });
  fileInput?.addEventListener('change',()=>{
    hideStatuses(); const file=fileInput.files?.[0]; if(!file){ if(fileName) fileName.textContent=''; return; }
    const ext=(file.name.split('.').pop()||'').toLowerCase();
    if(!allowed.includes(ext)||file.size>maxBytes){ fileInput.value=''; if(fileName) fileName.textContent=''; showError(text.fileError); return; }
    if(fileName) fileName.textContent=file.name;
  });
  form.addEventListener('submit',(event)=>{
    event.preventDefault(); hideStatuses();
    const nativeValid=form.checkValidity(); if(!nativeValid){ form.reportValidity(); return; }
    const channelsValid=validateGroup(channelGroup,channelError,text.channelError);
    const categoriesValid=validateGroup(categoryGroup,categoryError,text.categoryError);
    updateCounts();
    if(!channelsValid||!categoriesValid) return;
    const file=fileInput?.files?.[0];
    if(file){ const ext=(file.name.split('.').pop()||'').toLowerCase(); if(!allowed.includes(ext)||file.size>maxBytes){ showError(text.fileError); return; } }
    if(successBox){ successBox.textContent=text.success; successBox.hidden=false; successBox.focus?.(); }
  });
  updateCounts();
  loadMarkets();
})();
