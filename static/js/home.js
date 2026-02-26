/**
 * home.js — Homepage-specific JS
 * Hero slider + WhatsApp float (no deps)
 */

(function () {
  'use strict';

  /* ── Hero Slider ─────────────────────────────────────── */
  const slider   = document.getElementById('heroSlider');
  if (!slider) return;

  const slides   = Array.from(slider.querySelectorAll('[data-slide]'));
  const dots     = Array.from(document.querySelectorAll('[data-dot]'));
  const btnPrev  = document.getElementById('heroPrev');
  const btnNext  = document.getElementById('heroNext');
  const INTERVAL = 5000;

  let current   = 0;
  let timer     = null;
  let isPlaying = true;

  function goTo(idx) {
    slides[current].classList.remove('opacity-100', 'z-10');
    slides[current].classList.add('opacity-0', 'z-0');
    dots[current]?.classList.replace('bg-white', 'bg-white/40');

    current = (idx + slides.length) % slides.length;

    slides[current].classList.remove('opacity-0', 'z-0');
    slides[current].classList.add('opacity-100', 'z-10');
    dots[current]?.classList.replace('bg-white/40', 'bg-white');
  }

  function startTimer() {
    clearInterval(timer);
    timer = setInterval(() => goTo(current + 1), INTERVAL);
  }

  function pause()  { clearInterval(timer); isPlaying = false; }
  function resume() { if (!isPlaying) { startTimer(); isPlaying = true; } }

  btnPrev?.addEventListener('click', () => { goTo(current - 1); startTimer(); });
  btnNext?.addEventListener('click', () => { goTo(current + 1); startTimer(); });

  dots.forEach((dot, i) =>
    dot.addEventListener('click', () => { goTo(i); startTimer(); })
  );

  slider.addEventListener('mouseenter', pause);
  slider.addEventListener('mouseleave', () => { startTimer(); isPlaying = true; });

  // Keyboard support when slider is focused
  slider.setAttribute('tabindex', '0');
  slider.addEventListener('keydown', (e) => {
    if (e.key === 'ArrowLeft')  { goTo(current - 1); startTimer(); }
    if (e.key === 'ArrowRight') { goTo(current + 1); startTimer(); }
  });

  // Init first slide visible
  slides[0].classList.add('opacity-100', 'z-10');
  slides.slice(1).forEach(s => s.classList.add('opacity-0', 'z-0'));
  dots[0]?.classList.replace('bg-white/40', 'bg-white');

  startTimer();
})();
