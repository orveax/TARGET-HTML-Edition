(() => {
  'use strict';

  const root = document.querySelector('[data-pg29-root]');
  if (!root) return;

  const lang = document.documentElement.lang === 'ar' ? 'ar' : 'en';
  let timerId = null;

  const copy = {
    ar: {
      dateEmpty: 'لم يتم تحديد موعد إطلاق بعد. أضف تاريخًا مستقبليًا موثوقًا في config.js إذا أردت إظهار العد التنازلي.',
      dateLabel: 'موعد الإطلاق المضبوط',
      days: 'يوم', hours: 'ساعة', minutes: 'دقيقة', seconds: 'ثانية',
      complete: 'انتهى الموعد المضبوط. راجع الإعداد قبل النشر.',
      formError: 'أدخل بريدًا إلكترونيًا صالحًا لمراجعة حالة النموذج.',
      formSuccess: 'نجح التحقق التجريبي. لم يتم تسجيل اشتراك أو إرسال أي بيانات؛ اربط النموذج بخدمة حقيقية قبل النشر.'
    },
    en: {
      dateEmpty: 'No launch date is configured. Add a verified future date in config.js only if you want to display the countdown.',
      dateLabel: 'Configured launch date',
      days: 'Days', hours: 'Hours', minutes: 'Minutes', seconds: 'Seconds',
      complete: 'The configured date has passed. Review the setting before publishing.',
      formError: 'Enter a valid email address to review the Demo form state.',
      formSuccess: 'Demo validation passed. No subscription was created and no data was transmitted; connect a real service before production.'
    }
  }[lang];

  const config = () => window.ORIGEX_CONFIG || {};
  const dateEmpty = root.querySelector('[data-pg29-date-empty]');
  const countdown = root.querySelector('[data-pg29-countdown]');
  const dateValue = root.querySelector('[data-pg29-date-value]');
  const countdownStatus = root.querySelector('[data-pg29-countdown-status]');
  const units = {
    days: root.querySelector('[data-pg29-days]'),
    hours: root.querySelector('[data-pg29-hours]'),
    minutes: root.querySelector('[data-pg29-minutes]'),
    seconds: root.querySelector('[data-pg29-seconds]')
  };

  const clearTimer = () => {
    if (timerId) window.clearInterval(timerId);
    timerId = null;
  };

  const parseLaunchDate = () => {
    const raw = config().comingSoon?.launchDate;
    if (typeof raw !== 'string' || !raw.trim()) return null;
    const value = new Date(raw.trim());
    return Number.isNaN(value.getTime()) ? null : value;
  };

  const formatDate = (date) => {
    try {
      return new Intl.DateTimeFormat(lang === 'ar' ? 'ar-EG' : 'en-GB', {
        dateStyle: 'medium',
        timeStyle: 'short'
      }).format(date);
    } catch (_) {
      return date.toISOString();
    }
  };

  const setNeutralLaunchState = (message = copy.dateEmpty) => {
    clearTimer();
    if (countdown) countdown.hidden = true;
    if (dateEmpty) {
      dateEmpty.hidden = false;
      dateEmpty.textContent = message;
    }
    if (dateValue) dateValue.textContent = '';
    if (countdownStatus) countdownStatus.textContent = message;
    root.dataset.pg29LaunchState = 'not-configured';
  };

  const paintCountdown = (launchDate) => {
    const remaining = launchDate.getTime() - Date.now();
    if (remaining <= 0) {
      setNeutralLaunchState(copy.complete);
      root.dataset.pg29LaunchState = 'past';
      return false;
    }

    const totalSeconds = Math.floor(remaining / 1000);
    const days = Math.floor(totalSeconds / 86400);
    const hours = Math.floor((totalSeconds % 86400) / 3600);
    const minutes = Math.floor((totalSeconds % 3600) / 60);
    const seconds = totalSeconds % 60;

    if (units.days) units.days.textContent = String(days).padStart(2, '0');
    if (units.hours) units.hours.textContent = String(hours).padStart(2, '0');
    if (units.minutes) units.minutes.textContent = String(minutes).padStart(2, '0');
    if (units.seconds) units.seconds.textContent = String(seconds).padStart(2, '0');
    if (countdownStatus) countdownStatus.textContent = `${days} ${copy.days}, ${hours} ${copy.hours}, ${minutes} ${copy.minutes}, ${seconds} ${copy.seconds}`;
    return true;
  };

  const renderLaunchState = () => {
    clearTimer();
    const launchDate = parseLaunchDate();
    if (!launchDate) {
      setNeutralLaunchState();
      return;
    }
    if (launchDate.getTime() <= Date.now()) {
      setNeutralLaunchState(copy.complete);
      root.dataset.pg29LaunchState = 'past';
      return;
    }

    if (dateEmpty) dateEmpty.hidden = true;
    if (countdown) countdown.hidden = false;
    if (dateValue) dateValue.textContent = `${copy.dateLabel}: ${formatDate(launchDate)}`;
    root.dataset.pg29LaunchState = 'future';
    paintCountdown(launchDate);
    timerId = window.setInterval(() => paintCountdown(launchDate), 1000);
  };

  const isPublicUrl = (value) => {
    if (typeof value !== 'string' || !value.trim() || value.trim() === '#') return false;
    try {
      const url = new URL(value, window.location.href);
      return url.protocol === 'https:' || url.protocol === 'http:';
    } catch (_) {
      return false;
    }
  };

  const renderSocial = () => {
    const socialWrap = root.querySelector('[data-pg29-social]');
    const links = [...root.querySelectorAll('[data-pg29-social-link]')];
    const social = config().social || {};
    const globallyEnabled = social.enabled !== false && config().features?.showSocialLinks !== false;
    let visibleCount = 0;

    links.forEach((link) => {
      const key = link.dataset.pg29SocialLink;
      const url = globallyEnabled ? social[key] : '';
      const visible = isPublicUrl(url);
      link.hidden = !visible;
      if (visible) {
        link.href = url;
        link.rel = 'noopener noreferrer';
        link.target = '_blank';
        visibleCount += 1;
      } else {
        link.removeAttribute('href');
        link.removeAttribute('target');
        link.removeAttribute('rel');
      }
    });

    if (socialWrap) socialWrap.hidden = visibleCount === 0;
    root.dataset.pg29SocialCount = String(visibleCount);
  };

  const renderContact = () => {
    const email = config().site?.email;
    root.querySelectorAll('[data-pg29-email]').forEach((link) => {
      if (typeof email === 'string' && email.includes('@')) {
        link.textContent = email;
        link.href = `mailto:${email}`;
      }
    });
  };

  const setupSubscribe = () => {
    const form = root.querySelector('[data-pg29-form]');
    if (!form) return;
    const email = form.querySelector('input[type="email"]');
    const error = form.querySelector('[data-pg29-form-error]');
    const success = form.querySelector('[data-pg29-form-success]');

    const hideStates = () => {
      if (error) error.hidden = true;
      if (success) success.hidden = true;
    };

    form.addEventListener('submit', (event) => {
      event.preventDefault();
      hideStates();
      if (!email || !email.checkValidity()) {
        if (error) {
          error.textContent = copy.formError;
          error.hidden = false;
          error.focus();
        }
        if (email) email.setAttribute('aria-invalid', 'true');
        root.dataset.pg29FormState = 'error';
        return;
      }

      email.removeAttribute('aria-invalid');
      if (success) {
        success.textContent = copy.formSuccess;
        success.hidden = false;
        success.focus();
      }
      root.dataset.pg29FormState = 'validated';
    });

    form.addEventListener('reset', () => {
      window.setTimeout(() => {
        hideStates();
        if (email) email.removeAttribute('aria-invalid');
        root.dataset.pg29FormState = 'idle';
      }, 0);
    });
  };

  renderLaunchState();
  renderSocial();
  renderContact();
  setupSubscribe();

  root.dataset.pg29Ready = 'true';
  root.dataset.pg29FormState = 'idle';

  window.ORIGEXComingSoon = {
    refresh() {
      renderLaunchState();
      renderSocial();
      renderContact();
    }
  };
})();
