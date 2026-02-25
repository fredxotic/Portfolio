(function () {
  'use strict';

  /* ============================================================
     PRELOADER
     ============================================================ */
  const preloader = document.getElementById('preloader');
  if (preloader) {
    window.addEventListener('load', () => {
      preloader.classList.add('hidden');
      setTimeout(() => preloader.remove(), 500);
    });
  }

  /* ============================================================
     NAVBAR — scroll state + hamburger
     ============================================================ */
  const navbar     = document.getElementById('navbar');
  const navToggle  = document.getElementById('navToggle');
  const navMenu    = document.getElementById('navMenu');

  // Add scrolled class when page scrolls
  function onScroll() {
    if (!navbar) return;
    if (window.scrollY > 60) {
      navbar.classList.add('scrolled');
    } else {
      navbar.classList.remove('scrolled');
    }
  }
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  // Hamburger toggle
  if (navToggle && navMenu) {
    navToggle.addEventListener('click', () => {
      const isOpen = navMenu.classList.toggle('open');
      navToggle.classList.toggle('open', isOpen);
      navToggle.setAttribute('aria-expanded', String(isOpen));
      document.body.style.overflow = isOpen ? 'hidden' : '';
    });

    // Close on nav link click
    navMenu.querySelectorAll('.fk-nav-link').forEach(link => {
      link.addEventListener('click', () => {
        navMenu.classList.remove('open');
        navToggle.classList.remove('open');
        navToggle.setAttribute('aria-expanded', 'false');
        document.body.style.overflow = '';
      });
    });

    // Close on outside click
    document.addEventListener('click', (e) => {
      if (navMenu.classList.contains('open') &&
          !navMenu.contains(e.target) &&
          !navToggle.contains(e.target)) {
        navMenu.classList.remove('open');
        navToggle.classList.remove('open');
        navToggle.setAttribute('aria-expanded', 'false');
        document.body.style.overflow = '';
      }
    });
  }

  /* ============================================================
     SCROLL SPY — active nav link
     ============================================================ */
  const sections   = document.querySelectorAll('section[id]');
  const navLinks   = document.querySelectorAll('.fk-nav-link[href^="#"]');

  function updateActiveLink() {
    const scrollY = window.scrollY + 120;
    sections.forEach(section => {
      const top    = section.offsetTop;
      const height = section.offsetHeight;
      const id     = section.getAttribute('id');
      if (scrollY >= top && scrollY < top + height) {
        navLinks.forEach(link => {
          link.classList.remove('active');
          if (link.getAttribute('href') === '#' + id) {
            link.classList.add('active');
          }
        });
      }
    });
  }
  if (sections.length && navLinks.length) {
    window.addEventListener('scroll', updateActiveLink, { passive: true });
    updateActiveLink();
  }

  /* ============================================================
     SCROLL TOP BUTTON
     ============================================================ */
  const scrollTopBtn = document.getElementById('scrollTop');
  if (scrollTopBtn) {
    window.addEventListener('scroll', () => {
      scrollTopBtn.classList.toggle('visible', window.scrollY > 400);
    }, { passive: true });

    scrollTopBtn.addEventListener('click', () => {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }

  /* ============================================================
     AOS — Animate On Scroll
     ============================================================ */
  if (typeof AOS !== 'undefined') {
    AOS.init({
      duration: 700,
      easing: 'ease-out-cubic',
      once: true,
      offset: 60,
    });
  }

  /* ============================================================
     TYPED.JS — Typewriter effect in hero
     ============================================================ */
  const typedEl = document.getElementById('typedEl');
  if (typedEl && typeof Typed !== 'undefined') {
    const rawItems = typedEl.getAttribute('data-typed-items') || '';
    const items    = rawItems.split(',').map(s => s.trim()).filter(Boolean);

    new Typed('#typedEl', {
      strings:   items.length ? items : ['Developer'],
      loop:      true,
      typeSpeed: 80,
      backSpeed: 40,
      backDelay: 2200,
      showCursor: false,   // We render our own cursor in HTML/CSS
    });
  }

  /* ============================================================
     SKILLS PROGRESS BARS — animate on viewport entry
     ============================================================ */
  const skillsContainers = document.querySelectorAll('.skills-animation');

  function animateSkills(container) {
    container.querySelectorAll('.fk-progress__bar').forEach(bar => {
      const target = bar.getAttribute('data-width') || '0%';
      // Small delay so the animation is visible after AOS fade-in
      setTimeout(() => { bar.style.width = target; }, 200);
    });
  }

  if (typeof Waypoint !== 'undefined') {
    skillsContainers.forEach(container => {
      new Waypoint({
        element: container,
        offset: '85%',
        handler: function () {
          animateSkills(container);
          this.destroy(); // fire once
        }
      });
    });
  } else {
    // Fallback: IntersectionObserver
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          animateSkills(entry.target);
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.2 });

    skillsContainers.forEach(c => observer.observe(c));
  }

  /* ============================================================
     ISOTOPE — Portfolio filter
     ============================================================ */
  const isotopeGrid = document.querySelector('.isotope-container');
  if (isotopeGrid && typeof Isotope !== 'undefined' && typeof imagesLoaded !== 'undefined') {
    imagesLoaded(isotopeGrid, function () {
      const iso = new Isotope(isotopeGrid, {
        itemSelector:  '.isotope-item',
        layoutMode:    'fitRows',
        percentPosition: true,
      });

      document.querySelectorAll('.fk-filter-btn').forEach(btn => {
        btn.addEventListener('click', function () {
          document.querySelectorAll('.fk-filter-btn').forEach(b => b.classList.remove('active'));
          this.classList.add('active');
          iso.arrange({ filter: this.dataset.filter });
          if (typeof AOS !== 'undefined') AOS.refresh();
        });
      });
    });
  }

  /* ============================================================
     GLIGHTBOX — Image lightbox
     ============================================================ */
  if (typeof GLightbox !== 'undefined') {
    GLightbox({ selector: '.glightbox' });
  }

  /* ============================================================
     CONTACT FORM — loading spinner on submit
     ============================================================ */
  const contactForm = document.getElementById('contactForm');
  if (contactForm) {
    contactForm.addEventListener('submit', function () {
      const btn      = this.querySelector('button[type="submit"]');
      const txtSpan  = btn ? btn.querySelector('.fk-btn__text') : null;
      const spinSpan = btn ? btn.querySelector('.fk-btn__spinner') : null;
      if (btn) btn.disabled = true;
      if (txtSpan)  txtSpan.classList.add('d-none');
      if (spinSpan) spinSpan.classList.remove('d-none');
    });
  }

  /* ============================================================
     HASH SCROLL on load (for links like /#contact)
     ============================================================ */
  window.addEventListener('load', () => {
    if (window.location.hash) {
      const target = document.querySelector(window.location.hash);
      if (target) {
        setTimeout(() => {
          target.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }, 300);
      }
    }
  });

})();
