/**
 * animations.js — GSAP scroll & entrance animations
 * Requires: gsap + ScrollTrigger (loaded in base.html via CDN)
 */
(function () {
  'use strict';

  if (typeof gsap === 'undefined') return;
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;

  gsap.registerPlugin(ScrollTrigger);

  /* ── 1. Homepage hero entrance ────────────────────────────
     Staggered fade-up for eyebrow / H1 / subtitle / CTA row   */
  const heroContent = document.getElementById('heroContent');
  if (heroContent) {
    gsap.timeline({ delay: 0.3 })
      .from(heroContent.children, {
        y: 40,
        opacity: 0,
        duration: 0.7,
        stagger: 0.18,
        ease: 'power3.out',
      });
  }

  /* ── 2. Stats strip — fade-in + count-up ─────────────────  */
  const statsGrid = document.getElementById('statsGrid');
  if (statsGrid) {
    const items = Array.from(statsGrid.querySelectorAll('li'));
    ScrollTrigger.create({
      trigger: statsGrid,
      start: 'top 85%',
      once: true,
      onEnter: () => {
        gsap.from(items, {
          y: 20,
          opacity: 0,
          duration: 0.5,
          stagger: 0.1,
          ease: 'power2.out',
        });

        items.forEach(item => {
          const numEl = item.querySelector('.font-display');
          if (!numEl) return;
          const raw  = numEl.textContent.trim();
          const num  = parseInt(raw, 10);
          if (isNaN(num)) return;
          const suffix = raw.slice(String(num).length); // '+', '' etc.
          const obj  = { val: 0 };
          gsap.to(obj, {
            val: num,
            duration: 1.6,
            ease: 'power1.out',
            onUpdate: () => {
              numEl.textContent = Math.round(obj.val) + suffix;
            },
          });
        });
      },
    });
  }

  /* ── 3. Company intro — slide in from sides ───────────────  */
  const introGrid = document.getElementById('introGrid');
  if (introGrid) {
    const cols = introGrid.children;
    ScrollTrigger.create({
      trigger: introGrid,
      start: 'top 80%',
      once: true,
      onEnter: () => {
        gsap.from(cols[0], { x: -50, opacity: 0, duration: 0.8, ease: 'power2.out' });
        gsap.from(cols[1], { x:  50, opacity: 0, duration: 0.8, ease: 'power2.out', delay: 0.15 });
      },
    });
  }

  /* ── 4. Category cards — staggered fade-up ────────────────
     Used on both homepage (#catGrid) and products page        */
  const catGrid = document.getElementById('catGrid');
  if (catGrid) {
    ScrollTrigger.create({
      trigger: catGrid,
      start: 'top 85%',
      once: true,
      onEnter: () => {
        gsap.from(catGrid.children, {
          y: 40,
          opacity: 0,
          duration: 0.55,
          stagger: 0.07,
          ease: 'power2.out',
        });
      },
    });
  }

  /* ── 5. Inner page hero content ───────────────────────────
     Targets the .max-w-2xl content block inside any dark
     brand-900 hero section (all inner pages).
     Skipped on homepage which uses #heroContent instead.      */
  if (!heroContent) {
    const pageHeroInner = document.querySelector('section.bg-brand-900 .max-w-2xl');
    if (pageHeroInner) {
      gsap.timeline({ delay: 0.1 })
        .from(pageHeroInner.children, {
          y: 30,
          opacity: 0,
          duration: 0.6,
          stagger: 0.12,
          ease: 'power2.out',
        });
    }
  }

})();
