/* ORIGEX — ORX-P01 | PG12 Suppliers Directory runtime | Copyright © ORVEAX */
(() => {
  'use strict';

  const root = document.querySelector('[data-pg12-root]');
  if (!root) return;

  const isArabic = document.documentElement.lang.toLowerCase().startsWith('ar');
  const suppliersUrl = root.dataset.suppliersUrl || '../assets/data/suppliers.json';
  const productsUrl = root.dataset.productsUrl || '../assets/data/products.json';

  const labels = isArabic ? {
    origin: 'المنشأ', products: 'المنتجات المرتبطة', categories: 'الفئات', certRefs: 'مراجع شهادات Demo',
    details: 'تفاصيل المورد', viewProducts: 'عرض المنتجات', featuredMeta: (p, c) => `${p} منتجات · ${c} فئات`,
    results: n => `${n} ملف مورد مطابق`, allOrigins: 'كل المناشئ',
    emptyTitle: 'لا توجد ملفات موردين مطابقة', emptyCopy: 'عدّل الفلاتر أو قدّم منتجك للمراجعة.',
    reset: 'إعادة ضبط الفلاتر', clear: 'مسح', loadError: 'تعذر تحميل بيانات الموردين التجريبية.',
    loadHelp: 'راجع مسارات JSON أو شغّل القالب من خلال خادم محلي ثم أعد المحاولة.'
  } : {
    origin: 'Origin', products: 'Linked products', categories: 'Categories', certRefs: 'Demo certification refs',
    details: 'View Supplier Details', viewProducts: 'View Products', featuredMeta: (p, c) => `${p} products · ${c} categories`,
    results: n => `${n} matching supplier profile${n === 1 ? '' : 's'}`, allOrigins: 'All origins',
    emptyTitle: 'No matching supplier profiles', emptyCopy: 'Adjust the filters or submit your product for review.',
    reset: 'Reset Filters', clear: 'Clear', loadError: 'The illustrative supplier dataset could not be loaded.',
    loadHelp: 'Check the JSON paths or run the template through a local web server, then try again.'
  };

  const categoryLabels = isArabic ? {
    ambient: 'أغذية جافة', beverages: 'مشروبات', dairy: 'ألبان', frozen: 'مجمدات', confectionery: 'حلويات', ingredients: 'مكونات'
  } : {
    ambient: 'Ambient Foods', beverages: 'Beverages', dairy: 'Dairy', frozen: 'Frozen', confectionery: 'Confectionery', ingredients: 'Ingredients'
  };

  const originLabels = isArabic ? {
    IT: 'إيطاليا — توضيحي', JO: 'الأردن — توضيحي', NL: 'هولندا — توضيحي', PL: 'بولندا — توضيحي', EG: 'مصر — توضيحي', TR: 'تركيا — توضيحي', BE: 'بلجيكا — توضيحي'
  } : {
    IT: 'Italy — illustrative', JO: 'Jordan — illustrative', NL: 'Netherlands — illustrative', PL: 'Poland — illustrative', EG: 'Egypt — illustrative', TR: 'Türkiye — illustrative', BE: 'Belgium — illustrative'
  };

  const els = {
    search: root.querySelector('[data-pg12-search]'),
    category: root.querySelector('[data-pg12-category]'),
    origin: root.querySelector('[data-pg12-origin]'),
    reset: root.querySelector('[data-pg12-reset]'),
    count: root.querySelector('[data-pg12-count]'),
    summary: root.querySelector('[data-pg12-filter-summary]'),
    featured: root.querySelector('[data-pg12-featured]'),
    grid: root.querySelector('[data-pg12-grid]')
  };

  let suppliers = [];
  let products = [];
  let productById = new Map();
  let state = { search: '', category: 'all', origin: 'all' };

  const normalized = value => String(value || '').toLocaleLowerCase(isArabic ? 'ar' : 'en');

  const initials = supplier => {
    const raw = (isArabic ? supplier.nameAr : supplier.nameEn) || supplier.name || 'OR';
    const clean = raw.replace(/—\s*Demo/gi, '').replace(/Demo/gi, '').trim();
    const parts = clean.split(/\s+/).filter(Boolean);
    return parts.slice(0, 2).map(part => part[0]).join('').toUpperCase() || 'OR';
  };

  const supplierName = supplier => (isArabic ? supplier.nameAr : supplier.nameEn) || supplier.name;
  const supplierSummary = supplier => (isArabic ? supplier.summaryAr : supplier.summaryEn) || '';

  const brandIdForSupplier = supplier => {
    const brands = [...new Set((supplier.productIds || []).map(id => productById.get(id)?.brandId).filter(Boolean))];
    return brands.length === 1 ? brands[0] : null;
  };

  const createIdentity = (supplier, className) => {
    const identity = document.createElement('div');
    identity.className = className;
    identity.setAttribute('aria-hidden', 'true');
    identity.textContent = initials(supplier);
    return identity;
  };

  const createFeatured = supplier => {
    const article = document.createElement('article');
    article.className = 'orx-suppliers-featured__item';
    article.dataset.featuredSupplierId = supplier.id;
    const copy = document.createElement('div'); copy.className = 'orx-suppliers-featured__copy';
    const title = document.createElement('h3'); title.textContent = supplierName(supplier);
    const meta = document.createElement('p'); meta.textContent = labels.featuredMeta((supplier.productIds || []).length, (supplier.categoryIds || []).length);
    copy.append(title, meta); article.append(createIdentity(supplier, 'orx-suppliers-featured__identity'), copy);
    return article;
  };

  const fact = (term, value) => {
    const wrap = document.createElement('div'); wrap.className = 'orx-supplier-directory-card__fact';
    const dt = document.createElement('dt'); dt.textContent = term;
    const dd = document.createElement('dd'); dd.textContent = value;
    wrap.append(dt, dd); return wrap;
  };

  const createSupplierCard = supplier => {
    const article = document.createElement('article');
    article.className = 'orx-card orx-supplier-directory-card';
    article.dataset.supplierId = supplier.id;
    article.dataset.origin = supplier.countryCode;
    article.dataset.categories = (supplier.categoryIds || []).join(',');

    const head = document.createElement('div'); head.className = 'orx-supplier-directory-card__head';
    const text = document.createElement('div');
    const title = document.createElement('h2'); title.className = 'orx-card__title'; title.textContent = supplierName(supplier);
    const summary = document.createElement('p'); summary.className = 'orx-supplier-directory-card__summary'; summary.textContent = supplierSummary(supplier);
    text.append(title, summary); head.append(createIdentity(supplier, 'orx-supplier-directory-card__identity'), text);

    const meta = document.createElement('dl'); meta.className = 'orx-supplier-directory-card__meta';
    meta.append(
      fact(labels.origin, originLabels[supplier.countryCode] || supplier.countryCode),
      fact(labels.products, String((supplier.productIds || []).length)),
      fact(labels.categories, String((supplier.categoryIds || []).length)),
      fact(labels.certRefs, String((supplier.certifications || []).length))
    );

    const tags = document.createElement('div'); tags.className = 'orx-supplier-directory-card__tags';
    (supplier.categoryIds || []).forEach(id => {
      const badge = document.createElement('span'); badge.className = 'orx-badge'; badge.textContent = categoryLabels[id] || id; tags.append(badge);
    });

    const actions = document.createElement('div'); actions.className = 'orx-supplier-directory-card__actions';
    const details = document.createElement('a'); details.className = 'orx-btn orx-btn--secondary orx-btn--sm'; details.href = `supplier-details.html?id=${encodeURIComponent(supplier.id)}`; details.textContent = labels.details;
    actions.append(details);
    const brandId = brandIdForSupplier(supplier);
    if (brandId) {
      const productsLink = document.createElement('a'); productsLink.className = 'orx-btn orx-btn--primary orx-btn--sm'; productsLink.href = `products.html?brand=${encodeURIComponent(brandId)}`; productsLink.textContent = labels.viewProducts; actions.append(productsLink);
    }

    article.append(head, meta, tags, actions);
    return article;
  };

  const filtered = () => {
    const term = normalized(state.search.trim());
    return suppliers.filter(supplier => {
      const haystack = normalized(`${supplierName(supplier)} ${supplierSummary(supplier)} ${originLabels[supplier.countryCode] || supplier.countryCode}`);
      return (!term || haystack.includes(term)) &&
        (state.category === 'all' || (supplier.categoryIds || []).includes(state.category)) &&
        (state.origin === 'all' || supplier.countryCode === state.origin);
    });
  };

  const syncUrl = () => {
    const params = new URLSearchParams();
    if (state.search) params.set('q', state.search);
    if (state.category !== 'all') params.set('category', state.category);
    if (state.origin !== 'all') params.set('origin', state.origin);
    history.replaceState(null, '', `${window.location.pathname}${params.toString() ? `?${params}` : ''}${window.location.hash}`);
  };

  const renderSummary = () => {
    if (!els.summary) return;
    els.summary.replaceChildren();
    const entries = [];
    if (state.search) entries.push(['search', `“${state.search}”`]);
    if (state.category !== 'all') entries.push(['category', categoryLabels[state.category] || state.category]);
    if (state.origin !== 'all') entries.push(['origin', originLabels[state.origin] || state.origin]);
    entries.forEach(([key, value]) => {
      const badge = document.createElement('span'); badge.className = 'orx-badge'; badge.append(document.createTextNode(value));
      const remove = document.createElement('button'); remove.type = 'button'; remove.textContent = '×'; remove.setAttribute('aria-label', `${labels.clear} ${value}`);
      remove.addEventListener('click', () => {
        if (key === 'search') { state.search = ''; if (els.search) els.search.value = ''; }
        else { state[key] = 'all'; if (els[key]) els[key].value = 'all'; }
        render();
      });
      badge.append(remove); els.summary.append(badge);
    });
  };

  const renderEmpty = () => {
    const empty = document.createElement('div'); empty.className = 'orx-empty-state orx-suppliers-empty'; empty.setAttribute('role', 'status');
    const title = document.createElement('h2'); title.textContent = labels.emptyTitle;
    const copy = document.createElement('p'); copy.textContent = labels.emptyCopy;
    const link = document.createElement('a'); link.className = 'orx-btn orx-btn--primary'; link.href = 'submit-product.html'; link.textContent = isArabic ? 'قدّم منتجك' : 'Submit Your Product';
    empty.append(title, copy, link); return empty;
  };

  const render = () => {
    const matching = filtered();
    els.grid.replaceChildren();
    if (matching.length) matching.forEach(supplier => els.grid.append(createSupplierCard(supplier)));
    else els.grid.append(renderEmpty());
    if (els.count) els.count.textContent = labels.results(matching.length);
    renderSummary(); syncUrl();
  };

  const populateOrigin = () => {
    const origins = [...new Set(suppliers.map(s => s.countryCode).filter(Boolean))].sort();
    if (!els.origin) return origins;
    els.origin.replaceChildren();
    const all = document.createElement('option'); all.value = 'all'; all.textContent = labels.allOrigins; els.origin.append(all);
    origins.forEach(code => { const option = document.createElement('option'); option.value = code; option.textContent = originLabels[code] || code; els.origin.append(option); });
    return origins;
  };

  const hydrate = origins => {
    const params = new URLSearchParams(window.location.search);
    const q = params.get('q') || '';
    const category = params.get('category');
    const origin = params.get('origin');
    state.search = q;
    if (category && categoryLabels[category]) state.category = category;
    if (origin && origins.includes(origin)) state.origin = origin;
    if (els.search) els.search.value = state.search;
    if (els.category) els.category.value = state.category;
    if (els.origin) els.origin.value = state.origin;
  };

  const bind = () => {
    els.search?.addEventListener('input', () => { state.search = els.search.value; render(); });
    els.category?.addEventListener('change', () => { state.category = els.category.value; render(); });
    els.origin?.addEventListener('change', () => { state.origin = els.origin.value; render(); });
    els.reset?.addEventListener('click', () => {
      state = { search: '', category: 'all', origin: 'all' };
      if (els.search) els.search.value = '';
      if (els.category) els.category.value = 'all';
      if (els.origin) els.origin.value = 'all';
      render(); els.search?.focus();
    });
  };

  const renderError = () => {
    els.grid?.replaceChildren();
    const error = document.createElement('div'); error.className = 'orx-suppliers-error'; error.setAttribute('role', 'alert');
    const strong = document.createElement('strong'); strong.textContent = labels.loadError;
    const copy = document.createElement('p'); copy.textContent = labels.loadHelp;
    error.append(strong, copy); els.grid?.append(error);
    if (els.count) els.count.textContent = labels.results(0);
    root.dataset.loadState = 'error';
  };

  Promise.all([
    fetch(suppliersUrl).then(r => { if (!r.ok) throw new Error('suppliers'); return r.json(); }),
    fetch(productsUrl).then(r => { if (!r.ok) throw new Error('products'); return r.json(); })
  ]).then(([supplierData, productData]) => {
    suppliers = Array.isArray(supplierData) ? supplierData : [];
    products = Array.isArray(productData) ? productData : [];
    productById = new Map(products.map(product => [product.id, product]));
    els.featured?.replaceChildren(...suppliers.filter(s => s.featured === true).map(createFeatured));
    const origins = populateOrigin();
    hydrate(origins); bind(); render();
    root.dataset.loadState = 'ready';
    root.dataset.supplierCount = String(suppliers.length);
    root.dataset.featuredCount = String(suppliers.filter(s => s.featured === true).length);
  }).catch(renderError);
})();
