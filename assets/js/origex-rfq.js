/* ORIGEX — ORX-P01 | PG18 RFQ runtime | Copyright © ORVEAX */
(() => {
  'use strict';
  const root=document.querySelector('[data-pg18-root]'); if(!root) return;
  const form=root.querySelector('[data-orx-rfq-form]'); if(!form) return;
  const isArabic=document.documentElement.lang.toLowerCase().startsWith('ar');
  const productsUrl=root.dataset.productsUrl||'../assets/data/products.json';
  const productSelect=form.querySelector('[name="productId"]');
  const fileInput=form.querySelector('[data-orx-rfq-file]');
  const fileName=form.querySelector('[data-orx-rfq-file-name]');
  const errorBox=form.querySelector('[data-orx-rfq-error]');
  const successBox=form.querySelector('[data-orx-rfq-success]');
  const productSummary=root.querySelector('[data-orx-rfq-product-summary]');
  const queryNotice=root.querySelector('[data-orx-rfq-query-notice]');
  const languageLinks=[...document.querySelectorAll('.orx-lang-switch,.orx-mobile-nav a[lang][href*="rfq.html"]')];
  const maxBytes=10*1024*1024;
  const allowed=['pdf','jpg','jpeg','png','doc','docx'];
  let products=[];

  const text=isArabic?{
    select:'اختر منتج Demo', loadError:'تعذر تحميل قائمة المنتجات التجريبية. يمكنك إعادة المحاولة بعد تشغيل القالب من خادم ويب محلي.',
    invalidQuery:'Product ID الموجود في الرابط غير صالح؛ اختر المنتج المطلوب من القائمة.', fileError:'اختر ملف PDF أو JPG أو PNG أو DOC/DOCX بحجم لا يتجاوز 10 MB.',
    success:'تم التحقق من طلب عرض السعر داخل العرض التوضيحي. لم يتم إرسال أو حفظ أي بيانات أو ملفات، ولم يتم إنشاء سعر أو رقم طلب. اربط النموذج بخدمة معالجة فعلية قبل النشر.',
    category:'الفئة', origin:'المنشأ', pack:'العبوة'
  }:{
    select:'Select a Demo product', loadError:'The illustrative product list could not be loaded. Retry after running the template from a local web server.',
    invalidQuery:'The Product ID in the URL is not valid; select the required product from the list.', fileError:'Choose a PDF, JPG, PNG or DOC/DOCX file no larger than 10 MB.',
    success:'The demo RFQ has been validated. No data or files were transmitted or stored, and no price or request number was generated. Connect the form to a real processing service before publication.',
    category:'Category', origin:'Origin', pack:'Pack'
  };
  const categoryLabels=isArabic?{ambient:'أغذية جافة',beverages:'مشروبات',dairy:'ألبان',frozen:'مجمدات',confectionery:'حلويات',ingredients:'مكونات'}:{ambient:'Ambient Foods',beverages:'Beverages',dairy:'Dairy',frozen:'Frozen',confectionery:'Confectionery',ingredients:'Ingredients'};
  const originLabels=isArabic?{IT:'إيطاليا',JO:'الأردن',EG:'مصر',TR:'تركيا',NL:'هولندا',PL:'بولندا',BE:'بلجيكا'}:{IT:'Italy',JO:'Jordan',EG:'Egypt',TR:'Türkiye',NL:'Netherlands',PL:'Poland',BE:'Belgium'};
  const hideStatuses=()=>{ if(errorBox) errorBox.hidden=true; if(successBox) successBox.hidden=true; };
  const showError=(msg)=>{ if(!errorBox) return; errorBox.textContent=msg; errorBox.hidden=false; errorBox.focus?.(); };
  const displayName=(p)=>isArabic?p.nameAr:p.nameEn;
  const syncLanguage=(id)=>languageLinks.forEach(link=>{ const u=new URL(link.href,window.location.href); if(id) u.searchParams.set('product',id); else u.searchParams.delete('product'); link.href=`${u.pathname}${u.search}`; });
  const renderSummary=(p)=>{
    if(!productSummary) return;
    if(!p){ productSummary.hidden=true; productSummary.replaceChildren(); return; }
    const wrap=document.createElement('div'); wrap.className='orx-rfq-product-summary__head';
    const title=document.createElement('div'); const strong=document.createElement('strong'); strong.textContent=displayName(p); const small=document.createElement('div'); small.className='orx-muted'; small.textContent=isArabic?'سجل منتج Demo من البيانات المحلية':'Demo product record from the local dataset'; title.append(strong,small); wrap.append(title);
    const facts=document.createElement('div'); facts.className='orx-rfq-product-summary__facts';
    [[text.category,categoryLabels[p.categoryId]||p.categoryId],[text.origin,originLabels[p.originCode]||p.originCode],[text.pack,isArabic?p.packSizeAr:p.packSizeEn]].forEach(([label,value])=>{ const item=document.createElement('div'); item.className='orx-rfq-product-summary__fact'; const s=document.createElement('span'); s.textContent=label; const b=document.createElement('strong'); b.textContent=value||'—'; item.append(s,b); facts.append(item); });
    productSummary.replaceChildren(wrap,facts); productSummary.hidden=false;
  };
  const applySelection=(id,{fromQuery=false}={})=>{
    const p=products.find(x=>x.id===id);
    if(!p){ productSelect.value=''; renderSummary(null); syncLanguage(''); if(fromQuery&&queryNotice){ queryNotice.textContent=text.invalidQuery; queryNotice.hidden=false; } return false; }
    productSelect.value=p.id; renderSummary(p); syncLanguage(p.id); if(queryNotice) queryNotice.hidden=true; return true;
  };
  const loadProducts=async()=>{
    try{
      const res=await fetch(productsUrl,{credentials:'same-origin'}); if(!res.ok) throw new Error('products');
      products=await res.json();
      productSelect.replaceChildren(new Option(text.select,''));
      products.forEach(p=>productSelect.add(new Option(displayName(p),p.id)));
      const requested=new URLSearchParams(location.search).get('product');
      if(requested) applySelection(requested,{fromQuery:true}); else renderSummary(null);
      root.dataset.pg18Products='ready'; root.dataset.pg18ProductCount=String(products.length);
    }catch(e){ root.dataset.pg18Products='error'; productSelect.disabled=true; showError(text.loadError); }
  };
  productSelect.addEventListener('change',()=>{ hideStatuses(); applySelection(productSelect.value); });
  fileInput?.addEventListener('change',()=>{
    hideStatuses(); const file=fileInput.files?.[0]; if(!file){ if(fileName) fileName.textContent=''; return; }
    const ext=(file.name.split('.').pop()||'').toLowerCase();
    if(!allowed.includes(ext)||file.size>maxBytes){ fileInput.value=''; if(fileName) fileName.textContent=''; showError(text.fileError); return; }
    if(fileName) fileName.textContent=file.name;
  });
  form.addEventListener('submit',(event)=>{
    event.preventDefault(); hideStatuses();
    if(!form.checkValidity()){ form.reportValidity(); return; }
    const file=fileInput?.files?.[0];
    if(file){ const ext=(file.name.split('.').pop()||'').toLowerCase(); if(!allowed.includes(ext)||file.size>maxBytes){ showError(text.fileError); return; } }
    if(successBox){ successBox.textContent=text.success; successBox.hidden=false; successBox.focus?.(); }
  });
  loadProducts();
})();
