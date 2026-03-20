/**
 * chat.js — Vaible Herbal AI chat widget
 * Calls POST /chat with message + history, renders replies in the panel.
 */
(function () {
  'use strict';

  const toggle   = document.getElementById('chatToggle');
  const panel    = document.getElementById('chatPanel');
  const messages = document.getElementById('chatMessages');
  const input    = document.getElementById('chatInput');
  const sendBtn  = document.getElementById('chatSend');
  const iconOpen = document.getElementById('chatIconOpen');
  const iconClose= document.getElementById('chatIconClose');

  if (!toggle || !panel) return;

  /* ── History (Gemini format) ──────────────────────────── */
  let history = [];
  let isOpen  = false;
  let busy    = false;

  /* ── Toggle panel ─────────────────────────────────────── */
  toggle.addEventListener('click', () => {
    isOpen = !isOpen;
    panel.classList.toggle('hidden', !isOpen);
    iconOpen.classList.toggle('hidden', isOpen);
    iconClose.classList.toggle('hidden', !isOpen);
    toggle.setAttribute('aria-label', isOpen ? 'Close chat' : 'Open chat assistant');
    if (isOpen) input.focus();
  });

  /* ── Send on button click or Enter ───────────────────── */
  sendBtn.addEventListener('click', sendMessage);
  input.addEventListener('keydown', (e) => {
    if (e.key === 'Enter' && !e.shiftKey) { e.preventDefault(); sendMessage(); }
  });

  /* ── Core send function ───────────────────────────────── */
  async function sendMessage() {
    const text = input.value.trim();
    if (!text || busy) return;

    input.value = '';
    busy = true;
    sendBtn.disabled = true;

    appendMessage('user', text);
    const typingEl = appendTyping();
    scrollBottom();

    try {
      const res = await fetch('/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: text, history }),
      });
      const data = await res.json();
      const reply = (data.reply || '').trim();

      typingEl.remove();
      appendMessage('model', reply);

      // Update history
      history.push({ role: 'user',  parts: text  });
      history.push({ role: 'model', parts: reply });
      if (history.length > 20) history = history.slice(-20); // cap at 10 exchanges

    } catch (_) {
      typingEl.remove();
      appendMessage('model', 'Sorry, something went wrong. Please try again or email Sales@VaibleHerbal.com.');
    } finally {
      busy = false;
      sendBtn.disabled = false;
      input.focus();
      scrollBottom();
    }
  }

  /* ── DOM helpers ──────────────────────────────────────── */
  function appendMessage(role, text) {
    const isUser = role === 'user';
    const wrap = document.createElement('div');
    wrap.className = isUser
      ? 'flex justify-end'
      : 'flex justify-start';

    const bubble = document.createElement('div');
    bubble.className = isUser
      ? 'max-w-[75%] bg-brand-700 text-white text-sm rounded-2xl rounded-br-sm px-4 py-2.5'
      : 'max-w-[85%] bg-gray-100 dark:bg-gray-700 text-gray-800 dark:text-gray-100 text-sm rounded-2xl rounded-bl-sm px-4 py-2.5';

    // Safe rendering: textContent for user, allow line breaks for bot
    if (isUser) {
      bubble.textContent = text;
    } else {
      // Bot text: escape then convert newlines to <br>
      bubble.innerHTML = escHtml(text).replace(/\n/g, '<br>');
    }

    wrap.appendChild(bubble);
    messages.appendChild(wrap);
    return wrap;
  }

  function appendTyping() {
    const wrap = document.createElement('div');
    wrap.className = 'flex justify-start';
    wrap.innerHTML = `
      <div class="bg-gray-100 dark:bg-gray-700 rounded-2xl rounded-bl-sm px-4 py-3 flex gap-1 items-center">
        <span class="w-1.5 h-1.5 bg-gray-400 rounded-full animate-bounce" style="animation-delay:0ms"></span>
        <span class="w-1.5 h-1.5 bg-gray-400 rounded-full animate-bounce" style="animation-delay:150ms"></span>
        <span class="w-1.5 h-1.5 bg-gray-400 rounded-full animate-bounce" style="animation-delay:300ms"></span>
      </div>`;
    messages.appendChild(wrap);
    return wrap;
  }

  function scrollBottom() {
    messages.scrollTop = messages.scrollHeight;
  }

  function escHtml(str) {
    return str
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;');
  }

})();
