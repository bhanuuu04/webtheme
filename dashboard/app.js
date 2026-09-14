// Theme Library Dashboard JavaScript Application — Styled with Theme #011 (Apple)
// Precision High-Density Productivity Workspace System

let allThemes = [];
let filteredThemes = [];
let selectedCategories = new Set();
let selectedTags = new Set();
let selectedTone = 'all';
let currentSearch = '';
let currentSort = 'id-asc';
let currentView = 'grid';
let compareList = [];
let displayLimit = 40;

// DOM Elements
const themeContainer = document.getElementById('themeContainer');
const searchInput = document.getElementById('searchInput');
const categoryFilters = document.getElementById('categoryFilters');
const tagFilters = document.getElementById('tagFilters');
const visibleCount = document.getElementById('visibleCount');
const totalCount = document.getElementById('totalCount');
const filterNotice = document.getElementById('filterNotice');
const sortSelect = document.getElementById('sortSelect');
const gridViewBtn = document.getElementById('gridViewBtn');
const listViewBtn = document.getElementById('listViewBtn');
const resetFiltersBtn = document.getElementById('resetFiltersBtn');
const themeModal = document.getElementById('themeModal');
const modalContent = document.getElementById('modalContent');
const compareModal = document.getElementById('compareModal');
const compareGrid = document.getElementById('compareGrid');
const compareBtn = document.getElementById('compareBtn');
const compareCount = document.getElementById('compareCount');
const closeCompareBtn = document.getElementById('closeCompareBtn');
const exportJsonBtn = document.getElementById('exportJsonBtn');
const toast = document.getElementById('toast');
const toastMessage = document.getElementById('toastMessage');

// Initialize Application
async function initApp() {
  if (window.THEMES_DATA && Array.isArray(window.THEMES_DATA) && window.THEMES_DATA.length > 0) {
    allThemes = window.THEMES_DATA;
    console.log(`Loaded ${allThemes.length} themes directly from window.THEMES_DATA`);
  } else {
    try {
      const res = await fetch('themes.json');
      if (res.ok) {
        allThemes = await res.json();
      } else {
        const fallbackRes = await fetch('../themes.json');
        allThemes = await fallbackRes.json();
      }
    } catch (err) {
      console.error('Failed to load themes data:', err);
    }
  }

  if (totalCount) totalCount.textContent = allThemes.length;
  if (visibleCount) visibleCount.textContent = allThemes.length;
  buildFilters();
  setupEventListeners();
  applyFilters();
  if (window.lucide) lucide.createIcons();
}

// Build Sidebar Category and Tag filters
function buildFilters() {
  if (!categoryFilters || !tagFilters) return;

  const categoryCounts = {};
  const tagCounts = {};

  allThemes.forEach(t => {
    categoryCounts[t.category] = (categoryCounts[t.category] || 0) + 1;
    t.tags.forEach(tag => {
      tagCounts[tag] = (tagCounts[tag] || 0) + 1;
    });
  });

  // Populate categories
  categoryFilters.innerHTML = Object.entries(categoryCounts)
    .sort((a, b) => b[1] - a[1])
    .map(([cat, count]) => `
      <label class="flex items-center justify-between px-2.5 py-1.5 rounded-lg hover:bg-[#f3f4f6] cursor-pointer group transition-colors">
        <div class="flex items-center gap-2">
          <input type="checkbox" value="${cat}" class="category-checkbox rounded bg-white border-[#e5e7eb] text-[#0070f3] focus:ring-0">
          <span class="text-[#4b5563] group-hover:text-[#111827] text-xs font-medium">${cat}</span>
        </div>
        <span class="text-[10px] px-1.5 py-0.5 rounded bg-[#f3f4f6] text-[#6b7280] font-mono border border-[#e5e7eb]">${count}</span>
      </label>
    `).join('');

  // Populate style tags
  const popularTags = Object.entries(tagCounts)
    .sort((a, b) => b[1] - a[1])
    .slice(0, 18);

  tagFilters.innerHTML = popularTags.map(([tag, count]) => `
    <button data-tag="${tag}" class="tag-badge px-2.5 py-1 rounded-lg bg-white text-[#4b5563] border border-[#e5e7eb] hover:border-[#0070f3]/50 hover:text-[#0070f3] text-[11px] font-medium flex items-center gap-1 shadow-xs">
      <span>#${tag}</span>
      <span class="text-[9px] text-[#9ca3af] font-mono">(${count})</span>
    </button>
  `).join('');
}

