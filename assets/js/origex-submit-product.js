/* ORIGEX — ORX-P01 | PG17 Submit Product demo behavior | Copyright © ORVEAX */
(() => {
  const MAX_BYTES = 10 * 1024 * 1024;
  const allowedExtensions = new Set(['pdf', 'jpg', 'jpeg', 'png', 'doc', 'docx']);

  document.querySelectorAll('[data-orx-submit-product-form]').forEach((form) => {
    const fileInput = form.querySelector('[data-orx-submit-file]');
    const fileName = form.querySelector('[data-orx-submit-file-name]');
    const success = form.querySelector('[data-orx-submit-success]');
    const error = form.querySelector('[data-orx-submit-error]');
    const lang = document.documentElement.lang === 'ar' ? 'ar' : 'en';
    const messages = {
      ar: {
        none: 'لم يتم اختيار ملف.',
        invalid: 'اختر ملف PDF أو JPG أو PNG أو DOC/DOCX بحجم لا يتجاوز 10 MB.',
        success: 'تم التحقق من بيانات النموذج داخل العرض التوضيحي. لم يتم إرسال أو حفظ أي بيانات أو ملفات. اربط النموذج بخدمة معالجة فعلية قبل النشر.'
      },
      en: {
        none: 'No file selected.',
        invalid: 'Choose a PDF, JPG, PNG or DOC/DOCX file no larger than 10 MB.',
        success: 'The demo submission has been validated. No data or files were transmitted or stored. Connect the form to a real processing service before publication.'
      }
    }[lang];

    const clearStatus = () => {
      if (success) success.hidden = true;
      if (error) error.hidden = true;
    };

    const validateFile = () => {
      if (!fileInput || !fileInput.files || !fileInput.files.length) {
        if (fileName) fileName.textContent = messages.none;
        return true;
      }
      const file = fileInput.files[0];
      const ext = (file.name.split('.').pop() || '').toLowerCase();
      const valid = allowedExtensions.has(ext) && file.size <= MAX_BYTES;
      if (fileName) fileName.textContent = valid ? file.name : messages.invalid;
      if (!valid) {
        fileInput.value = '';
        if (error) {
          error.textContent = messages.invalid;
          error.hidden = false;
          error.focus?.();
        }
      }
      return valid;
    };

    fileInput?.addEventListener('change', () => {
      clearStatus();
      validateFile();
    });

    form.addEventListener('input', (event) => {
      if (event.target !== fileInput) clearStatus();
    });

    form.addEventListener('submit', (event) => {
      event.preventDefault();
      clearStatus();
      if (!validateFile()) return;
      if (!form.checkValidity()) {
        form.reportValidity();
        return;
      }
      if (success) {
        success.textContent = messages.success;
        success.hidden = false;
        success.focus?.();
      }
    });
  });
})();
