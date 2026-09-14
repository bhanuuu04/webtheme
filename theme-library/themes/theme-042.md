# THEME #042 --- Figma

- **Website URL:** [https://www.figma.com/](https://www.figma.com/)
- **Category:** SaaS / Product
- **Design Style:** Clean Minimal Enterprise Product
- **Mode:** dark
- **Tags:** `saas-product`, `light`, `minimal`, `saas`

---

## 🧬 Theme DNA Summary
> **Figma design DNA: Large typography, generous whitespace, monochrome palette, subtle borders, restrained motion, asymmetric hero composition and strong product-focused visual hierarchy.**

---

## 🔑 Signature Visual Element
Multi-panel design tool chrome aesthetic: layers panel on left, properties inspector on right, canvas in center. Purple (#A259FF) accent on selected components. Tool-metaphor UI elements (node connectors, component slots, variant pills) used decoratively throughout marketing.

---

## 🎭 Emotional Intent
Collaborative design mastery. The user feels they are part of the professional design community. Figma is where real design work happens — the UI communicates creative authority and team collaboration.

---

## 🎯 Design Principles ("Why does this look like this?")
Why Figma looks like this: Built to communicate speed, craft, and keyboard-first productivity by removing clutter and focusing on high contrast, micro-details, and crisp dark backgrounds.

---

## 🎨 Color System

### Primary Palette
- **`#0f172a`** --- Slate Dark Canvas
- **`#10b981`** --- Emerald Accent
- **`#ffffff`** --- Headline Text

### Secondary & Surface Palette
- **`#f9fafb`** --- Card Surface Light
- **`#e5e7eb`** --- Border Light
- **`#6b7280`** --- Secondary Text

### CSS Custom Properties
```css
:root {
  --bg: #1e1e1e;
  --surface: #2c2c2c;
  --border: #444444;
  --accent: #A259FF;
  --text-primary: #ffffff;
  --text-muted: #b3b3b3;
  --radius-sm: 4px;
  --radius-md: 8px;
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

**Copy Voice:** Confident design authority. 'Where teams design together.' Designer-to-designer language. Technical precision mixed with creative empowerment. CTAs: 'Get started for free', 'Contact sales', 'See plans'.

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
1. Nav: dark, Figma logo left, product links, 'Contact sales' + 'Get started' right
2. Hero: dark canvas bg, bold headline, product screenshot showing design tool with real design
3. Collaboration feature: animated multi-cursor demo, team collaboration callout
4. Component/plugin ecosystem: grid of plugin cards
5. Template gallery: horizontal scroll, card grid with design previews
6. Pricing table: 3 tiers, purple highlighted tier
7. Enterprise CTA: dark panel
8. Footer: dark 5-col

---

## 🚫 Anti-Patterns (What NOT to do)
- No light/white sections in main content — keep dark consistently
- No simple product screenshots — always show the design tool in use with real work
- No generic business language — speak to designers specifically
- No simple icon sets — use design-tool metaphors (component icons, variant chips)
- No static presentations — show collaboration (multiple cursors, comments)

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
- Figma-inspired applications
- SaaS / Product platforms

---

## ✅ Things To Reuse
  * 1px glowing border cards
  * Keyboard shortcut UI badges
  * Obsidian color system
  * Radial hero glow spotlight

---

## ❌ Things NOT To Copy
  * Proprietary Figma brand logos
  * Exact Figma copyrighted assets
  * Direct company trademarks

---

## 🛠️ Implementation Notes
Development Guide: Use Tailwind bg-[#08090a], border-white/10, hover:border-white/20, font-inter with -tracking-[0.02em] and lucide-react icons.

---

## 🤖 Deep Comprehensive AI Prompt
```text
[SYSTEM INSTRUCTION: SINGLE-SOURCE THEME DESIGN ADAPTER]
You are a Principal UI/UX Architect & Frontend Design System Engineer.
Your task is to analyze the user's current project / objective, and TRANSFORM / REDESIGN its entire frontend style, visual aesthetic, UX feeling, and component architecture strictly using the design system DNA of THEME #042 (Figma - https://www.figma.com/).

Maintain 100% strict theme isolation: extract and apply ONLY this reference theme's design language, tokens, and aesthetic principles.

==================================================================
🎯 CORE OBJECTIVE: ADAPT THEME TO USER'S PROJECT (NOT A BLIND CLONE)
==================================================================
1. ANALYZE CURRENT PROJECT & GOAL:
   - Carefully inspect the user's current project codebase, wireframes, or feature requirements (e.g. e-commerce clothing store selling shirts, SaaS tool, personal portfolio, marketplace, dashboard, etc.).
   - Preserve the user's core project purpose, domain data, functional workflows, and business logic.

2. TRANSLATE DESIGN DNA (DO NOT COPY PROPRIETARY CONTENT):
   - Do NOT blindly copy placeholder copy, trademarks, or unrelated product catalog from Figma (e.g., do not insert "Figma" branding or unrelated product listings).
   - DO extract and adopt 100% of Figma's visual craft, color palette, typography hierarchy, card structures, spacing rhythm, surface depth, micro-interactions, and UX feeling.

3. ELEVATE & RESKIN EVERY COMPONENT:
   - Reskin the user's existing components (navbars, heroes, product/feature cards, buttons, filters, inputs, modals, footers) into the authentic visual language of THEME #042.
   - Example: If the user's project is an apparel store selling shirts, design a high-craft shirt catalog with Figma's signature layouts, typography scale, lighting, and button styles.

==================================================================
🧬 THEME #042 IDENTITY & EMOTIONAL BRIEF
==================================================================
- Permanent Theme ID: THEME #042
- Reference Design Source: Figma (https://www.figma.com/)
- Mode: dark
- Archetype / Category: SaaS / Product
- Design Style: Clean Minimal Enterprise Product
- Visual Personality: Figma signature design: clean minimal enterprise product, engineered with high-craft aesthetics, structured hierarchy, and platform-native ergonomics.
- Core Design DNA: Figma design DNA: Large typography, generous whitespace, monochrome palette, subtle borders, restrained motion, asymmetric hero composition and strong product-focused visual hierarchy.

THE SIGNATURE VISUAL ELEMENT (What makes this theme unmistakably Figma):
Multi-panel design tool chrome aesthetic: layers panel on left, properties inspector on right, canvas in center. Purple (#A259FF) accent on selected components. Tool-metaphor UI elements (node connectors, component slots, variant pills) used decoratively throughout marketing.

EMOTIONAL INTENT (How the user should FEEL when they see this design):
Collaborative design mastery. The user feels they are part of the professional design community. Figma is where real design work happens — the UI communicates creative authority and team collaboration.

==================================================================
🎨 COLOR SYSTEM & APPLICATION RULES
==================================================================
#1e1e1e  ->  body background, all main sections
#A259FF  ->  primary CTAs, active selection highlights, featured tier, link accents
#ffffff  ->  all display text, tool labels, nav links
#2c2c2c  ->  card surfaces, panel backgrounds, modal surfaces
#444444  ->  borders, panel dividers, inspector separators
#b3b3b3  ->  secondary text, property labels, metadata

CSS Custom Properties (paste into :root {}):
:root {
  --bg: #1e1e1e;
  --surface: #2c2c2c;
  --border: #444444;
  --accent: #A259FF;
  --text-primary: #ffffff;
  --text-muted: #b3b3b3;
  --radius-sm: 4px;
  --radius-md: 8px;
}

Tailwind Config Extension (add inside extend: {}):
colors: { bg: '#1e1e1e', surface: '#2c2c2c', border: '#444444', accent: '#A259FF', primary: '#ffffff', muted: '#b3b3b3' }

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
Confident design authority. 'Where teams design together.' Designer-to-designer language. Technical precision mixed with creative empowerment. CTAs: 'Get started for free', 'Contact sales', 'See plans'.

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
1. Nav: dark, Figma logo left, product links, 'Contact sales' + 'Get started' right
2. Hero: dark canvas bg, bold headline, product screenshot showing design tool with real design
3. Collaboration feature: animated multi-cursor demo, team collaboration callout
4. Component/plugin ecosystem: grid of plugin cards
5. Template gallery: horizontal scroll, card grid with design previews
6. Pricing table: 3 tiers, purple highlighted tier
7. Enterprise CTA: dark panel
8. Footer: dark 5-col

==================================================================
ANTI-PATTERNS (what NOT to do -- these break theme authenticity)
==================================================================
  X No light/white sections in main content — keep dark consistently
  X No simple product screenshots — always show the design tool in use with real work
  X No generic business language — speak to designers specifically
  X No simple icon sets — use design-tool metaphors (component icons, variant chips)
  X No static presentations — show collaboration (multiple cursors, comments)

==================================================================
🛡️ DESIGN FIDELITY GUARDRAILS
==================================================================
- MUST ADOPT & REUSE:
  * 1px glowing border cards
  * Keyboard shortcut UI badges
  * Obsidian color system
  * Radial hero glow spotlight
- DO NOT COPY (Proprietary / Brand Specific):
  * Proprietary Figma brand logos
  * Exact Figma copyrighted assets
  * Direct company trademarks
- TECHNICAL IMPLEMENTATION GUIDANCE:
  Development Guide: Use Tailwind bg-[#08090a], border-white/10, hover:border-white/20, font-inter with -tracking-[0.02em] and lucide-react icons.

==================================================================
🛠️ STEP-BY-STEP REFACTORING INSTRUCTIONS
==================================================================
1. READ the user's current project files, identify domain, existing components, and tech stack.
2. INJECT the CSS custom properties above into the global stylesheet or Tailwind config.
3. RE-ARCHITECT each layout section to match the page architecture scaffold above.
4. RE-ENGINEER every UI component (nav, hero, cards, buttons, inputs, footer) into the Figma visual language while keeping the user's real content, data, and workflows intact.
5. APPLY motion physics (transitions, hover states, scroll reveals) as specified above.
6. WRITE all page copy in the Copy Voice defined above -- match the tone, not the brand name.
7. VERIFY: The output should feel unmistakably like Figma's design aesthetic applied to the user's own project domain.

==================================================================
📦 DELIVERABLE DEFINITION
==================================================================
Show the design tool aesthetic even if building a non-design product. Use the dark canvas, panel chrome metaphors, and component-grid layouts.
```
