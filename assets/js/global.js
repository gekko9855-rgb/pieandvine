document.addEventListener('DOMContentLoaded', function() {
  initMobileMenu();
  initScrollEffects();
  initLoadingScreen();
  initSmoothScroll();
  initFadeInElements();
});

function initMobileMenu() {
  const navToggle = document.querySelector('.nav-toggle-btn');
  const navPanel = document.querySelector('.site-header-mobi-panel');
  const body = document.body;

  if (navToggle && navPanel) {
    navToggle.addEventListener('click', function() {
      const isExpanded = this.getAttribute('aria-expanded') === 'true';
      this.setAttribute('aria-expanded', !isExpanded);
      navPanel.classList.toggle('is-open');
      body.classList.toggle('menu-open');
    });

    const navLinks = navPanel.querySelectorAll('.site-nav-link');
    navLinks.forEach(link => {
      link.addEventListener('click', function() {
        navPanel.classList.remove('is-open');
        body.classList.remove('menu-open');
        navToggle.setAttribute('aria-expanded', 'false');
      });
    });
  }
}

function initScrollEffects() {
  const header = document.querySelector('.site-header');
  let lastScroll = 0;

  window.addEventListener('scroll', function() {
    const currentScroll = window.pageYOffset;

    if (header) {
      if (currentScroll > 100) {
        header.classList.add('scrolled');
      } else {
        header.classList.remove('scrolled');
      }
    }

    lastScroll = currentScroll;
  });
}

function initLoadingScreen() {
  const loader = document.querySelector('.loading');

  window.addEventListener('load', function() {
    if (loader) {
      setTimeout(() => {
        loader.classList.add('hidden');
        setTimeout(() => {
          loader.style.display = 'none';
        }, 500);
      }, 300);
    }
  });
}

function initSmoothScroll() {
  const smoothScrollLinks = document.querySelectorAll('a[href^="#"]');

  smoothScrollLinks.forEach(link => {
    link.addEventListener('click', function(e) {
      const href = this.getAttribute('href');

      if (href === '#' || href === '#main-content') {
        return;
      }

      const targetId = href.substring(1);
      const targetElement = document.getElementById(targetId);

      if (targetElement) {
        e.preventDefault();
        targetElement.scrollIntoView({
          behavior: 'smooth',
          block: 'start'
        });
      }
    });
  });
}

function initFadeInElements() {
  const fadeElements = document.querySelectorAll('.fade-in');

  const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
  };

  const observer = new IntersectionObserver(function(entries) {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        observer.unobserve(entry.target);
      }
    });
  }, observerOptions);

  fadeElements.forEach(element => {
    observer.observe(element);
  });
}

function debounce(func, wait) {
  let timeout;
  return function executedFunction(...args) {
    const later = () => {
      clearTimeout(timeout);
      func(...args);
    };
    clearTimeout(timeout);
    timeout = setTimeout(later, wait);
  };
}

window.addEventListener('resize', debounce(function() {
  const width = window.innerWidth;
  const mobileMenu = document.querySelector('.site-header-mobi-panel');

  if (width > 768 && mobileMenu) {
    mobileMenu.classList.remove('is-open');
    document.body.classList.remove('menu-open');
  }
}, 250));
