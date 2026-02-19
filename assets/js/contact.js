document.addEventListener('DOMContentLoaded', function() {
  initContactForm();
  initMap();
});

function initContactForm() {
  const form = document.querySelector('.contact-form form');

  if (!form) return;

  form.addEventListener('submit', function(e) {
    e.preventDefault();

    const formData = new FormData(form);
    const data = Object.fromEntries(formData);

    if (validateForm(data)) {
      submitForm(data);
    }
  });

  const inputs = form.querySelectorAll('.form-control');
  inputs.forEach(input => {
    input.addEventListener('blur', function() {
      validateField(this);
    });

    input.addEventListener('input', function() {
      if (this.classList.contains('error')) {
        validateField(this);
      }
    });
  });
}

function validateForm(data) {
  let isValid = true;
  const form = document.querySelector('.contact-form form');

  form.querySelectorAll('.form-control').forEach(input => {
    if (!validateField(input)) {
      isValid = false;
    }
  });

  return isValid;
}

function validateField(field) {
  const value = field.value.trim();
  const fieldName = field.name || field.id;
  let isValid = true;
  let errorMessage = '';

  field.classList.remove('error');
  const existingError = field.parentElement.querySelector('.field-error');
  if (existingError) {
    existingError.remove();
  }

  if (field.hasAttribute('required') && !value) {
    isValid = false;
    errorMessage = 'This field is required';
  } else if (field.type === 'email' && value) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(value)) {
      isValid = false;
      errorMessage = 'Please enter a valid email address';
    }
  } else if (field.type === 'tel' && value) {
    const phoneRegex = /^[\d\s\-\+\(\)]+$/;
    if (!phoneRegex.test(value) || value.length < 10) {
      isValid = false;
      errorMessage = 'Please enter a valid phone number';
    }
  }

  if (!isValid) {
    field.classList.add('error');
    const errorDiv = document.createElement('div');
    errorDiv.className = 'field-error';
    errorDiv.textContent = errorMessage;
    field.parentElement.appendChild(errorDiv);
  }

  return isValid;
}

function submitForm(data) {
  const form = document.querySelector('.contact-form form');
  const submitBtn = form.querySelector('button[type="submit"]');
  const successMsg = document.querySelector('.form-success');
  const errorMsg = document.querySelector('.form-error');

  submitBtn.disabled = true;
  submitBtn.textContent = 'Sending...';

  setTimeout(() => {
    successMsg.classList.add('show');
    errorMsg.classList.remove('show');

    form.reset();

    submitBtn.disabled = false;
    submitBtn.textContent = 'Send Message';

    setTimeout(() => {
      successMsg.classList.remove('show');
    }, 5000);
  }, 1000);
}

function initMap() {
  const mapContainer = document.querySelector('.contact-map');

  if (!mapContainer) return;

  const address = '358 East Main St, Ashland, OR 97520';
  const encodedAddress = encodeURIComponent(address);

  const iframe = document.createElement('iframe');
  iframe.src = `https://www.google.com/maps?q=${encodedAddress}&output=embed`;
  iframe.setAttribute('loading', 'lazy');
  iframe.setAttribute('allowfullscreen', '');
  iframe.setAttribute('referrerpolicy', 'no-referrer-when-downgrade');

  mapContainer.appendChild(iframe);
}

const style = document.createElement('style');
style.textContent = `
  .form-control.error {
    border-color: var(--color-error);
    background-color: #fff5f5;
  }

  .field-error {
    color: var(--color-error);
    font-size: 0.875rem;
    margin-top: var(--spacing-xs);
  }

  button[type="submit"]:disabled {
    opacity: 0.6;
    cursor: not-allowed;
  }
`;

document.head.appendChild(style);
