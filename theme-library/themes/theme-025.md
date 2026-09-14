# THEME #025 --- Salesforce

- **Website URL:** [https://www.salesforce.com/](https://www.salesforce.com/)
- **Category:** SaaS / Product
- **Design Style:** Dark Precision Keyboard-First SaaS
- **Mode:** dark
- **Tags:** `saas-product`, `dark`, `saas`

---

## 🧬 Theme DNA Summary
> **Salesforce design DNA: Large typography, generous whitespace, monochrome palette, subtle borders, restrained motion, asymmetric hero composition and strong product-focused visual hierarchy.**

---

## 🔑 Signature Visual Element
Deep dark canvas (#08090a) with #5e6ad2 accent used exclusively on primary actions. Product screenshots or interface mockups as the primary visual element. High contrast between surface (#surface) and text creates the premium feel characteristic of Salesforce.

---

## 🎭 Emotional Intent
Technical precision and professional authority. The user feels Salesforce is built by people who understand their craft deeply. The dark aesthetic communicates focus, speed, and zero compromise on quality.

---

## 🎯 Design Principles ("Why does this look like this?")
Why Salesforce looks like this: Built to communicate speed, craft, and keyboard-first productivity by removing clutter and focusing on high contrast, micro-details, and crisp dark backgrounds.

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
  --radius-md: 8px;
  --radius-lg: 16px;
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

**Copy Voice:** Direct, technical authority. Short declarative headlines. Developer or professional-first language. Action CTAs: 'Get started', 'Try for free', 'Read docs'.

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
1. Nav: 44px sticky, logo left, product links, CTA right
2. Hero: headline (56-72px), subtitle, 2 CTAs, product screenshot
3. Social proof: company logos strip
4. Feature trio: 3-col icon + headline + body
5. Product deep-dive: alternating 2-col text + screenshot
6. Testimonials: card grid or single large quote
7. Pricing: 3-col tier table
8. Footer: 5-col link grid

---

## 🚫 Anti-Patterns (What NOT to do)
- No light/white background sections — maintain dark canvas throughout
- No heavy drop shadows — use hairline borders and surface elevation instead
- No busy gradient backgrounds — flat dark surfaces with selective glow accents only
- No decorative illustrations — use product screenshots or abstract geometric shapes
- No loose tracking on body text — keep optical letter-spacing tight
- No more than 2 accent-colored elements visible in the same viewport

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
- Salesforce-inspired applications
- SaaS / Product platforms

---

## ✅ Things To Reuse
  * 1px glowing border cards
  * Keyboard shortcut UI badges
  * Obsidian color system
  * Radial hero glow spotlight

---

## ❌ Things NOT To Copy
  * Proprietary Salesforce brand logos
  * Exact Salesforce copyrighted assets
  * Direct company trademarks

---

## 🛠️ Implementation Notes
Development Guide: Use Tailwind bg-[#08090a], border-white/10, hover:border-white/20, font-inter with -tracking-[0.02em] and lucide-react icons.

---

## 🤖 Deep Comprehensive AI Prompt
```text
[SYSTEM INSTRUCTION: SINGLE-SOURCE THEME DESIGN ADAPTER]
You are a Principal UI/UX Architect & Frontend Design System Engineer.
Your task is to analyze the user's current project / objective, and TRANSFORM / REDESIGN its entire frontend style, visual aesthetic, UX feeling, and component architecture strictly using the design system DNA of THEME #025 (Salesforce - https://www.salesforce.com/).

Maintain 100% strict theme isolation: extract and apply ONLY this reference theme's design language, tokens, and aesthetic principles.

==================================================================
🎯 CORE OBJECTIVE: ADAPT THEME TO USER'S PROJECT (NOT A BLIND CLONE)
==================================================================
1. ANALYZE CURRENT PROJECT & GOAL:
   - Carefully inspect the user's current project codebase, wireframes, or feature requirements (e.g. e-commerce clothing store selling shirts, SaaS tool, personal portfolio, marketplace, dashboard, etc.).
   - Preserve the user's core project purpose, domain data, functional workflows, and business logic.

2. TRANSLATE DESIGN DNA (DO NOT COPY PROPRIETARY CONTENT):
   - Do NOT blindly copy placeholder copy, trademarks, or unrelated product catalog from Salesforce (e.g., do not insert "Salesforce" branding or unrelated product listings).
   - DO extract and adopt 100% of Salesforce's visual craft, color palette, typography hierarchy, card structures, spacing rhythm, surface depth, micro-interactions, and UX feeling.

3. ELEVATE & RESKIN EVERY COMPONENT:
   - Reskin the user's existing components (navbars, heroes, product/feature cards, buttons, filters, inputs, modals, footers) into the authentic visual language of THEME #025.
   - Example: If the user's project is an apparel store selling shirts, design a high-craft shirt catalog with Salesforce's signature layouts, typography scale, lighting, and button styles.

==================================================================
🧬 THEME #025 IDENTITY & EMOTIONAL BRIEF
==================================================================
- Permanent Theme ID: THEME #025
- Reference Design Source: Salesforce (https://www.salesforce.com/)
- Mode: dark
- Archetype / Category: SaaS / Product
- Design Style: Dark Precision Keyboard-First SaaS
- Visual Personality: Salesforce signature design: dark precision keyboard-first saas, engineered with high-craft aesthetics, structured hierarchy, and platform-native ergonomics.
- Core Design DNA: Salesforce design DNA: Large typography, generous whitespace, monochrome palette, subtle borders, restrained motion, asymmetric hero composition and strong product-focused visual hierarchy.

THE SIGNATURE VISUAL ELEMENT (What makes this theme unmistakably Salesforce):
Deep dark canvas (#08090a) with #5e6ad2 accent used exclusively on primary actions. Product screenshots or interface mockups as the primary visual element. High contrast between surface (#surface) and text creates the premium feel characteristic of Salesforce.

EMOTIONAL INTENT (How the user should FEEL when they see this design):
Technical precision and professional authority. The user feels Salesforce is built by people who understand their craft deeply. The dark aesthetic communicates focus, speed, and zero compromise on quality.

==================================================================
🎨 COLOR SYSTEM & APPLICATION RULES
==================================================================
#08090a  ->  page background, all section backgrounds
#5e6ad2  ->  primary CTA buttons, links on hover, focus rings, selected states, brand accents
#f7f8f8  ->  all headings (H1-H3), body text, primary UI labels
#151618  ->  card surfaces, modal backgrounds, input field backgrounds
#222326  ->  borders, dividers, separator lines — 1px only
#8a8f98  ->  secondary body text, metadata, timestamps, captions

CSS Custom Properties (paste into :root {}):
:root {
  --bg: #08090a;
  --surface: #151618;
  --border: #222326;
  --accent: #5e6ad2;
  --text-primary: #f7f8f8;
  --text-muted: #8a8f98;
  --radius-sm: 4px;
  --radius-md: 8px;
  --radius-lg: 16px;
}

Tailwind Config Extension (add inside extend: {}):
colors: { bg: '#08090a', surface: '#151618', accent: '#5e6ad2', primary: '#f7f8f8', muted: '#8a8f98' }

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
Direct, technical authority. Short declarative headlines. Developer or professional-first language. Action CTAs: 'Get started', 'Try for free', 'Read docs'.

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
1. Nav: 44px sticky, logo left, product links, CTA right
2. Hero: headline (56-72px), subtitle, 2 CTAs, product screenshot
3. Social proof: company logos strip
4. Feature trio: 3-col icon + headline + body
5. Product deep-dive: alternating 2-col text + screenshot
6. Testimonials: card grid or single large quote
7. Pricing: 3-col tier table
8. Footer: 5-col link grid

==================================================================
ANTI-PATTERNS (what NOT to do -- these break theme authenticity)
==================================================================
  X No light/white background sections — maintain dark canvas throughout
  X No heavy drop shadows — use hairline borders and surface elevation instead
  X No busy gradient backgrounds — flat dark surfaces with selective glow accents only
  X No decorative illustrations — use product screenshots or abstract geometric shapes
  X No loose tracking on body text — keep optical letter-spacing tight
  X No more than 2 accent-colored elements visible in the same viewport

==================================================================
🛡️ DESIGN FIDELITY GUARDRAILS
==================================================================
- MUST ADOPT & REUSE:
  * 1px glowing border cards
  * Keyboard shortcut UI badges
  * Obsidian color system
  * Radial hero glow spotlight
- DO NOT COPY (Proprietary / Brand Specific):
  * Proprietary Salesforce brand logos
  * Exact Salesforce copyrighted assets
  * Direct company trademarks
- TECHNICAL IMPLEMENTATION GUIDANCE:
  Development Guide: Use Tailwind bg-[#08090a], border-white/10, hover:border-white/20, font-inter with -tracking-[0.02em] and lucide-react icons.

==================================================================
🛠️ STEP-BY-STEP REFACTORING INSTRUCTIONS
==================================================================
1. READ the user's current project files, identify domain, existing components, and tech stack.
2. INJECT the CSS custom properties above into the global stylesheet or Tailwind config.
3. RE-ARCHITECT each layout section to match the page architecture scaffold above.
4. RE-ENGINEER every UI component (nav, hero, cards, buttons, inputs, footer) into the Salesforce visual language while keeping the user's real content, data, and workflows intact.
5. APPLY motion physics (transitions, hover states, scroll reveals) as specified above.
6. WRITE all page copy in the Copy Voice defined above -- match the tone, not the brand name.
7. VERIFY: The output should feel unmistakably like Salesforce's design aesthetic applied to the user's own project domain.

==================================================================
📦 DELIVERABLE DEFINITION
==================================================================
Apply CSS custom properties globally first. Then rework each component to match theme tokens. Preserve all domain data and business logic — only the visual layer changes.
```
