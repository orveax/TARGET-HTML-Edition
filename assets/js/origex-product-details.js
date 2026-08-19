/* ORIGEX — ORX-P01 | PG11 Product Details runtime | Copyright © ORVEAX */
(() => {
  'use strict';

  const root = document.querySelector('[data-pg11-root]');
  if (!root) return;

  const isArabic = document.documentElement.lang.toLowerCase().startsWith('ar');
  const productsUrl = root.dataset.productsUrl || '../assets/data/products.json';
  const suppliersUrl = root.dataset.suppliersUrl || '../assets/data/suppliers.json';
  const defaultProductId = root.dataset.defaultProductId || 'prod-001';

  const labels = isArabic ? {
    category: 'الفئة', origin: 'بلد المنشأ', pack: 'حجم العبوة', packaging: 'التعبئة', shelfLife: 'مدة الصلاحية', storage: 'التخزين', moq: 'الحد الأدنى للطلب', availability: 'التوفر',
    brand: 'العلامة / المورد', supplierOrigin: 'بلد المورد', supplierProducts: 'منتجات Demo مرتبطة',
    requestQuote: 'إرسال طلب السعر', viewDetails: 'عرض التفاصيل', supplierDetails: 'ملف المورد',
    certificationRef: 'مرجع شهادة Demo', noCerts: 'لا توجد مراجع شهادات Demo مرتبطة بهذا السجل.',
    datasheet: 'ورقة البيانات', brochure: 'البروشور', resourcePlaceholder: 'رابط Demo غير مفعّل — استبدله بملف موثق.', resourceOpen: 'فتح المورد',
    loading: 'جاري تحميل بيانات المنتج التجريبية…',
    loadError: 'تعذر تحميل بيانات المنتج التجريبية.',
    loadHelp: 'راجع مسارات JSON أو شغّل القالب من خادم ويب محلي ثم أعد المحاولة.',
    fallback: 'لم يتم العثور على Product ID المطلوب؛ يتم عرض prod-001 كمنتج Demo افتراضي.',
    relatedEmpty: 'لا توجد منتجات Demo مرتبطة إضافية.',
    onRequest: 'حسب الطلب', available: 'متاح — Demo', limited: 'محدود — Demo', unavailable: 'غير متاح — Demo'
  } : {
    category: 'Category', origin: 'Country of Origin', pack: 'Pack Size', packaging: 'Packaging', shelfLife: 'Shelf Life', storage: 'Storage', moq: 'MOQ', availability: 'Availability',
    brand: 'Brand / Supplier', supplierOrigin: 'Supplier Country', supplierProducts: 'Linked Demo Products',
    requestQuote: 'Request a Quote', viewDetails: 'View Details', supplierDetails: 'Supplier Profile',
    certificationRef: 'Demo Certification Reference', noCerts: 'No demo certification references are attached to this record.',
    datasheet: 'Datasheet', brochure: 'Brochure', resourcePlaceholder: 'Demo link not configured — replace with a verified file.', resourceOpen: 'Open Resource',
    loading: 'Loading illustrative product data…',
    loadError: 'The illustrative product data could not be loaded.',
    loadHelp: 'Verify the JSON paths or run the template from a local web server, then try again.',
    fallback: 'The requested Product ID was not found; prod-001 is shown as the default demo product.',
    relatedEmpty: 'No additional related demo products are available.',
    onRequest: 'On request', available: 'Available — Demo', limited: 'Limited — Demo', unavailable: 'Unavailable — Demo'
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

  const availabilityLabels = {
    'on-request': labels.onRequest,
    available: labels.available,
    limited: labels.limited,
    unavailable: labels.unavailable
  };

  const els = {
    status: root.querySelector('[data-pg11-status]'),
    error: root.querySelector('[data-pg11-error]'),
    image: root.querySelector('[data-pg11-image]'),
    productName: root.querySelector('[data-pg11-product-name]'),
    brandName: root.querySelector('[data-pg11-brand-name]'),
    categoryBadge: root.querySelector('[data-pg11-category-badge]'),
    availabilityBadge: root.querySelector('[data-pg11-availability-badge]'),
    facts: root.querySelector('[data-pg11-facts]'),
    handling: root.querySelector('[data-pg11-handling]'),
    supplierName: root.querySelector('[data-pg11-supplier-name]'),
    supplierSummary: root.querySelector('[data-pg11-supplier-summary]'),
    supplierFacts: root.querySelector('[data-pg11-supplier-facts]'),
    supplierLinks: Array.from(root.querySelectorAll('[data-pg11-supplier-link]')),
    certifications: root.querySelector('[data-pg11-certifications]'),
    resources: root.querySelector('[data-pg11-resources]'),
    related: root.querySelector('[data-pg11-related]'),
    quoteLinks: Array.from(document.querySelectorAll('[data-pg11-rfq-link]')),
    languageLinks: Array.from(document.querySelectorAll('[data-pg11-language-link]')),
    productSchema: document.getElementById('pg11-product-schema')
  };

  const svg = (id) => {
    const el = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
    el.setAttribute('class', 'orx-icon');
    el.setAttribute('aria-hidden', 'true');
    const use = document.createElementNS('http://www.w3.org/2000/svg', 'use');
    use.setAttribute('href', `../assets/icons/sprite.svg#${id}`);
    el.append(use);
    return el;
  };

  const fact = (term, value) => {
    const item = document.createElement('div');
    item.className = 'orx-product-detail-fact';
    const dt = document.createElement('dt'); dt.textContent = term;
    const dd = document.createElement('dd'); dd.textContent = value || '—';
    item.append(dt, dd);
    return item;
  };

  const supplierDisplay = (supplier) => {
    if (!supplier) return isArabic ? 'مورد Demo غير محدد' : 'Unspecified Demo Supplier';
    return (isArabic ? supplier.nameAr : supplier.nameEn) || supplier.name;
  };

  const syncRoutes = (product, supplier) => {
    const encodedProduct = encodeURIComponent(product.id);
    els.quoteLinks.forEach((link) => { link.href = `rfq.html?product=${encodedProduct}`; });
    if (supplier) {
      const href = `supplier-details.html?id=${encodeURIComponent(supplier.id)}`;
      els.supplierLinks.forEach((link) => { link.href = href; });
    }
    els.languageLinks.forEach((link) => {
      const url = new URL(link.href, window.location.href);
      url.searchParams.set('id', product.id);
      link.href = `${url.pathname}${url.search}`;
    });
  };

  const renderFacts = (product, supplier) => {
    els.facts?.replaceChildren(
      fact(labels.brand, supplierDisplay(supplier)),
      fact(labels.category, categoryLabels[product.categoryId] || product.categoryId),
      fact(labels.origin, originLabels[product.originCode] || product.originCode),
      fact(labels.pack, isArabic ? product.packSizeAr : product.packSizeEn),
      fact(labels.moq, product.moq || labels.onRequest),
      fact(labels.availability, availabilityLabels[product.availability] || product.availability)
    );

    els.handling?.replaceChildren(
      fact(labels.packaging, isArabic ? product.packagingAr : product.packagingEn),
      fact(labels.shelfLife, isArabic ? product.shelfLifeAr : product.shelfLifeEn),
      fact(labels.storage, isArabic ? product.storageAr : product.storageEn)
    );
  };

  const renderSupplier = (product, supplier) => {
    if (els.supplierName) els.supplierName.textContent = supplierDisplay(supplier);
    if (els.supplierSummary) els.supplierSummary.textContent = supplier ? ((isArabic ? supplier.summaryAr : supplier.summaryEn) || '') : '';
    if (els.supplierFacts) {
      const linkedCount = supplier?.productIds?.length || 0;
      els.supplierFacts.replaceChildren(
        fact(labels.supplierOrigin, supplier ? (originLabels[supplier.countryCode] || supplier.countryCode) : '—'),
        fact(labels.supplierProducts, String(linkedCount))
      );
    }
  };

  const renderCertifications = (product) => {
    if (!els.certifications) return;
    els.certifications.replaceChildren();
    const refs = Array.isArray(product.certifications) ? product.certifications : [];
    if (!refs.length) {
      const item = document.createElement('li');
      item.className = 'orx-product-detail-cert';
      item.append(svg('info'));
      const text = document.createElement('span'); text.textContent = labels.noCerts;
      item.append(text);
      els.certifications.append(item);
      return;
    }
    refs.forEach((ref) => {
      const item = document.createElement('li');
      item.className = 'orx-product-detail-cert';
      item.append(svg('badge-check'));
      const body = document.createElement('div');
      const strong = document.createElement('strong'); strong.textContent = labels.certificationRef;
      const copy = document.createElement('div'); copy.className = 'orx-muted'; copy.textContent = ref;
      body.append(strong, copy);
      const tag = document.createElement('span'); tag.className = 'orx-badge'; tag.textContent = 'Demo';
      item.append(body, tag);
      els.certifications.append(item);
    });
  };

  const renderResource = (label, href) => {
    const item = document.createElement('li');
    item.className = 'orx-product-detail-resource';
    item.append(svg('file-text'));
    const body = document.createElement('div');
    const strong = document.createElement('strong'); strong.textContent = label;
    const copy = document.createElement('div'); copy.className = 'orx-muted';
    body.append(strong, copy);
    item.append(body);
    if (!href || href === '#') {
      copy.textContent = labels.resourcePlaceholder;
      const button = document.createElement('button');
      button.type = 'button'; button.className = 'orx-btn orx-btn--secondary orx-btn--sm'; button.disabled = true; button.textContent = isArabic ? 'غير مفعّل' : 'Not configured';
      item.append(button);
    } else {
      copy.textContent = isArabic ? 'مورد مرتبط بهذا السجل.' : 'Resource linked to this record.';
      const link = document.createElement('a'); link.className = 'orx-btn orx-btn--secondary orx-btn--sm'; link.href = href; link.textContent = labels.resourceOpen;
      item.append(link);
    }
    return item;
  };

  const renderResources = (product) => {
    els.resources?.replaceChildren(
      renderResource(labels.datasheet, product.datasheet),
      renderResource(labels.brochure, product.brochure)
    );
  };

  const relatedProducts = (product, products) => {
    const sameCategory = products.filter((item) => item.id !== product.id && item.categoryId === product.categoryId);
    const sameSupplier = products.filter((item) => item.id !== product.id && item.supplierId === product.supplierId && !sameCategory.some((entry) => entry.id === item.id));
    return [...sameCategory, ...sameSupplier].slice(0, 3);
  };

  const renderRelated = (product, products, supplierMap) => {
    if (!els.related) return;
    els.related.replaceChildren();
    const related = relatedProducts(product, products);
    if (!related.length) {
      const empty = document.createElement('p'); empty.className = 'orx-muted'; empty.textContent = labels.relatedEmpty;
      els.related.append(empty);
      return;
    }
    related.forEach((item) => {
      const supplier = supplierMap.get(item.supplierId);
      const article = document.createElement('article'); article.className = 'orx-card orx-product-detail-related-card'; article.dataset.relatedProductId = item.id;
      const media = document.createElement('div'); media.className = 'orx-product-detail-related-card__media';
      const image = document.createElement('img'); image.src = `../assets/media/demo/${item.images?.[0] || 'product-tomato-sauce.svg'}`; image.alt = isArabic ? `صورة توضيحية — ${item.nameAr}` : `Illustrative demo — ${item.nameEn}`; image.width = 320; image.height = 240; image.loading = 'lazy'; media.append(image);
      const body = document.createElement('div'); body.className = 'orx-product-detail-related-card__body';
      const badge = document.createElement('span'); badge.className = 'orx-badge'; badge.textContent = categoryLabels[item.categoryId] || item.categoryId;
      const title = document.createElement('h3'); title.className = 'orx-card__title'; title.textContent = isArabic ? item.nameAr : item.nameEn;
      const brand = document.createElement('p'); brand.className = 'orx-muted'; brand.textContent = supplierDisplay(supplier);
      const actions = document.createElement('div'); actions.className = 'orx-product-detail-related__actions';
      const details = document.createElement('a'); details.className = 'orx-btn orx-btn--secondary orx-btn--sm'; details.href = `product-details.html?id=${encodeURIComponent(item.id)}`; details.textContent = labels.viewDetails;
      const quote = document.createElement('a'); quote.className = 'orx-btn orx-btn--primary orx-btn--sm'; quote.href = `rfq.html?product=${encodeURIComponent(item.id)}`; quote.textContent = labels.requestQuote;
      actions.append(details, quote); body.append(badge, title, brand, actions); article.append(media, body); els.related.append(article);
    });
  };

  const updateSchema = (product, supplier) => {
    if (!els.productSchema) return;
    const name = isArabic ? product.nameAr : product.nameEn;
    const schema = {
      '@context': 'https://schema.org',
      '@type': 'Product',
      name,
      sku: product.id,
      image: (product.images || []).map((file) => `https://example.com/assets/media/demo/${file}`),
      category: categoryLabels[product.categoryId] || product.categoryId,
      brand: { '@type': 'Brand', name: supplierDisplay(supplier) },
      description: isArabic ? 'سجل منتج توضيحي داخل قالب ORIGEX لتجارة الأغذية B2B.' : 'An illustrative product record inside the ORIGEX B2B food-trading template.'
    };
    els.productSchema.textContent = JSON.stringify(schema);
  };

  const renderProduct = (product, products, supplierMap, fallbackUsed) => {
    const supplier = supplierMap.get(product.supplierId);
    const productName = isArabic ? product.nameAr : product.nameEn;
    const imageFile = product.images?.[0] || 'product-tomato-sauce.svg';

    if (els.image) {
      els.image.src = `../assets/media/demo/${imageFile}`;
      els.image.alt = isArabic ? `صورة توضيحية للمنتج — ${productName}` : `Illustrative product image — ${productName}`;
    }
    if (els.productName) els.productName.textContent = productName;
    if (els.brandName) els.brandName.textContent = supplierDisplay(supplier);
    if (els.categoryBadge) els.categoryBadge.textContent = categoryLabels[product.categoryId] || product.categoryId;
    if (els.availabilityBadge) els.availabilityBadge.textContent = availabilityLabels[product.availability] || product.availability;

    renderFacts(product, supplier);
    renderSupplier(product, supplier);
    renderCertifications(product);
    renderResources(product);
    renderRelated(product, products, supplierMap);
    syncRoutes(product, supplier);
    updateSchema(product, supplier);

    root.dataset.productId = product.id;
    root.dataset.loadState = 'ready';
    root.setAttribute('aria-busy', 'false');
    if (els.status) {
      els.status.textContent = fallbackUsed ? labels.fallback : '';
      els.status.hidden = !fallbackUsed;
    }
    if (els.error) els.error.hidden = true;
  };

  const renderError = () => {
    root.dataset.loadState = 'error';
    root.setAttribute('aria-busy', 'false');
    if (els.status) els.status.hidden = true;
    if (els.error) {
      els.error.hidden = false;
      els.error.replaceChildren();
      const strong = document.createElement('strong'); strong.textContent = labels.loadError;
      const copy = document.createElement('p'); copy.textContent = labels.loadHelp;
      const link = document.createElement('a'); link.className = 'orx-btn orx-btn--secondary'; link.href = 'products.html'; link.textContent = isArabic ? 'العودة إلى المنتجات' : 'Back to Products';
      els.error.append(strong, copy, link);
    }
  };

  const load = async () => {
    root.setAttribute('aria-busy', 'true');
    if (els.status) { els.status.hidden = false; els.status.textContent = labels.loading; }
    try {
      const [productsResponse, suppliersResponse] = await Promise.all([fetch(productsUrl), fetch(suppliersUrl)]);
      if (!productsResponse.ok || !suppliersResponse.ok) throw new Error('dataset-load');
      const [products, suppliers] = await Promise.all([productsResponse.json(), suppliersResponse.json()]);
      const supplierMap = new Map(suppliers.map((supplier) => [supplier.id, supplier]));
      const params = new URLSearchParams(window.location.search);
      const requestedId = params.get('id') || defaultProductId;
      let product = products.find((item) => item.id === requestedId);
      let fallbackUsed = false;
      if (!product) {
        product = products.find((item) => item.id === defaultProductId);
        fallbackUsed = true;
      }
      if (!product) throw new Error('default-product-missing');
      renderProduct(product, products, supplierMap, fallbackUsed);
    } catch (error) {
      console.error('PG11 product details:', error);
      renderError();
    }
  };

  load();
})();
