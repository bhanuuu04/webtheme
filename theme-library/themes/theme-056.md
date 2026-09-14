# THEME #056 --- Fathom Analytics

- **Website URL:** [https://usefathom.com/](https://usefathom.com/)
- **Category:** SaaS / Product
- **Design Style:** Vibrant Multi-Layered Product Hub
- **Mode:** light
- **Tags:** `saas-product`, `light`, `saas`

---

## 🧬 Theme DNA Summary
> **Fathom Analytics design DNA: Large typography, generous whitespace, monochrome palette, subtle borders, restrained motion, asymmetric hero composition and strong product-focused visual hierarchy.**

---

## 🔑 Signature Visual Element
Clean white editorial canvas with #0070f3 as the single brand accent color. Large display typography and generous whitespace communicate the premium quality of Fathom Analytics. Product screenshots or lifestyle imagery on clean white/off-white backgrounds.

---

## 🎭 Emotional Intent
Clarity and trustworthiness. The user feels confident that Fathom Analytics is the right choice — professional, accessible, and purpose-built for their needs. The clean light design removes friction and communicates reliability.

---

## 🎯 Design Principles ("Why does this look like this?")
Why Fathom Analytics looks like this: Built to communicate speed, craft, and keyboard-first productivity by removing clutter and focusing on high contrast, micro-details, and crisp dark backgrounds.

---

## 🎨 Color System

### Primary Palette
- **`#ffffff`** --- Light Clean Canvas
- **`#0070f3`** --- Geist Blue Accent
- **`#111827`** --- Deep Charcoal Text

### Secondary & Surface Palette
- **`#f9fafb`** --- Card Surface Light
- **`#e5e7eb`** --- Border Light
- **`#6b7280`** --- Secondary Text

### CSS Custom Properties
```css
:root {
  --bg: #ffffff;
  --surface: #f9fafb;
  --border: #e5e7eb;
  --accent: #0070f3;
  --text-primary: #111827;
  --text-muted: #6b7280;
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
- Developer tools
- Issue trackers
- Productivity suites
- High-craft B2B SaaS
- Command bar tools
- Fathom Analytics-inspired applications
- SaaS / Product platforms

---

## ✅ Things To Reuse
  * 1px glowing border cards
  * Keyboard shortcut UI badges
  * Obsidian color system
  * Radial hero glow spotlight

---

## ❌ Things NOT To Copy
  * Proprietary Fathom Analytics brand logos
  * Exact Fathom Analytics copyrighted assets
  * Direct company trademarks

---

## 🛠️ Implementation Notes
Development Guide: Use Tailwind bg-[#08090a], border-white/10, hover:border-white/20, font-inter with -tracking-[0.02em] and lucide-react icons.

---

## 🤖 Deep Comprehensive AI Prompt
```text
[SYSTEM INSTRUCTION: SINGLE-SOURCE THEME DESIGN ADAPTER]
You are a Principal UI/UX Architect & Frontend Design System Engineer.
Your task is to analyze the user's current project / objective, and TRANSFORM / REDESIGN its entire frontend style, visual aesthetic, UX feeling, and component architecture strictly using the design system DNA of THEME #056 (Fathom Analytics - https://usefathom.com/).

Maintain 100% strict theme isolation: extract and apply ONLY this reference theme's design language, tokens, and aesthetic principles.

==================================================================
🎯 CORE OBJECTIVE: ADAPT THEME TO USER'S PROJECT (NOT A BLIND CLONE)
==================================================================
1. ANALYZE CURRENT PROJECT & GOAL:
   - Carefully inspect the user's current project codebase, wireframes, or feature requirements (e.g. e-commerce clothing store selling shirts, SaaS tool, personal portfolio, marketplace, dashboard, etc.).
   - Preserve the user's core project purpose, domain data, functional workflows, and business logic.

2. TRANSLATE DESIGN DNA (DO NOT COPY PROPRIETARY CONTENT):
   - Do NOT blindly copy placeholder copy, trademarks, or unrelated product catalog from Fathom Analytics (e.g., do not insert "Fathom Analytics" branding or unrelated product listings).
   - DO extract and adopt 100% of Fathom Analytics's visual craft, color palette, typography hierarchy, card structures, spacing rhythm, surface depth, micro-interactions, and UX feeling.

3. ELEVATE & RESKIN EVERY COMPONENT:
   - Reskin the user's existing components (navbars, heroes, product/feature cards, buttons, filters, inputs, modals, footers) into the authentic visual language of THEME #056.
   - Example: If the user's project is an apparel store selling shirts, design a high-craft shirt catalog with Fathom Analytics's signature layouts, typography scale, lighting, and button styles.

==================================================================
🧬 THEME #056 IDENTITY & EMOTIONAL BRIEF
==================================================================
- Permanent Theme ID: THEME #056
- Reference Design Source: Fathom Analytics (https://usefathom.com/)
- Mode: light
- Archetype / Category: SaaS / Product
- Design Style: Vibrant Multi-Layered Product Hub
- Visual Personality: Fathom Analytics signature design: vibrant multi-layered product hub, engineered with high-craft aesthetics, structured hierarchy, and platform-native ergonomics.
- Core Design DNA: Fathom Analytics design DNA: Large typography, generous whitespace, monochrome palette, subtle borders, restrained motion, asymmetric hero composition and strong product-focused visual hierarchy.

THE SIGNATURE VISUAL ELEMENT (What makes this theme unmistakably Fathom Analytics):
Clean white editorial canvas with #0070f3 as the single brand accent color. Large display typography and generous whitespace communicate the premium quality of Fathom Analytics. Product screenshots or lifestyle imagery on clean white/off-white backgrounds.

EMOTIONAL INTENT (How the user should FEEL when they see this design):
Clarity and trustworthiness. The user feels confident that Fathom Analytics is the right choice — professional, accessible, and purpose-built for their needs. The clean light design removes friction and communicates reliability.

==================================================================
🎨 COLOR SYSTEM & APPLICATION RULES
==================================================================
#ffffff  ->  page background, all section backgrounds
#0070f3  ->  primary CTA buttons, links on hover, focus rings, selected states, brand accents
#111827  ->  all headings (H1-H3), body text, primary UI labels
#f9fafb  ->  card surfaces, modal backgrounds, input field backgrounds
#e5e7eb  ->  borders, dividers, separator lines — 1px only
#6b7280  ->  secondary body text, metadata, timestamps, captions

CSS Custom Properties (paste into :root {}):
:root {
  --bg: #ffffff;
  --surface: #f9fafb;
  --border: #e5e7eb;
  --accent: #0070f3;
  --text-primary: #111827;
  --text-muted: #6b7280;
  --radius-sm: 4px;
  --radius-md: 8px;
  --radius-lg: 16px;
}

Tailwind Config Extension (add inside extend: {}):
colors: { bg: '#ffffff', surface: '#f9fafb', accent: '#0070f3', primary: '#111827', muted: '#6b7280' }

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
  * 1px glowing border cards
  * Keyboard shortcut UI badges
  * Obsidian color system
  * Radial hero glow spotlight
- DO NOT COPY (Proprietary / Brand Specific):
  * Proprietary Fathom Analytics brand logos
  * Exact Fathom Analytics copyrighted assets
  * Direct company trademarks
- TECHNICAL IMPLEMENTATION GUIDANCE:
  Development Guide: Use Tailwind bg-[#08090a], border-white/10, hover:border-white/20, font-inter with -tracking-[0.02em] and lucide-react icons.

==================================================================
🛠️ STEP-BY-STEP REFACTORING INSTRUCTIONS
==================================================================
1. READ the user's current project files, identify domain, existing components, and tech stack.
2. INJECT the CSS custom properties above into the global stylesheet or Tailwind config.
3. RE-ARCHITECT each layout section to match the page architecture scaffold above.
4. RE-ENGINEER every UI component (nav, hero, cards, buttons, inputs, footer) into the Fathom Analytics visual language while keeping the user's real content, data, and workflows intact.
5. APPLY motion physics (transitions, hover states, scroll reveals) as specified above.
6. WRITE all page copy in the Copy Voice defined above -- match the tone, not the brand name.
7. VERIFY: The output should feel unmistakably like Fathom Analytics's design aesthetic applied to the user's own project domain.

==================================================================
📦 DELIVERABLE DEFINITION
==================================================================
Apply CSS custom properties globally first. Then rework each component to match theme tokens. Preserve all domain data and business logic — only the visual layer changes.
```
