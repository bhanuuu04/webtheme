# THEME #206 --- Aave

- **Website URL:** [https://aave.com/](https://aave.com/)
- **Category:** Fintech / Finance
- **Design Style:** Crypto-Forward Neomorphic Banking
- **Mode:** light
- **Tags:** `fintech-finance`, `light`, `fintech`

---

## 🧬 Theme DNA Summary
> **Aave design DNA: High-trust typography, dynamic financial metric counters, virtual debit card mockups, and regulatory rigor.**

---

## 🔑 Signature Visual Element
Clean white editorial canvas with #0284c7 as the single brand accent color. Large display typography and generous whitespace communicate the premium quality of Aave. Product screenshots or lifestyle imagery on clean white/off-white backgrounds.

---

## 🎭 Emotional Intent
Clarity and trustworthiness. The user feels confident that Aave is the right choice — professional, accessible, and purpose-built for their needs. The clean light design removes friction and communicates reliability.

---

## 🎯 Design Principles ("Why does this look like this?")
Why Aave looks like this: Engineered to project absolute security, frictionless capital flow, and financial empowerment.

---

## 🎨 Color System

### Primary Palette
- **`#f8fafc`** --- Crisp White Capital
- **`#0284c7`** --- Trust Cobalt Accent
- **`#0f172a`** --- Deep Slate Text

### Secondary & Surface Palette
- **`#112240`** --- Ledger Surface
- **`#233554`** --- Security Border
- **`#8892b0`** --- Financial Secondary Text

### CSS Custom Properties
```css
:root {
  --bg: #f8fafc;
  --surface: #112240;
  --border: #233554;
  --accent: #0284c7;
  --text-primary: #0f172a;
  --text-muted: #8892b0;
  --radius-sm: 4px;
  --radius-md: 8px;
  --radius-lg: 16px;
}
```

---

## 🔤 Typography System
- **Display Font:** `'Plus Jakarta Sans', 'Inter', -apple-system, sans-serif`
- **Body Font:** `'Inter', -apple-system, sans-serif`
- **Monospace Font:** `'JetBrains Mono', monospace`
- **Hierarchy & Scale:** Hero: 56-72px (-0.03em), H1: 36-40px, H2: 24-28px, Body: 15-16px
- **Weights:** 400 Regular, 500 Medium, 600 SemiBold, 700 Bold
- **Letter Spacing:** -0.025em display, -0.01em body

**Copy Voice:** Clear, benefit-focused. Friendly but professional. Accessible language. CTAs: 'Get started free', 'Try it out', 'See how it works'.

---

## 📐 Spacing & Layout Structure
- **Grid System:** 12-column responsive grid, max-width 1240px, 24px gutters
- **Padding Scale:** 4px, 8px, 16px, 24px, 48px, 96px
- **Whitespace Philosophy:** Balanced, generous vertical rhythm spotlighting structured visual hierarchy.

---

## 🧩 Component Language

### Buttons
8px rounded pills with solid accent or 1px hairline border.

### Cards
Structured cards with 1px border (rgba(255,255,255,0.08) or #e5e7eb) and subtle hover glow.

### Forms & Inputs
Clean inputs with 1px border, focus ring in primary accent.

### Navigation & Header
Sticky frosted pill header with minimal logo and action CTA.

### Hero Section
Asymmetric hero with high-impact headline, subtitle, and interactive mockup.

### Footer
Structured 4-5 column footer with system status and social links.

---

## 🏗️ Page Architecture
1. Sticky nav: logo, navigation links, primary CTA
2. Hero: strong headline, subtitle, CTA buttons, visual right
3. Trust indicators: logos or stats
4. Features: 3-col or alternating 2-col showcase
5. Testimonials: quote cards grid
6. Pricing or next-step section
7. Final CTA: centered, bold
8. Footer: standard 4-5 col

---

## 🚫 Anti-Patterns (What NOT to do)
- No dark section breaks that interrupt the light, airy flow
- No gradient backgrounds in main content areas
- No more than 1 accent color per section
- No heavy drop shadows — use soft shadows (0 2px 8px rgba(0,0,0,0.08))
- No cluttered layouts — generous whitespace is mandatory
- No condensed typography — maintain comfortable line-height (1.5-1.7 for body)

---

## ⚡ Motion & Animation
- **Transitions:** 180ms ease-out
- **Scroll Behavior:** Staggered reveal on scroll, smooth parallax card depth.
- **Micro-Interactions:** Subtle card translateY(-2px), smooth button active scale down.

---

## 📱 Responsive Strategy
- **Mobile:** Bottom sheet drawers, collapsible sidebars, single column stacked cards.
- **Desktop:** Multi-pane grid layout, 1240px max-width container.

---

## 🚀 Best Use Cases
- Banking apps
- Payment processors
- Crypto wallets
- Investment platforms
- Accounting SaaS
- Aave-inspired applications
- Fintech / Finance platforms

---

## ✅ Things To Reuse
  * Live financial metric ticker
  * Virtual card 3D tilt
  * Tabular numeric alignment
  * Security trust badges

---

## ❌ Things NOT To Copy
  * Proprietary Aave brand logos
  * Exact Aave copyrighted assets
  * Direct company trademarks

---

## 🛠️ Implementation Notes
Development Guide: Use tabular numeric font features (font-feature-settings: 'tnum'), vibrant green accents (#00e599), and subtle glass cards.

---

## 🤖 Deep Comprehensive AI Prompt
```text
[SYSTEM INSTRUCTION: SINGLE-SOURCE THEME DESIGN ADAPTER]
You are a Principal UI/UX Architect & Frontend Design System Engineer.
Your task is to analyze the user's current project / objective, and TRANSFORM / REDESIGN its entire frontend style, visual aesthetic, UX feeling, and component architecture strictly using the design system DNA of THEME #206 (Aave - https://aave.com/).

Maintain 100% strict theme isolation: extract and apply ONLY this reference theme's design language, tokens, and aesthetic principles.

==================================================================
🎯 CORE OBJECTIVE: ADAPT THEME TO USER'S PROJECT (NOT A BLIND CLONE)
==================================================================
1. ANALYZE CURRENT PROJECT & GOAL:
   - Carefully inspect the user's current project codebase, wireframes, or feature requirements (e.g. e-commerce clothing store selling shirts, SaaS tool, personal portfolio, marketplace, dashboard, etc.).
   - Preserve the user's core project purpose, domain data, functional workflows, and business logic.

2. TRANSLATE DESIGN DNA (DO NOT COPY PROPRIETARY CONTENT):
   - Do NOT blindly copy placeholder copy, trademarks, or unrelated product catalog from Aave (e.g., do not insert "Aave" branding or unrelated product listings).
   - DO extract and adopt 100% of Aave's visual craft, color palette, typography hierarchy, card structures, spacing rhythm, surface depth, micro-interactions, and UX feeling.

3. ELEVATE & RESKIN EVERY COMPONENT:
   - Reskin the user's existing components (navbars, heroes, product/feature cards, buttons, filters, inputs, modals, footers) into the authentic visual language of THEME #206.
   - Example: If the user's project is an apparel store selling shirts, design a high-craft shirt catalog with Aave's signature layouts, typography scale, lighting, and button styles.

==================================================================
🧬 THEME #206 IDENTITY & EMOTIONAL BRIEF
==================================================================
- Permanent Theme ID: THEME #206
- Reference Design Source: Aave (https://aave.com/)
- Mode: light
- Archetype / Category: Fintech / Finance
- Design Style: Crypto-Forward Neomorphic Banking
- Visual Personality: Aave signature design: crypto-forward neomorphic banking, engineered with high-craft aesthetics, structured hierarchy, and platform-native ergonomics.
- Core Design DNA: Aave design DNA: High-trust typography, dynamic financial metric counters, virtual debit card mockups, and regulatory rigor.

THE SIGNATURE VISUAL ELEMENT (What makes this theme unmistakably Aave):
Clean white editorial canvas with #0284c7 as the single brand accent color. Large display typography and generous whitespace communicate the premium quality of Aave. Product screenshots or lifestyle imagery on clean white/off-white backgrounds.

EMOTIONAL INTENT (How the user should FEEL when they see this design):
Clarity and trustworthiness. The user feels confident that Aave is the right choice — professional, accessible, and purpose-built for their needs. The clean light design removes friction and communicates reliability.

==================================================================
🎨 COLOR SYSTEM & APPLICATION RULES
==================================================================
#f8fafc  ->  page background, all section backgrounds
#0284c7  ->  primary CTA buttons, links on hover, focus rings, selected states, brand accents
#0f172a  ->  all headings (H1-H3), body text, primary UI labels
#112240  ->  card surfaces, modal backgrounds, input field backgrounds
#233554  ->  borders, dividers, separator lines — 1px only
#8892b0  ->  secondary body text, metadata, timestamps, captions

CSS Custom Properties (paste into :root {}):
:root {
  --bg: #f8fafc;
  --surface: #112240;
  --border: #233554;
  --accent: #0284c7;
  --text-primary: #0f172a;
  --text-muted: #8892b0;
  --radius-sm: 4px;
  --radius-md: 8px;
  --radius-lg: 16px;
}

Tailwind Config Extension (add inside extend: {}):
colors: { bg: '#f8fafc', surface: '#112240', accent: '#0284c7', primary: '#0f172a', muted: '#8892b0' }

==================================================================
🔤 TYPOGRAPHY & TEXT RHYTHM
==================================================================
- Display / Headline Font: 'Plus Jakarta Sans', 'Inter', -apple-system, sans-serif
- Body Copy Font: 'Inter', -apple-system, sans-serif
- Monospace / Data Font: 'JetBrains Mono', monospace
- Optical Tracking (Letter Spacing): -0.025em display, -0.01em body
- Scale & Proportions: Hero: 56-72px (-0.03em), H1: 36-40px, H2: 24-28px, Body: 15-16px
- Font Weights: 400 Regular, 500 Medium, 600 SemiBold, 700 Bold

Copy Voice & Tone (match this style in ALL generated text content):
Clear, benefit-focused. Friendly but professional. Accessible language. CTAs: 'Get started free', 'Try it out', 'See how it works'.

==================================================================
📐 SPACING, GRID & GEOMETRY
==================================================================
- Container Max-Width & Grid: 12-column responsive grid, max-width 1240px, 24px gutters
- Vertical Padding Scale: 4px, 8px, 16px, 24px, 48px, 96px
- Whitespace Philosophy: Balanced, generous vertical rhythm spotlighting structured visual hierarchy.

==================================================================
🧩 COMPONENT ARCHETYPE MAPPING
==================================================================
- Buttons (Primary, Secondary, Ghost): 8px rounded pills with solid accent or 1px hairline border.
- Cards, Modules & Bento Grids: Structured cards with 1px border (rgba(255,255,255,0.08) or #e5e7eb) and subtle hover glow.
- Header & Navigation System: Sticky frosted pill header with minimal logo and action CTA.
- Hero / Showcase Composition: Asymmetric hero with high-impact headline, subtitle, and interactive mockup.
- Forms, Filters & Pill Selectors: Clean inputs with 1px border, focus ring in primary accent.
- Footer & System Status: Structured 4-5 column footer with system status and social links.

Icon System: Lucide Icons, 1.5px stroke
Image Treatment: High-craft product screenshots and crisp vector mockups.

==================================================================
⚡ MOTION PHYSICS & MICRO-INTERACTIONS
==================================================================
- Transitions & Easing: 180ms ease-out
  Apply as: transition: all 150ms cubic-bezier(0.16, 1, 0.3, 1) on all interactive elements
- Card Hover: transform: translateY(-2px) + box-shadow escalation
- Button Press: transform: scale(0.97), transition: 80ms ease-in
- Modal Entry: opacity 0 to 1 + translateY(8px to 0px), 200ms
- Scroll Reveals: IntersectionObserver threshold 0.1, staggered 60ms per sibling
- Scroll Behavior: Staggered reveal on scroll, smooth parallax card depth.
- Micro-Interactions: Subtle card translateY(-2px), smooth button active scale down.

==================================================================
📱 RESPONSIVE ADAPTATION
==================================================================
- Mobile Layout Strategy: Bottom sheet drawers, collapsible sidebars, single column stacked cards.
- Desktop Ergonomics: Multi-pane grid layout, 1240px max-width container.

==================================================================
🏗️ PAGE ARCHITECTURE (ordered section scaffold for a typical page)
==================================================================
1. Sticky nav: logo, navigation links, primary CTA
2. Hero: strong headline, subtitle, CTA buttons, visual right
3. Trust indicators: logos or stats
4. Features: 3-col or alternating 2-col showcase
5. Testimonials: quote cards grid
6. Pricing or next-step section
7. Final CTA: centered, bold
8. Footer: standard 4-5 col

==================================================================
ANTI-PATTERNS (what NOT to do -- these break theme authenticity)
==================================================================
  X No dark section breaks that interrupt the light, airy flow
  X No gradient backgrounds in main content areas
  X No more than 1 accent color per section
  X No heavy drop shadows — use soft shadows (0 2px 8px rgba(0,0,0,0.08))
  X No cluttered layouts — generous whitespace is mandatory
  X No condensed typography — maintain comfortable line-height (1.5-1.7 for body)

==================================================================
🛡️ DESIGN FIDELITY GUARDRAILS
==================================================================
- MUST ADOPT & REUSE:
  * Live financial metric ticker
  * Virtual card 3D tilt
  * Tabular numeric alignment
  * Security trust badges
- DO NOT COPY (Proprietary / Brand Specific):
  * Proprietary Aave brand logos
  * Exact Aave copyrighted assets
  * Direct company trademarks
- TECHNICAL IMPLEMENTATION GUIDANCE:
  Development Guide: Use tabular numeric font features (font-feature-settings: 'tnum'), vibrant green accents (#00e599), and subtle glass cards.

==================================================================
🛠️ STEP-BY-STEP REFACTORING INSTRUCTIONS
==================================================================
1. READ the user's current project files, identify domain, existing components, and tech stack.
2. INJECT the CSS custom properties above into the global stylesheet or Tailwind config.
3. RE-ARCHITECT each layout section to match the page architecture scaffold above.
4. RE-ENGINEER every UI component (nav, hero, cards, buttons, inputs, footer) into the Aave visual language while keeping the user's real content, data, and workflows intact.
5. APPLY motion physics (transitions, hover states, scroll reveals) as specified above.
6. WRITE all page copy in the Copy Voice defined above -- match the tone, not the brand name.
7. VERIFY: The output should feel unmistakably like Aave's design aesthetic applied to the user's own project domain.

==================================================================
📦 DELIVERABLE DEFINITION
==================================================================
Apply CSS custom properties globally first. Then rework each component to match theme tokens. Preserve all domain data and business logic — only the visual layer changes.
```
