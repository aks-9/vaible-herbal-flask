/**
 * product-detail.js
 * Handles search, filter, sort, card rendering and modal for product detail pages.
 */

(function () {
  'use strict';

  // ---------------------------------------------------------------------------
  // DOM references
  // ---------------------------------------------------------------------------
  const dataEl       = document.getElementById('pdData');
  const grid         = document.getElementById('pdGrid');
  const emptyEl      = document.getElementById('pdEmpty');
  const countEl      = document.getElementById('pdCount');
  const searchEl     = document.getElementById('pdSearch');
  const industryEl   = document.getElementById('pdFilterIndustry');
  const functionEl   = document.getElementById('pdFilterFunction');
  const sortEl       = document.getElementById('pdSort');
  const clearBtn     = document.getElementById('pdClear');
  const modal        = document.getElementById('pdModal');
  const modalClose   = document.getElementById('pdModalClose');
  const modalBody    = document.getElementById('pdModalBody');
  const modalBackdrop = document.getElementById('pdModalBackdrop');

  if (!dataEl || !grid) return;

  // ---------------------------------------------------------------------------
  // Data
  // ---------------------------------------------------------------------------
  let ALL_PRODUCTS = [];
  try {
    ALL_PRODUCTS = JSON.parse(dataEl.textContent || '[]');
  } catch (e) {
    console.error('product-detail: failed to parse product data', e);
    return;
  }

  // ---------------------------------------------------------------------------
  // State
  // ---------------------------------------------------------------------------
  const state = { q: '', industry: '', func: '', sort: 'az' };

  // ---------------------------------------------------------------------------
  // Helpers
  // ---------------------------------------------------------------------------
  const norm = (s) => (s || '').toLowerCase().trim();

  function getFiltered() {
    let list = ALL_PRODUCTS.slice();

    if (state.q) {
      const q = norm(state.q);
      list = list.filter((p) => {
        const hay = [
          p.name,
          p.botanical,
          p.part_used,
          (p.industries || []).join(' '),
          (p.functions  || []).join(' '),
        ].join(' ');
        return norm(hay).includes(q);
      });
    }

    if (state.industry) {
      list = list.filter((p) => (p.industries || []).includes(state.industry));
    }

    if (state.func) {
      list = list.filter((p) => (p.functions || []).includes(state.func));
    }

    list.sort((a, b) => a.name.localeCompare(b.name));
    if (state.sort === 'za') list.reverse();

    return list;
  }

  function isFiltered() {
    return state.q || state.industry || state.func || state.sort !== 'az';
  }

  // ---------------------------------------------------------------------------
  // Card HTML
  // ---------------------------------------------------------------------------
  function cardHTML(p, idx) {
    const industries = (p.industries || []).join(', ') || '—';
    const functions  = (p.functions  || []).join(', ') || '—';
    return `
      <article
        class="group bg-white dark:bg-gray-800
               rounded-xl border border-gray-200 dark:border-gray-700
               shadow-sm hover:shadow-md hover:border-brand-400 dark:hover:border-brand-600
               transition-all duration-200 p-5 flex flex-col gap-3 cursor-pointer"
        data-idx="${idx}"
        tabindex="0"
        role="button"
        aria-label="View details for ${escHtml(p.name)}">

        <div class="flex items-start justify-between gap-2">
          <h3 class="font-semibold text-gray-900 dark:text-white text-sm leading-snug
                     group-hover:text-brand-700 dark:group-hover:text-brand-400
                     transition-colors duration-150">
            ${escHtml(p.name)}
          </h3>
        </div>

        ${p.botanical ? `
        <p class="text-xs italic text-gray-400 dark:text-gray-500 leading-snug">
          ${escHtml(p.botanical)}
        </p>` : ''}

        <div class="flex flex-wrap gap-1.5 mt-auto pt-1">
          ${(p.industries || []).slice(0, 2).map((ind) => `
          <span class="text-[10px] font-semibold uppercase tracking-wider
                       bg-brand-50 dark:bg-brand-900/30
                       text-brand-700 dark:text-brand-400
                       px-2 py-0.5 rounded">
            ${escHtml(ind)}
          </span>`).join('')}
        </div>

        <button type="button"
                data-idx="${idx}"
                class="mt-1 text-xs font-semibold text-brand-700 dark:text-brand-400
                       hover:text-brand-900 dark:hover:text-brand-300
                       transition-colors duration-150 text-left
                       flex items-center gap-1">
          View details
          <svg class="w-3 h-3 group-hover:translate-x-0.5 transition-transform duration-150"
               fill="none" stroke="currentColor" stroke-width="2.5"
               viewBox="0 0 24 24" aria-hidden="true">
            <path stroke-linecap="round" stroke-linejoin="round" d="M9 5l7 7-7 7" />
          </svg>
        </button>
      </article>`;
  }

  // ---------------------------------------------------------------------------
  // Modal HTML
  // ---------------------------------------------------------------------------
  function modalHTML(p) {
    const rows = [
      ['Botanical Name', p.botanical],
      ['Part Used',      p.part_used],
      ['Industries',     (p.industries || []).join(', ')],
      ['Functions',      (p.functions  || []).join(', ')],
    ]
      .filter(([, v]) => v)
      .map(([k, v]) => `
        <tr class="border-b border-gray-100 dark:border-gray-800 last:border-0">
          <td class="py-2.5 pr-4 text-xs font-semibold text-gray-500 dark:text-gray-400
                     whitespace-nowrap w-32 align-top">${escHtml(k)}</td>
          <td class="py-2.5 text-sm text-gray-800 dark:text-gray-200">${escHtml(v)}</td>
        </tr>`)
      .join('');

    return `
      <div class="p-6">
        <div class="mb-1">
          <span class="text-[10px] font-bold uppercase tracking-widest
                       text-brand-700 dark:text-brand-400">Product Details</span>
        </div>
        <h2 class="font-display text-2xl font-bold text-gray-900 dark:text-white mb-1">
          ${escHtml(p.name)}
        </h2>
        ${p.botanical ? `
        <p class="text-sm italic text-gray-400 dark:text-gray-500 mb-5">
          ${escHtml(p.botanical)}
        </p>` : '<div class="mb-5"></div>'}

        <table class="w-full mb-6">
          <tbody>${rows}</tbody>
        </table>

        <div class="flex flex-wrap gap-3">
          <a href="#"
             class="inline-flex items-center justify-center
                    bg-brand-700 hover:bg-brand-800 text-white
                    text-sm font-semibold px-5 py-2.5 rounded-lg
                    transition-colors duration-200">
            Request COA / Quote
          </a>
          <a href="https://wa.me/919911154497?text=Hi%20Vaible%20Herbal%2C%20I%27d%20like%20to%20enquire%20about%20${encodeURIComponent(p.name)}."
             target="_blank"
             rel="noopener noreferrer"
             class="inline-flex items-center gap-1.5 justify-center
                    border border-gray-200 dark:border-gray-700
                    text-gray-700 dark:text-gray-300 text-sm font-semibold
                    px-5 py-2.5 rounded-lg
                    hover:bg-gray-50 dark:hover:bg-gray-800
                    transition-colors duration-200">
            <svg class="w-4 h-4 text-[#25D366]" viewBox="0 0 32 32"
                 fill="currentColor" aria-hidden="true">
              <path d="M19.11 17.39c-.27-.14-1.61-.79-1.86-.88-.25-.09-.43-.14-.61.14-.18.27-.7.88-.86
                       1.06-.16.18-.32.2-.59.07-.27-.14-1.14-.42-2.18-1.34-.81-.72-1.36-1.61-1.52-1.88
                       -.16-.27-.02-.42.12-.56.12-.12.27-.32.41-.48.14-.16.18-.27.27-.45.09-.18.05-.34
                       -.02-.48-.07-.14-.61-1.47-.84-2.01-.22-.53-.45-.46-.61-.47h-.52c-.18 0-.48.07
                       -.73.34-.25.27-.95.93-.95 2.27s.98 2.64 1.11 2.82c.14.18 1.93 2.95 4.67 4.14
                       .65.28 1.16.45 1.56.58.66.21 1.26.18 1.74.11.53-.08 1.61-.66 1.84-1.29.23-.63
                       .23-1.17.16-1.29-.07-.12-.25-.2-.52-.34z"/>
              <path d="M26.67 5.33C23.92 2.58 20.27 1.07 16.4 1.07 8.67 1.07 2.4 7.34 2.4 15.07
                       c0 2.46.64 4.87 1.86 6.99L2.27 30.93l9.09-1.95c2.05 1.12 4.37 1.71 6.74 1.71
                       h.01c7.73 0 14-6.27 14-14 0-3.87-1.51-7.52-4.44-10.36zM18.1 28.15h-.01
                       c-2.1 0-4.16-.56-5.97-1.62l-.43-.25-5.39 1.16 1.14-5.25-.28-.45
                       c-1.17-1.85-1.79-3.99-1.79-6.17 0-6.46 5.26-11.72 11.73-11.72
                       3.14 0 6.09 1.22 8.31 3.44 2.22 2.22 3.44 5.17 3.44 8.31
                       0 6.46-5.26 11.72-11.75 11.72z"/>
            </svg>
            WhatsApp
          </a>
        </div>
      </div>`;
  }

  // ---------------------------------------------------------------------------
  // Render
  // ---------------------------------------------------------------------------
  let _lastFiltered = [];

  function render() {
    const list = getFiltered();
    _lastFiltered = list;

    grid.innerHTML = list.map((p, i) => cardHTML(p, i)).join('');
    countEl.textContent = `${list.length} product${list.length !== 1 ? 's' : ''}`;
    emptyEl.classList.toggle('hidden', list.length > 0);
    grid.classList.toggle('hidden', list.length === 0);

    if (clearBtn) {
      clearBtn.classList.toggle('hidden', !isFiltered());
    }
  }

  // ---------------------------------------------------------------------------
  // Modal open / close
  // ---------------------------------------------------------------------------
  function openModal(idx) {
    const p = _lastFiltered[idx];
    if (!p || !modalBody) return;
    modalBody.innerHTML = modalHTML(p);
    modal.setAttribute('aria-hidden', 'false');
    modal.classList.remove('opacity-0', 'pointer-events-none');
    modal.classList.add('opacity-100');
    document.body.style.overflow = 'hidden';
    modalClose && modalClose.focus();
  }

  function closeModal() {
    modal.setAttribute('aria-hidden', 'true');
    modal.classList.add('opacity-0', 'pointer-events-none');
    modal.classList.remove('opacity-100');
    document.body.style.overflow = '';
    if (modalBody) modalBody.innerHTML = '';
  }

  // ---------------------------------------------------------------------------
  // XSS-safe HTML escape
  // ---------------------------------------------------------------------------
  function escHtml(str) {
    return String(str || '')
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#x27;');
  }

  // ---------------------------------------------------------------------------
  // Events — grid (delegated)
  // ---------------------------------------------------------------------------
  grid.addEventListener('click', (e) => {
    const target = e.target.closest('[data-idx]');
    if (!target) return;
    openModal(parseInt(target.getAttribute('data-idx'), 10));
  });

  grid.addEventListener('keydown', (e) => {
    if (e.key === 'Enter' || e.key === ' ') {
      const target = e.target.closest('[data-idx]');
      if (target) {
        e.preventDefault();
        openModal(parseInt(target.getAttribute('data-idx'), 10));
      }
    }
  });

  // ---------------------------------------------------------------------------
  // Events — modal close
  // ---------------------------------------------------------------------------
  modalClose  && modalClose.addEventListener('click', closeModal);
  modalBackdrop && modalBackdrop.addEventListener('click', closeModal);

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && modal.getAttribute('aria-hidden') === 'false') {
      closeModal();
    }
  });

  // ---------------------------------------------------------------------------
  // Events — filters
  // ---------------------------------------------------------------------------
  searchEl && searchEl.addEventListener('input', () => {
    state.q = norm(searchEl.value);
    render();
  });

  industryEl && industryEl.addEventListener('change', () => {
    state.industry = industryEl.value;
    render();
  });

  functionEl && functionEl.addEventListener('change', () => {
    state.func = functionEl.value;
    render();
  });

  sortEl && sortEl.addEventListener('change', () => {
    state.sort = sortEl.value;
    render();
  });

  clearBtn && clearBtn.addEventListener('click', () => {
    state.q = '';
    state.industry = '';
    state.func = '';
    state.sort = 'az';
    if (searchEl)   searchEl.value   = '';
    if (industryEl) industryEl.value = '';
    if (functionEl) functionEl.value = '';
    if (sortEl)     sortEl.value     = 'az';
    render();
  });

  // ---------------------------------------------------------------------------
  // Init
  // ---------------------------------------------------------------------------
  render();

})();
