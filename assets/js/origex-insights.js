/* ORIGEX — PG24 Insights runtime */
(()=>{
  'use strict';
  const root=document.querySelector('[data-pg24-root]');
  if(!root) return;
  const cards=[...root.querySelectorAll('[data-orx-article-card]')];
  const filters=[...root.querySelectorAll('[data-orx-insights-filter]')];
  const search=root.querySelector('[data-orx-insights-search]');
  const count=root.querySelector('[data-orx-insights-count]');
  const empty=root.querySelector('[data-orx-insights-empty]');
  const pages=root.querySelector('[data-orx-insights-pages]');
  const langSwitch=document.querySelector('.orx-lang-switch');
  const validCategories=new Set(filters.map(b=>b.dataset.orxInsightsFilter));
  const pageSize=6;
  const params=new URLSearchParams(location.search);
  let category=validCategories.has(params.get('category'))?params.get('category'):'all';
  let query=(params.get('q')||'').trim();
  let page=Math.max(1,parseInt(params.get('page')||'1',10)||1);

  const normalize=s=>(s||'').toLocaleLowerCase().normalize('NFKD');
  const matches=card=>{
    const cat=card.dataset.articleCategory||'';
    const hay=normalize([card.dataset.articleTitle,card.dataset.articleExcerpt,card.dataset.articleKeywords].join(' '));
    return (category==='all'||cat===category)&&(!query||hay.includes(normalize(query)));
  };
  const updateUrl=()=>{
    const next=new URLSearchParams();
    if(category!=='all') next.set('category',category);
    if(query) next.set('q',query);
    if(page>1) next.set('page',String(page));
    history.replaceState(null,'',location.pathname+(next.toString()?`?${next}`:'')+location.hash);
    if(langSwitch){
      const u=new URL(langSwitch.getAttribute('href'),location.href);
      u.search=next.toString();
      langSwitch.setAttribute('href',u.pathname+u.search+u.hash);
    }
  };
  const renderPagination=(totalPages)=>{
    pages.innerHTML='';
    if(totalPages<=1){ pages.hidden=true; return; }
    pages.hidden=false;
    const prev=document.createElement('button');
    prev.type='button';prev.className='orx-page-btn';prev.textContent=root.dataset.prevLabel||'Prev';prev.disabled=page===1;
    prev.addEventListener('click',()=>{if(page>1){page--;render();root.querySelector('[data-orx-article-grid]').scrollIntoView({block:'start'});}});
    pages.append(prev);
    for(let i=1;i<=totalPages;i++){
      const b=document.createElement('button');b.type='button';b.className='orx-page-btn';b.textContent=String(i);
      if(i===page)b.setAttribute('aria-current','page');
      b.setAttribute('aria-label',`${root.dataset.pageLabel||'Page'} ${i}`);
      b.addEventListener('click',()=>{page=i;render();root.querySelector('[data-orx-article-grid]').scrollIntoView({block:'start'});});
      pages.append(b);
    }
    const next=document.createElement('button');
    next.type='button';next.className='orx-page-btn';next.textContent=root.dataset.nextLabel||'Next';next.disabled=page===totalPages;
    next.addEventListener('click',()=>{if(page<totalPages){page++;render();root.querySelector('[data-orx-article-grid]').scrollIntoView({block:'start'});}});
    pages.append(next);
  };
  const render=()=>{
    filters.forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.orxInsightsFilter===category)));
    if(search&&search.value!==query) search.value=query;
    const matched=cards.filter(matches);
    const totalPages=Math.max(1,Math.ceil(matched.length/pageSize));
    if(page>totalPages) page=totalPages;
    cards.forEach(c=>c.hidden=true);
    matched.slice((page-1)*pageSize,page*pageSize).forEach(c=>c.hidden=false);
    if(count) count.textContent=String(matched.length);
    if(empty) empty.hidden=matched.length!==0;
    renderPagination(matched.length?totalPages:0);
    updateUrl();
    root.dataset.pg24Ready='true';
    root.dataset.pg24Visible=String(matched.length);
    root.dataset.pg24Page=String(page);
  };
  filters.forEach(b=>b.addEventListener('click',()=>{category=b.dataset.orxInsightsFilter;page=1;render();}));
  if(search){
    search.value=query;
    let timer;
    search.addEventListener('input',()=>{clearTimeout(timer);timer=setTimeout(()=>{query=search.value.trim();page=1;render();},120);});
    search.addEventListener('search',()=>{query=search.value.trim();page=1;render();});
  }
  render();
})();
