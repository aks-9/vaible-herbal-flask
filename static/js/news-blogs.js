/**
 * news-blogs.js — client-side search, filter, sort and modal for News & Blogs page.
 * Data is injected server-side as JSON in <script id="nbData" type="application/json">.
 */

(function () {
  'use strict';

  // ── Helpers ─────────────────────────────────────────────────────────────────

  function escHtml(str) {
    return String(str)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#39;');
  }

  function formatDate(dateStr) {
    try {
      const d = new Date(dateStr + 'T00:00:00');
      return d.toLocaleDateString('en-GB', { day: 'numeric', month: 'short', year: 'numeric' });
    } catch (e) {
      return dateStr;
    }
  }

  function categoryLabel(slug) {
    const map = {
      'quality-systems': 'Quality Systems',
      'process': 'Process & Manufacturing',
      'analytical': 'Analytical',
      'regulatory': 'Regulatory',
      'sustainability': 'Sustainability',
    };
    return map[slug] || slug;
  }

  // ── State ────────────────────────────────────────────────────────────────────

  let allPosts = [];
  let debounceTimer = null;

  // ── DOM refs ─────────────────────────────────────────────────────────────────

  const grid      = document.getElementById('nbGrid');
  const empty     = document.getElementById('nbEmpty');
  const stats     = document.getElementById('nbStats');
  const search    = document.getElementById('nbSearch');
  const catSelect = document.getElementById('nbCategory');
  const sortSel   = document.getElementById('nbSort');
  const pills     = document.querySelectorAll('#nbPills [data-cat]');

  // Modal refs
  const overlay    = document.getElementById('nbOverlay');
  const modalMeta  = document.getElementById('nbModalMeta');
  const modalTitle = document.getElementById('nbModalTitle');
  const modalBody  = document.getElementById('nbModalBody');
  const closeBtn   = document.getElementById('nbClose');

  // ── Card rendering ────────────────────────────────────────────────────────────

  function renderCards(posts) {
    if (!grid) return;

    if (posts.length === 0) {
      grid.innerHTML = '';
      if (empty) empty.classList.remove('hidden');
      if (stats) stats.textContent = '0 posts';
      return;
    }

    if (empty) empty.classList.add('hidden');
    if (stats) stats.textContent = posts.length === 1 ? '1 post' : posts.length + ' posts';

    grid.innerHTML = posts.map(function (post) {
      return '<article data-id="' + escHtml(String(post.id)) + '" ' +
        'tabindex="0" role="button" aria-label="Read: ' + escHtml(post.title) + '" ' +
        'class="bg-white dark:bg-gray-900 rounded-xl border border-gray-100 dark:border-gray-800 ' +
        'p-6 shadow-sm hover:shadow-md hover:border-brand-200 dark:hover:border-brand-800 ' +
        'transition-all duration-200 cursor-pointer group">' +

        '<div class="flex items-center justify-between mb-3 gap-2">' +
        '<span class="inline-block bg-brand-50 dark:bg-brand-900/30 text-brand-700 dark:text-brand-400 ' +
        'text-xs font-semibold px-2.5 py-1 rounded-full">' + escHtml(categoryLabel(post.category)) + '</span>' +
        '<time class="text-xs text-gray-400 shrink-0" datetime="' + escHtml(post.date) + '">' +
        escHtml(formatDate(post.date)) + '</time>' +
        '</div>' +

        '<h3 class="font-semibold text-gray-900 dark:text-white text-base leading-snug mb-2 ' +
        'group-hover:text-brand-700 dark:group-hover:text-brand-400 transition-colors">' +
        escHtml(post.title) + '</h3>' +

        '<p class="text-sm text-gray-500 dark:text-gray-400 leading-relaxed mb-4 line-clamp-2">' +
        escHtml(post.summary) + '</p>' +

        '<span class="text-xs font-medium text-brand-700 dark:text-brand-400 ' +
        'group-hover:underline transition-colors">Read more →</span>' +

        '</article>';
    }).join('');
  }

  // ── Filter + sort ─────────────────────────────────────────────────────────────

  function filterAndRender() {
    const q   = search ? search.value.trim().toLowerCase() : '';
    const cat = catSelect ? catSelect.value : 'all';
    const srt = sortSel ? sortSel.value : 'newest';

    let result = allPosts.slice();

    // Search
    if (q) {
      result = result.filter(function (p) {
        return (
          p.title.toLowerCase().includes(q) ||
          p.summary.toLowerCase().includes(q) ||
          (p.tags || []).some(function (t) { return t.toLowerCase().includes(q); })
        );
      });
    }

    // Category
    if (cat && cat !== 'all') {
      result = result.filter(function (p) { return p.category === cat; });
    }

    // Sort
    if (srt === 'oldest') {
      result.sort(function (a, b) { return a.date < b.date ? -1 : a.date > b.date ? 1 : 0; });
    } else if (srt === 'title-az') {
      result.sort(function (a, b) { return a.title.localeCompare(b.title); });
    } else if (srt === 'title-za') {
      result.sort(function (a, b) { return b.title.localeCompare(a.title); });
    } else {
      // newest (default)
      result.sort(function (a, b) { return a.date < b.date ? 1 : a.date > b.date ? -1 : 0; });
    }

    renderCards(result);
  }

  // ── Modal ────────────────────────────────────────────────────────────────────

  function openModal(postId) {
    const post = allPosts.find(function (p) { return p.id === postId; });
    if (!post || !overlay) return;

    if (modalMeta) {
      modalMeta.innerHTML =
        '<span class="inline-block bg-brand-50 dark:bg-brand-900/30 text-brand-700 dark:text-brand-400 ' +
        'text-xs font-semibold px-2.5 py-1 rounded-full mr-2">' + escHtml(categoryLabel(post.category)) + '</span>' +
        '<time class="text-xs text-gray-400" datetime="' + escHtml(post.date) + '">' +
        escHtml(formatDate(post.date)) + '</time>';
    }

    if (modalTitle) {
      modalTitle.textContent = post.title;
    }

    if (modalBody) {
      // Split content on newlines to create paragraphs (XSS-safe)
      const paragraphs = (post.content || '').split('\n\n').filter(Boolean);
      modalBody.innerHTML = paragraphs.map(function (p) {
        return '<p class="text-sm text-gray-600 dark:text-gray-400 leading-relaxed mb-4">' +
          escHtml(p.trim()) + '</p>';
      }).join('');

      // Tags
      if (post.tags && post.tags.length) {
        modalBody.innerHTML += '<div class="flex flex-wrap gap-2 mt-4">' +
          post.tags.map(function (t) {
            return '<span class="bg-gray-100 dark:bg-gray-800 text-gray-600 dark:text-gray-300 ' +
              'text-xs px-2.5 py-1 rounded-full">' + escHtml(t) + '</span>';
          }).join('') +
          '</div>';
      }
    }

    overlay.classList.remove('hidden');
    overlay.classList.add('flex');
    document.body.style.overflow = 'hidden';

    // Focus the close button for accessibility
    if (closeBtn) setTimeout(function () { closeBtn.focus(); }, 50);
  }

  function closeModal() {
    if (!overlay) return;
    overlay.classList.add('hidden');
    overlay.classList.remove('flex');
    document.body.style.overflow = '';
  }

  // ── Pill sync ─────────────────────────────────────────────────────────────────

  function syncPills(catValue) {
    pills.forEach(function (pill) {
      const active = pill.dataset.cat === catValue;
      pill.classList.toggle('bg-brand-700', active);
      pill.classList.toggle('text-white', active);
      pill.classList.toggle('border-brand-700', active);
      pill.classList.toggle('bg-white', !active);
      pill.classList.toggle('dark:bg-gray-900', !active);
      pill.classList.toggle('text-gray-700', !active);
      pill.classList.toggle('dark:text-gray-300', !active);
      pill.classList.toggle('border-gray-300', !active);
      pill.classList.toggle('dark:border-gray-700', !active);
    });
  }

  // ── Event listeners ───────────────────────────────────────────────────────────

  function init() {
    // Load data
    const dataEl = document.getElementById('nbData');
    if (!dataEl) return;
    try {
      allPosts = JSON.parse(dataEl.textContent);
    } catch (e) {
      console.error('news-blogs.js: failed to parse nbData JSON', e);
      return;
    }

    // Initial render
    filterAndRender();

    // Search (debounced 200ms)
    if (search) {
      search.addEventListener('input', function () {
        clearTimeout(debounceTimer);
        debounceTimer = setTimeout(filterAndRender, 200);
      });
    }

    // Category select
    if (catSelect) {
      catSelect.addEventListener('change', function () {
        syncPills(this.value);
        filterAndRender();
      });
    }

    // Sort select
    if (sortSel) {
      sortSel.addEventListener('change', filterAndRender);
    }

    // Pill buttons
    pills.forEach(function (pill) {
      pill.addEventListener('click', function () {
        const cat = this.dataset.cat;
        if (catSelect) catSelect.value = cat;
        syncPills(cat);
        filterAndRender();
      });
    });

    // Initial pill state
    syncPills(catSelect ? catSelect.value : 'all');

    // Card clicks (event delegation)
    if (grid) {
      grid.addEventListener('click', function (e) {
        const card = e.target.closest('[data-id]');
        if (card) openModal(parseInt(card.dataset.id, 10));
      });
      grid.addEventListener('keydown', function (e) {
        if (e.key === 'Enter' || e.key === ' ') {
          const card = e.target.closest('[data-id]');
          if (card) {
            e.preventDefault();
            openModal(parseInt(card.dataset.id, 10));
          }
        }
      });
    }

    // Close modal
    if (closeBtn) {
      closeBtn.addEventListener('click', closeModal);
    }
    if (overlay) {
      overlay.addEventListener('click', function (e) {
        if (e.target === overlay) closeModal();
      });
    }
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') closeModal();
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

})();