// Setup Event Listeners
function setupEventListeners() {
  // Global ⌘K shortcut for search
  window.addEventListener('keydown', (e) => {
    if ((e.metaKey || e.ctrlKey) && e.key === 'k') {
      e.preventDefault();
      if (searchInput) {
        searchInput.focus();
        searchInput.select();
      }
    }
  });

  if (searchInput) {
    searchInput.addEventListener('input', (e) => {
      currentSearch = e.target.value.trim().toLowerCase();
      applyFilters();
    });
  }

  if (categoryFilters) {
    categoryFilters.addEventListener('change', (e) => {
      if (e.target.classList.contains('category-checkbox')) {
        if (e.target.checked) {
          selectedCategories.add(e.target.value);
        } else {
          selectedCategories.delete(e.target.value);
        }
        applyFilters();
      }
    });
  }

  if (tagFilters) {
    tagFilters.addEventListener('click', (e) => {
      const btn = e.target.closest('.tag-badge');
      if (!btn) return;
      const tag = btn.dataset.tag;
      if (selectedTags.has(tag)) {
        selectedTags.delete(tag);
        btn.classList.remove('active');
      } else {
        selectedTags.add(tag);
        btn.classList.add('active');
      }
      applyFilters();
    });
  }

  document.querySelectorAll('.tone-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      document.querySelectorAll('.tone-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      selectedTone = btn.dataset.tone;
      applyFilters();
    });
  });

  if (resetFiltersBtn) {
    resetFiltersBtn.addEventListener('click', () => {
      if (searchInput) searchInput.value = '';
      currentSearch = '';
      selectedCategories.clear();
      document.querySelectorAll('.category-checkbox').forEach(cb => cb.checked = false);
      selectedTags.clear();
      document.querySelectorAll('.tag-badge').forEach(b => b.classList.remove('active'));
      selectedTone = 'all';
      document.querySelectorAll('.tone-btn').forEach(b => b.classList.toggle('active', b.dataset.tone === 'all'));
      applyFilters();
      showToast('Filters reset');
    });
  }

  if (sortSelect) {
    sortSelect.addEventListener('change', (e) => {
      currentSort = e.target.value;
      applySorting();
      renderThemes();
    });
  }

  if (gridViewBtn && listViewBtn) {
    gridViewBtn.addEventListener('click', () => {
      currentView = 'grid';
      gridViewBtn.classList.add('bg-[#0070f3]', 'text-white');
      gridViewBtn.classList.remove('text-[#6b7280]');
      listViewBtn.classList.remove('bg-[#0070f3]', 'text-white');
      listViewBtn.classList.add('text-[#6b7280]');
      if (themeContainer) {
        themeContainer.classList.remove('list-view-mode');
        themeContainer.classList.add('grid');
      }
      renderThemes();
    });

    listViewBtn.addEventListener('click', () => {
      currentView = 'list';
      listViewBtn.classList.add('bg-[#0070f3]', 'text-white');
      listViewBtn.classList.remove('text-[#6b7280]');
      gridViewBtn.classList.remove('bg-[#0070f3]', 'text-white');
      gridViewBtn.classList.add('text-[#6b7280]');
      if (themeContainer) {
        themeContainer.classList.remove('grid');
        themeContainer.classList.add('list-view-mode');
      }
      renderThemes();
    });
  }

  if (exportJsonBtn) {
    exportJsonBtn.addEventListener('click', () => {
      const dataStr = 'data:text/json;charset=utf-8,' + encodeURIComponent(JSON.stringify(filteredThemes, null, 2));
      const dl = document.createElement('a');
      dl.setAttribute('href', dataStr);
      dl.setAttribute('download', `theme_library_${filteredThemes.length}_themes.json`);
      dl.click();
      showToast(`Exported ${filteredThemes.length} themes as JSON`);
    });
  }

  if (compareBtn) {
    compareBtn.addEventListener('click', () => {
      if (compareList.length === 0) {
        showToast('Select 1 or 2 themes to compare');
        return;
      }
      renderCompareModal();
      if (compareModal) {
        compareModal.classList.remove('hidden');
        setTimeout(() => compareModal.classList.add('open'), 10);
      }
    });
  }

  if (closeCompareBtn && compareModal) {
    closeCompareBtn.addEventListener('click', () => {
      compareModal.classList.remove('open');
      setTimeout(() => compareModal.classList.add('hidden'), 200);
    });
  }

  if (themeModal) {
    themeModal.addEventListener('click', (e) => {
      if (e.target === themeModal) {
        closeDetailModal();
      }
    });
  }

  window.addEventListener('scroll', () => {
    if ((window.innerHeight + window.scrollY) >= document.body.offsetHeight - 500) {
      if (displayLimit < filteredThemes.length) {
        displayLimit += 30;
        renderThemes(false);
      }
    }
  });
}

function applyFilters() {
  filteredThemes = allThemes.filter(t => {
    if (selectedCategories.size > 0 && !selectedCategories.has(t.category)) {
      return false;
    }

    if (selectedTags.size > 0) {
      for (let tag of selectedTags) {
        if (!t.tags.includes(tag)) return false;
      }
    }

    if (selectedTone !== 'all') {
      if (selectedTone === 'dark' && !t.tags.includes('dark')) return false;
      if (selectedTone === 'light' && !t.tags.includes('light')) return false;
    }

    if (currentSearch) {
      const q = currentSearch;
      const numMatch = t.theme_id.toLowerCase().includes(q) || `theme ${t.theme_number}`.includes(q) || `#${t.theme_number}`.includes(q);
      const nameMatch = t.name.toLowerCase().includes(q);
      const urlMatch = t.url.toLowerCase().includes(q);
      const catMatch = t.category.toLowerCase().includes(q);
      const dnaMatch = t.overall_design_dna.toLowerCase().includes(q);
      const styleMatch = t.design_style.toLowerCase().includes(q);
      const tagMatch = t.tags.some(tag => tag.toLowerCase().includes(q));

      if (!numMatch && !nameMatch && !urlMatch && !catMatch && !dnaMatch && !styleMatch && !tagMatch) {
        return false;
      }
    }

    return true;
  });

  if (visibleCount) visibleCount.textContent = filteredThemes.length;
  
  if (filterNotice) {
    const activeBadges = [];
    if (currentSearch) activeBadges.push(`Search: "${currentSearch}"`);
    selectedCategories.forEach(c => activeBadges.push(`Category: ${c}`));
    selectedTags.forEach(t => activeBadges.push(`#${t}`));
    if (selectedTone !== 'all') activeBadges.push(`Tone: ${selectedTone}`);

    if (activeBadges.length === 0) {
      filterNotice.innerHTML = `<span class="px-2 py-0.5 rounded-md bg-white border border-[#e5e7eb] text-[11px] text-[#6b7280]">None (Showing All)</span>`;
    } else {
      filterNotice.innerHTML = activeBadges.map(b => 
        `<span class="px-2 py-0.5 rounded-md bg-[#0070f3]/10 border border-[#0070f3]/30 text-[11px] font-medium text-[#0070f3]">${b}</span>`
      ).join('');
    }
  }

  displayLimit = 40;
  applySorting();
  renderThemes();
}

function applySorting() {
  if (currentSort === 'id-asc') {
    filteredThemes.sort((a, b) => a.theme_number - b.theme_number);
  } else if (currentSort === 'id-desc') {
    filteredThemes.sort((a, b) => b.theme_number - a.theme_number);
  } else if (currentSort === 'name-asc') {
    filteredThemes.sort((a, b) => a.name.localeCompare(b.name));
  } else if (currentSort === 'name-desc') {
    filteredThemes.sort((a, b) => b.name.localeCompare(a.name));
  } else if (currentSort === 'category') {
    filteredThemes.sort((a, b) => a.category.localeCompare(b.category));
  }
}

