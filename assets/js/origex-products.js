/* ORIGEX — ORX-P01 | PG10 Products Grid runtime | Copyright © ORVEAX */
(() => {
  'use strict';

  const root = document.querySelector('[data-pg10-products]');
  if (!root) return;

  const isArabic = document.documentElement.lang.toLowerCase().startsWith('ar');
  const productsUrl = root.dataset.productsUrl || '../assets/data/products.json';
  const suppliersUrl = root.dataset.suppliersUrl || '../assets/data/suppliers.json';
  const pageSize = Number(root.dataset.pageSize || 6);

  const els = {
    search: root.querySelector('[data-pg10-search]'),
    category: root.querySelector('[data-pg10-category]'),
    brand: root.querySelector('[data-pg10-brand]'),
    origin: root.querySelector('[data-pg10-origin]'),
    reset: root.querySelector('[data-pg10-reset]'),
    grid: root.querySelector('[data-pg10-grid]'),
    count: root.querySelector('[data-pg10-count]'),
    pagination: root.querySelector('[data-pg10-pagination]'),
    summary: root.querySelector('[data-pg10-filter-summary]')
  };

  const labels = isArabic ? {
    brand: 'العلامة', category: 'الفئة', origin: 'المنشأ', pack: 'العبوة',
    details: 'تفاصيل المنتج', quote: 'طلب سعر', onRequest: 'حسب الطلب',
    results: n => `${n} منتج مطابق`, loading: 'جاري تحميل بيانات الديمو…',
    loadError: 'تعذر تحميل بيانات المنتجات التجريبية.', loadHelp: 'استخدم خادمًا محليًا أو راجع مسارات JSON ثم أعد المحاولة.',
    emptyTitle: 'لا توجد منتجات مطابقة', emptyCopy: 'عدّل الفلاتر أو أرسل طلبًا بفئتك المطلوبة.',
    clear: 'مسح', previous: 'السابق', next: 'التالي', page: n => `صفحة ${n}`,
    allBrands: 'كل العلامات', allOrigins: 'كل المناشئ'
  } : {
    brand: 'Brand', category: 'Category', origin: 'Origin', pack: 'Pack',
    details: 'View Product Details', quote: 'Request Quote', onRequest: 'On request',
    results: n => `${n} matching product${n === 1 ? '' : 's'}`, loading: 'Loading demo catalogue…',
    loadError: 'The illustrative product dataset could not be loaded.', loadHelp: 'Use a local web server or verify the JSON paths, then try again.',
    emptyTitle: 'No matching products', emptyCopy: 'Adjust filters or submit an enquiry for the category you need.',
    clear: 'Clear', previous: 'Previous', next: 'Next', page: n => `Page ${n}`,
    allBrands: 'All brands', allOrigins: 'All origins'
  };

  const categoryLabels = isArabic ? {
    ambient: 'أغذية جافة', beverages: 'مشروبات', dairy: 'ألبان', frozen: 'مجمدات', confectionery: 'حلويات', ingredients: 'مكونات'
  } : {
    ambient: 'Ambient Foods', beverages: 'Beverages', dairy: 'Dairy', frozen: 'Frozen', confectionery: 'Confectionery', ingredients: 'Ingredients'
  };

  const originLabels = isArabic ? {
    IT: 'إيطاليا — توضيحي', JO: 'الأردن — توضيحي', EG: 'مصر — توضيحي', TR: 'تركيا — توضيحي', NL: 'هولندا — توضيحي', PL: 'بولندا — توضيحي', BE: 'بلجيكا — توضيحي'
  } : {
    IT: 'Italy — illustrative', JO: 'Jordan — illustrative', EG: 'Egypt — illustrative', TR: 'Türkiye — illustrative', NL: 'Netherlands — illustrative', PL: 'Poland — illustrative', BE: 'Belgium — illustrative'
  };

  let products = [];
  let suppliers = [];
  let supplierByBrand = new Map();
  let state = { search: '', category: 'all', brand: 'all', origin: 'all', page: 1 };

  const svg = (id) => {
    const el = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
    el.setAttribute('class', 'orx-icon');
    el.setAttribute('aria-hidden', 'true');
    const use = document.createElementNS('http://www.w3.org/2000/svg', 'use');
    use.setAttribute('href', `../assets/icons/sprite.svg#${id}`);
    el.append(use);
    return el;
  };

  const button = (text, className) => {
    const el = document.createElement('button');
    el.type = 'button';
    el.className = className;
    el.textContent = text;
    return el;
  };

  const supplierLabel = (brandId) => {
    const supplier = supplierByBrand.get(brandId);
    if (!supplier) return brandId;
    return (isArabic ? supplier.nameAr : supplier.nameEn) || supplier.name;
  };

  const normalized = (value) => String(value || '').toLocaleLowerCase(isArabic ? 'ar' : 'en');

  const filteredProducts = () => {
    const term = normalized(state.search.trim());
    return products.filter((product) => {
      const productName = isArabic ? product.nameAr : product.nameEn;
      const brandName = supplierLabel(product.brandId);
      const originName = originLabels[product.originCode] || product.originCode;
      const haystack = normalized(`${productName} ${brandName} ${originName}`);
      return (!term || haystack.includes(term)) &&
        (state.category === 'all' || product.categoryId === state.category) &&
        (state.brand === 'all' || product.brandId === state.brand) &&
        (state.origin === 'all' || product.originCode === state.origin);
    });
  };

  const syncUrl = () => {
    const params = new URLSearchParams();
    if (state.search) params.set('q', state.search);
    if (state.category !== 'all') params.set('category', state.category);
    if (state.brand !== 'all') params.set('brand', state.brand);
    if (state.origin !== 'all') params.set('origin', state.origin);
    if (state.page > 1) params.set('page', String(state.page));
    const next = `${window.location.pathname}${params.toString() ? `?${params}` : ''}${window.location.hash}`;
    history.replaceState(null, '', next);
  };

  const createFact = (term, value) => {
    const wrap = document.createElement('div');
    wrap.className = 'orx-product-card__fact';
    const dt = document.createElement('dt'); dt.textContent = term;
    const dd = document.createElement('dd'); dd.textContent = value;
    wrap.append(dt, dd);
    return wrap;
  };

  const createProductCard = (product) => {
    const article = document.createElement('article');
    article.className = 'orx-card orx-product-card';
    article.dataset.productId = product.id;
    article.dataset.category = product.categoryId;
    article.dataset.brand = product.brandId;
    article.dataset.origin = product.originCode;

    const media = document.createElement('div'); media.className = 'orx-product-card__media';
    const img = document.createElement('img');
    img.src = `../assets/media/demo/${product.images?.[0] || 'product-tomato-sauce.svg'}`;
    img.alt = isArabic ? `صورة توضيحية — ${product.nameAr}` : `Illustrative demo — ${product.nameEn}`;
    img.width = 420; img.height = 315; img.loading = 'lazy';
    media.append(img);

    const body = document.createElement('div'); body.className = 'orx-product-card__body';
    const badges = document.createElement('div'); badges.className = 'orx-card__meta';
    const categoryBadge = document.createElement('span'); categoryBadge.className = 'orx-badge'; categoryBadge.textContent = categoryLabels[product.categoryId] || product.categoryId;
    const availability = document.createElement('span'); availability.className = 'orx-badge orx-badge--accent'; availability.textContent = labels.onRequest;
    badges.append(categoryBadge, availability);

    const identity = document.createElement('div'); identity.className = 'orx-product-card__identity';
    const names = document.createElement('div');
    const title = document.createElement('h2'); title.className = 'orx-card__title'; title.textContent = isArabic ? product.nameAr : product.nameEn;
    const brand = document.createElement('p'); brand.className = 'orx-product-card__brand'; brand.textContent = supplierLabel(product.brandId);
    names.append(title, brand); identity.append(names);

    const facts = document.createElement('dl'); facts.className = 'orx-product-card__facts';
    facts.append(
      createFact(labels.origin, originLabels[product.originCode] || product.originCode),
      createFact(labels.pack, isArabic ? product.packSizeAr : product.packSizeEn)
    );

    const actions = document.createElement('div'); actions.className = 'orx-product-card__actions';
    const details = document.createElement('a'); details.className = 'orx-btn orx-btn--secondary orx-btn--sm'; details.href = `product-details.html?id=${encodeURIComponent(product.id)}`; details.textContent = labels.details;
    const quote = document.createElement('a'); quote.className = 'orx-btn orx-btn--primary orx-btn--sm'; quote.href = `rfq.html?product=${encodeURIComponent(product.id)}`; quote.textContent = labels.quote;
    actions.append(details, quote);
    body.append(badges, identity, facts, actions);
    article.append(media, body);
    return article;
  };

  const renderEmpty = () => {
    const empty = document.createElement('div'); empty.className = 'orx-empty-state orx-products-empty'; empty.setAttribute('role', 'status');
    const title = document.createElement('h2'); title.textContent = labels.emptyTitle;
    const copy = document.createElement('p'); copy.textContent = labels.emptyCopy;
    const link = document.createElement('a'); link.className = 'orx-btn orx-btn--primary'; link.href = 'rfq.html'; link.textContent = labels.quote;
    empty.append(title, copy, link); return empty;
  };

  const renderError = () => {
    els.grid.replaceChildren();
    const error = document.createElement('div'); error.className = 'orx-products-error'; error.setAttribute('role', 'alert');
    const strong = document.createElement('strong'); strong.textContent = labels.loadError;
    const copy = document.createElement('p'); copy.textContent = labels.loadHelp;
    error.append(strong, copy); els.grid.append(error);
    if (els.count) els.count.textContent = labels.results(0);
    if (els.pagination) els.pagination.replaceChildren();
  };

  const renderPagination = (total) => {
    if (!els.pagination) return;
    els.pagination.replaceChildren();
    const pages = Math.max(1, Math.ceil(total / pageSize));
    if (pages <= 1 || total === 0) return;
    state.page = Math.min(state.page, pages);
    const list = document.createElement('div'); list.className = 'orx-pagination'; list.setAttribute('aria-label', isArabic ? 'صفحات المنتجات' : 'Product pages');

    const prev = button(labels.previous, ''); prev.disabled = state.page === 1; prev.setAttribute('aria-label', labels.previous);
    prev.addEventListener('click', () => { state.page -= 1; render(); root.scrollIntoView({ behavior: 'auto', block: 'start' }); });
    list.append(prev);

    for (let page = 1; page <= pages; page += 1) {
      const pageButton = button(String(page), '');
      pageButton.setAttribute('aria-label', labels.page(page));
      if (page === state.page) pageButton.setAttribute('aria-current', 'page');
      pageButton.addEventListener('click', () => { state.page = page; render(); root.scrollIntoView({ behavior: 'auto', block: 'start' }); });
      list.append(pageButton);
    }

    const next = button(labels.next, ''); next.disabled = state.page === pages; next.setAttribute('aria-label', labels.next);
    next.addEventListener('click', () => { state.page += 1; render(); root.scrollIntoView({ behavior: 'auto', block: 'start' }); });
    list.append(next); els.pagination.append(list);
  };

  const renderSummary = () => {
    if (!els.summary) return;
    els.summary.replaceChildren();
    const entries = [];
    if (state.category !== 'all') entries.push(['category', categoryLabels[state.category] || state.category]);
    if (state.brand !== 'all') entries.push(['brand', supplierLabel(state.brand)]);
    if (state.origin !== 'all') entries.push(['origin', originLabels[state.origin] || state.origin]);
    if (state.search) entries.push(['search', `“${state.search}”`]);
    entries.forEach(([key, value]) => {
      const badge = document.createElement('span'); badge.className = 'orx-badge'; badge.textContent = value;
      const remove = button('×', ''); remove.setAttribute('aria-label', `${labels.clear} ${value}`);
      remove.addEventListener('click', () => {
        if (key === 'search') { state.search = ''; if (els.search) els.search.value = ''; }
        else { state[key] = 'all'; const control = els[key]; if (control) control.value = 'all'; }
        state.page = 1; render();
      });
      badge.append(remove); els.summary.append(badge);
    });
  };

  const render = () => {
    const matching = filteredProducts();
    const pages = Math.max(1, Math.ceil(matching.length / pageSize));
    state.page = Math.min(Math.max(state.page, 1), pages);
    const start = (state.page - 1) * pageSize;
    const visible = matching.slice(start, start + pageSize);
    els.grid.replaceChildren();
    if (visible.length) visible.forEach((product) => els.grid.append(createProductCard(product)));
    else els.grid.append(renderEmpty());
    if (els.count) els.count.textContent = labels.results(matching.length);
    renderPagination(matching.length); renderSummary(); syncUrl();
  };

  const populateSelect = (select, items, allLabel) => {
    if (!select) return;
    select.replaceChildren();
    const all = document.createElement('option'); all.value = 'all'; all.textContent = allLabel; select.append(all);
    items.forEach(([value, label]) => { const option = document.createElement('option'); option.value = value; option.textContent = label; select.append(option); });
  };

  const hydrateControls = () => {
    const brandIds = [...new Set(products.map(p => p.brandId))];
    populateSelect(els.brand, brandIds.map(id => [id, supplierLabel(id)]), labels.allBrands);
    const originIds = [...new Set(products.map(p => p.originCode))].sort();
    populateSelect(els.origin, originIds.map(id => [id, originLabels[id] || id]), labels.allOrigins);

    const params = new URLSearchParams(window.location.search);
    const category = params.get('category');
    const brand = params.get('brand');
    const origin = params.get('origin');
    const q = params.get('q') || '';
    const page = Number(params.get('page') || 1);
    if (categoryLabels[category]) state.category = category;
    if (brandIds.includes(brand)) state.brand = brand;
    if (originIds.includes(origin)) state.origin = origin;
    state.search = q; state.page = Number.isFinite(page) && page > 0 ? page : 1;
    if (els.category) els.category.value = state.category;
    if (els.brand) els.brand.value = state.brand;
    if (els.origin) els.origin.value = state.origin;
    if (els.search) els.search.value = state.search;
  };

  const bind = () => {
    let searchTimer = null;
    els.search?.addEventListener('input', () => {
      clearTimeout(searchTimer);
      searchTimer = setTimeout(() => { state.search = els.search.value.trim(); state.page = 1; render(); }, 120);
    });
    ['category', 'brand', 'origin'].forEach((key) => {
      els[key]?.addEventListener('change', () => { state[key] = els[key].value; state.page = 1; render(); });
    });
    els.reset?.addEventListener('click', () => {
      state = { search: '', category: 'all', brand: 'all', origin: 'all', page: 1 };
      if (els.search) els.search.value = '';
      if (els.category) els.category.value = 'all';
      if (els.brand) els.brand.value = 'all';
      if (els.origin) els.origin.value = 'all';
      render();
    });
  };

  const init = async () => {
    if (els.grid) { const loading = document.createElement('div'); loading.className = 'orx-products-loading'; loading.setAttribute('role', 'status'); loading.textContent = labels.loading; els.grid.replaceChildren(loading); }
    try {
      const [productsResponse, suppliersResponse] = await Promise.all([fetch(productsUrl), fetch(suppliersUrl)]);
      if (!productsResponse.ok || !suppliersResponse.ok) throw new Error('Dataset request failed');
      [products, suppliers] = await Promise.all([productsResponse.json(), suppliersResponse.json()]);
      supplierByBrand = new Map(suppliers.map(supplier => [`brand-${supplier.id.replace(/^supplier-/, '')}`, supplier]));
      hydrateControls(); bind(); render();
    } catch (error) {
      console.error('ORIGEX PG10 data load error', error);
      renderError();
    }
  };

  init();
})();
