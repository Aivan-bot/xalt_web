// XALT Website v2 — Minimal JS for Static Site
// Mobile menu, smooth scroll, intersection observer

document.addEventListener('DOMContentLoaded', () => {
  // Mobile menu toggle
  const menuToggle = document.querySelector('.header-menu-toggle');
  const headerLinks = document.querySelector('.header-links');
  
  if (menuToggle && headerLinks) {
    menuToggle.addEventListener('click', () => {
      const isOpen = menuToggle.getAttribute('aria-expanded') === 'true';
      
      menuToggle.setAttribute('aria-expanded', !isOpen);
      
      if (!isOpen) {
        headerLinks.style.display = 'flex';
        headerLinks.style.flexDirection = 'column';
        headerLinks.style.position = 'absolute';
        headerLinks.style.top = '72px';
        headerLinks.style.left = '0';
        headerLinks.style.right = '0';
        headerLinks.style.background = 'var(--bg)';
        headerLinks.style.padding = '24px';
        headerLinks.style.borderBottom = '1px solid var(--border)';
        headerLinks.style.zIndex = '999';
        headerLinks.style.animation = 'fadeIn 0.3s ease-out';
      } else {
        headerLinks.style.display = 'none';
      }
    });
    
    // Close menu on window resize
    window.addEventListener('resize', () => {
      if (window.innerWidth > 768) {
        headerLinks.style.display = 'flex';
        headerLinks.style.flexDirection = 'row';
        headerLinks.style.position = 'static';
        headerLinks.style.animation = 'none';
      } else {
        headerLinks.style.display = 'none';
      }
    });
  }
  
  // Smooth scroll for anchor links
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', (e) => {
      const target = document.querySelector(anchor.getAttribute('href'));
      if (target) {
        e.preventDefault();
        target.scrollIntoView({ behavior: 'smooth' });
      }
    });
  });
  
  // Intersection Observer for fade-in animations
  const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
  };
  
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.style.opacity = '1';
        entry.target.style.transform = 'translateY(0)';
        observer.unobserve(entry.target);
      }
    });
  }, observerOptions);
  
  // Observe all cards and sections
  document.querySelectorAll('.card, .section-header, .cta-content').forEach((el, i) => {
    el.style.opacity = '0';
    el.style.transform = 'translateY(20px)';
    el.style.transition = `opacity 0.6s ease-out ${i * 0.1}s, transform 0.6s ease-out ${i * 0.1}s`;
    observer.observe(el);
  });
  
  // Add fadeIn keyframe if not exists
  const style = document.createElement('style');
  style.textContent = `
    @keyframes fadeIn {
      from { opacity: 0; }
      to { opacity: 1; }
    }
  `;
  document.head.appendChild(style);
});
