# THEME #030 --- Craft

- **Website URL:** [https://www.craft.do/](https://www.craft.do/)
- **Category:** SaaS / Product
- **Design Style:** Clean Minimal Enterprise Product
- **Mode:** light
- **Tags:** `saas-product`, `light`, `minimal`, `saas`

---

## 🧬 Theme DNA Summary
> **Craft design DNA: Large typography, generous whitespace, monochrome palette, subtle borders, restrained motion, asymmetric hero composition and strong product-focused visual hierarchy.**

---

## 🔑 Signature Visual Element
Large editorial typography (64px+) in near-black on pristine white, combined with the document card stack visual — showing nested documents with clean drop shadows. Generous whitespace as a luxury design statement. Monochrome palette with single emerald (#10b981) accent.

---

## 🎭 Emotional Intent
Premium writing tool for people who care about craft. The user feels inspired to write something beautiful. Notion's calmer, more refined cousin — where the document itself is the art. Clarity of thought reflected in clarity of design.

---

## 🎯 Design Principles ("Why does this look like this?")
Why Craft looks like this: Built to communicate speed, craft, and keyboard-first productivity by removing clutter and focusing on high contrast, micro-details, and crisp dark backgrounds.

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
  --bg: #ffffff;
  --surface: #f8fafc;
  --border: #e2e8f0;
  --accent: #10b981;
  --text-primary: #0f172a;
  --text-muted: #64748b;
  --radius-sm: 6px;
  --radius-md: 10px;
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

**Copy Voice:** Refined, thoughtful, writing-focused. 'A new home for your ideas.' Celebrates the craft of writing and thinking. CTAs: 'Try Craft free', 'Download for Mac', 'Get started'. Tone is calm and confident — never loud.

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
1. Nav: pure white, Craft logo left, links center, 'Try Craft' pill right
2. Hero: white, asymmetric 2-col (headline left, document stack visual right)
3. Feature trio: 3-col, icon + headline + body, spacious
4. Product deep-dive: alternating 2-col editorial showcases
5. Platform showcase: iOS + Mac + Web platform cards
6. Testimonials: large pull quote, minimal attribution
7. CTA: centered, white, large headline + single CTA
8. Footer: minimal 4-col on white

---

## 🚫 Anti-Patterns (What NOT to do)
- No dark sections — pure white editorial throughout
- No gradient backgrounds or gradient text
- No decorative elements beyond clean typography and document card imagery
- No rounded corners above 12px for structural elements
- No more than 1 emerald accent visible at a time
- No dense layouts — generous breathing room is mandatory

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
- Craft-inspired applications
- SaaS / Product platforms

---

## ✅ Things To Reuse
  * 1px glowing border cards
  * Keyboard shortcut UI badges
  * Obsidian color system
  * Radial hero glow spotlight

---

## ❌ Things NOT To Copy
  * Proprietary Craft brand logos
  * Exact Craft copyrighted assets
  * Direct company trademarks

---

## 🛠️ Implementation Notes
Development Guide: Use Tailwind bg-[#08090a], border-white/10, hover:border-white/20, font-inter with -tracking-[0.02em] and lucide-react icons.

---

## 🤖 Deep Comprehensive AI Prompt
```text
[SYSTEM INSTRUCTION: SINGLE-SOURCE THEME DESIGN ADAPTER]
You are a Principal UI/UX Architect & Frontend Design System Engineer.
Your task is to analyze the user's current project / objective, and TRANSFORM / REDESIGN its entire frontend style, visual aesthetic, UX feeling, and component architecture strictly using the design system DNA of THEME #030 (Craft - https://www.craft.do/).

Maintain 100% strict theme isolation: extract and apply ONLY this reference theme's design language, tokens, and aesthetic principles.

==================================================================
🎯 CORE OBJECTIVE: ADAPT THEME TO USER'S PROJECT (NOT A BLIND CLONE)
==================================================================
1. ANALYZE CURRENT PROJECT & GOAL:
   - Carefully inspect the user's current project codebase, wireframes, or feature requirements (e.g. e-commerce clothing store selling shirts, SaaS tool, personal portfolio, marketplace, dashboard, etc.).
   - Preserve the user's core project purpose, domain data, functional workflows, and business logic.

2. TRANSLATE DESIGN DNA (DO NOT COPY PROPRIETARY CONTENT):
   - Do NOT blindly copy placeholder copy, trademarks, or unrelated product catalog from Craft (e.g., do not insert "Craft" branding or unrelated product listings).
   - DO extract and adopt 100% of Craft's visual craft, color palette, typography hierarchy, card structures, spacing rhythm, surface depth, micro-interactions, and UX feeling.

3. ELEVATE & RESKIN EVERY COMPONENT:
   - Reskin the user's existing components (navbars, heroes, product/feature cards, buttons, filters, inputs, modals, footers) into the authentic visual language of THEME #030.
   - Example: If the user's project is an apparel store selling shirts, design a high-craft shirt catalog with Craft's signature layouts, typography scale, lighting, and button styles.

==================================================================
🧬 THEME #030 IDENTITY & EMOTIONAL BRIEF
==================================================================
- Permanent Theme ID: THEME #030
- Reference Design Source: Craft (https://www.craft.do/)
- Mode: light
- Archetype / Category: SaaS / Product
- Design Style: Clean Minimal Enterprise Product
- Visual Personality: Craft signature design: clean minimal enterprise product, engineered with high-craft aesthetics, structured hierarchy, and platform-native ergonomics.
- Core Design DNA: Craft design DNA: Large typography, generous whitespace, monochrome palette, subtle borders, restrained motion, asymmetric hero composition and strong product-focused visual hierarchy.

THE SIGNATURE VISUAL ELEMENT (What makes this theme unmistakably Craft):
Large editorial typography (64px+) in near-black on pristine white, combined with the document card stack visual — showing nested documents with clean drop shadows. Generous whitespace as a luxury design statement. Monochrome palette with single emerald (#10b981) accent.

EMOTIONAL INTENT (How the user should FEEL when they see this design):
Premium writing tool for people who care about craft. The user feels inspired to write something beautiful. Notion's calmer, more refined cousin — where the document itself is the art. Clarity of thought reflected in clarity of design.

==================================================================
🎨 COLOR SYSTEM & APPLICATION RULES
==================================================================
#ffffff  ->  all backgrounds — absolute white editorial canvas
#0f172a  ->  all headings, all body text — near-black slate
#10b981  ->  primary CTA buttons, active states, accent links, selection highlights
#f8fafc  ->  alternate section backgrounds, card surfaces
#e2e8f0  ->  borders, dividers — ultra-light hairline borders
#64748b  ->  secondary text, metadata, captions, eyebrow labels

CSS Custom Properties (paste into :root {}):
:root {
  --bg: #ffffff;
  --surface: #f8fafc;
  --border: #e2e8f0;
  --accent: #10b981;
  --text-primary: #0f172a;
  --text-muted: #64748b;
  --radius-sm: 6px;
  --radius-md: 10px;
  --radius-lg: 16px;
}

Tailwind Config Extension (add inside extend: {}):
colors: { bg: '#ffffff', surface: '#f8fafc', border: '#e2e8f0', accent: '#10b981', primary: '#0f172a', muted: '#64748b' }

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
Refined, thoughtful, writing-focused. 'A new home for your ideas.' Celebrates the craft of writing and thinking. CTAs: 'Try Craft free', 'Download for Mac', 'Get started'. Tone is calm and confident — never loud.

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
1. Nav: pure white, Craft logo left, links center, 'Try Craft' pill right
2. Hero: white, asymmetric 2-col (headline left, document stack visual right)
3. Feature trio: 3-col, icon + headline + body, spacious
4. Product deep-dive: alternating 2-col editorial showcases
5. Platform showcase: iOS + Mac + Web platform cards
6. Testimonials: large pull quote, minimal attribution
7. CTA: centered, white, large headline + single CTA
8. Footer: minimal 4-col on white

==================================================================
ANTI-PATTERNS (what NOT to do -- these break theme authenticity)
==================================================================
  X No dark sections — pure white editorial throughout
  X No gradient backgrounds or gradient text
  X No decorative elements beyond clean typography and document card imagery
  X No rounded corners above 12px for structural elements
  X No more than 1 emerald accent visible at a time
  X No dense layouts — generous breathing room is mandatory

==================================================================
🛡️ DESIGN FIDELITY GUARDRAILS
==================================================================
- MUST ADOPT & REUSE:
  * 1px glowing border cards
  * Keyboard shortcut UI badges
  * Obsidian color system
  * Radial hero glow spotlight
- DO NOT COPY (Proprietary / Brand Specific):
  * Proprietary Craft brand logos
  * Exact Craft copyrighted assets
  * Direct company trademarks
- TECHNICAL IMPLEMENTATION GUIDANCE:
  Development Guide: Use Tailwind bg-[#08090a], border-white/10, hover:border-white/20, font-inter with -tracking-[0.02em] and lucide-react icons.

==================================================================
🛠️ STEP-BY-STEP REFACTORING INSTRUCTIONS
==================================================================
1. READ the user's current project files, identify domain, existing components, and tech stack.
2. INJECT the CSS custom properties above into the global stylesheet or Tailwind config.
3. RE-ARCHITECT each layout section to match the page architecture scaffold above.
4. RE-ENGINEER every UI component (nav, hero, cards, buttons, inputs, footer) into the Craft visual language while keeping the user's real content, data, and workflows intact.
5. APPLY motion physics (transitions, hover states, scroll reveals) as specified above.
6. WRITE all page copy in the Copy Voice defined above -- match the tone, not the brand name.
7. VERIFY: The output should feel unmistakably like Craft's design aesthetic applied to the user's own project domain.

==================================================================
📦 DELIVERABLE DEFINITION
==================================================================
Generous whitespace is not waste — it IS the design. Every section should have at least 96px vertical padding. Typography hierarchy must be very clear (H1 >> H2 >> body).
```
