document.addEventListener('DOMContentLoaded', function() {
  initTimelineAnimation();
  initParallax();
});

function initTimelineAnimation() {
  const timelineItems = document.querySelectorAll('.timeline-item');

  const observerOptions = {
    threshold: 0.3,
    rootMargin: '0px 0px -100px 0px'
  };

  const observer = new IntersectionObserver(function(entries) {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.style.opacity = '1';
        entry.target.style.transform = 'translateY(0)';
      }
    });
  }, observerOptions);

  timelineItems.forEach((item, index) => {
    item.style.opacity = '0';
    item.style.transform = 'translateY(30px)';
    item.style.transition = `all 0.6s ease ${index * 0.1}s`;
    observer.observe(item);
  });
}

function initParallax() {
  const images = document.querySelectorAll('.story-image, .team-member__image');

  window.addEventListener('scroll', function() {
    const scrolled = window.pageYOffset;

    images.forEach(image => {
      const rect = image.getBoundingClientRect();
      const imageTop = rect.top + scrolled;
      const imageHeight = rect.height;

      if (rect.top < window.innerHeight && rect.bottom > 0) {
        const offset = (scrolled - imageTop + window.innerHeight) / (window.innerHeight + imageHeight);
        const parallaxValue = (offset - 0.5) * 50;
        image.style.transform = `translateY(${parallaxValue}px)`;
      }
    });
  });
}
