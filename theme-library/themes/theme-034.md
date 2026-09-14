# THEME #034 --- Cron

- **Website URL:** [https://cron.com/](https://cron.com/)
- **Category:** SaaS / Product
- **Design Style:** Clean Minimal Enterprise Product
- **Mode:** dark
- **Tags:** `saas-product`, `dark`, `minimal`, `saas`

---

## 🧬 Theme DNA Summary
> **Cron design DNA: Large typography, generous whitespace, monochrome palette, subtle borders, restrained motion, asymmetric hero composition and strong product-focused visual hierarchy.**

---

## 🔑 Signature Visual Element
Deep dark canvas (#08090a) with #5e6ad2 accent used exclusively on primary actions. Product screenshots or interface mockups as the primary visual element. High contrast between surface (#surface) and text creates the premium feel characteristic of Cron.

---

## 🎭 Emotional Intent
Technical precision and professional authority. The user feels Cron is built by people who understand their craft deeply. The dark aesthetic communicates focus, speed, and zero compromise on quality.

---

## 🎯 Design Principles ("Why does this look like this?")
Why Cron looks like this: Built to communicate speed, craft, and keyboard-first productivity by removing clutter and focusing on high contrast, micro-details, and crisp dark backgrounds.

---

## 🎨 Color System

### Primary Palette
- **`#08090a`** --- Obsidian Dark Canvas
- **`#5e6ad2`** --- Brand Indigo Accent
- **`#f7f8f8`** --- Primary Text

### Secondary & Surface Palette
- **`#f9fafb`** --- Card Surface Light
- **`#e5e7eb`** --- Border Light
- **`#6b7280`** --- Secondary Text

### CSS Custom Properties
```css
:root {
  --bg: #08090a;
  --surface: #f9fafb;
  --border: #e5e7eb;
  --accent: #5e6ad2;
  --text-primary: #f7f8f8;
  --text-muted: #6b7280;
  --radius-sm: 4px;
  --radius-md: 8px;
  --radius-lg: 16px;
}
```

---

## 🔤 Typography System
- **Display Font:** `'Geist Sans', 'Plus Jakarta Sans', 'Inter', sans-serif`
- **Body Font:** `'Geist Sans', 'Inter', sans-serif`
- **Monospace Font:** `'Geist Mono', 'Fira Code', monospace`
- **Hierarchy & Scale:** Hero: 60-84px (-0.04em), H1: 40px, H2: 28px, Body: 15-16px
- **Weights:** 400 Regular, 500 Medium, 600 SemiBold, 700 Bold
- **Letter Spacing:** -0.035em for headings, -0.01em for body text

**Copy Voice:** Direct, technical authority. Short declarative headlines. Developer or professional-first language. Action CTAs: 'Get started', 'Try for free', 'Read docs'.

---

## 📐 Spacing & Layout Structure
- **Grid System:** 12-column grid, max-width 1200px, 24px gutters
- **Padding Scale:** 4px, 8px, 16px, 24px, 40px, 80px, 120px
- **Whitespace Philosophy:** Pristine white canvas with generous negative space spotlighting typography clarity.

---

## 🧩 Component Language

### Buttons
Pill buttons with 6-8px radius, solid black with white text or pure white with 1px border.

### Cards
Pure white cards with 1px hairline border (#e5e7eb), subtle shadow on hover (0 4px 20px rgba(0,0,0,0.05)).

### Forms & Inputs
Crisp white inputs with light grey borders and blue or black focus rings.

### Navigation & Header
Clean top bar with logo, dropdown menus, and CTA on right.

### Hero Section
Centered large bold statement, 2-line subtitle, primary & secondary CTA pills, framework/tech logos.

### Footer
Clean 5-column link directory with copyright and status indicator.

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
- **Transitions:** 150ms ease-out
- **Scroll Behavior:** Clean reveal transitions with crisp 100ms timing, zero blur lag.
- **Micro-Interactions:** Subtle border color shift on hover (#e5e7eb to #111827), button ripple effect.

---

## 📱 Responsive Strategy
- **Mobile:** Clean slide-down mobile nav, single column feature cards, full-width buttons.
- **Desktop:** 1200px container, multi-column grid, hover card previews.

---

## 🚀 Best Use Cases
- Developer tools
- Issue trackers
- Productivity suites
- High-craft B2B SaaS
- Command bar tools
- Cron-inspired applications
- SaaS / Product platforms

---

## ✅ Things To Reuse
  * 1px glowing border cards
  * Keyboard shortcut UI badges
  * Obsidian color system
  * Radial hero glow spotlight

---

## ❌ Things NOT To Copy
  * Proprietary Cron brand logos
  * Exact Cron copyrighted assets
  * Direct company trademarks

---

## 🛠️ Implementation Notes
Development Guide: Use Tailwind bg-[#08090a], border-white/10, hover:border-white/20, font-inter with -tracking-[0.02em] and lucide-react icons.

---

## 🤖 Deep Comprehensive AI Prompt
```text
[SYSTEM INSTRUCTION: SINGLE-SOURCE THEME DESIGN ADAPTER]
You are a Principal UI/UX Architect & Frontend Design System Engineer.
Your task is to analyze the user's current project / objective, and TRANSFORM / REDESIGN its entire frontend style, visual aesthetic, UX feeling, and component architecture strictly using the design system DNA of THEME #034 (Cron - https://cron.com/).

Maintain 100% strict theme isolation: extract and apply ONLY this reference theme's design language, tokens, and aesthetic principles.

==================================================================
🎯 CORE OBJECTIVE: ADAPT THEME TO USER'S PROJECT (NOT A BLIND CLONE)
==================================================================
1. ANALYZE CURRENT PROJECT & GOAL:
   - Carefully inspect the user's current project codebase, wireframes, or feature requirements (e.g. e-commerce clothing store selling shirts, SaaS tool, personal portfolio, marketplace, dashboard, etc.).
   - Preserve the user's core project purpose, domain data, functional workflows, and business logic.

2. TRANSLATE DESIGN DNA (DO NOT COPY PROPRIETARY CONTENT):
   - Do NOT blindly copy placeholder copy, trademarks, or unrelated product catalog from Cron (e.g., do not insert "Cron" branding or unrelated product listings).
   - DO extract and adopt 100% of Cron's visual craft, color palette, typography hierarchy, card structures, spacing rhythm, surface depth, micro-interactions, and UX feeling.

3. ELEVATE & RESKIN EVERY COMPONENT:
   - Reskin the user's existing components (navbars, heroes, product/feature cards, buttons, filters, inputs, modals, footers) into the authentic visual language of THEME #034.
   - Example: If the user's project is an apparel store selling shirts, design a high-craft shirt catalog with Cron's signature layouts, typography scale, lighting, and button styles.

==================================================================
🧬 THEME #034 IDENTITY & EMOTIONAL BRIEF
==================================================================
- Permanent Theme ID: THEME #034
- Reference Design Source: Cron (https://cron.com/)
- Mode: dark
- Archetype / Category: SaaS / Product
- Design Style: Clean Minimal Enterprise Product
- Visual Personality: Cron signature design: clean minimal enterprise product, engineered with high-craft aesthetics, structured hierarchy, and platform-native ergonomics.
- Core Design DNA: Cron design DNA: Large typography, generous whitespace, monochrome palette, subtle borders, restrained motion, asymmetric hero composition and strong product-focused visual hierarchy.

THE SIGNATURE VISUAL ELEMENT (What makes this theme unmistakably Cron):
Deep dark canvas (#08090a) with #5e6ad2 accent used exclusively on primary actions. Product screenshots or interface mockups as the primary visual element. High contrast between surface (#surface) and text creates the premium feel characteristic of Cron.

EMOTIONAL INTENT (How the user should FEEL when they see this design):
Technical precision and professional authority. The user feels Cron is built by people who understand their craft deeply. The dark aesthetic communicates focus, speed, and zero compromise on quality.

==================================================================
🎨 COLOR SYSTEM & APPLICATION RULES
==================================================================
#08090a  ->  page background, all section backgrounds
#5e6ad2  ->  primary CTA buttons, links on hover, focus rings, selected states, brand accents
#f7f8f8  ->  all headings (H1-H3), body text, primary UI labels
#f9fafb  ->  card surfaces, modal backgrounds, input field backgrounds
#e5e7eb  ->  borders, dividers, separator lines — 1px only
#6b7280  ->  secondary body text, metadata, timestamps, captions

CSS Custom Properties (paste into :root {}):
:root {
  --bg: #08090a;
  --surface: #f9fafb;
  --border: #e5e7eb;
  --accent: #5e6ad2;
  --text-primary: #f7f8f8;
  --text-muted: #6b7280;
  --radius-sm: 4px;
  --radius-md: 8px;
  --radius-lg: 16px;
}

Tailwind Config Extension (add inside extend: {}):
colors: { bg: '#08090a', surface: '#f9fafb', accent: '#5e6ad2', primary: '#f7f8f8', muted: '#6b7280' }

==================================================================
🔤 TYPOGRAPHY & TEXT RHYTHM
==================================================================
- Display / Headline Font: 'Geist Sans', 'Plus Jakarta Sans', 'Inter', sans-serif
- Body Copy Font: 'Geist Sans', 'Inter', sans-serif
- Monospace / Data Font: 'Geist Mono', 'Fira Code', monospace
- Optical Tracking (Letter Spacing): -0.035em for headings, -0.01em for body text
- Scale & Proportions: Hero: 60-84px (-0.04em), H1: 40px, H2: 28px, Body: 15-16px
- Font Weights: 400 Regular, 500 Medium, 600 SemiBold, 700 Bold

Copy Voice & Tone (match this style in ALL generated text content):
Direct, technical authority. Short declarative headlines. Developer or professional-first language. Action CTAs: 'Get started', 'Try for free', 'Read docs'.

==================================================================
📐 SPACING, GRID & GEOMETRY
==================================================================
- Container Max-Width & Grid: 12-column grid, max-width 1200px, 24px gutters
- Vertical Padding Scale: 4px, 8px, 16px, 24px, 40px, 80px, 120px
- Whitespace Philosophy: Pristine white canvas with generous negative space spotlighting typography clarity.

==================================================================
🧩 COMPONENT ARCHETYPE MAPPING
==================================================================
- Buttons (Primary, Secondary, Ghost): Pill buttons with 6-8px radius, solid black with white text or pure white with 1px border.
- Cards, Modules & Bento Grids: Pure white cards with 1px hairline border (#e5e7eb), subtle shadow on hover (0 4px 20px rgba(0,0,0,0.05)).
- Header & Navigation System: Clean top bar with logo, dropdown menus, and CTA on right.
- Hero / Showcase Composition: Centered large bold statement, 2-line subtitle, primary & secondary CTA pills, framework/tech logos.
- Forms, Filters & Pill Selectors: Crisp white inputs with light grey borders and blue or black focus rings.
- Footer & System Status: Clean 5-column link directory with copyright and status indicator.

Icon System: Geist Icons / Lucide Icons, 1.25px stroke, 16px-20px
Image Treatment: Clean terminal mockups, component cards, and vector diagrams with crisp borders.

==================================================================
⚡ MOTION PHYSICS & MICRO-INTERACTIONS
==================================================================
- Transitions & Easing: 150ms ease-out
  Apply as: transition: all 150ms cubic-bezier(0.16, 1, 0.3, 1) on all interactive elements
- Card Hover: transform: translateY(-2px) + box-shadow escalation
- Button Press: transform: scale(0.97), transition: 80ms ease-in
- Modal Entry: opacity 0 to 1 + translateY(8px to 0px), 200ms
- Scroll Reveals: IntersectionObserver threshold 0.1, staggered 60ms per sibling
- Scroll Behavior: Clean reveal transitions with crisp 100ms timing, zero blur lag.
- Micro-Interactions: Subtle border color shift on hover (#e5e7eb to #111827), button ripple effect.

==================================================================
📱 RESPONSIVE ADAPTATION
==================================================================
- Mobile Layout Strategy: Clean slide-down mobile nav, single column feature cards, full-width buttons.
- Desktop Ergonomics: 1200px container, multi-column grid, hover card previews.

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
  * Proprietary Cron brand logos
  * Exact Cron copyrighted assets
  * Direct company trademarks
- TECHNICAL IMPLEMENTATION GUIDANCE:
  Development Guide: Use Tailwind bg-[#08090a], border-white/10, hover:border-white/20, font-inter with -tracking-[0.02em] and lucide-react icons.

==================================================================
🛠️ STEP-BY-STEP REFACTORING INSTRUCTIONS
==================================================================
1. READ the user's current project files, identify domain, existing components, and tech stack.
2. INJECT the CSS custom properties above into the global stylesheet or Tailwind config.
3. RE-ARCHITECT each layout section to match the page architecture scaffold above.
4. RE-ENGINEER every UI component (nav, hero, cards, buttons, inputs, footer) into the Cron visual language while keeping the user's real content, data, and workflows intact.
5. APPLY motion physics (transitions, hover states, scroll reveals) as specified above.
6. WRITE all page copy in the Copy Voice defined above -- match the tone, not the brand name.
7. VERIFY: The output should feel unmistakably like Cron's design aesthetic applied to the user's own project domain.

==================================================================
📦 DELIVERABLE DEFINITION
==================================================================
Apply CSS custom properties globally first. Then rework each component to match theme tokens. Preserve all domain data and business logic — only the visual layer changes.
```