function cleanDomain(url) {
  try {
    return new URL(url).hostname.replace('www.', '');
  } catch(e) {
    return url.replace('https://', '').replace('http://', '').replace('www.', '').split('/')[0];
  }
}

function getPrimaryScreenshotUrl(url) {
  return `https://s0.wp.com/mshots/v1/${encodeURIComponent(url)}?w=640&h=420`;
}

function getFallbackScreenshotUrl(url) {
  return `https://image.thum.io/get/width/640/crop/420/${url}`;
}
function getFaviconUrl(domain) {
  return `https://www.google.com/s2/favicons?domain=${domain}&sz=64`;
}

// 🧠 Deep High-Fidelity AI Prompt Generator Engine (Project Adaptation & Reskinning Mode)
function generateDetailedAiPrompt(t) {
  const primaryHex = t.primary_colors[0] ? t.primary_colors[0].hex : '#08090a';
  const accentHex = t.primary_colors[1] ? t.primary_colors[1].hex : (t.primary_colors[0] ? t.primary_colors[0].hex : '#0070f3');
  const surfaceHex = t.secondary_colors[0] ? t.secondary_colors[0].hex : '#151618';
  const borderHex = t.secondary_colors[1] ? t.secondary_colors[1].hex : '#222326';
  const domain = cleanDomain(t.url);

  // Build color application rules string
  const colorRulesStr = t.color_application_rules
    ? Object.entries(t.color_application_rules).map(([hex, usage]) => `${hex}  →  ${usage}`).join('\n')
    : [...t.primary_colors.map(c => `${c.hex}  →  ${c.role}`), ...t.secondary_colors.map(c => `${c.hex}  →  ${c.role}`)].join('\n');

  // Build anti-patterns string
  const antiPatternsStr = t.anti_patterns
    ? t.anti_patterns.map(p => `  ❌ ${p}`).join('\n')
    : `  ❌ Do not mix styles from other themes\n  ❌ Do not use generic Bootstrap/Material components\n  ❌ Do not ignore the whitespace and spacing rhythm`;

  // Build page architecture string
  const pageArchStr = t.page_architecture
    ? t.page_architecture.join('\n')
    : `1. Sticky nav → 2. Hero → 3. Features → 4. Social proof → 5. CTA → 6. Footer`;

  return `[SYSTEM INSTRUCTION: SINGLE-SOURCE THEME DESIGN ADAPTER]
You are a Principal UI/UX Architect & Frontend Design System Engineer.
Your task is to analyze the user's current project / objective, and TRANSFORM / REDESIGN its entire frontend style, visual aesthetic, UX feeling, and component architecture strictly using the design system DNA of THEME #${t.theme_id} (${t.name} - ${t.url}).

Maintain 100% strict theme isolation: extract and apply ONLY this reference theme's design language, tokens, and aesthetic principles.

══════════════════════════════════════════════════════════════════
🎯 CORE OBJECTIVE: ADAPT THEME TO USER'S PROJECT (NOT A BLIND CLONE)
══════════════════════════════════════════════════════════════════
1. ANALYZE CURRENT PROJECT & GOAL:
   - Carefully inspect the user's current project codebase, wireframes, or feature requirements (e.g. e-commerce clothing store selling shirts, SaaS tool, personal portfolio, marketplace, dashboard, etc.).
   - Preserve the user's core project purpose, domain data, functional workflows, and business logic.

2. TRANSLATE DESIGN DNA (DO NOT COPY PROPRIETARY CONTENT):
   - Do NOT blindly copy placeholder copy, trademarks, or unrelated product catalog from ${t.name} (e.g., do not insert "${t.name}" branding or unrelated product listings).
   - DO extract and adopt 100% of ${t.name}'s visual craft, color palette, typography hierarchy, card structures, spacing rhythm, surface depth, micro-interactions, and UX feeling.

3. ELEVATE & RESKIN EVERY COMPONENT:
   - Reskin the user's existing components (navbars, heroes, product/feature cards, buttons, filters, inputs, modals, footers) into the authentic visual language of THEME #${t.theme_id}.
   - Example: If the user's project is an apparel store selling shirts, design a high-craft shirt catalog with ${t.name}'s signature layouts, typography scale, lighting, and button styles.

══════════════════════════════════════════════════════════════════
🧬 THEME #${t.theme_id} IDENTITY & EMOTIONAL BRIEF
══════════════════════════════════════════════════════════════════
- Permanent Theme ID: THEME #${t.theme_id}
- Reference Design Source: ${t.name} (${t.url})
- Mode: ${t.mode || 'light'}
- Archetype / Category: ${t.category}
- Design Style: ${t.design_style}
- Visual Personality: ${t.visual_personality}
- Core Design DNA: ${t.overall_design_dna}

🔑 THE SIGNATURE VISUAL ELEMENT (What makes this theme unmistakably ${t.name}):
${t.signature_visual_element || t.design_principles}

🎭 EMOTIONAL INTENT (How the user should FEEL when they see this design):
${t.emotional_intent || t.design_principles}

══════════════════════════════════════════════════════════════════
🎨 COLOR SYSTEM & APPLICATION RULES
══════════════════════════════════════════════════════════════════
${colorRulesStr}

CSS Custom Properties (paste into :root {}):
${t.css_variables || `:root { --accent: ${accentHex}; --bg: ${primaryHex}; --surface: ${surfaceHex}; --border: ${borderHex}; }`}

Tailwind Config Extension (add inside extend: {}):
${t.tailwind_tokens || `colors: { accent: '${accentHex}', bg: '${primaryHex}', surface: '${surfaceHex}' }`}

══════════════════════════════════════════════════════════════════
🔤 TYPOGRAPHY & TEXT RHYTHM
══════════════════════════════════════════════════════════════════
- Display / Headline Font: ${t.typography.font_family_display}
- Body Copy Font: ${t.typography.font_family_body}
- Monospace / Data Font: ${t.typography.font_family_mono}
- Optical Tracking (Letter Spacing): ${t.typography.letter_spacing}
- Scale & Proportions: ${t.typography.scale}
- Font Weights: ${t.typography.weights}

Copy Voice & Tone (match this style in ALL generated text content):
${t.copy_voice || 'Professional, benefit-focused, clear. Short declarative headlines. Action CTAs.'}

══════════════════════════════════════════════════════════════════
📐 SPACING, GRID & GEOMETRY
══════════════════════════════════════════════════════════════════
- Container Max-Width & Grid: ${t.spacing.grid_system}
- Vertical Padding Scale: ${t.spacing.padding_scale}
- Whitespace Philosophy: ${t.spacing.whitespace_philosophy}

══════════════════════════════════════════════════════════════════
🧩 COMPONENT ARCHETYPE MAPPING
══════════════════════════════════════════════════════════════════
- Buttons (Primary, Secondary, Ghost): ${t.components.buttons}
- Cards, Modules & Bento Grids: ${t.components.cards}
- Header & Navigation System: ${t.components.navigation}
- Hero / Showcase Composition: ${t.components.hero_section}
- Forms, Filters & Pill Selectors: ${t.components.forms}
- Footer & System Status: ${t.components.footer}

Icon System: ${t.icon_system || 'Lucide Icons, clean stroke style, monochrome'}
Image Treatment: ${t.image_treatment || 'Product screenshots or lifestyle photography appropriate to the project domain'}

══════════════════════════════════════════════════════════════════
⚡ MOTION PHYSICS & MICRO-INTERACTIONS
══════════════════════════════════════════════════════════════════
- Transitions & Easing: ${t.motion.transitions}
  Apply as: transition: all 150ms cubic-bezier(0.16, 1, 0.3, 1) on all interactive elements
- Card Hover: transform: translateY(-2px) + box-shadow escalation
- Button Press: transform: scale(0.97), transition: 80ms ease-in
- Modal Entry: opacity 0 to 1 + translateY(8px to 0px), 200ms
- Scroll Reveals: IntersectionObserver at threshold 0.1, staggered 60ms per sibling
- Scroll Behavior: ${t.motion.scroll_effects}
- Micro-Interactions: ${t.motion.micro_interactions}

══════════════════════════════════════════════════════════════════
📱 RESPONSIVE ADAPTATION
══════════════════════════════════════════════════════════════════
- Mobile Layout Strategy: ${t.responsive.mobile_strategy}
- Desktop Ergonomics: ${t.responsive.desktop_strategy}

══════════════════════════════════════════════════════════════════
🏗️ PAGE ARCHITECTURE (ordered section scaffold)
══════════════════════════════════════════════════════════════════
${pageArchStr}

══════════════════════════════════════════════════════════════════
🚫 ANTI-PATTERNS (what NOT to do — these break theme authenticity)
══════════════════════════════════════════════════════════════════
${antiPatternsStr}

══════════════════════════════════════════════════════════════════
🛡️ DESIGN FIDELITY GUARDRAILS
══════════════════════════════════════════════════════════════════
- MUST ADOPT & REUSE:
${t.things_to_reuse.map(r => `  * ${r}`).join('\n')}
- DO NOT COPY (Proprietary / Brand Specific):
${t.things_not_to_copy.map(n => `  * ${n}`).join('\n')}
- TECHNICAL IMPLEMENTATION GUIDANCE:
  ${t.implementation_notes}

══════════════════════════════════════════════════════════════════
🛠️ STEP-BY-STEP REFACTORING INSTRUCTIONS
══════════════════════════════════════════════════════════════════
1. READ the user's current project files, identify domain, existing components, and tech stack.
2. INJECT CSS custom properties (above) into the global stylesheet / Tailwind config.
3. RE-ARCHITECT each layout section to match the page architecture scaffold above.
4. RE-ENGINEER every UI component (nav, hero, cards, buttons, inputs, footer) into the ${t.name} visual language while keeping the user's real content, data, and workflows intact.
5. APPLY motion physics (transitions, hover states, scroll reveals) as specified.
6. WRITE all page copy in the Copy Voice defined above — match the tone, not the brand.
7. VERIFY: The output should feel unmistakably like ${t.name}'s design aesthetic applied to the user's own project domain.

══════════════════════════════════════════════════════════════════
📦 DELIVERABLE DEFINITION
══════════════════════════════════════════════════════════════════
${t.deliverable_note || 'Output the complete reskinned project files. Apply theme tokens via CSS custom properties globally, then rework component markup. Preserve all business logic and domain data.'}`;
}

