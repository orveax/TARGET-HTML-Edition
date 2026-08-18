/* ORIGEX Preview Frame — ORX-P01 / ORVEAX — review only */
(() => {
  const screens = [
    {id:'m360', label:'Mobile Small', w:360, h:800},
    {id:'iphone', label:'iPhone Common', w:390, h:844},
    {id:'m412', label:'Mobile Large', w:412, h:915},
    {id:'tablet', label:'Tablet Portrait', w:768, h:1024},
    {id:'tabletxl', label:'Large Tablet', w:1024, h:1366},
    {id:'laptop', label:'Laptop Common', w:1366, h:768},
    {id:'desktop', label:'Desktop', w:1440, h:900},
    {id:'fhd', label:'Full HD', w:1920, h:1080}
  ];

  const primaryGrid = ['iphone','m412','tablet','tabletxl','laptop','desktop'];
  const qs = new URLSearchParams(location.search);
  let lang = qs.get('lang') === 'en' ? 'en' : 'ar';
  let mode = qs.get('mode') === 'focus' ? 'focus' : 'grid';
  let screenId = screens.some(s => s.id === qs.get('screen')) ? qs.get('screen') : 'desktop';
  const pageAr = qs.get('pageAr') || '../ar/index.html';
  const pageEn = qs.get('pageEn') || '../en/index.html';

  const stage = document.querySelector('[data-pf-stage]');
  const select = document.querySelector('[data-pf-screen]');
  const raw = document.querySelector('[data-pf-raw]');
  const langButtons = [...document.querySelectorAll('[data-pf-lang]')];
  const modeButtons = [...document.querySelectorAll('[data-pf-mode]')];

  screens.forEach(s => {
    const o = document.createElement('option');
    o.value = s.id;
    o.textContent = `${s.label} — ${s.w}×${s.h}`;
    select.append(o);
  });
  select.value = screenId;

  const pageUrl = (language) => language === 'en' ? pageEn : pageAr;

  function card(s, focus=false){
    const article = document.createElement('article');
    article.className = 'pf-device';
    article.innerHTML = `<div class="pf-device__meta"><strong>${s.label}</strong><span>${s.w} × ${s.h}</span></div>`;
    const shell = document.createElement('div');
    shell.className = 'pf-viewport-shell';
    const iframe = document.createElement('iframe');
    iframe.src = pageUrl(lang);
    iframe.title = `${s.label} ${lang === 'ar' ? 'Arabic' : 'English'} preview`;
    iframe.width = s.w;
    iframe.height = s.h;

    if(focus){
      shell.style.width = `${s.w}px`;
      shell.style.height = `${s.h}px`;
    }else{
      const maxW = Math.min(420, s.w);
      const scale = maxW / s.w;
      shell.style.width = `${maxW}px`;
      shell.style.height = `${Math.round(s.h * scale)}px`;
      iframe.style.transform = `scale(${scale})`;
    }
    shell.append(iframe);
    article.append(shell);
    return article;
  }

  function syncControls(){
    document.documentElement.lang = lang === 'ar' ? 'ar' : 'en';
    document.documentElement.dir = lang === 'ar' ? 'rtl' : 'ltr';
    langButtons.forEach(b => b.setAttribute('aria-pressed', String(b.dataset.pfLang === lang)));
    modeButtons.forEach(b => b.setAttribute('aria-pressed', String(b.dataset.pfMode === mode)));
    select.disabled = mode !== 'focus';
    raw.href = pageUrl(lang);
  }

  function render(){
    syncControls();
    stage.innerHTML = '';
    if(mode === 'grid'){
      const grid = document.createElement('div');
      grid.className = 'pf-grid';
      primaryGrid.map(id => screens.find(s => s.id === id)).forEach(s => grid.append(card(s, false)));
      stage.append(grid);
    }else{
      const wrap = document.createElement('div');
      wrap.className = 'pf-focus';
      wrap.append(card(screens.find(s => s.id === screenId), true));
      stage.append(wrap);
    }
    const hint = document.createElement('div');
    hint.className = 'pf-hint';
    hint.textContent = mode === 'grid'
      ? (lang === 'ar' ? 'عرض سريع لأكثر المقاسات شيوعًا. استخدم Focus لاختبار viewport بالحجم الحقيقي.' : 'Quick common-screen matrix. Use Focus for the exact viewport size.')
      : (lang === 'ar' ? 'Focus يعرض الـviewport بالمقاس الحقيقي؛ قد تحتاج للتمرير أفقيًا على شاشة أصغر.' : 'Focus uses the exact viewport size; horizontal scrolling may be required on a smaller monitor.');
    stage.append(hint);
  }

  langButtons.forEach(b => b.addEventListener('click', () => {lang = b.dataset.pfLang; render();}));
  modeButtons.forEach(b => b.addEventListener('click', () => {mode = b.dataset.pfMode; render();}));
  select.addEventListener('change', () => {screenId = select.value; render();});

  render();
})();
