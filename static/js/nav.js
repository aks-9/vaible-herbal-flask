/* =====================================================
   nav.js — Navbar, dropdowns, mobile drawer, dark mode
   ===================================================== */

(function () {
  'use strict';

  const html = document.documentElement;

  /* --------------------------------------------------
     Dark mode
  -------------------------------------------------- */
  function applyTheme(theme) {
    if (theme === 'dark') {
      html.classList.add('dark');
    } else {
      html.classList.remove('dark');
    }
    localStorage.setItem('theme', theme);
    syncToggleIcon();
  }

  function syncToggleIcon() {
    const isDark = html.classList.contains('dark');
    const moonIcon = document.getElementById('iconMoon');
    const sunIcon  = document.getElementById('iconSun');
    if (moonIcon) moonIcon.classList.toggle('hidden', isDark);
    if (sunIcon)  sunIcon.classList.toggle('hidden', !isDark);
  }

  // Apply saved or system preference on load
  const saved = localStorage.getItem('theme');
  if (saved) {
    applyTheme(saved);
  } else if (window.matchMedia('(prefers-color-scheme: dark)').matches) {
    applyTheme('dark');
  } else {
    applyTheme('light');
  }

  document.getElementById('darkToggle')?.addEventListener('click', function () {
    applyTheme(html.classList.contains('dark') ? 'light' : 'dark');
  });

  /* --------------------------------------------------
     Desktop dropdowns
  -------------------------------------------------- */
  function closeAllDropdowns() {
    document.querySelectorAll('[data-dropdown-menu]').forEach(function (menu) {
      menu.classList.add('hidden');
    });
    document.querySelectorAll('[data-dropdown-btn]').forEach(function (btn) {
      btn.setAttribute('aria-expanded', 'false');
      const chevron = btn.querySelector('[data-chevron]');
      if (chevron) chevron.style.transform = '';
    });
  }

  document.querySelectorAll('[data-dropdown-btn]').forEach(function (btn) {
    btn.addEventListener('click', function (e) {
      e.stopPropagation();
      const wrapper = btn.closest('[data-dropdown-wrapper]');
      const menu    = wrapper.querySelector('[data-dropdown-menu]');
      const isOpen  = !menu.classList.contains('hidden');

      closeAllDropdowns();

      if (!isOpen) {
        menu.classList.remove('hidden');
        btn.setAttribute('aria-expanded', 'true');
        const chevron = btn.querySelector('[data-chevron]');
        if (chevron) chevron.style.transform = 'rotate(180deg)';
      }
    });
  });

  // Close on outside click
  document.addEventListener('click', closeAllDropdowns);

  /* --------------------------------------------------
     Mobile drawer
  -------------------------------------------------- */
  const hamburger     = document.getElementById('navHamburger');
  const drawer        = document.getElementById('mobileDrawer');
  const drawerBackdrop = document.getElementById('drawerBackdrop');
  const drawerClose   = document.getElementById('drawerClose');

  function openDrawer() {
    drawer.classList.remove('translate-x-full');
    drawerBackdrop.classList.remove('hidden');
    document.body.classList.add('overflow-hidden');
    hamburger.setAttribute('aria-expanded', 'true');
  }

  function closeDrawer() {
    drawer.classList.add('translate-x-full');
    drawerBackdrop.classList.add('hidden');
    document.body.classList.remove('overflow-hidden');
    hamburger.setAttribute('aria-expanded', 'false');
  }

  hamburger?.addEventListener('click', openDrawer);
  drawerClose?.addEventListener('click', closeDrawer);
  drawerBackdrop?.addEventListener('click', closeDrawer);

  /* --------------------------------------------------
     Mobile accordion submenus
  -------------------------------------------------- */
  document.querySelectorAll('[data-mobile-toggle]').forEach(function (toggle) {
    toggle.addEventListener('click', function () {
      const sub     = toggle.nextElementSibling;
      const isOpen  = !sub.classList.contains('hidden');
      const chevron = toggle.querySelector('[data-chevron]');

      sub.classList.toggle('hidden', isOpen);
      toggle.setAttribute('aria-expanded', String(!isOpen));
      if (chevron) chevron.style.transform = isOpen ? '' : 'rotate(180deg)';
    });
  });

})();