// Render Themes in Theme #014 (Arc) Clean Minimal Enterprise Product System
function renderThemes(reset = true) {
  const themesToDisplay = filteredThemes.slice(0, displayLimit);

  if (themesToDisplay.length === 0) {
    themeContainer.innerHTML = `
      <div class="col-span-full py-16 text-center flex flex-col items-center justify-center gap-3">
        <div class="p-3 rounded-lg bg-[#f9fafb] border border-[#e5e7eb] text-[#6b7280]">
          <i data-lucide="search-x" class="w-6 h-6"></i>
        </div>
        <h3 class="text-base font-semibold text-[#111827] tracking-display">No matching themes found</h3>
        <p class="text-xs text-[#6b7280] max-w-sm">Try adjusting your filters or clearing your search term.</p>
        <button onclick="document.getElementById('resetFiltersBtn').click()" class="mt-2 px-4 py-2 rounded-lg bg-[#0070f3] text-xs font-semibold text-white hover:bg-[#0060df] transition-colors shadow-sm">
          Reset All Filters
        </button>
      </div>
    `;
    lucide.createIcons();
    return;
  }

  const cardsHtml = themesToDisplay.map(t => {
    const primaryHex = t.primary_colors[0] ? t.primary_colors[0].hex : '#ffffff';
    const accentHex = t.primary_colors[1] ? t.primary_colors[1].hex : (t.primary_colors[0] ? t.primary_colors[0].hex : '#0070f3');
    const isCompared = compareList.some(c => c.theme_id === t.theme_id);
    const domain = cleanDomain(t.url);
    const screenshotUrl = getPrimaryScreenshotUrl(t.url);
    const fallbackScreenshotUrl = getFallbackScreenshotUrl(t.url);
    const faviconUrl = getFaviconUrl(domain);

    return `
      <div class="theme-card flex flex-col justify-between group cursor-pointer" onclick="openDetailModal('${t.theme_id}')">
        <div>
          <!-- REAL WEBSITE SCREENSHOT PREVIEW -->
          <div class="screenshot-container">
            <!-- Browser Header Bar -->
            <div class="absolute top-0 inset-x-0 h-7 bg-white/90 backdrop-blur-md border-b border-[#e5e7eb] z-10 px-3 flex items-center justify-between">
              <div class="flex items-center gap-1.5">
                <span class="w-2 h-2 rounded-full bg-rose-400"></span>
                <span class="w-2 h-2 rounded-full bg-amber-400"></span>
                <span class="w-2 h-2 rounded-full bg-emerald-400"></span>
                <span class="ml-2 text-[10px] font-mono text-[#6b7280] truncate max-w-[120px] font-medium">${domain}</span>
              </div>
              <div class="flex items-center gap-1">
                <span class="px-1.5 py-0.5 rounded bg-[#0070f3]/10 text-[#0070f3] font-mono font-bold text-[9px] border border-[#0070f3]/25">
                  ${t.theme_id}
                </span>
              </div>
            </div>

            <!-- Screenshot Image -->
            <img src="${screenshotUrl}" 
                 alt="${t.name} Website Preview Screenshot"
                 loading="lazy"
                 class="screenshot-img pt-7"
                 onerror="this.onerror=null; this.src='${fallbackScreenshotUrl}';" />

            <!-- Bottom Floating Quick-Actions Overlay -->
            <div class="absolute bottom-2 right-2 z-10 flex items-center gap-1.5">
              <button onclick="event.stopPropagation(); copyAiPrompt('${t.theme_id}')" title="Copy exact AI prompt" 
                class="px-2 py-1 rounded-md text-[10px] font-bold backdrop-blur-md transition-all shadow-sm bg-[#0070f3] text-white hover:bg-[#0060df] flex items-center gap-1">
                <i data-lucide="sparkles" class="w-2.5 h-2.5"></i> Prompt
              </button>
              <button onclick="event.stopPropagation(); toggleCompare('${t.theme_id}')" title="${isCompared ? 'Remove from compare' : 'Add to compare'}" 
                class="px-2 py-1 rounded-md text-[10px] font-bold backdrop-blur-md transition-all shadow-sm ${isCompared ? 'bg-[#111827] text-white' : 'bg-white/90 text-[#4b5563] hover:text-[#111827] border border-[#e5e7eb]'}">
                ${isCompared ? '✓ Comp' : '+ Comp'}
              </button>
              <a href="${t.url}" target="_blank" onclick="event.stopPropagation()" class="p-1.5 rounded-md bg-white/90 text-[#4b5563] hover:text-[#111827] backdrop-blur-md border border-[#e5e7eb] transition-colors shadow-sm" title="Open ${domain} in new tab">
                <i data-lucide="external-link" class="w-3.5 h-3.5"></i>
              </a>
            </div>
          </div>

          <!-- Card Header & Meta -->
          <div class="card-body p-4 pb-2">
            <div class="flex items-center justify-between mb-1.5">
              <div class="flex items-center gap-2">
                <img src="${faviconUrl}" alt="${t.name} logo" class="w-4 h-4 rounded shrink-0" onerror="this.style.display='none'" />
                <h3 class="text-sm font-bold text-[#111827] group-hover:text-[#0070f3] transition-colors tracking-display">
                  ${t.name}
                </h3>
              </div>
              <div class="flex items-center gap-1.5">
                <span class="w-3 h-3 rounded-full border border-black/10 shadow-xs" style="background-color: ${primaryHex}" title="Primary: ${primaryHex}"></span>
                <span class="w-3 h-3 rounded-full border border-black/10 shadow-xs" style="background-color: ${accentHex}" title="Accent: ${accentHex}"></span>
              </div>
            </div>

            <p class="text-[11px] text-[#6b7280] line-clamp-2 leading-relaxed mb-3">
              ${t.overall_design_dna}
            </p>
          </div>
        </div>

        <!-- Card Footer -->
        <div class="px-4 py-2.5 border-t border-[#e5e7eb] flex items-center justify-between text-xs bg-[#f9fafb]">
          <div class="flex items-center gap-1.5">
            <span class="text-[10px] px-2 py-0.5 rounded bg-white text-[#4b5563] border border-[#e5e7eb] font-mono">${t.category.split('/')[0].trim()}</span>
            ${t.tags.slice(0, 1).map(tag => `
              <span class="text-[10px] px-1.5 py-0.5 rounded bg-white text-[#6b7280] border border-[#e5e7eb]">#${tag}</span>
            `).join('')}
          </div>
          <span class="text-[11px] text-[#0070f3] font-medium group-hover:translate-x-0.5 transition-transform flex items-center gap-0.5">
            Design Specs <i data-lucide="chevron-right" class="w-3 h-3"></i>
          </span>
        </div>
      </div>
    `;
  }).join('');

  themeContainer.innerHTML = cardsHtml;
  lucide.createIcons();
}

