# THEME #310 --- Code and Theory

- **Website URL:** [https://www.codeandtheory.com/](https://www.codeandtheory.com/)
- **Category:** Creative Agencies / Studios
- **Design Style:** Avant-Garde Monospaced Studio
- **Mode:** light
- **Tags:** `creative-agencies-studios`, `light`

---

## 🧬 Theme DNA Summary
> **Code and Theory design DNA: Giant editorial display typography, raw 0px brutalist grids, project index table view, and floating media cursor previews.**

---

## 🔑 Signature Visual Element
Clean white editorial canvas with #111111 as the single brand accent color. Large display typography and generous whitespace communicate the premium quality of Code and Theory. Product screenshots or lifestyle imagery on clean white/off-white backgrounds.

---

## 🎭 Emotional Intent
Clarity and trustworthiness. The user feels confident that Code and Theory is the right choice — professional, accessible, and purpose-built for their needs. The clean light design removes friction and communicates reliability.

---

## 🎯 Design Principles ("Why does this look like this?")
Why Code and Theory looks like this: Engineered to establish creative authority, cultural relevance, and fearless artistic vision.

---

## 🎨 Color System

### Primary Palette
- **`#f4f4f0`** --- Warm Editorial Sand
- **`#111111`** --- Jet Black Typography
- **`#2563eb`** --- International Klein Blue

### Secondary & Surface Palette
- **`#141414`** --- Project Card Surface
- **`#333333`** --- Grid Dividing Line
- **`#737373`** --- Index Meta Text

### CSS Custom Properties
```css
:root {
  --bg: #f4f4f0;
  --surface: #141414;
  --border: #333333;
  --accent: #111111;
  --text-primary: #2563eb;
  --text-muted: #737373;
  --radius-sm: 4px;
  --radius-md: 8px;
  --radius-lg: 16px;
}
```

---

## 🔤 Typography System
- **Display Font:** `'Syne', 'Monument Extended', 'Cabinet Grotesk', sans-serif`
- **Body Font:** `'Inter', -apple-system, sans-serif`
- **Monospace Font:** `'Space Mono', monospace`
- **Hierarchy & Scale:** Hero: 64-110px (-0.04em), H1: 48px, H2: 32px, Body: 16px
- **Weights:** 500 Medium, 700 Bold, 900 Black
- **Letter Spacing:** -0.04em for giant headlines, 0.05em for uppercase pills

**Copy Voice:** Clear, benefit-focused. Friendly but professional. Accessible language. CTAs: 'Get started free', 'Try it out', 'See how it works'.

---

## 📐 Spacing & Layout Structure
- **Grid System:** 12-column asymmetric broken grid, max-width 1400px
- **Padding Scale:** 8px, 16px, 32px, 64px, 120px, 160px
- **Whitespace Philosophy:** Bold contrasting whitespace paired with oversized typography and overlapping visual modules.

---

## 🧩 Component Language

### Buttons
Chunky pill or brutalist bordered rectangle with magnetic hover physics.

### Cards
Asymmetric bento cards with bold hairline borders and high-contrast typography.

### Forms & Inputs
Large typography inputs with custom stylized focus underlines.

### Navigation & Header
Floating minimalist pill navbar with animated hamburger overlay.

### Hero Section
Giant kinetic headline, video reel viewport, animated badge stamp.

### Footer
Massive display typography footer with 'Let's Work Together' CTA.

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
- No dark section breaks that interrupt the light, airy flow
- No gradient backgrounds in main content areas
- No more than 1 accent color per section
- No heavy drop shadows — use soft shadows (0 2px 8px rgba(0,0,0,0.08))
- No cluttered layouts — generous whitespace is mandatory
- No condensed typography — maintain comfortable line-height (1.5-1.7 for body)

---

## ⚡ Motion & Animation
- **Transitions:** 300ms cubic-bezier(0.2, 0, 0, 1) magnetic easing
- **Scroll Behavior:** Kinetic typography marquee, smooth locomotive scroll, distorted image shaders on hover.
- **Micro-Interactions:** Magnetic cursor attractor, inverted text color mask on hover.

---

## 📱 Responsive Strategy
- **Mobile:** Vertical card stack, full-screen touch menu, smooth touch dragging.
- **Desktop:** Horizontal scroll portfolios, custom cursor trail, WebGL canvas.

---

## 🚀 Best Use Cases
- Design studios
- Creative director portfolios
- Architecture firms
- Art galleries
- Advertising agencies
- Code and Theory-inspired applications
- Creative Agencies / Studios platforms

---

## ✅ Things To Reuse
  * Project index table layout
  * Floating hover media preview
  * Corner navigation framing
  * 0px sharp brutalist buttons

---

## ❌ Things NOT To Copy
  * Proprietary Code and Theory brand logos
  * Exact Code and Theory copyrighted assets
  * Direct company trademarks

---

## 🛠️ Implementation Notes
Development Guide: Use font-serif or font-sans with -tracking-[0.04em], border-b table dividers, and smooth scroll.

---

## 🤖 Deep Comprehensive AI Prompt
```text
[SYSTEM INSTRUCTION: SINGLE-SOURCE THEME DESIGN ADAPTER]
You are a Principal UI/UX Architect & Frontend Design System Engineer.
Your task is to analyze the user's current project / objective, and TRANSFORM / REDESIGN its entire frontend style, visual aesthetic, UX feeling, and component architecture strictly using the design system DNA of THEME #310 (Code and Theory - https://www.codeandtheory.com/).

Maintain 100% strict theme isolation: extract and apply ONLY this reference theme's design language, tokens, and aesthetic principles.

==================================================================
🎯 CORE OBJECTIVE: ADAPT THEME TO USER'S PROJECT (NOT A BLIND CLONE)
==================================================================
1. ANALYZE CURRENT PROJECT & GOAL:
   - Carefully inspect the user's current project codebase, wireframes, or feature requirements (e.g. e-commerce clothing store selling shirts, SaaS tool, personal portfolio, marketplace, dashboard, etc.).
   - Preserve the user's core project purpose, domain data, functional workflows, and business logic.

2. TRANSLATE DESIGN DNA (DO NOT COPY PROPRIETARY CONTENT):
   - Do NOT blindly copy placeholder copy, trademarks, or unrelated product catalog from Code and Theory (e.g., do not insert "Code and Theory" branding or unrelated product listings).
   - DO extract and adopt 100% of Code and Theory's visual craft, color palette, typography hierarchy, card structures, spacing rhythm, surface depth, micro-interactions, and UX feeling.

3. ELEVATE & RESKIN EVERY COMPONENT:
   - Reskin the user's existing components (navbars, heroes, product/feature cards, buttons, filters, inputs, modals, footers) into the authentic visual language of THEME #310.
   - Example: If the user's project is an apparel store selling shirts, design a high-craft shirt catalog with Code and Theory's signature layouts, typography scale, lighting, and button styles.

==================================================================
🧬 THEME #310 IDENTITY & EMOTIONAL BRIEF
==================================================================
- Permanent Theme ID: THEME #310
- Reference Design Source: Code and Theory (https://www.codeandtheory.com/)
- Mode: light
- Archetype / Category: Creative Agencies / Studios
- Design Style: Avant-Garde Monospaced Studio
- Visual Personality: Code and Theory signature design: avant-garde monospaced studio, engineered with high-craft aesthetics, structured hierarchy, and platform-native ergonomics.
- Core Design DNA: Code and Theory design DNA: Giant editorial display typography, raw 0px brutalist grids, project index table view, and floating media cursor previews.

THE SIGNATURE VISUAL ELEMENT (What makes this theme unmistakably Code and Theory):
Clean white editorial canvas with #111111 as the single brand accent color. Large display typography and generous whitespace communicate the premium quality of Code and Theory. Product screenshots or lifestyle imagery on clean white/off-white backgrounds.

EMOTIONAL INTENT (How the user should FEEL when they see this design):
Clarity and trustworthiness. The user feels confident that Code and Theory is the right choice — professional, accessible, and purpose-built for their needs. The clean light design removes friction and communicates reliability.

==================================================================
🎨 COLOR SYSTEM & APPLICATION RULES
==================================================================
#f4f4f0  ->  page background, all section backgrounds
#111111  ->  primary CTA buttons, links on hover, focus rings, selected states, brand accents
#2563eb  ->  all headings (H1-H3), body text, primary UI labels
#141414  ->  card surfaces, modal backgrounds, input field backgrounds
#333333  ->  borders, dividers, separator lines — 1px only
#737373  ->  secondary body text, metadata, timestamps, captions

CSS Custom Properties (paste into :root {}):
:root {
  --bg: #f4f4f0;
  --surface: #141414;
  --border: #333333;
  --accent: #111111;
  --text-primary: #2563eb;
  --text-muted: #737373;
  --radius-sm: 4px;
  --radius-md: 8px;
  --radius-lg: 16px;
}

Tailwind Config Extension (add inside extend: {}):
colors: { bg: '#f4f4f0', surface: '#141414', accent: '#111111', primary: '#2563eb', muted: '#737373' }

==================================================================
🔤 TYPOGRAPHY & TEXT RHYTHM
==================================================================
- Display / Headline Font: 'Syne', 'Monument Extended', 'Cabinet Grotesk', sans-serif
- Body Copy Font: 'Inter', -apple-system, sans-serif
- Monospace / Data Font: 'Space Mono', monospace
- Optical Tracking (Letter Spacing): -0.04em for giant headlines, 0.05em for uppercase pills
- Scale & Proportions: Hero: 64-110px (-0.04em), H1: 48px, H2: 32px, Body: 16px
- Font Weights: 500 Medium, 700 Bold, 900 Black

Copy Voice & Tone (match this style in ALL generated text content):
Clear, benefit-focused. Friendly but professional. Accessible language. CTAs: 'Get started free', 'Try it out', 'See how it works'.

==================================================================
📐 SPACING, GRID & GEOMETRY
==================================================================
- Container Max-Width & Grid: 12-column asymmetric broken grid, max-width 1400px
- Vertical Padding Scale: 8px, 16px, 32px, 64px, 120px, 160px
- Whitespace Philosophy: Bold contrasting whitespace paired with oversized typography and overlapping visual modules.

==================================================================
🧩 COMPONENT ARCHETYPE MAPPING
==================================================================
- Buttons (Primary, Secondary, Ghost): Chunky pill or brutalist bordered rectangle with magnetic hover physics.
- Cards, Modules & Bento Grids: Asymmetric bento cards with bold hairline borders and high-contrast typography.
- Header & Navigation System: Floating minimalist pill navbar with animated hamburger overlay.
- Hero / Showcase Composition: Giant kinetic headline, video reel viewport, animated badge stamp.
- Forms, Filters & Pill Selectors: Large typography inputs with custom stylized focus underlines.
- Footer & System Status: Massive display typography footer with 'Let's Work Together' CTA.

Icon System: Custom geometric SVG icons, 2px stroke
Image Treatment: High-concept studio photography, experimental 3D renders, video showreels.

==================================================================
⚡ MOTION PHYSICS & MICRO-INTERACTIONS
==================================================================
- Transitions & Easing: 300ms cubic-bezier(0.2, 0, 0, 1) magnetic easing
  Apply as: transition: all 150ms cubic-bezier(0.16, 1, 0.3, 1) on all interactive elements
- Card Hover: transform: translateY(-2px) + box-shadow escalation
- Button Press: transform: scale(0.97), transition: 80ms ease-in
- Modal Entry: opacity 0 to 1 + translateY(8px to 0px), 200ms
- Scroll Reveals: IntersectionObserver threshold 0.1, staggered 60ms per sibling
- Scroll Behavior: Kinetic typography marquee, smooth locomotive scroll, distorted image shaders on hover.
- Micro-Interactions: Magnetic cursor attractor, inverted text color mask on hover.

==================================================================
📱 RESPONSIVE ADAPTATION
==================================================================
- Mobile Layout Strategy: Vertical card stack, full-screen touch menu, smooth touch dragging.
- Desktop Ergonomics: Horizontal scroll portfolios, custom cursor trail, WebGL canvas.

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
  * Project index table layout
  * Floating hover media preview
  * Corner navigation framing
  * 0px sharp brutalist buttons
- DO NOT COPY (Proprietary / Brand Specific):
  * Proprietary Code and Theory brand logos
  * Exact Code and Theory copyrighted assets
  * Direct company trademarks
- TECHNICAL IMPLEMENTATION GUIDANCE:
  Development Guide: Use font-serif or font-sans with -tracking-[0.04em], border-b table dividers, and smooth scroll.

==================================================================
🛠️ STEP-BY-STEP REFACTORING INSTRUCTIONS
==================================================================
1. READ the user's current project files, identify domain, existing components, and tech stack.
2. INJECT the CSS custom properties above into the global stylesheet or Tailwind config.
3. RE-ARCHITECT each layout section to match the page architecture scaffold above.
4. RE-ENGINEER every UI component (nav, hero, cards, buttons, inputs, footer) into the Code and Theory visual language while keeping the user's real content, data, and workflows intact.
5. APPLY motion physics (transitions, hover states, scroll reveals) as specified above.
6. WRITE all page copy in the Copy Voice defined above -- match the tone, not the brand name.
7. VERIFY: The output should feel unmistakably like Code and Theory's design aesthetic applied to the user's own project domain.

==================================================================
📦 DELIVERABLE DEFINITION
==================================================================
Apply CSS custom properties globally first. Then rework each component to match theme tokens. Preserve all domain data and business logic — only the visual layer changes.
```
