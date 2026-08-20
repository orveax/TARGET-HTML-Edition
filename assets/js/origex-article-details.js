(()=>{
  const root=document.querySelector('[data-pg25-root]');
  if(!root)return;
  const params=new URLSearchParams(location.search);
  const requested=params.get('id');
  const templates=[...document.querySelectorAll('template[data-article-template]')];
  const defaultId='article-001';
  const order=[defaultId,...templates.map(t=>t.dataset.articleTemplate)];
  const validIds=new Set(order);
  const selected=requested&&validIds.has(requested)?requested:defaultId;
  const invalid=Boolean(requested&&!validIds.has(requested));

  const fields={
    title:root.querySelector('[data-orx-article-title]'),
    category:root.querySelector('[data-orx-article-category]'),
    date:root.querySelector('[data-orx-article-date]'),
    read:root.querySelector('[data-orx-article-read]'),
    deck:root.querySelector('[data-orx-article-deck]'),
    body:root.querySelector('[data-orx-article-body]')
  };
  const invalidBox=root.querySelector('[data-orx-article-invalid]');
  const langSwitches=[...document.querySelectorAll('.orx-lang-switch,.orx-mobile-nav a[lang]')];
  const prev=root.querySelector('[data-orx-article-prev]');
  const next=root.querySelector('[data-orx-article-next]');
  const related=root.querySelector('[data-orx-related-articles]');
  const copyBtn=root.querySelector('[data-orx-share-copy]');
  const copyStatus=root.querySelector('[data-orx-share-status]');
  const email=root.querySelector('[data-orx-share-email]');
  const linkedin=root.querySelector('[data-orx-share-linkedin]');
  const whatsapp=root.querySelector('[data-orx-share-whatsapp]');

  const liveMeta={
    id:defaultId,
    title:root.dataset.defaultTitle||fields.title?.textContent.trim()||'',
    category:root.dataset.defaultCategory||fields.category?.textContent.trim()||'',
    date:root.dataset.defaultDate||fields.date?.textContent.trim()||'',
    read:root.dataset.defaultRead||fields.read?.textContent.trim()||'',
    deck:root.dataset.defaultDeck||fields.deck?.textContent.trim()||'',
    excerpt:root.dataset.defaultExcerpt||fields.deck?.textContent.trim()||''
  };
  const catalog=[liveMeta,...templates.map(t=>({
    id:t.dataset.articleTemplate,
    title:t.dataset.title||'',
    category:t.dataset.category||'',
    date:t.dataset.date||'',
    read:t.dataset.read||'',
    deck:t.dataset.deck||'',
    excerpt:t.dataset.excerpt||t.dataset.deck||''
  }))];
  const byId=new Map(catalog.map(x=>[x.id,x]));

  function renderTemplate(id){
    if(id===defaultId)return;
    const t=templates.find(x=>x.dataset.articleTemplate===id);
    if(!t)return;
    const meta=byId.get(id);
    if(fields.title)fields.title.textContent=meta.title;
    if(fields.category)fields.category.textContent=meta.category;
    if(fields.date)fields.date.textContent=meta.date;
    if(fields.read)fields.read.textContent=meta.read;
    if(fields.deck)fields.deck.textContent=meta.deck;
    if(fields.body){fields.body.replaceChildren();fields.body.append(t.content.cloneNode(true));}
  }

  function setInvalidState(){
    if(!invalidBox)return;
    invalidBox.hidden=!invalid;
    if(invalid)invalidBox.setAttribute('data-invalid-id',requested);
  }

  function articleHref(id){return `article-details.html?id=${encodeURIComponent(id)}`;}

  function setLanguageSwitches(){
    for(const link of langSwitches){
      const base=link.getAttribute('href')?.split('?')[0];
      if(base)link.setAttribute('href',`${base}?id=${encodeURIComponent(selected)}`);
    }
  }

  function setAdjacent(){
    const index=order.indexOf(selected);
    const prevId=index>0?order[index-1]:null;
    const nextId=index<order.length-1?order[index+1]:null;
    for(const [link,id] of [[prev,prevId],[next,nextId]]){
      if(!link)continue;
      if(!id){link.hidden=true;link.removeAttribute('href');continue;}
      const item=byId.get(id);link.hidden=false;link.href=articleHref(id);
      const title=link.querySelector('[data-orx-adjacent-title]');if(title)title.textContent=item.title;
    }
  }

  function relatedItems(){
    const current=byId.get(selected);
    const same=catalog.filter(x=>x.id!==selected&&x.category===current.category);
    const other=catalog.filter(x=>x.id!==selected&&x.category!==current.category);
    return [...same,...other].slice(0,3);
  }

  function setRelated(){
    if(!related)return;
    related.replaceChildren(...relatedItems().map(item=>{
      const a=document.createElement('a');a.className='orx-related-card';a.href=articleHref(item.id);
      const meta=document.createElement('div');meta.className='orx-related-card__meta';meta.textContent=`${item.category} · ${item.read}`;
      const h=document.createElement('h3');h.textContent=item.title;
      const p=document.createElement('p');p.textContent=item.excerpt;
      const action=document.createElement('span');action.className='orx-text-action';action.textContent=root.dataset.relatedAction||'Read article';
      a.append(meta,h,p,action);return a;
    }));
  }

  function currentShareUrl(){
    const u=new URL(location.href);u.search='';u.hash='';u.searchParams.set('id',selected);return u.href;
  }

  function setShare(){
    const item=byId.get(selected);const url=currentShareUrl();
    if(email)email.href=`mailto:?subject=${encodeURIComponent(item.title)}&body=${encodeURIComponent(url)}`;
    if(linkedin)linkedin.href=`https://www.linkedin.com/sharing/share-offsite/?url=${encodeURIComponent(url)}`;
    if(whatsapp)whatsapp.href=`https://wa.me/?text=${encodeURIComponent(item.title+' '+url)}`;
    if(copyBtn)copyBtn.dataset.copyUrl=url;
  }

  async function copyUrl(){
    const url=copyBtn?.dataset.copyUrl||currentShareUrl();let ok=false;
    try{if(navigator.clipboard&&window.isSecureContext){await navigator.clipboard.writeText(url);ok=true;}}catch(_){ok=false;}
    if(!ok){
      const ta=document.createElement('textarea');ta.value=url;ta.setAttribute('readonly','');ta.style.position='fixed';ta.style.opacity='0';document.body.append(ta);ta.select();
      try{ok=document.execCommand('copy');}catch(_){ok=false;}ta.remove();
    }
    if(copyStatus)copyStatus.textContent=ok?(root.dataset.copySuccess||'Link copied'):(root.dataset.copyFailure||'Copy unavailable');
  }

  copyBtn?.addEventListener('click',copyUrl);
  renderTemplate(selected);
  setInvalidState();
  setLanguageSwitches();
  setAdjacent();
  setRelated();
  setShare();
  root.dataset.pg25Ready='true';
  root.dataset.pg25Article=selected;
})();