// Open Theme Detail Drawer
function openDetailModal(themeId) {
  const t = allThemes.find(item => item.theme_id === themeId);
  if (!t) return;

  const domain = cleanDomain(t.url);
  const screenshotUrl = getPrimaryScreenshotUrl(t.url);
  const faviconUrl = getFaviconUrl(domain);
  const detailedAiPrompt = generateDetailedAiPrompt(t);

  modalContent.innerHTML = `
    <!-- Top Action Bar -->
    <div class="flex items-center justify-between border-b border-[#e5e7eb] pb-4 mb-5">
      <div class="flex items-center gap-2">
        <span class="px-2.5 py-1 rounded-lg bg-[#0070f3] text-white font-mono font-bold text-xs shadow-xs">
          ${t.theme_display_id}
        </span>
        <span class="text-xs text-[#6b7280] font-mono">${t.category}</span>
      </div>
      <div class="flex items-center gap-2">
        <button onclick="copyAiPrompt('${t.theme_id}')" class="flex items-center gap-1.5 px-3 py-1.5 rounded-lg bg-[#0070f3] hover:bg-[#0060df] text-white text-xs font-semibold shadow-sm transition-all">
          <i data-lucide="sparkles" class="w-3.5 h-3.5"></i>
          <span>Copy Complete AI Prompt</span>
        </button>
        <button onclick="closeDetailModal()" class="p-1.5 rounded-lg bg-[#f9fafb] text-[#6b7280] hover:text-[#111827] border border-[#e5e7eb]">
          <i data-lucide="x" class="w-5 h-5"></i>
        </button>
      </div>
    </div>

    <!-- Title & Reference Link -->
    <div class="flex items-start justify-between gap-4 mb-5">
      <div class="flex items-center gap-3">
        <img src="${faviconUrl}" alt="${t.name}" class="w-8 h-8 rounded-lg p-1 bg-[#f9fafb] border border-[#e5e7eb]" onerror="this.style.display='none'" />
        <div>
          <h2 class="text-2xl font-bold text-[#111827] mb-0.5 tracking-display">${t.name}</h2>
          <p class="text-xs text-[#0070f3] font-medium">${t.design_style}</p>
        </div>
      </div>
      <a href="${t.url}" target="_blank" class="flex items-center gap-1.5 px-3.5 py-2 rounded-lg bg-[#f9fafb] border border-[#e5e7eb] text-[#4b5563] hover:text-[#111827] text-xs font-semibold transition-colors shadow-xs">
        <span>Visit ${domain}</span>
        <i data-lucide="external-link" class="w-3.5 h-3.5"></i>
      </a>
    </div>

    <!-- REAL WEBSITE PREVIEW BANNER -->
    <div class="relative rounded-xl overflow-hidden border border-[#e5e7eb] mb-6 bg-[#f9fafb] shadow-sm">
      <div class="h-8 bg-white border-b border-[#e5e7eb] px-3 flex items-center justify-between text-xs">
        <div class="flex items-center gap-1.5">
          <span class="w-2.5 h-2.5 rounded-full bg-rose-400"></span>
          <span class="w-2.5 h-2.5 rounded-full bg-amber-400"></span>
          <span class="w-2.5 h-2.5 rounded-full bg-emerald-400"></span>
          <span class="ml-2 font-mono text-[11px] text-[#6b7280] font-medium">${t.url}</span>
        </div>
        <div class="flex items-center gap-2">
          <button onclick="toggleIframe('${t.url}')" id="iframeToggleBtn" class="text-[10px] font-semibold text-[#0070f3] hover:underline flex items-center gap-1">
            <i data-lucide="play-circle" class="w-3 h-3"></i> Load Live Interactive Frame
          </button>
        </div>
      </div>

      <div id="screenshotView" class="relative max-h-72 overflow-hidden">
        <img src="${screenshotUrl}" alt="${t.name} Full Preview" class="w-full object-cover object-top" />
      </div>

      <div id="iframeView" class="hidden w-full h-80">
        <iframe id="liveIframe" src="" class="w-full h-full border-0" loading="lazy"></iframe>
      </div>
    </div>

    <!-- Deep Master AI Prompt Box -->
    <div class="bg-gradient-to-br from-[#0070f3]/5 via-[#f9fafb] to-[#f9fafb] border border-[#0070f3]/25 rounded-xl p-4 mb-6 shadow-sm">
      <div class="flex items-center justify-between mb-2">
        <span class="text-xs font-bold text-[#0070f3] flex items-center gap-1.5 font-mono">
          <i data-lucide="terminal" class="w-4 h-4 text-[#0070f3]"></i>
          Complete High-Fidelity AI Prompt (Click to Copy)
        </span>
        <button onclick="copyAiPrompt('${t.theme_id}')" class="px-2.5 py-1 rounded bg-[#0070f3] hover:bg-[#0060df] text-white text-[11px] font-semibold transition-all shadow-xs">Copy Prompt</button>
      </div>
      <p class="text-[11px] text-[#6b7280] mb-2 leading-relaxed">
        Pass this complete prompt to any AI to instantly build or reskin your project into ${t.name}'s design aesthetic with exact tokens, fonts, geometry, and component specs.
      </p>
      <pre class="bg-white p-3.5 rounded-lg text-[10px] font-mono text-[#374151] whitespace-pre-wrap leading-relaxed border border-[#e5e7eb] max-h-60 overflow-y-auto custom-scrollbar">${detailedAiPrompt}</pre>
    </div>

    <!-- Theme DNA Quote -->
    <div class="bg-gradient-to-r from-[#0070f3]/10 to-[#f9fafb] border-l-3 border-[#0070f3] p-4 rounded-r-xl mb-6">
      <div class="text-[10px] uppercase font-bold text-[#0070f3] tracking-wider mb-1 flex items-center gap-1 font-mono">
        <i data-lucide="dna" class="w-3 h-3"></i> Theme DNA
      </div>
      <p class="text-xs text-[#111827] leading-relaxed font-medium">"${t.overall_design_dna}"</p>
    </div>

    <!-- Design Principles -->
    <div class="bg-[#f9fafb] border border-[#e5e7eb] rounded-xl p-4 mb-6">
      <h4 class="text-xs font-bold uppercase tracking-wider text-[#111827] mb-2 flex items-center gap-1.5 font-mono">
        <i data-lucide="compass" class="w-3.5 h-3.5 text-[#0070f3]"></i>
        Design Principles ("Why does this look like this?")
      </h4>
      <p class="text-xs text-[#4b5563] leading-relaxed">${t.design_principles}</p>
    </div>

    <!-- Color System Swatches -->
    <div class="bg-[#f9fafb] border border-[#e5e7eb] rounded-xl p-4 mb-6">
      <h4 class="text-xs font-bold uppercase tracking-wider text-[#111827] mb-3 flex items-center gap-1.5 font-mono">
        <i data-lucide="palette" class="w-3.5 h-3.5 text-[#0070f3]"></i>
        Color Palette System (Click to copy hex)
      </h4>
      
      <div class="text-[11px] font-semibold text-[#6b7280] mb-1.5">Primary Palette:</div>
      <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 mb-3">
        ${t.primary_colors.map(c => `
          <div onclick="copyText('${c.hex}', 'Copied ${c.hex}')" class="flex items-center gap-2.5 p-2 rounded-lg bg-white border border-[#e5e7eb] hover:border-[#0070f3]/50 cursor-pointer transition-all shadow-xs">
            <span class="w-6 h-6 rounded-md border border-black/10 shrink-0 shadow-xs" style="background-color: ${c.hex}"></span>
            <div class="overflow-hidden">
              <div class="text-xs font-mono font-bold text-[#111827]">${c.hex}</div>
              <div class="text-[10px] text-[#6b7280] truncate">${c.role}</div>
            </div>
          </div>
        `).join('')}
      </div>

      <div class="text-[11px] font-semibold text-[#6b7280] mb-1.5">Secondary & Surface Palette:</div>
      <div class="grid grid-cols-1 sm:grid-cols-2 gap-2">
        ${t.secondary_colors.map(c => `
          <div onclick="copyText('${c.hex}', 'Copied ${c.hex}')" class="flex items-center gap-2.5 p-2 rounded-lg bg-white border border-[#e5e7eb] hover:border-[#0070f3]/50 cursor-pointer transition-all shadow-xs">
            <span class="w-6 h-6 rounded-md border border-black/10 shrink-0 shadow-xs" style="background-color: ${c.hex}"></span>
            <div class="overflow-hidden">
              <div class="text-xs font-mono font-bold text-[#111827]">${c.hex}</div>
              <div class="text-[10px] text-[#6b7280] truncate">${c.role}</div>
            </div>
          </div>
        `).join('')}
      </div>
    </div>

    <!-- Typography System -->
    <div class="bg-[#f9fafb] border border-[#e5e7eb] rounded-xl p-4 mb-6">
      <h4 class="text-xs font-bold uppercase tracking-wider text-[#111827] mb-3 flex items-center gap-1.5 font-mono">
        <i data-lucide="type" class="w-3.5 h-3.5 text-[#0070f3]"></i>
        Typography System
      </h4>
      <div class="space-y-2 text-xs">
        <div class="flex justify-between py-1 border-b border-[#e5e7eb]">
          <span class="text-[#6b7280]">Display Font:</span>
          <span class="text-[#111827] font-mono text-[11px] font-medium">${t.typography.font_family_display}</span>
        </div>
        <div class="flex justify-between py-1 border-b border-[#e5e7eb]">
          <span class="text-[#6b7280]">Body Font:</span>
          <span class="text-[#111827] font-mono text-[11px] font-medium">${t.typography.font_family_body}</span>
        </div>
        <div class="flex justify-between py-1 border-b border-[#e5e7eb]">
          <span class="text-[#6b7280]">Mono Font:</span>
          <span class="text-[#111827] font-mono text-[11px] font-medium">${t.typography.font_family_mono}</span>
        </div>
        <div class="py-1">
          <span class="text-[#6b7280] block mb-0.5">Scale & Hierarchy:</span>
          <span class="text-[#374151] text-[11px] leading-relaxed">${t.typography.scale}</span>
        </div>
      </div>
    </div>

    <!-- Component Language Matrix -->
    <div class="bg-[#f9fafb] border border-[#e5e7eb] rounded-xl p-4 mb-6">
      <h4 class="text-xs font-bold uppercase tracking-wider text-[#111827] mb-3 flex items-center gap-1.5 font-mono">
        <i data-lucide="component" class="w-3.5 h-3.5 text-[#0070f3]"></i>
        Component Language
      </h4>
      <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs">
        <div class="p-3 rounded-lg bg-white border border-[#e5e7eb] shadow-xs">
          <span class="font-bold text-[#0070f3] block mb-1">Buttons:</span>
          <p class="text-[#4b5563] text-[11px] leading-relaxed">${t.components.buttons}</p>
        </div>
        <div class="p-3 rounded-lg bg-white border border-[#e5e7eb] shadow-xs">
          <span class="font-bold text-[#0070f3] block mb-1">Cards:</span>
          <p class="text-[#4b5563] text-[11px] leading-relaxed">${t.components.cards}</p>
        </div>
        <div class="p-3 rounded-lg bg-white border border-[#e5e7eb] shadow-xs">
          <span class="font-bold text-[#0070f3] block mb-1">Navigation:</span>
          <p class="text-[#4b5563] text-[11px] leading-relaxed">${t.components.navigation}</p>
        </div>
        <div class="p-3 rounded-lg bg-white border border-[#e5e7eb] shadow-xs">
          <span class="font-bold text-[#0070f3] block mb-1">Hero Section:</span>
          <p class="text-[#4b5563] text-[11px] leading-relaxed">${t.components.hero_section}</p>
        </div>
      </div>
    </div>

    <!-- Do's & Don'ts -->
    <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 mb-6 text-xs">
      <div class="p-4 rounded-xl bg-emerald-50 border border-emerald-200">
        <span class="font-bold text-emerald-800 flex items-center gap-1.5 mb-2">
          <i data-lucide="check-circle-2" class="w-4 h-4"></i> Things to Reuse
        </span>
        <ul class="space-y-1 text-[11px] text-emerald-900">
          ${t.things_to_reuse.map(r => `<li>• ${r}</li>`).join('')}
        </ul>
      </div>
      <div class="p-4 rounded-xl bg-rose-50 border border-rose-200">
        <span class="font-bold text-rose-800 flex items-center gap-1.5 mb-2">
          <i data-lucide="alert-triangle" class="w-4 h-4"></i> Things NOT to Copy
        </span>
        <ul class="space-y-1 text-[11px] text-rose-900">
          ${t.things_not_to_copy.map(n => `<li>• ${n}</li>`).join('')}
        </ul>
      </div>
    </div>

    <!-- Implementation Notes -->
    <div class="bg-[#f9fafb] border border-[#e5e7eb] rounded-xl p-4 mb-6">
      <h4 class="text-xs font-bold uppercase tracking-wider text-[#111827] mb-2 flex items-center gap-1.5 font-mono">
        <i data-lucide="code" class="w-3.5 h-3.5 text-[#0070f3]"></i>
        Implementation & Styling Notes
      </h4>
      <p class="text-xs text-[#374151] leading-relaxed font-mono text-[11px] bg-white p-3 rounded-lg border border-[#e5e7eb]">${t.implementation_notes}</p>
    </div>
  `;

  themeModal.classList.remove('hidden');
  setTimeout(() => themeModal.classList.add('open'), 10);
  lucide.createIcons();
}

