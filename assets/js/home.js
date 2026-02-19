document.addEventListener('DOMContentLoaded', function() {
  initHeroAnimation();
  initGallery();
  initTestimonialSlider();
  initCounters();
});

function initHeroAnimation() {
  const heroButtons = document.querySelectorAll('.home-hero__buttons .btn');

  heroButtons.forEach((button, index) => {
    button.style.animationDelay = `${1.6 + (index * 0.2)}s`;
  });
}

function initGallery() {
  const galleryItems = document.querySelectorAll('.gallery-item');

  galleryItems.forEach(item => {
    item.addEventListener('click', function() {
      const img = this.querySelector('img');
      if (img) {
        openLightbox(img.src, img.alt);
      }
    });
  });
}

function openLightbox(src, alt) {
  const lightbox = document.createElement('div');
  lightbox.className = 'lightbox';
  lightbox.innerHTML = `
    <div class="lightbox__overlay"></div>
    <div class="lightbox__content">
      <button class="lightbox__close">&times;</button>
      <img src="${src}" alt="${alt}">
    </div>
  `;

  document.body.appendChild(lightbox);
  document.body.style.overflow = 'hidden';

  setTimeout(() => lightbox.classList.add('active'), 10);

  const close = () => {
    lightbox.classList.remove('active');
    setTimeout(() => {
      document.body.removeChild(lightbox);
      document.body.style.overflow = '';
    }, 300);
  };

  lightbox.querySelector('.lightbox__close').addEventListener('click', close);
  lightbox.querySelector('.lightbox__overlay').addEventListener('click', close);

  document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape') close();
  });
}

function initTestimonialSlider() {
  const testimonials = document.querySelectorAll('.testimonial-card');
  let currentIndex = 0;

  if (testimonials.length === 0) return;

  setInterval(() => {
    testimonials[currentIndex].style.opacity = '0.5';

    currentIndex = (currentIndex + 1) % testimonials.length;

    testimonials.forEach((testimonial, index) => {
      if (index === currentIndex) {
        testimonial.style.opacity = '1';
        testimonial.style.transform = 'scale(1.05)';
      } else {
        testimonial.style.opacity = '0.7';
        testimonial.style.transform = 'scale(1)';
      }
    });
  }, 5000);
}

function initCounters() {
  const counters = document.querySelectorAll('.counter');

  const observerOptions = {
    threshold: 0.5
  };

  const observer = new IntersectionObserver(function(entries) {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const counter = entry.target;
        const target = parseInt(counter.getAttribute('data-target'));
        const duration = 2000;
        const increment = target / (duration / 16);
        let current = 0;

        const updateCounter = () => {
          current += increment;
          if (current < target) {
            counter.textContent = Math.ceil(current);
            requestAnimationFrame(updateCounter);
          } else {
            counter.textContent = target;
          }
        };

        updateCounter();
        observer.unobserve(counter);
      }
    });
  }, observerOptions);

  counters.forEach(counter => {
    observer.observe(counter);
  });
}

const style = document.createElement('style');
style.textContent = `
  .lightbox {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: 10000;
    opacity: 0;
    transition: opacity 0.3s ease;
  }

  .lightbox.active {
    opacity: 1;
  }

  .lightbox__overlay {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.9);
    cursor: pointer;
  }

  .lightbox__content {
    position: relative;
    width: 100%;
    height: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 40px;
  }

  .lightbox__content img {
    max-width: 90%;
    max-height: 90%;
    object-fit: contain;
    box-shadow: 0 0 50px rgba(0, 0, 0, 0.5);
  }

  .lightbox__close {
    position: absolute;
    top: 20px;
    right: 20px;
    width: 50px;
    height: 50px;
    background-color: rgba(255, 255, 255, 0.1);
    border: 2px solid white;
    border-radius: 50%;
    color: white;
    font-size: 30px;
    cursor: pointer;
    transition: all 0.3s ease;
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 10001;
  }

  .lightbox__close:hover {
    background-color: rgba(255, 255, 255, 0.2);
    transform: rotate(90deg);
  }
`;

document.head.appendChild(style);
