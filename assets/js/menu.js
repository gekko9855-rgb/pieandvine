document.addEventListener('DOMContentLoaded', function() {
  initMenuCategories();
  initMenuItems();
});

function initMenuCategories() {
  const categoryButtons = document.querySelectorAll('.menu-category-btn');
  const menuSections = document.querySelectorAll('.menu-section');

  if (categoryButtons.length > 0 && menuSections.length > 0) {
    categoryButtons[0].classList.add('active');
    menuSections[0].classList.add('active');
  }

  categoryButtons.forEach(button => {
    button.addEventListener('click', function() {
      const category = this.getAttribute('data-category');

      categoryButtons.forEach(btn => btn.classList.remove('active'));
      this.classList.add('active');

      menuSections.forEach(section => {
        section.classList.remove('active');
        if (section.getAttribute('data-category') === category) {
          section.classList.add('active');

          section.scrollIntoView({
            behavior: 'smooth',
            block: 'nearest'
          });
        }
      });
    });
  });
}

function initMenuItems() {
  const menuItems = document.querySelectorAll('.menu-item');

  menuItems.forEach(item => {
    item.addEventListener('click', function() {
      openMenuModal(this);
    });
  });
}

function openMenuModal(menuItem) {
  const name = menuItem.querySelector('.menu-item__name').textContent;
  const price = menuItem.querySelector('.menu-item__price').textContent;
  const description = menuItem.querySelector('.menu-item__description').textContent;
  const imageSrc = menuItem.querySelector('.menu-item__image').src;
  const tags = Array.from(menuItem.querySelectorAll('.menu-item__tag')).map(tag => tag.textContent);

  const modal = document.createElement('div');
  modal.className = 'menu-modal';
  modal.innerHTML = `
    <div class="menu-modal__content">
      <button class="menu-modal__close">&times;</button>
      <img src="${imageSrc}" alt="${name}" class="menu-modal__image">
      <div class="menu-modal__info">
        <div class="menu-modal__header">
          <h3 class="menu-modal__name">${name}</h3>
          <span class="menu-modal__price">${price}</span>
        </div>
        <p class="menu-modal__description">${description}</p>
        <div class="menu-item__tags">
          ${tags.map(tag => `<span class="menu-item__tag">${tag}</span>`).join('')}
        </div>
      </div>
    </div>
  `;

  document.body.appendChild(modal);
  document.body.style.overflow = 'hidden';

  setTimeout(() => modal.classList.add('active'), 10);

  const close = () => {
    modal.classList.remove('active');
    setTimeout(() => {
      document.body.removeChild(modal);
      document.body.style.overflow = '';
    }, 300);
  };

  modal.querySelector('.menu-modal__close').addEventListener('click', close);
  modal.addEventListener('click', function(e) {
    if (e.target === modal) close();
  });

  document.addEventListener('keydown', function escHandler(e) {
    if (e.key === 'Escape') {
      close();
      document.removeEventListener('keydown', escHandler);
    }
  });
}
