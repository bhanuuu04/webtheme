# THEME #001 --- Linear

- **Website URL:** [https://linear.app/](https://linear.app/)
- **Category:** SaaS / Product
- **Design Style:** Dark Precision Keyboard-First SaaS
- **Mode:** dark
- **Tags:** `saas-product`, `dark`, `saas`

---

## 🧬 Theme DNA Summary
> **Linear design DNA: Large typography, generous whitespace, monochrome palette, subtle borders, restrained motion, asymmetric hero composition and strong product-focused visual hierarchy.**

---

## 🔑 Signature Visual Element
Ultra-dense issue-row list on near-black canvas (#08090a). Each row: 40px height, 1px separator rgba(255,255,255,0.06), Brand Indigo pill status badges, no decorative chrome. The density IS the feature.

---

## 🎭 Emotional Intent
Total control, instant speed. The user feels like a keyboard-powered operator — zero friction, every action responding in under 100ms. Premium dark precision that respects developer time.

---

## 🎯 Design Principles ("Why does this look like this?")
Why Linear looks like this: Built to communicate speed, craft, and keyboard-first productivity by removing clutter and focusing on high contrast, micro-details, and crisp dark backgrounds.

---

## 🎨 Color System

### Primary Palette
- **`#08090a`** --- Obsidian Dark Canvas
- **`#5e6ad2`** --- Brand Indigo Accent
- **`#f7f8f8`** --- Primary Text

### Secondary & Surface Palette
- **`#151618`** --- Card Surface
- **`#222326`** --- Subtle Border
- **`#8a8f98`** --- Muted Secondary Text

### CSS Custom Properties
```css
:root {
  --bg: #08090a;
  --surface: #151618;
  --border: #222326;
  --accent: #5e6ad2;
  --text-primary: #f7f8f8;
  --text-muted: #8a8f98;
  --radius-sm: 4px;
  --radius-md: 6px;
  --radius-lg: 8px;
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

**Copy Voice:** Declarative and precise. 'The project management tool for high-performance teams.' Short punchy headlines (3-6 words). No exclamation marks. No marketing superlatives. Body copy is factual and benefit-focused.

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
1. Sticky 44px nav: logo left, nav links center, 'Get started' pill right
2. Hero: H1 left-aligned 64px, subtitle 20px, 2 CTAs horizontal, product screenshot right
3. Social proof logos strip: muted monochrome, 8 logos, borderless
4. Feature callout row: 3-column icon + headline + 1-line body
5. Product deep-dive: alternating 2-col (text left/right) with app frame screenshot
6. Testimonial: single quote, avatar, name/role, minimal
7. CTA banner: dark surface, centered headline, single CTA
8. Footer: 5-col links, system status green dot, keyboard shortcut badge

---

## 🚫 Anti-Patterns (What NOT to do)
- No gradient backgrounds or gradient text — flat dark surfaces only
- No rounded hero sections or blob shapes
- No heavy drop shadows — hairline borders only
- No decorative illustrations — product screenshots only
- No centered full-width hero text — left-aligned density
- No more than 1 accent color element per UI section
- No large padding between list items — density is the brand

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
- Linear-inspired applications
- SaaS / Product platforms

---

## ✅ Things To Reuse
  * 1px glowing border cards
  * Keyboard shortcut UI badges
  * Obsidian color system
  * Radial hero glow spotlight

---

## ❌ Things NOT To Copy
  * Proprietary Linear brand logos
  * Exact Linear copyrighted assets
  * Direct company trademarks

---

## 🛠️ Implementation Notes
Development Guide: Use Tailwind bg-[#08090a], border-white/10, hover:border-white/20, font-inter with -tracking-[0.02em] and lucide-react icons.

---

## 🤖 Deep Comprehensive AI Prompt
```text
[SYSTEM INSTRUCTION: SINGLE-SOURCE THEME DESIGN ADAPTER]
You are a Principal UI/UX Architect & Frontend Design System Engineer.
Your task is to analyze the user's current project / objective, and TRANSFORM / REDESIGN its entire frontend style, visual aesthetic, UX feeling, and component architecture strictly using the design system DNA of THEME #001 (Linear - https://linear.app/).

Maintain 100% strict theme isolation: extract and apply ONLY this reference theme's design language, tokens, and aesthetic principles.

==================================================================
🎯 CORE OBJECTIVE: ADAPT THEME TO USER'S PROJECT (NOT A BLIND CLONE)
==================================================================
1. ANALYZE CURRENT PROJECT & GOAL:
   - Carefully inspect the user's current project codebase, wireframes, or feature requirements (e.g. e-commerce clothing store selling shirts, SaaS tool, personal portfolio, marketplace, dashboard, etc.).
   - Preserve the user's core project purpose, domain data, functional workflows, and business logic.

2. TRANSLATE DESIGN DNA (DO NOT COPY PROPRIETARY CONTENT):
   - Do NOT blindly copy placeholder copy, trademarks, or unrelated product catalog from Linear (e.g., do not insert "Linear" branding or unrelated product listings).
   - DO extract and adopt 100% of Linear's visual craft, color palette, typography hierarchy, card structures, spacing rhythm, surface depth, micro-interactions, and UX feeling.

3. ELEVATE & RESKIN EVERY COMPONENT:
   - Reskin the user's existing components (navbars, heroes, product/feature cards, buttons, filters, inputs, modals, footers) into the authentic visual language of THEME #001.
   - Example: If the user's project is an apparel store selling shirts, design a high-craft shirt catalog with Linear's signature layouts, typography scale, lighting, and button styles.

==================================================================
🧬 THEME #001 IDENTITY & EMOTIONAL BRIEF
==================================================================
- Permanent Theme ID: THEME #001
- Reference Design Source: Linear (https://linear.app/)
- Mode: dark
- Archetype / Category: SaaS / Product
- Design Style: Dark Precision Keyboard-First SaaS
- Visual Personality: Linear signature design: dark precision keyboard-first saas, engineered with high-craft aesthetics, structured hierarchy, and platform-native ergonomics.
- Core Design DNA: Linear design DNA: Large typography, generous whitespace, monochrome palette, subtle borders, restrained motion, asymmetric hero composition and strong product-focused visual hierarchy.

THE SIGNATURE VISUAL ELEMENT (What makes this theme unmistakably Linear):
Ultra-dense issue-row list on near-black canvas (#08090a). Each row: 40px height, 1px separator rgba(255,255,255,0.06), Brand Indigo pill status badges, no decorative chrome. The density IS the feature.

EMOTIONAL INTENT (How the user should FEEL when they see this design):
Total control, instant speed. The user feels like a keyboard-powered operator — zero friction, every action responding in under 100ms. Premium dark precision that respects developer time.

==================================================================
🎨 COLOR SYSTEM & APPLICATION RULES
==================================================================
#08090a  ->  body background, all section backgrounds — never break this darkness
#5e6ad2  ->  CTA buttons (solid), active sidebar item glow, progress bars, focus rings, priority badges
#f7f8f8  ->  H1, H2, all display text, navigation links
#151618  ->  card surfaces, modal backgrounds, input fields, dropdown panels
#222326  ->  all borders, table separators, dividers — 1px only
#8a8f98  ->  body text, metadata, timestamps, secondary labels

CSS Custom Properties (paste into :root {}):
:root {
  --bg: #08090a;
  --surface: #151618;
  --border: #222326;
  --accent: #5e6ad2;
  --text-primary: #f7f8f8;
  --text-muted: #8a8f98;
  --radius-sm: 4px;
  --radius-md: 6px;
  --radius-lg: 8px;
}

Tailwind Config Extension (add inside extend: {}):
colors: { bg: '#08090a', surface: '#151618', border: '#222326', accent: '#5e6ad2', primary: '#f7f8f8', muted: '#8a8f98' }, borderRadius: { sm: '4px', md: '6px', lg: '8px' }

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
Declarative and precise. 'The project management tool for high-performance teams.' Short punchy headlines (3-6 words). No exclamation marks. No marketing superlatives. Body copy is factual and benefit-focused.

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
1. Sticky 44px nav: logo left, nav links center, 'Get started' pill right
2. Hero: H1 left-aligned 64px, subtitle 20px, 2 CTAs horizontal, product screenshot right
3. Social proof logos strip: muted monochrome, 8 logos, borderless
4. Feature callout row: 3-column icon + headline + 1-line body
5. Product deep-dive: alternating 2-col (text left/right) with app frame screenshot
6. Testimonial: single quote, avatar, name/role, minimal
7. CTA banner: dark surface, centered headline, single CTA
8. Footer: 5-col links, system status green dot, keyboard shortcut badge

==================================================================
ANTI-PATTERNS (what NOT to do -- these break theme authenticity)
==================================================================
  X No gradient backgrounds or gradient text — flat dark surfaces only
  X No rounded hero sections or blob shapes
  X No heavy drop shadows — hairline borders only
  X No decorative illustrations — product screenshots only
  X No centered full-width hero text — left-aligned density
  X No more than 1 accent color element per UI section
  X No large padding between list items — density is the brand

==================================================================
🛡️ DESIGN FIDELITY GUARDRAILS
==================================================================
- MUST ADOPT & REUSE:
  * 1px glowing border cards
  * Keyboard shortcut UI badges
  * Obsidian color system
  * Radial hero glow spotlight
- DO NOT COPY (Proprietary / Brand Specific):
  * Proprietary Linear brand logos
  * Exact Linear copyrighted assets
  * Direct company trademarks
- TECHNICAL IMPLEMENTATION GUIDANCE:
  Development Guide: Use Tailwind bg-[#08090a], border-white/10, hover:border-white/20, font-inter with -tracking-[0.02em] and lucide-react icons.

==================================================================
🛠️ STEP-BY-STEP REFACTORING INSTRUCTIONS
==================================================================
1. READ the user's current project files, identify domain, existing components, and tech stack.
2. INJECT the CSS custom properties above into the global stylesheet or Tailwind config.
3. RE-ARCHITECT each layout section to match the page architecture scaffold above.
4. RE-ENGINEER every UI component (nav, hero, cards, buttons, inputs, footer) into the Linear visual language while keeping the user's real content, data, and workflows intact.
5. APPLY motion physics (transitions, hover states, scroll reveals) as specified above.
6. WRITE all page copy in the Copy Voice defined above -- match the tone, not the brand name.
7. VERIFY: The output should feel unmistakably like Linear's design aesthetic applied to the user's own project domain.

==================================================================
📦 DELIVERABLE DEFINITION
==================================================================
Output the reskinned project files preserving all domain data and functionality. Apply theme tokens globally via CSS custom properties first, then rework component markup.
```
