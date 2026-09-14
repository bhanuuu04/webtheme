# THEME #065 --- GitHub

- **Website URL:** [https://github.com/](https://github.com/)
- **Category:** SaaS / Product
- **Design Style:** Dark Precision Keyboard-First SaaS
- **Mode:** dark
- **Tags:** `saas-product`, `dark`, `saas`

---

## 🧬 Theme DNA Summary
> **GitHub design DNA: Large typography, generous whitespace, monochrome palette, subtle borders, restrained motion, asymmetric hero composition and strong product-focused visual hierarchy.**

---

## 🔑 Signature Visual Element
Dark developer canvas (#0d1117) with green contribution graph (#238636 accent). Repository card grids, code block snippets with syntax highlighting, and the iconic octocat silhouette. Developer-native density with clean monospace type.

---

## 🎭 Emotional Intent
Community, craft, open collaboration. The developer feels at home — GitHub is where code lives. The design radiates technical legitimacy and open-source community spirit.

---

## 🎯 Design Principles ("Why does this look like this?")
Why GitHub looks like this: Built to communicate speed, craft, and keyboard-first productivity by removing clutter and focusing on high contrast, micro-details, and crisp dark backgrounds.

---

## 🎨 Color System

### Primary Palette
- **`#ffffff`** --- Light Clean Canvas
- **`#0070f3`** --- Geist Blue Accent
- **`#111827`** --- Deep Charcoal Text

### Secondary & Surface Palette
- **`#151618`** --- Card Surface
- **`#222326`** --- Subtle Border
- **`#8a8f98`** --- Muted Secondary Text

### CSS Custom Properties
```css
:root {
  --bg: #0d1117;
  --surface: #161b22;
  --border: #30363d;
  --accent: #238636;
  --link: #58a6ff;
  --text-primary: #c9d1d9;
  --text-muted: #8b949e;
  --radius-sm: 4px;
  --radius-md: 6px;
}
```

---

## 🔤 Typography System
- **Display Font:** `'Inter', -apple-system, BlinkMacSystemFont, sans-serif`
- **Body Font:** `'Inter', -apple-system, BlinkMacSystemFont, sans-serif`
- **Monospace Font:** `'JetBrains Mono', 'SF Mono', monospace`
- **Hierarchy & Scale:** Hero: 56-72px (-0.035em), H1: 36-40px, H2: 24-28px, Body: 14-15px, Mono: 12-13px
- **Weights:** 400 Regular, 500 Medium, 600 SemiBold
- **Letter Spacing:** -0.03em for display headings, -0.01em for body text, 0 for mono

**Copy Voice:** Developer-first, community-focused. 'Where the world builds software.' Open-source values language. Technical precision. CTAs: 'Sign up for free', 'Start a free trial', 'Contact sales'. Avoids marketing fluff entirely.

---

## 📐 Spacing & Layout Structure
- **Grid System:** 12-column responsive grid, max-width 1240px, 20px gutters
- **Padding Scale:** 2px (hairline), 4px, 8px, 16px, 24px (cards), 48px, 96px (sections)
- **Whitespace Philosophy:** High information density balanced by structured syntax blocks and generous vertical margins.

---

## 🧩 Component Language

### Buttons
6px rounded micro-pills with 1px border (#222326), solid primary accent with white text, or frosted translucent glass.

### Cards
Subtle 1px border (rgba(255,255,255,0.08)), obsidian dark surface (#151618), radial hover glow spotlight.

### Forms & Inputs
Minimal dark inputs with 1px border (#28282c), focus ring in primary accent with 2px offset.

### Navigation & Header
44px sticky frosted header (backdrop-blur-md, bg-black/60), minimal logo left, keyboard shortcuts right.

### Hero Section
Asymmetric hero with glowing radial gradient spotlight, high-impact headline, interactive app viewport mockup.

### Footer
Structured 4-5 column dark footer with system status indicator dot and keyboard shortcut badge.

---

## 🏗️ Page Architecture
1. Nav: dark #161b22, GitHub logo + search + nav links, avatar right
2. Hero: dark, bold headline, green CTA, contribution graph graphic
3. Feature sections: alternating dark panels with code snippets + description
4. Repository card grid: 3-col cards with language color dot, stars, forks
5. Open source showcase: project cards with contributor avatars
6. Enterprise feature panel: dark, security/compliance callouts
7. Pricing: 3-col, green border on featured tier
8. Footer: dark 5-col minimal

---

## 🚫 Anti-Patterns (What NOT to do)
- No light background sections — fully dark throughout
- No decorative gradients or blob shapes
- No photography — illustrations and product screenshots only
- No serif fonts — monospace + system-ui only
- No large padding — developer density is expected
- No color-heavy UI — monochrome with selective green/blue accents only

---

## ⚡ Motion & Animation
- **Transitions:** 120ms-180ms cubic-bezier(0.16, 1, 0.3, 1) ease-out
- **Scroll Behavior:** Staggered fade-up reveal on scroll with 40ms index delay, zero parallax blur.
- **Micro-Interactions:** Instant 80ms active scale down (0.98), keyboard shortcut badge pulse, active row highlight.

---

## 📱 Responsive Strategy
- **Mobile:** Bottom sheet drawers, collapsible sidebars, single column stacked cards, 44px touch targets.
- **Desktop:** Full keyboard navigation (⌘K command palette), multi-pane issue columns, split view inspect.

---

## 🚀 Best Use Cases
- Developer tools
- Issue trackers
- Productivity suites
- High-craft B2B SaaS
- Command bar tools
- GitHub-inspired applications
- SaaS / Product platforms

---

## ✅ Things To Reuse
  * 1px glowing border cards
  * Keyboard shortcut UI badges
  * Obsidian color system
  * Radial hero glow spotlight

---

## ❌ Things NOT To Copy
  * Proprietary GitHub brand logos
  * Exact GitHub copyrighted assets
  * Direct company trademarks

---

## 🛠️ Implementation Notes
Development Guide: Use Tailwind bg-[#08090a], border-white/10, hover:border-white/20, font-inter with -tracking-[0.02em] and lucide-react icons.

---

## 🤖 Deep Comprehensive AI Prompt
```text
[SYSTEM INSTRUCTION: SINGLE-SOURCE THEME DESIGN ADAPTER]
You are a Principal UI/UX Architect & Frontend Design System Engineer.
Your task is to analyze the user's current project / objective, and TRANSFORM / REDESIGN its entire frontend style, visual aesthetic, UX feeling, and component architecture strictly using the design system DNA of THEME #065 (GitHub - https://github.com/).

Maintain 100% strict theme isolation: extract and apply ONLY this reference theme's design language, tokens, and aesthetic principles.

==================================================================
🎯 CORE OBJECTIVE: ADAPT THEME TO USER'S PROJECT (NOT A BLIND CLONE)
==================================================================
1. ANALYZE CURRENT PROJECT & GOAL:
   - Carefully inspect the user's current project codebase, wireframes, or feature requirements (e.g. e-commerce clothing store selling shirts, SaaS tool, personal portfolio, marketplace, dashboard, etc.).
   - Preserve the user's core project purpose, domain data, functional workflows, and business logic.

2. TRANSLATE DESIGN DNA (DO NOT COPY PROPRIETARY CONTENT):
   - Do NOT blindly copy placeholder copy, trademarks, or unrelated product catalog from GitHub (e.g., do not insert "GitHub" branding or unrelated product listings).
   - DO extract and adopt 100% of GitHub's visual craft, color palette, typography hierarchy, card structures, spacing rhythm, surface depth, micro-interactions, and UX feeling.

3. ELEVATE & RESKIN EVERY COMPONENT:
   - Reskin the user's existing components (navbars, heroes, product/feature cards, buttons, filters, inputs, modals, footers) into the authentic visual language of THEME #065.
   - Example: If the user's project is an apparel store selling shirts, design a high-craft shirt catalog with GitHub's signature layouts, typography scale, lighting, and button styles.

==================================================================
🧬 THEME #065 IDENTITY & EMOTIONAL BRIEF
==================================================================
- Permanent Theme ID: THEME #065
- Reference Design Source: GitHub (https://github.com/)
- Mode: dark
- Archetype / Category: SaaS / Product
- Design Style: Dark Precision Keyboard-First SaaS
- Visual Personality: GitHub signature design: dark precision keyboard-first saas, engineered with high-craft aesthetics, structured hierarchy, and platform-native ergonomics.
- Core Design DNA: GitHub design DNA: Large typography, generous whitespace, monochrome palette, subtle borders, restrained motion, asymmetric hero composition and strong product-focused visual hierarchy.

THE SIGNATURE VISUAL ELEMENT (What makes this theme unmistakably GitHub):
Dark developer canvas (#0d1117) with green contribution graph (#238636 accent). Repository card grids, code block snippets with syntax highlighting, and the iconic octocat silhouette. Developer-native density with clean monospace type.

EMOTIONAL INTENT (How the user should FEEL when they see this design):
Community, craft, open collaboration. The developer feels at home — GitHub is where code lives. The design radiates technical legitimacy and open-source community spirit.

==================================================================
🎨 COLOR SYSTEM & APPLICATION RULES
==================================================================
#0d1117  ->  body background, all main sections
#238636  ->  primary CTA buttons (solid), success states, contribution squares, action confirmations
#c9d1d9  ->  all body text, headings, nav links
#161b22  ->  card surfaces, repo cards, modal backgrounds
#30363d  ->  borders, input outlines, dividers
#8b949e  ->  secondary text, metadata, timestamps, muted labels
#58a6ff  ->  links, secondary accents, code references, PR/issue numbers

CSS Custom Properties (paste into :root {}):
:root {
  --bg: #0d1117;
  --surface: #161b22;
  --border: #30363d;
  --accent: #238636;
  --link: #58a6ff;
  --text-primary: #c9d1d9;
  --text-muted: #8b949e;
  --radius-sm: 4px;
  --radius-md: 6px;
}

Tailwind Config Extension (add inside extend: {}):
colors: { bg: '#0d1117', surface: '#161b22', border: '#30363d', accent: '#238636', link: '#58a6ff', primary: '#c9d1d9', muted: '#8b949e' }

==================================================================
🔤 TYPOGRAPHY & TEXT RHYTHM
==================================================================
- Display / Headline Font: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif
- Body Copy Font: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif
- Monospace / Data Font: 'JetBrains Mono', 'SF Mono', monospace
- Optical Tracking (Letter Spacing): -0.03em for display headings, -0.01em for body text, 0 for mono
- Scale & Proportions: Hero: 56-72px (-0.035em), H1: 36-40px, H2: 24-28px, Body: 14-15px, Mono: 12-13px
- Font Weights: 400 Regular, 500 Medium, 600 SemiBold

Copy Voice & Tone (match this style in ALL generated text content):
Developer-first, community-focused. 'Where the world builds software.' Open-source values language. Technical precision. CTAs: 'Sign up for free', 'Start a free trial', 'Contact sales'. Avoids marketing fluff entirely.

==================================================================
📐 SPACING, GRID & GEOMETRY
==================================================================
- Container Max-Width & Grid: 12-column responsive grid, max-width 1240px, 20px gutters
- Vertical Padding Scale: 2px (hairline), 4px, 8px, 16px, 24px (cards), 48px, 96px (sections)
- Whitespace Philosophy: High information density balanced by structured syntax blocks and generous vertical margins.

==================================================================
🧩 COMPONENT ARCHETYPE MAPPING
==================================================================
- Buttons (Primary, Secondary, Ghost): 6px rounded micro-pills with 1px border (#222326), solid primary accent with white text, or frosted translucent glass.
- Cards, Modules & Bento Grids: Subtle 1px border (rgba(255,255,255,0.08)), obsidian dark surface (#151618), radial hover glow spotlight.
- Header & Navigation System: 44px sticky frosted header (backdrop-blur-md, bg-black/60), minimal logo left, keyboard shortcuts right.
- Hero / Showcase Composition: Asymmetric hero with glowing radial gradient spotlight, high-impact headline, interactive app viewport mockup.
- Forms, Filters & Pill Selectors: Minimal dark inputs with 1px border (#28282c), focus ring in primary accent with 2px offset.
- Footer & System Status: Structured 4-5 column dark footer with system status indicator dot and keyboard shortcut badge.

Icon System: Lucide Icons, 1.5px stroke, 16px default, strictly monochrome
Image Treatment: High-fidelity dark app UI screenshots and interactive canvas viewports only. No stock photography.

==================================================================
⚡ MOTION PHYSICS & MICRO-INTERACTIONS
==================================================================
- Transitions & Easing: 120ms-180ms cubic-bezier(0.16, 1, 0.3, 1) ease-out
  Apply as: transition: all 150ms cubic-bezier(0.16, 1, 0.3, 1) on all interactive elements
- Card Hover: transform: translateY(-2px) + box-shadow escalation
- Button Press: transform: scale(0.97), transition: 80ms ease-in
- Modal Entry: opacity 0 to 1 + translateY(8px to 0px), 200ms
- Scroll Reveals: IntersectionObserver threshold 0.1, staggered 60ms per sibling
- Scroll Behavior: Staggered fade-up reveal on scroll with 40ms index delay, zero parallax blur.
- Micro-Interactions: Instant 80ms active scale down (0.98), keyboard shortcut badge pulse, active row highlight.

==================================================================
📱 RESPONSIVE ADAPTATION
==================================================================
- Mobile Layout Strategy: Bottom sheet drawers, collapsible sidebars, single column stacked cards, 44px touch targets.
- Desktop Ergonomics: Full keyboard navigation (⌘K command palette), multi-pane issue columns, split view inspect.

==================================================================
🏗️ PAGE ARCHITECTURE (ordered section scaffold for a typical page)
==================================================================
1. Nav: dark #161b22, GitHub logo + search + nav links, avatar right
2. Hero: dark, bold headline, green CTA, contribution graph graphic
3. Feature sections: alternating dark panels with code snippets + description
4. Repository card grid: 3-col cards with language color dot, stars, forks
5. Open source showcase: project cards with contributor avatars
6. Enterprise feature panel: dark, security/compliance callouts
7. Pricing: 3-col, green border on featured tier
8. Footer: dark 5-col minimal

==================================================================
ANTI-PATTERNS (what NOT to do -- these break theme authenticity)
==================================================================
  X No light background sections — fully dark throughout
  X No decorative gradients or blob shapes
  X No photography — illustrations and product screenshots only
  X No serif fonts — monospace + system-ui only
  X No large padding — developer density is expected
  X No color-heavy UI — monochrome with selective green/blue accents only

==================================================================
🛡️ DESIGN FIDELITY GUARDRAILS
==================================================================
- MUST ADOPT & REUSE:
  * 1px glowing border cards
  * Keyboard shortcut UI badges
  * Obsidian color system
  * Radial hero glow spotlight
- DO NOT COPY (Proprietary / Brand Specific):
  * Proprietary GitHub brand logos
  * Exact GitHub copyrighted assets
  * Direct company trademarks
- TECHNICAL IMPLEMENTATION GUIDANCE:
  Development Guide: Use Tailwind bg-[#08090a], border-white/10, hover:border-white/20, font-inter with -tracking-[0.02em] and lucide-react icons.

==================================================================
🛠️ STEP-BY-STEP REFACTORING INSTRUCTIONS
==================================================================
1. READ the user's current project files, identify domain, existing components, and tech stack.
2. INJECT the CSS custom properties above into the global stylesheet or Tailwind config.
3. RE-ARCHITECT each layout section to match the page architecture scaffold above.
4. RE-ENGINEER every UI component (nav, hero, cards, buttons, inputs, footer) into the GitHub visual language while keeping the user's real content, data, and workflows intact.
5. APPLY motion physics (transitions, hover states, scroll reveals) as specified above.
6. WRITE all page copy in the Copy Voice defined above -- match the tone, not the brand name.
7. VERIFY: The output should feel unmistakably like GitHub's design aesthetic applied to the user's own project domain.

==================================================================
📦 DELIVERABLE DEFINITION
==================================================================
Include a code snippet display component — it's central to GitHub's visual identity. Syntax highlighting colors: comments #8b949e, strings #a5d6ff, keywords #ff7b72.
```
