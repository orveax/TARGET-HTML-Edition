/* ORIGEX — ORX-P01 | PG20 Case Studies runtime | Copyright © ORVEAX */
(() => {
  'use strict';
  const root=document.querySelector('[data-pg20-root]'); if(!root) return;
  const buttons=[...root.querySelectorAll('[data-orx-case-filter]')];
  const cards=[...root.querySelectorAll('[data-orx-case-card]')];
  const count=root.querySelector('[data-orx-case-count]');
  const empty=root.querySelector('[data-orx-case-empty]');
  const languageLinks=[...document.querySelectorAll('.orx-lang-switch,.orx-mobile-nav a[lang][href*="case-studies.html"]')];
  const valid=new Set(buttons.map(button=>button.dataset.orxCaseFilter));
  const fallback='all';

  const syncLanguage=(focus)=>languageLinks.forEach(link=>{
    const url=new URL(link.href,window.location.href);
    if(focus&&focus!==fallback) url.searchParams.set('focus',focus); else url.searchParams.delete('focus');
    link.href=`${url.pathname}${url.search}`;
  });

  const apply=(focus,{updateUrl=true}={})=>{
    const next=valid.has(focus)?focus:fallback;
    let visible=0;
    buttons.forEach(button=>button.setAttribute('aria-pressed',String(button.dataset.orxCaseFilter===next)));
    cards.forEach(card=>{
      const show=next===fallback||card.dataset.caseFocus===next;
      card.hidden=!show;
      if(show) visible+=1;
    });
    if(count) count.textContent=String(visible);
    if(empty) empty.hidden=visible!==0;
    root.dataset.pg20Filter=next;
    root.dataset.pg20Visible=String(visible);
    syncLanguage(next);
    if(updateUrl){
      const url=new URL(window.location.href);
      if(next===fallback) url.searchParams.delete('focus'); else url.searchParams.set('focus',next);
      history.replaceState({},'',`${url.pathname}${url.search}${url.hash}`);
    }
  };

  buttons.forEach(button=>button.addEventListener('click',()=>apply(button.dataset.orxCaseFilter)));
  const requested=new URLSearchParams(location.search).get('focus');
  apply(requested&&valid.has(requested)?requested:fallback,{updateUrl:false});
  root.dataset.pg20Ready='true';
})();
