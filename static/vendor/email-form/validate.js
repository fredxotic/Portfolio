/**
* Django Email Form Validation
*/
(function () {
  "use strict";

  let forms = document.querySelectorAll('.php-email-form');

  forms.forEach(function(e) {
    e.addEventListener('submit', function(event) {
      event.preventDefault();

      let thisForm = this;
      let formData = new FormData(thisForm);

      // Show loading
      thisForm.querySelector('.loading').style.display = 'block';
      thisForm.querySelector('.error-message').style.display = 'none';
      thisForm.querySelector('.sent-message').style.display = 'none';

      fetch(thisForm.action, {
        method: 'POST',
        body: formData,
        headers: {'X-Requested-With': 'XMLHttpRequest'}
      })
      .then(response => {
        thisForm.querySelector('.loading').style.display = 'none';
        
        if(response.ok) {
          thisForm.querySelector('.sent-message').style.display = 'block';
          thisForm.reset();
          
          // Hide success message after 5 seconds
          setTimeout(() => {
            thisForm.querySelector('.sent-message').style.display = 'none';
          }, 5000);
        } else {
          throw new Error('Form submission failed');
        }
      })
      .catch((error) => {
        thisForm.querySelector('.loading').style.display = 'none';
        thisForm.querySelector('.error-message').innerHTML = 'An error occurred. Please try again later.';
        thisForm.querySelector('.error-message').style.display = 'block';
      });
    });
  });

})();