function toggleIframe(url) {
  const ssView = document.getElementById('screenshotView');
  const ifView = document.getElementById('iframeView');
  const iframe = document.getElementById('liveIframe');
  const btn = document.getElementById('iframeToggleBtn');

  if (ifView.classList.contains('hidden')) {
    ssView.classList.add('hidden');
    ifView.classList.remove('hidden');
    iframe.src = url;
    btn.innerHTML = `<i data-lucide="image" class="w-3 h-3"></i> Show Static Screenshot`;
  } else {
    ifView.classList.add('hidden');
    ssView.classList.remove('hidden');
    iframe.src = '';
    btn.innerHTML = `<i data-lucide="play-circle" class="w-3 h-3"></i> Load Live Interactive Frame`;
  }
  lucide.createIcons();
}

function closeDetailModal() {
  themeModal.classList.remove('open');
  setTimeout(() => themeModal.classList.add('hidden'), 200);
}

function toggleCompare(themeId) {
  const existingIdx = compareList.findIndex(c => c.theme_id === themeId);
  if (existingIdx >= 0) {
    compareList.splice(existingIdx, 1);
    showToast(`Removed Theme ${themeId} from compare`);
  } else {
    if (compareList.length >= 2) {
      compareList.shift();
    }
    const t = allThemes.find(item => item.theme_id === themeId);
    if (t) compareList.push(t);
    showToast(`Added Theme ${themeId} to compare`);
  }
  compareCount.textContent = compareList.length;
  renderThemes(false);
}

