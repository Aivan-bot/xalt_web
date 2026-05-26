// XALT Website v2 — Mobile Menu, Animations, Scroll

document.addEventListener('DOMContentLoaded', () => {
  
  // === MOBILE MENU ===
  const menuToggle = document.getElementById('menuToggle');
  const mainNav = document.getElementById('mainNav');
  const mobileDrop = document.getElementById('mobileDrop');
  
  if (menuToggle && mobileDrop) {
    menuToggle.addEventListener('click', () => {
      const isOpen = mobileDrop.style.display === 'flex';
      mobileDrop.style.display = isOpen ? 'none' : 'flex';
      mobileDrop.style.flexDirection = 'column';
      mainNav.classList.toggle('open', !isOpen);
      menuToggle.setAttribute('aria-expanded', !isOpen);
    });
  }
  
  // Close menu on resize
  window.addEventListener('resize', () => {
    if (window.innerWidth > 768 && mobileDrop) {
      mobileDrop.style.display = 'none';
      mainNav?.classList.remove('open');
    }
  });

  // === INTERSECTION OBSERVER (Fade-in Animation) ===
  const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -30px 0px'
  };
  
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('vis');
        observer.unobserve(entry.target);
      }
    });
  }, observerOptions);
  
  document.querySelectorAll('.fani').forEach(el => observer.observe(el));
});
