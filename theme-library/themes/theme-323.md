# THEME #323 --- Jam3 Labs

- **Website URL:** [https://www.jam3.com/](https://www.jam3.com/)
- **Category:** Creative Agencies / Studios
- **Design Style:** High-Contrast Minimalist Agency
- **Mode:** dark
- **Tags:** `creative-agencies-studios`, `dark`, `minimal`

---

## 🧬 Theme DNA Summary
> **Jam3 Labs design DNA: Giant editorial display typography, raw 0px brutalist grids, project index table view, and floating media cursor previews.**

---

## 🔑 Signature Visual Element
Deep dark canvas (#000000) with #ffffff accent used exclusively on primary actions. Product screenshots or interface mockups as the primary visual element. High contrast between surface (#surface) and text creates the premium feel characteristic of Jam3 Labs.

---

## 🎭 Emotional Intent
Technical precision and professional authority. The user feels Jam3 Labs is built by people who understand their craft deeply. The dark aesthetic communicates focus, speed, and zero compromise on quality.

---

## 🎯 Design Principles ("Why does this look like this?")
Why Jam3 Labs looks like this: Engineered to establish creative authority, cultural relevance, and fearless artistic vision.

---

## 🎨 Color System

### Primary Palette
- **`#000000`** --- Raw Black Canvas
- **`#ffffff`** --- Pure White Display
- **`#e11d48`** --- Crimson Studio Accent

### Secondary & Surface Palette
- **`#141414`** --- Project Card Surface
- **`#333333`** --- Grid Dividing Line
- **`#737373`** --- Index Meta Text

### CSS Custom Properties
```css
:root {
  --bg: #000000;
  --surface: #141414;
  --border: #333333;
  --accent: #ffffff;
  --text-primary: #e11d48;
  --text-muted: #737373;
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

**Copy Voice:** Direct, technical authority. Short declarative headlines. Developer or professional-first language. Action CTAs: 'Get started', 'Try for free', 'Read docs'.

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
1. Nav: minimal logo + 3-4 links
2. Hero: full-viewport, name/title, brief description, scroll indicator
3. Work grid: masonry or 2-3 col project cards
4. About: 2-col photo + biography
5. Services/Skills: 3-col specialty cards
6. Contact: centered form or email CTA
7. Footer: minimal social links

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
- **Transitions:** 180ms ease-out
- **Scroll Behavior:** Staggered reveal on scroll, smooth parallax card depth.
- **Micro-Interactions:** Subtle card translateY(-2px), smooth button active scale down.

---

## 📱 Responsive Strategy
- **Mobile:** Bottom sheet drawers, collapsible sidebars, single column stacked cards.
- **Desktop:** Multi-pane grid layout, 1240px max-width container.

---

## 🚀 Best Use Cases
- Design studios
- Creative director portfolios
- Architecture firms
- Art galleries
- Advertising agencies
- Jam3 Labs-inspired applications
- Creative Agencies / Studios platforms

---

## ✅ Things To Reuse
  * Project index table layout
  * Floating hover media preview
  * Corner navigation framing
  * 0px sharp brutalist buttons

---

## ❌ Things NOT To Copy
  * Proprietary Jam3 Labs brand logos
  * Exact Jam3 Labs copyrighted assets
  * Direct company trademarks

---

## 🛠️ Implementation Notes
Development Guide: Use font-serif or font-sans with -tracking-[0.04em], border-b table dividers, and smooth scroll.

---

## 🤖 Deep Comprehensive AI Prompt
```text
[SYSTEM INSTRUCTION: SINGLE-SOURCE THEME DESIGN ADAPTER]
You are a Principal UI/UX Architect & Frontend Design System Engineer.
Your task is to analyze the user's current project / objective, and TRANSFORM / REDESIGN its entire frontend style, visual aesthetic, UX feeling, and component architecture strictly using the design system DNA of THEME #323 (Jam3 Labs - https://www.jam3.com/).

Maintain 100% strict theme isolation: extract and apply ONLY this reference theme's design language, tokens, and aesthetic principles.

==================================================================
🎯 CORE OBJECTIVE: ADAPT THEME TO USER'S PROJECT (NOT A BLIND CLONE)
==================================================================
1. ANALYZE CURRENT PROJECT & GOAL:
   - Carefully inspect the user's current project codebase, wireframes, or feature requirements (e.g. e-commerce clothing store selling shirts, SaaS tool, personal portfolio, marketplace, dashboard, etc.).
   - Preserve the user's core project purpose, domain data, functional workflows, and business logic.

2. TRANSLATE DESIGN DNA (DO NOT COPY PROPRIETARY CONTENT):
   - Do NOT blindly copy placeholder copy, trademarks, or unrelated product catalog from Jam3 Labs (e.g., do not insert "Jam3 Labs" branding or unrelated product listings).
   - DO extract and adopt 100% of Jam3 Labs's visual craft, color palette, typography hierarchy, card structures, spacing rhythm, surface depth, micro-interactions, and UX feeling.

3. ELEVATE & RESKIN EVERY COMPONENT:
   - Reskin the user's existing components (navbars, heroes, product/feature cards, buttons, filters, inputs, modals, footers) into the authentic visual language of THEME #323.
   - Example: If the user's project is an apparel store selling shirts, design a high-craft shirt catalog with Jam3 Labs's signature layouts, typography scale, lighting, and button styles.

==================================================================
🧬 THEME #323 IDENTITY & EMOTIONAL BRIEF
==================================================================
- Permanent Theme ID: THEME #323
- Reference Design Source: Jam3 Labs (https://www.jam3.com/)
- Mode: dark
- Archetype / Category: Creative Agencies / Studios
- Design Style: High-Contrast Minimalist Agency
- Visual Personality: Jam3 Labs signature design: high-contrast minimalist agency, engineered with high-craft aesthetics, structured hierarchy, and platform-native ergonomics.
- Core Design DNA: Jam3 Labs design DNA: Giant editorial display typography, raw 0px brutalist grids, project index table view, and floating media cursor previews.

THE SIGNATURE VISUAL ELEMENT (What makes this theme unmistakably Jam3 Labs):
Deep dark canvas (#000000) with #ffffff accent used exclusively on primary actions. Product screenshots or interface mockups as the primary visual element. High contrast between surface (#surface) and text creates the premium feel characteristic of Jam3 Labs.

EMOTIONAL INTENT (How the user should FEEL when they see this design):
Technical precision and professional authority. The user feels Jam3 Labs is built by people who understand their craft deeply. The dark aesthetic communicates focus, speed, and zero compromise on quality.

==================================================================
🎨 COLOR SYSTEM & APPLICATION RULES
==================================================================
#000000  ->  page background, all section backgrounds
#ffffff  ->  primary CTA buttons, links on hover, focus rings, selected states, brand accents
#e11d48  ->  all headings (H1-H3), body text, primary UI labels
#141414  ->  card surfaces, modal backgrounds, input field backgrounds
#333333  ->  borders, dividers, separator lines — 1px only
#737373  ->  secondary body text, metadata, timestamps, captions

CSS Custom Properties (paste into :root {}):
:root {
  --bg: #000000;
  --surface: #141414;
  --border: #333333;
  --accent: #ffffff;
  --text-primary: #e11d48;
  --text-muted: #737373;
  --radius-sm: 4px;
  --radius-md: 8px;
  --radius-lg: 16px;
}

Tailwind Config Extension (add inside extend: {}):
colors: { bg: '#000000', surface: '#141414', accent: '#ffffff', primary: '#e11d48', muted: '#737373' }

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
Direct, technical authority. Short declarative headlines. Developer or professional-first language. Action CTAs: 'Get started', 'Try for free', 'Read docs'.

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
1. Nav: minimal logo + 3-4 links
2. Hero: full-viewport, name/title, brief description, scroll indicator
3. Work grid: masonry or 2-3 col project cards
4. About: 2-col photo + biography
5. Services/Skills: 3-col specialty cards
6. Contact: centered form or email CTA
7. Footer: minimal social links

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
  * Project index table layout
  * Floating hover media preview
  * Corner navigation framing
  * 0px sharp brutalist buttons
- DO NOT COPY (Proprietary / Brand Specific):
  * Proprietary Jam3 Labs brand logos
  * Exact Jam3 Labs copyrighted assets
  * Direct company trademarks
- TECHNICAL IMPLEMENTATION GUIDANCE:
  Development Guide: Use font-serif or font-sans with -tracking-[0.04em], border-b table dividers, and smooth scroll.

==================================================================
🛠️ STEP-BY-STEP REFACTORING INSTRUCTIONS
==================================================================
1. READ the user's current project files, identify domain, existing components, and tech stack.
2. INJECT the CSS custom properties above into the global stylesheet or Tailwind config.
3. RE-ARCHITECT each layout section to match the page architecture scaffold above.
4. RE-ENGINEER every UI component (nav, hero, cards, buttons, inputs, footer) into the Jam3 Labs visual language while keeping the user's real content, data, and workflows intact.
5. APPLY motion physics (transitions, hover states, scroll reveals) as specified above.
6. WRITE all page copy in the Copy Voice defined above -- match the tone, not the brand name.
7. VERIFY: The output should feel unmistakably like Jam3 Labs's design aesthetic applied to the user's own project domain.

==================================================================
📦 DELIVERABLE DEFINITION
==================================================================
Apply CSS custom properties globally first. Then rework each component to match theme tokens. Preserve all domain data and business logic — only the visual layer changes.
```
