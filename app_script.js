// HostMastery Application Core Logic - Ultra Edition with 10,000+ Prompt Matrix & Hinglish Mode
(function() {
  const root = document.getElementById('hm-app');
  if (!root || root.dataset.hmReady === '1') return;
  root.dataset.hmReady = '1';

  // Helper shortcuts
  const $ = (s, ctx = root) => ctx.querySelector(s);
  const $$ = (s, ctx = root) => Array.from(ctx.querySelectorAll(s));

  // Safe Load Prompt Data (from document, not limited to root)
  let prompts = [];
  try {
    const promptEl = document.getElementById('hm-prompt-data') || root.querySelector('#hm-prompt-data');
    if (promptEl) {
      prompts = JSON.parse(promptEl.textContent || '[]');
    }
  } catch (e) {
    console.error('Failed to parse prompts data', e);
  }

  // Load Saved Prompts from localStorage
  let savedPrompts = new Set();
  try {
    const saved = localStorage.getItem('hm_saved_prompts');
    if (saved) savedPrompts = new Set(JSON.parse(saved));
  } catch(e) {}

  // Load Property Profile from localStorage
  const defaultProfile = {
    name: "The Himalayan Pine Villa",
    host: "Rajesh & Aditi Sharma",
    city: "Old Manali, Himachal Pradesh",
    type: "Boutique Mountain Homestay",
    guests: "Couples, Families & Workationers",
    amenities: "100 Mbps Wi-Fi, Mountain View Balcony, Bonfire, Home-cooked Pahadi Food, Power Backup",
    checkin: "2:00 PM onwards",
    checkout: "11:00 AM",
    wifi: "PineVilla_Guest_5G",
    password: "HimalayanPeace2026",
    contact: "+91 98765 43210 (WhatsApp)",
    greeting: "Namaste & Welcome to The Himalayan Pine Villa! We are delighted to host you. Settle in, sip on fresh local chai, and make yourself completely at home.",
    rules: "Quiet hours from 10:30 PM to 7:00 AM.\nNo smoking inside rooms (balcony allowed).\nPlease keep shoes on the shoe rack at entrance.\nEco-friendly stay: switch off geyser & room heater when not in use.\nRegistered guests only: no outside visitors after 9:00 PM.",
    steps: "Ensure all geysers, room heaters, and lights are switched off.\nReturn room keys to caretaker Ramesh or drop in key box.\nCheck wardrobes & bathroom for personal chargers/belongings.\nMessage us on WhatsApp when you head out!",
    local: "Chopsticks Restaurant (Mall Road) - Best Tibetan Thukpa & Momos (10 mins)\nJogini Waterfall Trek - Scenic 45-min easy hike from Vashisht (2 kms)\nOld Manali Village Cafes (Cafe 1947, Dylan's) - Great coffee & live acoustic music\nLocal Chemist: Gupta Medicos, Old Manali (+91 98160 12345)",
    note: "Thank you for respecting our home and supporting local Himalayan tourism."
  };

  let propertyProfile = { ...defaultProfile };
  try {
    const saved = localStorage.getItem('hm_property_profile');
    if (saved) propertyProfile = { ...defaultProfile, ...JSON.parse(saved) };
  } catch(e) {}

  // State variables
  let activeView = 'prompts';
  let activeCategory = 'All prompts';
  let searchTerm = '';
  let isPersonalizeActive = false;
  let globalLang = 'hinglish'; // Default to Hinglish as requested!
  let activeTemplate = 'welcome';
  let displayedLimit = 40; // Chunked rendering for speed

  // Per-card language preferences override
  let cardLangOverrides = {};

  // Utilities
  function escapeHTML(v) {
    return String(v ?? '').replace(/[&<>"']/g, c => ({
      '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;'
    }[c]));
  }

  function toast(message) {
    const t = $('#hm-toast');
    if (!t) return;
    t.textContent = message;
    t.classList.add('hm-show');
    clearTimeout(t._timeout);
    t._timeout = setTimeout(() => t.classList.remove('hm-show'), 2400);
  }

  async function copyText(text) {
    try {
      if (navigator.clipboard && navigator.clipboard.writeText) {
        await navigator.clipboard.writeText(text);
        toast('Copied to clipboard ✓');
        return true;
      }
    } catch (e) {}
    try {
      const ta = document.createElement('textarea');
      ta.value = text;
      ta.setAttribute('readonly', '');
      ta.style.position = 'fixed';
      ta.style.opacity = '0';
      ta.style.left = '-9999px';
      document.body.appendChild(ta);
      ta.focus();
      ta.select();
      const ok = document.execCommand('copy');
      ta.remove();
      if (ok) {
        toast('Copied to clipboard ✓');
        return true;
      }
    } catch (e) {}
    toast('Copy blocked. Select and copy manually.');
    return false;
  }

  // Personalization engine
  function personalizePromptText(text) {
    if (!text) return '';
    let p = text;
    const prof = propertyProfile;
    p = p.replace(/\[flat\/studio\/villa\/homestay\/farmhouse\/room\]/gi, prof.type || "Homestay");
    p = p.replace(/\[property type\]/gi, prof.type || "Homestay");
    p = p.replace(/\[property\/type\]/gi, prof.type || "Homestay");
    p = p.replace(/\[type\]/gi, prof.type || "Homestay");
    p = p.replace(/\[location\]/gi, prof.city || "Manali, Himachal Pradesh");
    p = p.replace(/\[city\/area\]/gi, prof.city || "Manali, Himachal Pradesh");
    p = p.replace(/\[area\/city\]/gi, prof.city || "Manali, Himachal Pradesh");
    p = p.replace(/\[city\]/gi, prof.city || "Manali");
    p = p.replace(/\[area\]/gi, prof.city || "Manali");
    p = p.replace(/\[property name\]/gi, prof.name || "Our Homestay");
    p = p.replace(/\[stay name\]/gi, prof.name || "Our Homestay");
    p = p.replace(/\[name\]/gi, prof.host || "Host");
    p = p.replace(/\[host name\]/gi, prof.host || "Host");
    p = p.replace(/\[name\/host brand\]/gi, prof.host || "Host");
    p = p.replace(/\[host\]/gi, prof.host || "Host");
    p = p.replace(/\[amenities\]/gi, prof.amenities || "Wi-Fi, Mountain View, Kitchen");
    p = p.replace(/\[verified amenity list\]/gi, prof.amenities || "Wi-Fi, Mountain View, Kitchen");
    p = p.replace(/\[target guest\]/gi, prof.guests || "Couples & Families");
    p = p.replace(/\[guest segment\]/gi, prof.guests || "Couples & Families");
    p = p.replace(/\[target guests\]/gi, prof.guests || "Couples & Families");
    p = p.replace(/\[best-fit guest\]/gi, prof.guests || "Couples & Families");
    return p;
  }

  function highlightPlaceholders(text) {
    return escapeHTML(text).replace(/\[(.*?)\]/g, '<span class="hm-highlight-var">[$1]</span>');
  }

  // Update counts
  function updateCounters() {
    const totalEl = $('#hm-total-prompts-count');
    if (totalEl) totalEl.textContent = String(prompts.length) + '+';
    const topFavEl = $('#top-fav-count');
    if (topFavEl) topFavEl.textContent = String(savedPrompts.size);
    const sideFavEl = $('#sidebar-fav-count');
    if (sideFavEl) sideFavEl.textContent = String(savedPrompts.size);
    const profileBtn = $('#btn-open-profile');
    if (profileBtn && propertyProfile.name) {
      profileBtn.innerHTML = '🏠 ' + escapeHTML(propertyProfile.name.split(' ')[0]) + ' Stay';
    }
  }

  // Navigation & View switching
  function showView(name) {
    activeView = name;
    $$('.hm-view').forEach(v => v.classList.toggle('hm-active', v.dataset.view === name));
    $$('.hm-tab-btn').forEach(b => b.setAttribute('aria-selected', String(b.dataset.tab === name)));
    $$('.hm-mbar-btn').forEach(b => b.classList.toggle('hm-active', b.dataset.tab === name));

    if (name === 'guest') renderSheet();
    if (name === 'growth') calculateAudit();
    if (name === 'resources') calculatePricing();

    window.scrollTo({ top: 0, behavior: 'smooth' });
  }

  $$('[data-tab]').forEach(b => b.addEventListener('click', () => showView(b.dataset.tab)));
  $$('[data-go]').forEach(b => b.addEventListener('click', () => showView(b.dataset.go)));

  // Categories list
  const categoryNames = Array.from(new Set(prompts.map(p => p.category))).sort();

  function renderCategories() {
    const holder = $('#hm-categories-list');
    if (!holder) return;
    holder.innerHTML = '';

    // "All prompts" button
    const allBtn = document.createElement('button');
    allBtn.className = 'hm-cat-btn';
    allBtn.setAttribute('aria-pressed', String(activeCategory === 'All prompts'));
    allBtn.innerHTML = '<span>✦ All Prompts</span><span class="hm-cat-count">' + prompts.length + '</span>';
    allBtn.addEventListener('click', () => {
      activeCategory = 'All prompts';
      displayedLimit = 40;
      renderCategories();
      renderPrompts();
    });
    holder.appendChild(allBtn);

    // "⭐ Saved / Favourites" button
    const favBtn = document.createElement('button');
    favBtn.className = 'hm-cat-btn';
    favBtn.setAttribute('aria-pressed', String(activeCategory === 'favorites'));
    favBtn.innerHTML = '<span>⭐ Saved / Favourites</span><span class="hm-cat-count" id="sidebar-fav-count">' + savedPrompts.size + '</span>';
    favBtn.addEventListener('click', () => {
      activeCategory = 'favorites';
      displayedLimit = 100;
      renderCategories();
      renderPrompts();
    });
    holder.appendChild(favBtn);

    // Individual category buttons
    categoryNames.forEach(cat => {
      const count = prompts.filter(p => p.category === cat).length;
      const b = document.createElement('button');
      b.className = 'hm-cat-btn';
      b.setAttribute('aria-pressed', String(activeCategory === cat));
      b.innerHTML = '<span>' + escapeHTML(cat) + '</span><span class="hm-cat-count">' + count + '</span>';
      b.addEventListener('click', () => {
        activeCategory = cat;
        displayedLimit = 40;
        renderCategories();
        renderPrompts();
      });
      holder.appendChild(b);
    });
  }

  function getFilteredPrompts() {
    return prompts.filter(p => {
      if (activeCategory === 'favorites') {
        if (!savedPrompts.has(p.id)) return false;
      } else if (activeCategory !== 'All prompts' && p.category !== activeCategory) {
        return false;
      }
      if (searchTerm) {
        const hay = [p.title, p.category, p.description, p.prompt, p.prompt_hinglish || '', p.tags].join(' ').toLowerCase();
        if (!hay.includes(searchTerm)) return false;
      }
      return true;
    });
  }

  function renderPrompts() {
    const list = getFilteredPrompts();
    const grid = $('#hm-prompt-grid');
    const resultCountEl = $('#hm-result-count');
    if (!grid) return;
    grid.innerHTML = '';

    const visibleList = list.slice(0, displayedLimit);

    if (resultCountEl) {
      resultCountEl.textContent = `Showing ${visibleList.length} of ${list.length} prompts (Total Library: ${prompts.length})`;
    }

    if (!list.length) {
      grid.innerHTML = '<div style="grid-column:1/-1;background:#fff;border:1px dashed var(--hm-line);border-radius:16px;padding:36px;text-align:center;color:var(--hm-muted);"><div style="font-size:28px;margin-bottom:8px">🔍</div><b>No prompts matched your search</b><p style="font-size:12px;margin:4px 0 0">Try searching another keyword or select "All Prompts".</p></div>';
      return;
    }

    const frag = document.createDocumentFragment();
    visibleList.forEach(p => {
      const card = document.createElement('article');
      card.className = 'hm-pcard';
      const isStarred = savedPrompts.has(p.id);

      // Determine language for this card: override > globalLang
      const cardLang = cardLangOverrides[p.id] || globalLang;
      const rawPrompt = (cardLang === 'hinglish' && p.prompt_hinglish) ? p.prompt_hinglish : p.prompt;

      const displayText = isPersonalizeActive ? personalizePromptText(rawPrompt) : rawPrompt;
      const formattedBox = isPersonalizeActive ? escapeHTML(displayText) : highlightPlaceholders(displayText);

      card.innerHTML = `
        <div class="hm-pcard-header">
          <span class="hm-pill-cat">✦ ${escapeHTML(p.category)}</span>
          <div style="display:flex;align-items:center;gap:6px">
            <div class="hm-card-lang-toggle" data-card-id="${escapeHTML(p.id)}">
              <button class="hm-card-lang-btn ${cardLang === 'hinglish' ? 'hm-active' : ''}" data-set-lang="hinglish">🇮🇳 Hinglish</button>
              <button class="hm-card-lang-btn ${cardLang === 'en' ? 'hm-active' : ''}" data-set-lang="en">🇬🇧 English</button>
            </div>
            <button class="hm-pcard-fav ${isStarred ? 'hm-starred' : ''}" data-fav="${escapeHTML(p.id)}" title="${isStarred ? 'Remove favorite' : 'Save prompt'}">★</button>
          </div>
        </div>
        <h3>${escapeHTML(p.title)}</h3>
        <p class="hm-pcard-desc">${escapeHTML(p.description)}</p>
        <div class="hm-pcard-box">${formattedBox}</div>
        <div class="hm-pcard-tags">
          ${String(p.tags || '').split(',').map(t => `<span class="hm-tag-item">${escapeHTML(t.trim())}</span>`).join('')}
        </div>
        <div class="hm-pcard-how">
          <strong>💡 Hinglish Usage Guide:</strong> Is prompt ko copy karke seedha ChatGPT ya Gemini me paste karo. Agar ⚡ Auto-Personalize ON hai to aapki real property details already filled hain. AI ko best output ke liye bolo: <i>"Natural conversational tone me likhein, koi jhooth ya fake promises na karein."</i>
        </div>
        <div class="hm-pcard-actions">
          <button class="hm-btn hm-btn-primary hm-btn-sm" data-copy-prompt="${escapeHTML(p.id)}">📋 Copy (${cardLang === 'hinglish' ? 'Hinglish' : 'English'})</button>
          <button class="hm-btn hm-btn-soft hm-btn-sm" data-personalize-prompt="${escapeHTML(p.id)}">⚡ Personalize</button>
          <button class="hm-btn hm-btn-outline hm-btn-sm" data-toggle-how>💡 Tips</button>
        </div>
      `;

      // Copy Button
      card.querySelector('[data-copy-prompt]').addEventListener('click', () => {
        copyText(displayText);
      });

      // Language Switcher on card
      card.querySelectorAll('[data-set-lang]').forEach(btn => {
        btn.addEventListener('click', (e) => {
          cardLangOverrides[p.id] = e.currentTarget.dataset.setLang;
          renderPrompts();
        });
      });

      // Favorite toggle
      card.querySelector('[data-fav]').addEventListener('click', (e) => {
        if (savedPrompts.has(p.id)) {
          savedPrompts.delete(p.id);
          e.currentTarget.classList.remove('hm-starred');
          toast('Removed from saved prompts');
        } else {
          savedPrompts.add(p.id);
          e.currentTarget.classList.add('hm-starred');
          toast('Saved to Favourites ⭐');
        }
        try {
          localStorage.setItem('hm_saved_prompts', JSON.stringify(Array.from(savedPrompts)));
        } catch(err) {}
        updateCounters();
        if (activeCategory === 'favorites') renderPrompts();
      });

      // Personalize prompt modal open
      card.querySelector('[data-personalize-prompt]').addEventListener('click', () => {
        openPersonalizeModal(p, cardLang);
      });

      // Tips toggle
      card.querySelector('[data-toggle-how]').addEventListener('click', (e) => {
        const howBox = card.querySelector('.hm-pcard-how');
        howBox.classList.toggle('hm-open');
        e.currentTarget.textContent = howBox.classList.contains('hm-open') ? 'Hide tips' : '💡 Tips';
      });

      frag.appendChild(card);
    });
    grid.appendChild(frag);

    // Load More Row
    const loadMoreRow = $('#hm-load-more-container');
    if (loadMoreRow) {
      if (displayedLimit < list.length) {
        loadMoreRow.style.display = 'flex';
        loadMoreRow.querySelector('button').textContent = `⚡ Load More Prompts (Showing ${visibleList.length} of ${list.length})`;
      } else {
        loadMoreRow.style.display = 'none';
      }
    }
  }

  // Load More Button Listener
  $('#btn-load-more')?.addEventListener('click', () => {
    displayedLimit += 40;
    renderPrompts();
  });

  // Global Language Switcher Listener
  $$('.hm-lang-opt').forEach(btn => {
    btn.addEventListener('click', (e) => {
      $$('.hm-lang-opt').forEach(b => b.classList.remove('hm-active'));
      e.currentTarget.classList.add('hm-active');
      globalLang = e.currentTarget.dataset.lang;
      cardLangOverrides = {}; // Reset overrides to follow global
      renderPrompts();
      toast(globalLang === 'hinglish' ? 'Hinglish Mode Activated 🇮🇳' : 'English Mode Activated 🇬🇧');
    });
  });

  // Search input listeners
  const searchInput = $('#hm-lib-search');
  if (searchInput) {
    searchInput.addEventListener('input', e => {
      searchTerm = e.target.value.trim().toLowerCase();
      displayedLimit = 40;
      renderPrompts();
    });
  }

  // Hero search listener
  const heroSearch = $('#hm-hero-search-input');
  if (heroSearch) {
    heroSearch.addEventListener('input', e => {
      searchTerm = e.target.value.trim().toLowerCase();
      if (searchInput) searchInput.value = e.target.value;
      if (activeView !== 'prompts') showView('prompts');
      displayedLimit = 40;
      renderPrompts();
    });
  }

  // Toggle Auto-Personalize
  const togglePersonalize = $('#hm-toggle-personalize-chk');
  if (togglePersonalize) {
    togglePersonalize.addEventListener('change', e => {
      isPersonalizeActive = e.target.checked;
      renderPrompts();
      toast(isPersonalizeActive ? 'Personalized with your Property Profile ⚡' : 'Showing master prompts with placeholders');
    });
  }

  // Copy visible pack button
  const copyPackBtn = $('#hm-copy-visible-pack');
  if (copyPackBtn) {
    copyPackBtn.addEventListener('click', () => {
      const list = getFilteredPrompts();
      if (!list.length) {
        toast('No prompts to copy.');
        return;
      }
      const text = list.map(p => {
        const raw = (globalLang === 'hinglish' && p.prompt_hinglish) ? p.prompt_hinglish : p.prompt;
        const pt = isPersonalizeActive ? personalizePromptText(raw) : raw;
        return `### ${p.title} (${p.category})\n${pt}`;
      }).join('\n\n---\n\n');
      copyText(text);
    });
  }

  // ==========================================
  // 10,000+ COMBINATIONS PROMPT MATRIX GENERATOR
  // ==========================================
  function generateMatrixPrompt() {
    const dest = $('#mat-dest')?.value || "Manali, Himachal Pradesh";
    const ptype = $('#mat-type')?.value || "Mountain Homestay / Pine Cabin";
    const aud = $('#mat-aud')?.value || "Romantic Couples & Honeymooners";
    const goal = $('#mat-goal')?.value || "Viral 15-Second Aesthetic Reel Script";
    const lang = $('#mat-lang')?.value || "hinglish";

    let p = '';
    if (lang === 'hinglish') {
      p = `Act as an expert Indian Airbnb & Homestay growth strategist.
PROPERTY PROFILE:
- Type: ${ptype}
- Destination / City: ${dest}
- Target Traveller Segment: ${aud}
- Primary Marketing Goal: ${goal}
- Verified Amenities: ${propertyProfile.amenities || "Wi-Fi, Mountain/Scenic View, Private Balcony, Bonfire, Home Cooked Food"}
- Host Name: ${propertyProfile.host || "Host"}

TASK INSTRUCTIONS:
1. Generate an irresistible, high-converting ${goal} tailored specifically for ${aud} visiting ${dest}.
2. Hook: Provide 3 high-impact opening lines (Curiosity, Scenic Aesthetic, and Relatable Indian Travel).
3. Body / Breakdown: Step-by-step scene/script instructions with visual cues, camera angles, and text overlays.
4. Tone: Natural, hospitable conversational Hinglish (Indian English + Hindi touch) that feels authentic and trustworthy.
5. Trust & Accuracy: Mention real benefits (peace, hygiene, local food, power backup) without fake claims or exaggerated proximity.
6. Call-to-Action (CTA): Direct guests to check calendar availability on our Airbnb listing link in bio.`;
    } else {
      p = `Act as an expert Airbnb & boutique hospitality marketing strategist for India.
PROPERTY PROFILE:
- Property Type: ${ptype}
- Destination / City: ${dest}
- Best-Fit Guest Segment: ${aud}
- Objective: Create an outstanding, high-conversion ${goal}
- Confirmed Amenities: ${propertyProfile.amenities || "High-Speed Wi-Fi, Scenic Balcony View, Bonfire, Homemade Meals"}
- Host: ${propertyProfile.host || "Host"}

DELIVERABLES:
1. 3 Irresistible opening hooks tailored for ${aud} travelling to ${dest}.
2. Step-by-step script / copy structure formatted with scannable timestamps, on-screen text overlays, and audio direction.
3. Authentic Indian hospitality positioning highlighting comfort, cleanliness, and local cultural charm.
4. Clear call-to-action encouraging travelers to view available dates on Airbnb.
5. 5 targeted hashtags for the ${dest} travel niche.`;
    }

    const box = $('#hm-matrix-result-box');
    const pre = $('#hm-matrix-pre');
    if (box && pre) {
      pre.textContent = p;
      box.style.display = 'block';
    }
  }

  $('#btn-matrix-generate')?.addEventListener('click', generateMatrixPrompt);

  $('#btn-matrix-random')?.addEventListener('click', () => {
    // Randomize dropdowns
    function rand(id) {
      const el = $('#' + id);
      if (!el) return;
      const opts = el.options;
      el.selectedIndex = Math.floor(Math.random() * opts.length);
    }
    rand('mat-dest');
    rand('mat-type');
    rand('mat-aud');
    rand('mat-goal');
    generateMatrixPrompt();
    toast('Surprise combination generated! 🎲');
  });

  $('#btn-matrix-copy')?.addEventListener('click', () => {
    const text = $('#hm-matrix-pre')?.textContent;
    if (text) copyText(text);
  });

  // SECTION 2: INTERACTIVE LISTING AUDIT TOOL
  const auditQuestions = [
    { id: 'q1', text: 'Hero Cover Photo Quality', sub: 'Bright daylight shot of the main living space or standout mountain/pool view without wide-angle fisheye distortion' },
    { id: 'q2', text: 'Minimum 25+ Room-by-Room Photos', sub: 'Every bedroom, bathroom, kitchen, entrance, and parking verified with clean lighting' },
    { id: 'q3', text: 'Specific, Benefit-Driven Listing Title', sub: 'States key differentiator, distance to landmark, or workation/balcony feature (not generic "2BHK Luxury Flat")' },
    { id: 'q4', text: 'Accurate Sleeping Layout Specified', sub: 'Exact bed sizes (King/Queen), extra mattresses, linens, and room capacities clearly disclosed' },
    { id: 'q5', text: 'Dedicated Workation Setup Disclosed', sub: 'Speed-tested Wi-Fi screenshot (50+ Mbps), ergonomic desk/chair, and inverter/power backup status' },
    { id: 'q6', text: 'Clear Property Constraints & Limitations', sub: 'Number of stairs, lift availability, parking dimensions, quiet hours, and pet restrictions openly stated' },
    { id: 'q7', text: 'Friendly, Enforceable House Rules', sub: 'Warm and welcoming tone covering quiet hours, outside visitors policy, and smoking areas' },
    { id: 'q8', text: 'Pre-Booking Guest FAQs Section', sub: 'Answers top 5 questions (cook availability, grocery delivery, early check-in, heater/AC charges)' },
    { id: 'q9', text: 'Realistic Local Distances', sub: 'Real driving and walking minutes to railway station, airport, and tourist spots (no exaggerated claims)' },
    { id: 'q10', text: 'Dynamic Pricing Strategy', sub: 'Different rates for weekdays vs weekends, plus festive season & long-weekend price adjustments' }
  ];

  let auditAnswers = {};
  try {
    const saved = localStorage.getItem('hm_audit_answers');
    if (saved) auditAnswers = JSON.parse(saved);
  } catch(e) {}

  function renderAuditQuestions() {
    const container = $('#hm-audit-questions-list');
    if (!container) return;
    container.innerHTML = '';

    auditQuestions.forEach((q, idx) => {
      const val = auditAnswers[q.id] || 'partial';
      const item = document.createElement('div');
      item.className = 'hm-audit-item';
      item.innerHTML = `
        <div class="hm-audit-q">
          ${idx + 1}. ${escapeHTML(q.text)}
          <small>${escapeHTML(q.sub)}</small>
        </div>
        <div class="hm-audit-options">
          <label><input type="radio" name="${q.id}" value="yes" ${val === 'yes' ? 'checked' : ''}> Yes (+10)</label>
          <label><input type="radio" name="${q.id}" value="partial" ${val === 'partial' ? 'checked' : ''}> Partial (+5)</label>
          <label><input type="radio" name="${q.id}" value="no" ${val === 'no' ? 'checked' : ''}> No (+0)</label>
        </div>
      `;
      item.querySelectorAll('input[type="radio"]').forEach(r => {
        r.addEventListener('change', (e) => {
          auditAnswers[q.id] = e.target.value;
          try {
            localStorage.setItem('hm_audit_answers', JSON.stringify(auditAnswers));
          } catch(err) {}
          calculateAudit();
        });
      });
      container.appendChild(item);
    });
  }

  function calculateAudit() {
    let score = 0;
    const failedItems = [];
    auditQuestions.forEach(q => {
      const val = auditAnswers[q.id] || 'partial';
      if (val === 'yes') score += 10;
      else if (val === 'partial') {
        score += 5;
        failedItems.push({ text: q.text, tip: 'Optimize: ' + q.sub });
      } else {
        failedItems.push({ text: q.text, tip: 'High Priority: ' + q.sub });
      }
    });

    const digitEl = $('#hm-audit-score-digit');
    if (digitEl) digitEl.textContent = String(score);

    const badgeEl = $('#hm-audit-badge');
    if (badgeEl) {
      if (score >= 80) {
        badgeEl.textContent = '⭐ Superhost Ready Listing';
        badgeEl.style.background = '#d8f3dc';
        badgeEl.style.color = '#0f3e30';
      } else if (score >= 50) {
        badgeEl.textContent = '🟡 Good Foundation (Key Gaps to Fix)';
        badgeEl.style.background = '#fef5ea';
        badgeEl.style.color = '#8c5b00';
      } else {
        badgeEl.textContent = '🚨 Needs Optimization to Win Bookings';
        badgeEl.style.background = '#fff0f1';
        badgeEl.style.color = '#c0392b';
      }
    }

    const actionList = $('#hm-audit-action-items');
    if (actionList) {
      actionList.innerHTML = '';
      if (!failedItems.length) {
        actionList.innerHTML = '<div style="color:var(--hm-accent-dark);font-size:13px;font-weight:700">🎉 Outstanding! Your listing follows all best practices. Keep photos and pricing refreshed regularly.</div>';
      } else {
        failedItems.forEach(item => {
          const row = document.createElement('div');
          row.className = 'hm-check-row';
          row.innerHTML = `
            <input type="checkbox">
            <div>
              <b style="color:var(--hm-primary)">${escapeHTML(item.text)}</b>
              <div style="color:var(--hm-muted);font-size:11.5px">${escapeHTML(item.tip)}</div>
            </div>
          `;
          actionList.appendChild(row);
        });
      }
    }
  }

  // SECTION 3: SOCIAL MEDIA STUDIO
  const viralHooksData = [
    { cat: 'Aesthetic', text: 'POV: Waking up to chirping birds, misty mountain air, and fresh chai on this private balcony...' },
    { cat: 'Aesthetic', text: 'This corner of our homestay during golden hour is proof that heaven is a place on earth.' },
    { cat: 'Curiosity', text: 'The #1 mistake people make when booking a stay in [city] (and how to avoid it)...' },
    { cat: 'Curiosity', text: '3 hidden things you get in an authentic homestay that luxury hotels can never give you.' },
    { cat: 'Value', text: 'Why pay ₹8,000 for a cramped hotel room when you can rent this entire 2-bedroom villa for less?' },
    { cat: 'Value', text: 'The ultimate workation hack in [city]: 100 Mbps Wi-Fi, mountain view, and home-cooked meals under ₹...' },
    { cat: 'Hospitality', text: 'When our guests arrive tired after a 6-hour road trip, this is the welcome chai we brew for them...' },
    { cat: 'Hospitality', text: 'Behind the scenes: How we deep clean and stage every room before our next guests arrive.' },
    { cat: 'Local', text: 'Skip the crowded tourist spots! Here are 4 secret local cafes within 10 mins of our stay.' },
    { cat: 'Local', text: 'What 24 hours of slow living looks like in [city] when you stay with us.' },
    { cat: 'Weekend', text: 'Tag the friends who owe you a long-weekend getaway to this scenic farmhouse...' },
    { cat: 'Weekend', text: 'Only 3 hours drive from [capital city] — your weekend recharge starts right here.' },
    { cat: 'Curiosity', text: 'Is this the coziest hidden homestay in [city]? Tour with me!' },
    { cat: 'Aesthetic', text: 'Rainy days hit completely different when you are watching the raindrops from this window.' },
    { cat: 'Value', text: '5 free amenities our homestay includes that most hotels charge extra for.' }
  ];

  function renderViralHooks(filterCat = 'All') {
    const list = $('#hm-hooks-list');
    if (!list) return;
    list.innerHTML = '';
    const filtered = filterCat === 'All' ? viralHooksData : viralHooksData.filter(h => h.cat === filterCat);

    filtered.forEach(h => {
      const pText = personalizePromptText(h.text);
      const row = document.createElement('div');
      row.className = 'hm-hook-item';
      row.innerHTML = `
        <div>
          <span style="font-size:10px;font-weight:800;color:var(--hm-accent-dark);background:#eef7ed;padding:2px 6px;border-radius:4px;margin-right:6px">${escapeHTML(h.cat)}</span>
          <span>${escapeHTML(pText)}</span>
        </div>
        <button class="hm-btn hm-btn-primary hm-btn-sm" data-copy-hook>Copy Hook</button>
      `;
      row.querySelector('[data-copy-hook]').addEventListener('click', () => copyText(pText));
      list.appendChild(row);
    });
  }
  window.renderViralHooksInternal = renderViralHooks;

  // SECTION 4: GUEST COMMUNICATION TOOLKIT
  const guestMessagesData = [
    {
      id: 'm1',
      title: 'Booking Confirmation & Welcome',
      en: "Hello [Guest Name]! Thank you for booking your stay at [Property Name]. We are delighted to host you. Check-in is at [Check-in Time]. Please let us know your expected arrival time so we can prepare your welcome tea!",
      hinglish: "Namaste [Guest Name] ji! [Property Name] me aapki booking confirm ho gayi hai. Hume aapko host karke bohot khushi hogi. Check-in ka time [Check-in Time] se hai. Kripya apna approximate arrival time share karein taaki hum aapke welcome ki tayari kar sakein!",
      hi: "नमस्ते [Guest Name] जी! [Property Name] में आपका स्वागत है। आपकी बुकिंग की पुष्टि हो गई है। चेक-इन का समय [Check-in Time] है। कृपया अपने पहुंचने का अनुमानित समय बताएं ताकि हम सब तैयारी कर सकें।"
    },
    {
      id: 'm2',
      title: 'Pre-Arrival Driving & Landmarks',
      en: "Hi [Guest Name], here are the directions to reach [Property Name] in [City]: Take the main highway towards [Landmark]. Our gate is 200m ahead on the left. If you need any assistance on the road, call host at [Host Contact]. Safe travels!",
      hinglish: "Hi [Guest Name]! [Property Name] pahunchne ka aasan route yeh hai: Main highway se [Landmark] ki taraf turn lijiye, wahan se 200m aage left side hamara gate hai. Raste me koi bhi confusion ho toh host ko [Host Contact] par call kar sakte hain. Shubh yatra!",
      hi: "नमस्ते [Guest Name], [Property Name] पहुंचने के लिए: [Landmark] की तरफ मुड़ें, 200 मीटर आगे बाईं ओर हमारा गेट है। कोई भी परेशानी होने पर [Host Contact] पर संपर्क करें।"
    },
    {
      id: 'm3',
      title: 'Self Check-in & Key Instructions',
      en: "Welcome to [Property Name]! Your keys are placed in the lockbox beside the front door. The passcode is [FILL PRIVATE CODE]. Please dial [Host Contact] once you enter so we can ensure everything is perfect.",
      hinglish: "Welcome to [Property Name]! Main door ke paas lockbox me aapki keys rakhi hui hain. Passcode hai [FILL PRIVATE CODE]. Ghar me enter karke please hume [Host Contact] par ek message kar dein taaki hum ensure karein aap comfortable hain.",
      hi: "स्वागत है! मुख्य दरवाजे के पास लॉकबॉक्स में चाबियां हैं। कोड [FILL PRIVATE CODE] है। अंदर पहुंचकर कृपया [Host Contact] पर सूचित करें।"
    },
    {
      id: 'm4',
      title: 'Wi-Fi & House Rules Reminder',
      en: "We hope you are settling in well! Wi-Fi: [Wi-Fi Network] | Password: [Wi-Fi Password]. A quick reminder that quiet hours start at 10:30 PM. Please switch off AC/heaters when stepping out. Enjoy your stay!",
      hinglish: "Asha hai aap aaram se settle ho gaye honge! Wi-Fi: [Wi-Fi Network] | Password: [Wi-Fi Password]. Ek chhota sa request hai ki 10:30 PM ke baad shanti banaye rakhein. Bahar jaate waqt AC/heater switch off kar dein. Have a lovely stay!",
      hi: "आशा है आप आराम से पहुंच गए होंगे। वाई-फाई: [Wi-Fi Network] | पासवर्ड: [Wi-Fi Password]। कृपया रात 10:30 के बाद शांति बनाए रखें। बाहर जाते समय एसी/हीटर बंद रखें।"
    },
    {
      id: 'm5',
      title: 'Mid-Stay Check-in (Everything comfortable?)',
      en: "Hi [Guest Name], just checking in! Is the stay comfortable? Do you need fresh towels, extra blankets, or local dining recommendations for tonight? We are just a message away.",
      hinglish: "Hi [Guest Name] ji, bas check karne ke liye message kiya ki sab theek chal raha hai na? Kya aapko fresh towels, extra blanket ya aaj raat ke liye koi badhiya restaurant ka suggestion chahiye? Hume zaroor batayein!",
      hi: "नमस्ते [Guest Name] जी, क्या सब कुछ आरामदायक है? क्या आपको ताज़े तौलिये या रात के खाने के लिए किसी सुझाव की ज़रूरत है? हमें ज़रूर बताएं।"
    },
    {
      id: 'm6',
      title: 'Issue: Power Cut / Inverter Backup Active',
      en: "Dear [Guest Name], there is a temporary grid power cut in our area. Our inverter backup is running the lights, fans, and Wi-Fi. Heavy appliances (AC/geysers) will resume once grid power returns (expected in ~30 mins). We apologize for the inconvenience!",
      hinglish: "Dear [Guest Name], area me temporary power cut hua hai. Hamara inverter backup currently lights, fans aur Wi-Fi chala raha hai. AC aur geyser power aate hi resume ho jayenge (approx 30 mins). Asuvidha ke liye maafi chahte hain!",
      hi: "प्रिय अतिथि, क्षेत्र में बिजली कटौती हुई है। इन्वर्टर से पंखे, लाइट और वाई-फाई चालू हैं। बिजली आते ही एसी और गीज़र शुरू हो जाएंगे। असुविधा के लिए खेद है।"
    },
    {
      id: 'm7',
      title: 'Issue: Wi-Fi Down / Slow Internet',
      en: "Hi [Guest Name], we notice the Wi-Fi connection is momentarily slow due to a provider cable maintenance. We have restarted the router and lodged an urgent ticket with the ISP. We are monitoring this closely for you.",
      hinglish: "Hi [Guest Name], provider ki maintenance ki wajah se Wi-Fi thoda slow chal raha hai. Humne router restart kar diya hai aur provider ko urgent complaint lodge kar di hai. Hum isse closely monitor kar rahe hain.",
      hi: "नमस्ते, इंटरनेट सेवा प्रदाता के रख-रखाव के कारण वाई-फाई धीमा है। हमने राउटर रीस्टार्ट किया है और शिकायत दर्ज कराई है। हम जल्द समाधान कर रहे हैं।"
    },
    {
      id: 'm8',
      title: 'Early Check-in / Late Checkout Response',
      en: "Hi [Guest Name], while our standard checkout is [Checkout Time] due to incoming cleaning schedules, we are happy to offer a late checkout until [Time] / luggage storage in the common lobby. Let us know what suits you!",
      hinglish: "Hi [Guest Name] ji! Cleaning schedule ki wajah se standard checkout [Checkout Time] rehta hai, lekin hum aapko [Time] tak late checkout ya reception par luggage store karne ki facility provide kar sakte hain. Please batayein kya sahi rahega!",
      hi: "नमस्ते, सफाई के कारण सामान्य चेकआउट [Checkout Time] है, लेकिन हम आपके लिए [Time] तक चेकआउट या सामान रखने की सुविधा दे सकते हैं।"
    },
    {
      id: 'm9',
      title: 'Checkout Reminder & Key Drop',
      en: "Good morning [Guest Name]! A reminder that checkout is at [Checkout Time]. Please ensure all room heaters/ACs are off and leave the keys with our caretaker or inside the keybox. We wish you safe travels ahead!",
      hinglish: "Good morning [Guest Name] ji! Aaj checkout ka time [Checkout Time] hai. Kripya ensure karein ki heaters aur AC off hain, aur keys caretaker ko hand over kar dein ya keybox me drop kar dein. Aapki aage ki yatra mangalmay ho!",
      hi: "शुभ प्रभात! चेकआउट का समय [Checkout Time] है। कृपया सभी लाइट/एसी बंद कर दें और चाबी केयरटेकर को सौंप दें। सुरक्षित यात्रा की शुभकामनाएं!"
    },
    {
      id: 'm10',
      title: 'Post-Stay Warm Thank You Message',
      en: "Dear [Guest Name], thank you so much for choosing [Property Name] and treating our home with such care! It was an absolute pleasure hosting you. We hope to welcome you back whenever you visit [City] next.",
      hinglish: "Dear [Guest Name] ji, [Property Name] ko choose karne aur ghar ko itne pyaar aur care ke saath rakhne ke liye dil se shukriya! Aapko host karke bohot accha laga. Agli baar jab bhi [City] aayein, zaroor batayein!",
      hi: "प्रिय अतिथि, [Property Name] में रुकने और हमारे घर का ध्यान रखने के लिए बहुत-बहुत धन्यवाद! आपको होस्ट करके बेहद खुशी हुई। दोबारा ज़रूर पधारें!"
    },
    {
      id: 'm11',
      title: '5-Star Review Request (Platform Compliant)',
      en: "Hi [Guest Name], reviews help independent homestays like ours immensely. If you enjoyed your time at [Property Name], we would be truly grateful if you could take 60 seconds to share your 5-star experience on Airbnb. Thank you!",
      hinglish: "Hi [Guest Name] ji! Hamare jaise independent homestay ke liye guest reviews bohot important hote hain. Agar aapko hamari service aur stay pasand aaya ho, toh please Airbnb par apna 5-star review aur feedback zaroor share karein. Bohot bohot dhanyawaad!",
      hi: "नमस्ते, आपके 5-स्टार रिव्यू से हमारे जैसे होमस्टे को बहुत मदद मिलती है। यदि आपको हमारा आतिथ्य पसंद आया, तो कृपया Airbnb पर अपना अनुभव साझा करें। धन्यवाद!"
    },
    {
      id: 'm12',
      title: 'Resolving a Complaint Calmly',
      en: "Dear [Guest Name], I am sincerely sorry to hear about this issue. Your comfort is our top priority. Our caretaker is heading over to resolve this immediately. Thank you for your patience while we fix this for you.",
      hinglish: "Dear [Guest Name], is problem ke baare me jaan kar bohot khed hua. Aapka comfort hamari sabse badi priority hai. Hamare caretaker abhi turant aakar isse theek kar rahe hain. Please thoda sa samay dein, hum isse abhi resolve karte hain.",
      hi: "प्रिय अतिथि, असुविधा के लिए हमें गहरा खेद है। आपका आराम हमारी प्राथमिकता है। हमारे केयरटेकर इसे तुरंत ठीक करने आ रहे हैं। धैर्य के लिए धन्यवाद।"
    }
  ];

  function renderGuestMessages() {
    const grid = $('#hm-guest-messages-grid');
    if (!grid) return;
    grid.innerHTML = '';

    guestMessagesData.forEach(m => {
      const card = document.createElement('article');
      card.className = 'hm-msg-card';
      let currentLang = 'hinglish'; // Default to Hinglish for instant Indian relevance

      function getMsgText(lang) {
        let raw = m[lang] || m.en;
        return personalizePromptText(raw);
      }

      card.innerHTML = `
        <div style="display:flex;justify-content:space-between;align-items:center">
          <b style="font-size:14.5px;color:var(--hm-primary)">${escapeHTML(m.title)}</b>
          <div class="hm-lang-toggle-row">
            <button class="hm-lang-btn ${currentLang === 'hinglish' ? 'hm-active' : ''}" data-lang="hinglish">🇮🇳 Hinglish</button>
            <button class="hm-lang-btn ${currentLang === 'en' ? 'hm-active' : ''}" data-lang="en">🇬🇧 English</button>
            <button class="hm-lang-btn ${currentLang === 'hi' ? 'hm-active' : ''}" data-lang="hi">हिंदी</button>
          </div>
        </div>
        <div class="hm-msg-content">${escapeHTML(getMsgText(currentLang))}</div>
        <div style="display:flex;gap:8px;margin-top:auto">
          <button class="hm-btn hm-btn-primary hm-btn-sm" data-copy-msg>📋 Copy Message</button>
          <button class="hm-btn hm-btn-soft hm-btn-sm" data-wa-msg>💬 Send via WhatsApp</button>
        </div>
      `;

      const contentBox = card.querySelector('.hm-msg-content');
      card.querySelectorAll('.hm-lang-btn').forEach(btn => {
        btn.addEventListener('click', (e) => {
          card.querySelectorAll('.hm-lang-btn').forEach(b => b.classList.remove('hm-active'));
          e.currentTarget.classList.add('hm-active');
          currentLang = e.currentTarget.dataset.lang;
          contentBox.textContent = getMsgText(currentLang);
        });
      });

      card.querySelector('[data-copy-msg]').addEventListener('click', () => {
        copyText(contentBox.textContent);
      });

      card.querySelector('[data-wa-msg]').addEventListener('click', () => {
        const text = encodeURIComponent(contentBox.textContent);
        window.open('https://api.whatsapp.com/send?text=' + text, '_blank');
      });

      grid.appendChild(card);
    });
  }

  // WELCOME STUDIO RENDERER
  function renderSheet() {
    const sheet = $('#hm-print-sheet');
    if (!sheet) return;

    function f(id, def) {
      const el = $('#field-' + id);
      return (el && el.value.trim()) ? el.value.trim() : (propertyProfile[id] || def || '');
    }

    const prop = f('name', 'The Himalayan Pine Villa');
    const host = f('host', 'Rajesh & Aditi Sharma');
    const loc = f('city', 'Manali, Himachal Pradesh');
    const cin = f('checkin', 'After 2:00 PM');
    const cout = f('checkout', 'Before 11:00 AM');
    const wifi = f('wifi', 'PineVilla_Guest_5G');
    const pass = f('password', 'HimalayanPeace2026');
    const contact = f('contact', '+91 98765 43210 (WhatsApp)');
    const greeting = f('greeting', 'We are delighted to host you. Make yourself completely at home.');
    const rules = f('rules', 'Quiet hours from 10:30 PM.\nRegistered guests only.\nNo smoking indoors.');
    const steps = f('steps', 'Switch off geyser & heaters.\nReturn keys to caretaker.\nCheck for belongings.');
    const local = f('local', 'Local cafe 5 mins walk.\nMedicines & grocery 200m ahead.');
    const note = f('note', 'Wishing you a peaceful and rejuvenating stay!');

    let html = '';

    if (activeTemplate === 'welcome') {
      html = `
        <div class="hm-sheet-badge">Warmest Welcome To</div>
        <div class="hm-sheet-title">${escapeHTML(prop)}</div>
        <div class="hm-sheet-subtitle">${escapeHTML(loc)} · Hosted with love by ${escapeHTML(host)}</div>
        <div class="hm-sheet-divider"></div>
        <p style="font-size:12.5px;line-height:1.65;color:#283d34;margin:0 0 16px">${escapeHTML(greeting)}</p>
        <div class="hm-sheet-grid">
          <div class="hm-sheet-box">
            <div class="hm-sheet-lbl">CHECK-IN</div>
            <div class="hm-sheet-val">${escapeHTML(cin)}</div>
          </div>
          <div class="hm-sheet-box">
            <div class="hm-sheet-lbl">CHECKOUT</div>
            <div class="hm-sheet-val">${escapeHTML(cout)}</div>
          </div>
        </div>
        <div style="margin-top:10px" class="hm-sheet-grid">
          <div class="hm-sheet-box">
            <div class="hm-sheet-lbl">WI-FI NETWORK</div>
            <div class="hm-sheet-val">${escapeHTML(wifi)}</div>
          </div>
          <div class="hm-sheet-box">
            <div class="hm-sheet-lbl">WI-FI PASSWORD</div>
            <div class="hm-sheet-val">${escapeHTML(pass)}</div>
          </div>
        </div>
        <div class="hm-sheet-divider"></div>
        <div class="hm-sheet-box">
          <div class="hm-sheet-lbl">HOST ASSISTANCE & EMERGENCY</div>
          <div class="hm-sheet-val">${escapeHTML(contact)}</div>
        </div>
        <p style="font-size:11px;color:#677d71;margin-top:16px;text-align:center">${escapeHTML(note)}</p>
      `;
    } else if (activeTemplate === 'wifi') {
      html = `
        <div style="text-align:center;padding:18px 0">
          <div style="font-size:38px;margin-bottom:6px">📶</div>
          <div class="hm-sheet-badge">HIGH-SPEED IN-ROOM INTERNET</div>
          <div class="hm-sheet-title" style="font-size:30px">${escapeHTML(prop)}</div>
          <p class="hm-sheet-subtitle">Connect your devices and enjoy fast, uninterrupted Wi-Fi.</p>
          <div style="background:#f4f7f1;border:2px dashed #b8cebe;border-radius:12px;padding:16px;margin:18px 0;text-align:left">
            <div style="margin-bottom:12px">
              <span class="hm-sheet-lbl">NETWORK NAME</span>
              <div style="font-size:18px;font-weight:850;color:var(--hm-primary)">${escapeHTML(wifi)}</div>
            </div>
            <div>
              <span class="hm-sheet-lbl">PASSWORD</span>
              <div style="font-size:18px;font-weight:850;color:var(--hm-primary);font-family:monospace">${escapeHTML(pass)}</div>
            </div>
          </div>
          <p style="font-size:11.5px;color:#5a6e63">Having trouble connecting? Contact: <b>${escapeHTML(contact)}</b></p>
          <div style="font-size:10px;color:#8ba093;margin-top:20px">For registered guests only · ${escapeHTML(loc)}</div>
        </div>
      `;
    } else if (activeTemplate === 'rules') {
      const ruleLines = rules.split('\n').filter(Boolean);
      html = `
        <div class="hm-sheet-badge">Care & Respect</div>
        <div class="hm-sheet-title">House Guidelines</div>
        <p class="hm-sheet-subtitle">To ensure a peaceful and memorable stay for you and our neighbors at ${escapeHTML(prop)}.</p>
        <div class="hm-sheet-divider"></div>
        <ol style="padding-left:18px;margin:14px 0">
          ${ruleLines.map(r => `<li style="font-size:12.5px;line-height:1.6;margin-bottom:8px;color:#2c3e36">${escapeHTML(r)}</li>`).join('')}
        </ol>
        <div class="hm-sheet-divider"></div>
        <div class="hm-sheet-box">
          <div class="hm-sheet-lbl">QUESTIONS OR SUPPORT</div>
          <div class="hm-sheet-val">${escapeHTML(contact)}</div>
        </div>
        <p style="font-size:11px;color:#677d71;margin-top:14px">${escapeHTML(note)}</p>
      `;
    } else if (activeTemplate === 'checkout') {
      const stepLines = steps.split('\n').filter(Boolean);
      html = `
        <div class="hm-sheet-badge">Departure Information</div>
        <div class="hm-sheet-title">Checkout Checklist</div>
        <p class="hm-sheet-subtitle">Checkout Time: <b>${escapeHTML(cout)}</b> · ${escapeHTML(prop)}</p>
        <div class="hm-sheet-divider"></div>
        <div style="margin:16px 0">
          ${stepLines.map(s => `
            <div style="display:flex;align-items:flex-start;gap:10px;padding:8px 0;border-bottom:1px solid #edf1ea;font-size:12.5px">
              <span style="display:inline-block;width:16px;height:16px;border:1.5px solid #6b8275;border-radius:4px;margin-top:2px;flex-shrink:0"></span>
              <span>${escapeHTML(s)}</span>
            </div>
          `).join('')}
        </div>
        <div class="hm-sheet-divider"></div>
        <div class="hm-sheet-box">
          <div class="hm-sheet-lbl">KEY RETURN & QUESTIONS</div>
          <div class="hm-sheet-val">${escapeHTML(contact)}</div>
        </div>
        <p style="font-size:11px;color:#677d71;margin-top:16px;text-align:center">Thank you for staying with us! Safe travels ahead.</p>
      `;
    } else if (activeTemplate === 'local') {
      const recLines = local.split('\n').filter(Boolean);
      html = `
        <div class="hm-sheet-badge">Host Recommendations</div>
        <div class="hm-sheet-title">Local Experience Guide</div>
        <p class="hm-sheet-subtitle">Handpicked recommendations near ${escapeHTML(prop)}, ${escapeHTML(loc)}.</p>
        <div class="hm-sheet-divider"></div>
        <div style="margin:14px 0">
          ${recLines.map(r => `
            <div style="background:#f6f9f3;border-left:3px solid var(--hm-primary);border-radius:0 8px 8px 0;padding:8px 12px;margin-bottom:8px;font-size:12px;line-height:1.5">
              ${escapeHTML(r)}
            </div>
          `).join('')}
        </div>
        <div class="hm-sheet-divider"></div>
        <div class="hm-sheet-box">
          <div class="hm-sheet-lbl">LOCAL ASSISTANCE</div>
          <div class="hm-sheet-val">${escapeHTML(contact)}</div>
        </div>
        <p style="font-size:10.5px;color:#788c81;margin-top:14px">Please verify opening hours before heading out. Enjoy exploring!</p>
      `;
    }

    sheet.innerHTML = html;
  }

  // Populate form fields from profile
  function syncFormFromProfile() {
    const fields = ['name', 'host', 'city', 'checkin', 'checkout', 'wifi', 'password', 'contact', 'greeting', 'rules', 'steps', 'local', 'note'];
    fields.forEach(f => {
      const el = $('#field-' + f);
      if (el) el.value = propertyProfile[f] || '';
    });
    renderSheet();
  }

  // SECTION 5: NIGHTLY PRICING & EXPENSE CALCULATOR
  function calculatePricing() {
    const fixedRent = parseFloat($('#calc-fixed-rent')?.value || 25000);
    const fixedUtil = parseFloat($('#calc-fixed-util')?.value || 5000);
    const fixedStaff = parseFloat($('#calc-fixed-staff')?.value || 8000);
    const fixedOther = parseFloat($('#calc-fixed-other')?.value || 2000);

    const varLaundry = parseFloat($('#calc-var-laundry')?.value || 400);
    const varCleaning = parseFloat($('#calc-var-cleaning')?.value || 300);
    const varWelcome = parseFloat($('#calc-var-welcome')?.value || 200);

    const stayNights = parseFloat($('#calc-stay-nights')?.value || 2.5);
    const occupancyPct = parseFloat($('#calc-occupancy')?.value || 50);
    const targetProfit = parseFloat($('#calc-profit')?.value || 30000);

    const totalFixed = fixedRent + fixedUtil + fixedStaff + fixedOther;
    const bookedNights = Math.round((30 * occupancyPct) / 100);
    const numTurnovers = Math.max(1, Math.round(bookedNights / stayNights));
    const totalVariable = numTurnovers * (varLaundry + varCleaning + varWelcome);
    const totalExpenses = totalFixed + totalVariable;

    const breakEvenNightly = bookedNights > 0 ? Math.round(totalExpenses / bookedNights) : 0;
    const requiredNightly = bookedNights > 0 ? Math.round((totalExpenses + targetProfit) / bookedNights) : 0;

    const weekdayNights = Math.round(bookedNights * 0.73);
    const weekendNights = bookedNights - weekdayNights;
    const baseWeekday = Math.round((totalExpenses + targetProfit) / (weekdayNights + (weekendNights * 1.3)));
    const baseWeekend = Math.round(baseWeekday * 1.3);

    const airbnbFeeDeduction = Math.round(requiredNightly * 0.03);

    const beEl = $('#calc-out-breakeven');
    if (beEl) beEl.textContent = '₹' + breakEvenNightly.toLocaleString('en-IN');
    const recEl = $('#calc-out-target');
    if (recEl) recEl.textContent = '₹' + requiredNightly.toLocaleString('en-IN');
    const wdEl = $('#calc-out-weekday');
    if (wdEl) wdEl.textContent = '₹' + baseWeekday.toLocaleString('en-IN');
    const weEl = $('#calc-out-weekend');
    if (weEl) weEl.textContent = '₹' + baseWeekend.toLocaleString('en-IN');
    const expEl = $('#calc-out-expenses');
    if (expEl) expEl.textContent = '₹' + totalExpenses.toLocaleString('en-IN');
    const nightsEl = $('#calc-out-nights');
    if (nightsEl) nightsEl.textContent = bookedNights + ' nights (' + occupancyPct + '%)';
    const feeEl = $('#calc-out-fee');
    if (feeEl) feeEl.textContent = '₹' + airbnbFeeDeduction.toLocaleString('en-IN') + ' / night (3%)';
  }

  // 30-DAY ACTION PLAN CHECKLIST
  let actionPlanState = {};
  try {
    const saved = localStorage.getItem('hm_action_plan_checked');
    if (saved) actionPlanState = JSON.parse(saved);
  } catch(e) {}

  function initActionPlan() {
    const checkboxes = $$('[data-plan-task]');
    const total = checkboxes.length;
    if (!total) return;

    function updateProgress() {
      let done = 0;
      checkboxes.forEach(chk => {
        const id = chk.dataset.planTask;
        if (actionPlanState[id]) {
          chk.checked = true;
          done++;
        } else {
          chk.checked = false;
        }
      });
      const pct = Math.round((done / total) * 100);
      const bar = $('#hm-plan-progress-bar');
      if (bar) bar.style.width = pct + '%';
      const label = $('#hm-plan-progress-label');
      if (label) label.textContent = `${done} of ${total} Tasks Completed (${pct}%)`;
    }

    checkboxes.forEach(chk => {
      chk.addEventListener('change', (e) => {
        actionPlanState[e.target.dataset.planTask] = e.target.checked;
        try {
          localStorage.setItem('hm_action_plan_checked', JSON.stringify(actionPlanState));
        } catch(err) {}
        updateProgress();
      });
    });

    updateProgress();
  }

  // MODAL LOGIC
  function openModal(id) {
    const el = $('#' + id);
    if (el) el.classList.add('hm-open');
  }

  function closeModal(id) {
    const el = $('#' + id);
    if (el) el.classList.remove('hm-open');
  }

  $$('.hm-modal-close, [data-close-modal]').forEach(btn => {
    btn.addEventListener('click', () => {
      $$('.hm-modal-backdrop').forEach(m => m.classList.remove('hm-open'));
    });
  });

  // Profile Modal setup
  $('#btn-open-profile')?.addEventListener('click', () => {
    const fields = ['name', 'host', 'city', 'type', 'guests', 'amenities', 'checkin', 'checkout', 'wifi', 'password', 'contact'];
    fields.forEach(k => {
      const input = $('#modal-prof-' + k);
      if (input) input.value = propertyProfile[k] || '';
    });
    openModal('hm-modal-profile');
  });

  $('#btn-save-profile')?.addEventListener('click', () => {
    const fields = ['name', 'host', 'city', 'type', 'guests', 'amenities', 'checkin', 'checkout', 'wifi', 'password', 'contact'];
    fields.forEach(k => {
      const input = $('#modal-prof-' + k);
      if (input) propertyProfile[k] = input.value.trim();
    });
    try {
      localStorage.setItem('hm_property_profile', JSON.stringify(propertyProfile));
    } catch(err) {}
    updateCounters();
    syncFormFromProfile();
    renderPrompts();
    closeModal('hm-modal-profile');
    toast('Property Profile Saved & Applied ✓');
  });

  // Custom Prompt Generator Wizard
  $('#btn-open-wizard')?.addEventListener('click', () => openModal('hm-modal-wizard'));

  $('#btn-generate-wizard')?.addEventListener('click', () => {
    const pType = $('#wiz-type')?.value || 'Homestay';
    const pAud = $('#wiz-audience')?.value || 'Couples & Small Families';
    const pGoal = $('#wiz-goal')?.value || 'Instagram Reel Script';
    const pTone = $('#wiz-tone')?.value || 'Warm & Hospitable Indian Tone';

    const promptOutput = `Act as an expert Airbnb & short-term rental marketing consultant for Indian stays.
PROPERTY TYPE: ${pType}
STAY NAME & LOCATION: ${propertyProfile.name} in ${propertyProfile.city}
TARGET AUDIENCE: ${pAud}
MARKETING GOAL: Create high-converting ${pGoal}
TONE OF VOICE: ${pTone}
REAL AMENITIES: ${propertyProfile.amenities}
HOST DETAILS: Hosted by ${propertyProfile.host}

Please generate:
1. 3 High-converting hooks tailored for Indian travel segments
2. Step-by-step scene/script breakdown or copy draft
3. Clear call-to-action directing travellers to check dates on our Airbnb listing
4. 5 Niche-specific hashtags and caption copy
Ensure all suggestions are strictly truthful, avoid unverified superlatives, and sound natural in conversational Indian English/Hinglish.`;

    const outBox = $('#wiz-output-box');
    if (outBox) {
      outBox.style.display = 'block';
      outBox.querySelector('pre').textContent = promptOutput;
    }
  });

  $('#wiz-copy-btn')?.addEventListener('click', () => {
    const text = $('#wiz-output-box pre')?.textContent;
    if (text) copyText(text);
  });

  // Personalize Prompt Modal
  function openPersonalizeModal(p, lang = 'hinglish') {
    const modal = $('#hm-modal-personalize');
    if (!modal) return;
    $('#pers-modal-title').textContent = p.title;
    const raw = (lang === 'hinglish' && p.prompt_hinglish) ? p.prompt_hinglish : p.prompt;
    const pre = $('#pers-modal-preview');
    pre.textContent = personalizePromptText(raw);
    $('#pers-modal-copy').onclick = () => copyText(pre.textContent);
    openModal('hm-modal-personalize');
  }

  // Export Marketing Kit Modal
  $('#btn-open-export')?.addEventListener('click', () => {
    const prof = propertyProfile;
    const md = `# HostMastery — Marketing Kit for ${prof.name}
Generated from HostMastery All-in-One Airbnb Host Kit

## 1. Property Overview
- **Stay Name:** ${prof.name}
- **Host:** ${prof.host}
- **Location:** ${prof.city}
- **Type:** ${prof.type}
- **Target Audience:** ${prof.guests}
- **Key Amenities:** ${prof.amenities}
- **Check-in / Checkout:** ${prof.checkin} / ${prof.checkout}
- **Wi-Fi:** Network "${prof.wifi}" | Password "${prof.password}"
- **Host Contact:** ${prof.contact}

---

## 2. Essential Guest Messages (Hinglish & English)
${guestMessagesData.slice(0, 6).map(m => `### ${m.title}
**Hinglish:**
${personalizePromptText(m.hinglish)}

**English:**
${personalizePromptText(m.en)}
`).join('\n---\n')}

---

## 3. Printable Welcome Information
**Greeting:**
${prof.greeting}

**House Rules:**
${prof.rules}

**Checkout Steps:**
${prof.steps}

**Local Recommendations:**
${prof.local}
`;

    const pre = $('#export-kit-preview');
    if (pre) pre.textContent = md;
    openModal('hm-modal-export');
  });

  $('#btn-download-export-md')?.addEventListener('click', () => {
    const text = $('#export-kit-preview')?.textContent || '';
    const blob = new Blob([text], { type: 'text/markdown' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `HostMastery_${propertyProfile.name.replace(/\s+/g, '_')}_Kit.md`;
    a.click();
    URL.revokeObjectURL(url);
    toast('Downloaded Marketing Kit (.md) ✓');
  });

  // Welcome Studio Templates switcher
  $$('[data-template]').forEach(btn => {
    btn.addEventListener('click', (e) => {
      activeTemplate = e.currentTarget.dataset.template;
      $$('[data-template]').forEach(b => b.setAttribute('aria-pressed', String(b === e.currentTarget)));
      renderSheet();
    });
  });

  // Welcome Studio form field inputs
  $$('[id^="field-"]').forEach(el => el.addEventListener('input', renderSheet));

  $('#btn-print-sheet')?.addEventListener('click', () => {
    renderSheet();
    try { window.print(); } catch(e) { toast('Use browser menu to print sheet.'); }
  });

  $('#btn-copy-sheet')?.addEventListener('click', () => {
    const text = $('#hm-print-sheet')?.innerText;
    if (text) copyText(text);
  });

  $('#btn-sync-profile-studio')?.addEventListener('click', () => {
    syncFormFromProfile();
    toast('Loaded all details from Property Profile ✓');
  });

  // Calculator inputs listener
  $$('[id^="calc-"]').forEach(el => el.addEventListener('input', calculatePricing));

  // Initialize
  updateCounters();
  renderCategories();
  renderPrompts();
  renderAuditQuestions();
  calculateAudit();
  renderViralHooks('All');
  renderGuestMessages();
  syncFormFromProfile();
  renderSheet();
  calculatePricing();
  initActionPlan();

})();
