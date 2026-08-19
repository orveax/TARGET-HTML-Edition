/* ORIGEX — ORX-P01 | PG04 demo form behavior | Copyright © ORVEAX */
(() => {
  const forms = document.querySelectorAll('[data-orx-demo-enquiry-form]');
  forms.forEach((form) => {
    const status = form.querySelector('[data-orx-demo-form-status]');
    form.addEventListener('submit', (event) => {
      event.preventDefault();
      if (!form.checkValidity()) {
        form.reportValidity();
        return;
      }
      if (status) {
        status.hidden = false;
        status.focus?.();
      }
    });
  });
})();