function renderCompareModal() {
  compareGrid.innerHTML = compareList.map(t => {
    const screenshotUrl = getPrimaryScreenshotUrl(t.url);
    const domain = cleanDomain(t.url);
    return `
      <div class="bg-white border border-[#e5e7eb] rounded-xl overflow-hidden flex flex-col gap-4 shadow-sm">
        <div class="h-36 overflow-hidden border-b border-[#e5e7eb] relative bg-[#f9fafb]">
          <img src="${screenshotUrl}" alt="${t.name}" class="w-full h-full object-cover object-top" />
          <div class="absolute top-2 left-2 px-2 py-0.5 rounded bg-white/90 backdrop-blur-md text-[#111827] font-mono font-bold text-xs border border-[#e5e7eb] shadow-xs">
            ${t.theme_display_id}
          </div>
        </div>

        <div class="p-5 flex flex-col gap-4">
          <div class="flex items-center justify-between border-b border-[#e5e7eb] pb-3">
            <h3 class="text-lg font-bold text-[#111827] tracking-display">${t.name}</h3>
            <a href="${t.url}" target="_blank" class="text-xs text-[#0070f3] hover:underline flex items-center gap-1">
              <span>${domain}</span>
              <i data-lucide="external-link" class="w-3 h-3"></i>
            </a>
          </div>

          <div class="text-xs">
            <span class="font-bold text-[#0070f3] block mb-1">Design DNA:</span>
            <p class="text-[#4b5563] leading-relaxed">${t.overall_design_dna}</p>
          </div>

          <div class="text-xs">
            <span class="font-bold text-[#6b7280] block mb-1.5">Primary Palette:</span>
            <div class="flex items-center gap-2">
              ${t.primary_colors.map(c => `
                <span class="px-2 py-1 rounded bg-[#f9fafb] border border-[#e5e7eb] text-[10px] font-mono flex items-center gap-1 text-[#111827]">
                  <span class="w-3 h-3 rounded-full shadow-xs" style="background-color: ${c.hex}"></span>
                  ${c.hex}
                </span>
              `).join('')}
            </div>
          </div>

          <div class="text-xs">
            <span class="font-bold text-[#6b7280] block mb-1">Typography:</span>
            <p class="text-[#374151] text-[11px] font-mono">${t.typography.font_family_display}</p>
          </div>

          <button onclick="copyAiPrompt('${t.theme_id}')" class="mt-2 w-full py-2 rounded-lg bg-[#0070f3] hover:bg-[#0060df] text-white text-xs font-semibold shadow-xs">
            Copy ${t.theme_id} Prompt
          </button>
        </div>
      </div>
    `;
  }).join('');
  lucide.createIcons();
}

function copyText(text, msg = 'Copied to clipboard!') {
  navigator.clipboard.writeText(text).then(() => {
    showToast(msg);
  });
}

function copyAiPrompt(themeId) {
  const t = allThemes.find(item => item.theme_id === themeId);
  if (!t) return;
  const prompt = generateDetailedAiPrompt(t);
  copyText(prompt, `Copied Complete High-Fidelity Prompt for ${t.theme_display_id}`);
}

function showToast(msg) {
  toastMessage.textContent = msg;
  toast.classList.remove('translate-y-20', 'opacity-0');
  setTimeout(() => {
    toast.classList.add('translate-y-20', 'opacity-0');
  }, 2500);
}

document.addEventListener('DOMContentLoaded', initApp);
