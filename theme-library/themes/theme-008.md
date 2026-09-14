# THEME #008 --- Notion

- **Website URL:** [https://www.notion.com/](https://www.notion.com/)
- **Category:** SaaS / Product
- **Design Style:** Vibrant Multi-Layered Product Hub
- **Mode:** adaptive
- **Tags:** `saas-product`, `light`, `saas`

---

## 🧬 Theme DNA Summary
> **Notion design DNA: Large typography, generous whitespace, monochrome palette, subtle borders, restrained motion, asymmetric hero composition and strong product-focused visual hierarchy.**

---

## 🔑 Signature Visual Element
Clean blank-canvas aesthetic: default serif-less type on pure white, sidebar tree navigation, block-based content modular system. The page itself IS the product — no decorative chrome, zero visual clutter.

---

## 🎭 Emotional Intent
Calm, infinite flexibility, your second brain. The user feels perfectly organized and infinitely capable. Notion is the world's most flexible notebook — the UI should feel blank, inviting, and effortlessly structured.

---

## 🎯 Design Principles ("Why does this look like this?")
Why Notion looks like this: Built to communicate speed, craft, and keyboard-first productivity by removing clutter and focusing on high contrast, micro-details, and crisp dark backgrounds.

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
  --surface: #f7f6f3;
  --border: #e3e2e0;
  --accent: #0f7b6c;
  --text-primary: #37352f;
  --text-muted: #9b9a97;
  --radius-sm: 3px;
  --radius-md: 6px;
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

**Copy Voice:** Friendly, inclusive, capability-focused. 'Write, plan, organize. Notion is the connected workspace where better, faster work happens.' Simple language. Anyone can understand. CTAs: 'Get Notion free', 'Try it out', 'See how it works'.

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
1. Nav: white, logo left, product dropdown, 'Request a demo' + 'Get Notion free'
2. Hero: centered headline (56px), subtitle, 2 CTAs, product screenshot below
3. Company logos: 'Trusted by 35 million users at...' colored logos strip
4. Feature trio: 3-column icon + headline + body, clean white section
5. Product demo block: actual product GIF/screenshot showing block editing
6. Use-case tabs: 'For teams', 'For personal', 'For startups' — each shows different view
7. Templates gallery: card grid, hover reveals template preview
8. Social proof: quote + avatar + company
9. Footer: 5-col link grid on white

---

## 🚫 Anti-Patterns (What NOT to do)
- No dark hero sections — Notion is always light/white first
- No gradient backgrounds or gradient text
- No heavy shadows on cards — use very subtle shadows (0 1px 3px rgba(0,0,0,0.08))
- No rounded corners above 6px on structural containers
- No animations beyond simple fade/slide reveals
- No bold color accents except in CTA buttons

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
- Notion-inspired applications
- SaaS / Product platforms

---

## ✅ Things To Reuse
  * 1px glowing border cards
  * Keyboard shortcut UI badges
  * Obsidian color system
  * Radial hero glow spotlight

---

## ❌ Things NOT To Copy
  * Proprietary Notion brand logos
  * Exact Notion copyrighted assets
  * Direct company trademarks

---

## 🛠️ Implementation Notes
Development Guide: Use Tailwind bg-[#08090a], border-white/10, hover:border-white/20, font-inter with -tracking-[0.02em] and lucide-react icons.

---

## 🤖 Deep Comprehensive AI Prompt
```text
[SYSTEM INSTRUCTION: SINGLE-SOURCE THEME DESIGN ADAPTER]
You are a Principal UI/UX Architect & Frontend Design System Engineer.
Your task is to analyze the user's current project / objective, and TRANSFORM / REDESIGN its entire frontend style, visual aesthetic, UX feeling, and component architecture strictly using the design system DNA of THEME #008 (Notion - https://www.notion.com/).

Maintain 100% strict theme isolation: extract and apply ONLY this reference theme's design language, tokens, and aesthetic principles.

==================================================================
🎯 CORE OBJECTIVE: ADAPT THEME TO USER'S PROJECT (NOT A BLIND CLONE)
==================================================================
1. ANALYZE CURRENT PROJECT & GOAL:
   - Carefully inspect the user's current project codebase, wireframes, or feature requirements (e.g. e-commerce clothing store selling shirts, SaaS tool, personal portfolio, marketplace, dashboard, etc.).
   - Preserve the user's core project purpose, domain data, functional workflows, and business logic.

2. TRANSLATE DESIGN DNA (DO NOT COPY PROPRIETARY CONTENT):
   - Do NOT blindly copy placeholder copy, trademarks, or unrelated product catalog from Notion (e.g., do not insert "Notion" branding or unrelated product listings).
   - DO extract and adopt 100% of Notion's visual craft, color palette, typography hierarchy, card structures, spacing rhythm, surface depth, micro-interactions, and UX feeling.

3. ELEVATE & RESKIN EVERY COMPONENT:
   - Reskin the user's existing components (navbars, heroes, product/feature cards, buttons, filters, inputs, modals, footers) into the authentic visual language of THEME #008.
   - Example: If the user's project is an apparel store selling shirts, design a high-craft shirt catalog with Notion's signature layouts, typography scale, lighting, and button styles.

==================================================================
🧬 THEME #008 IDENTITY & EMOTIONAL BRIEF
==================================================================
- Permanent Theme ID: THEME #008
- Reference Design Source: Notion (https://www.notion.com/)
- Mode: adaptive
- Archetype / Category: SaaS / Product
- Design Style: Vibrant Multi-Layered Product Hub
- Visual Personality: Notion signature design: vibrant multi-layered product hub, engineered with high-craft aesthetics, structured hierarchy, and platform-native ergonomics.
- Core Design DNA: Notion design DNA: Large typography, generous whitespace, monochrome palette, subtle borders, restrained motion, asymmetric hero composition and strong product-focused visual hierarchy.

THE SIGNATURE VISUAL ELEMENT (What makes this theme unmistakably Notion):
Clean blank-canvas aesthetic: default serif-less type on pure white, sidebar tree navigation, block-based content modular system. The page itself IS the product — no decorative chrome, zero visual clutter.

EMOTIONAL INTENT (How the user should FEEL when they see this design):
Calm, infinite flexibility, your second brain. The user feels perfectly organized and infinitely capable. Notion is the world's most flexible notebook — the UI should feel blank, inviting, and effortlessly structured.

==================================================================
🎨 COLOR SYSTEM & APPLICATION RULES
==================================================================
#ffffff  ->  page canvas background, sidebar background
#37352f  ->  all body text, headings, UI labels — deep warm black
#0f7b6c  ->  primary CTAs, active states, links, selection highlights
#f7f6f3  ->  hover backgrounds on sidebar items, table row alternates
#e3e2e0  ->  borders, dividers, database table lines
#9b9a97  ->  placeholder text, metadata, secondary labels

CSS Custom Properties (paste into :root {}):
:root {
  --bg: #ffffff;
  --surface: #f7f6f3;
  --border: #e3e2e0;
  --accent: #0f7b6c;
  --text-primary: #37352f;
  --text-muted: #9b9a97;
  --radius-sm: 3px;
  --radius-md: 6px;
}

Tailwind Config Extension (add inside extend: {}):
colors: { bg: '#ffffff', surface: '#f7f6f3', border: '#e3e2e0', accent: '#0f7b6c', primary: '#37352f', muted: '#9b9a97' }

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
Friendly, inclusive, capability-focused. 'Write, plan, organize. Notion is the connected workspace where better, faster work happens.' Simple language. Anyone can understand. CTAs: 'Get Notion free', 'Try it out', 'See how it works'.

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
1. Nav: white, logo left, product dropdown, 'Request a demo' + 'Get Notion free'
2. Hero: centered headline (56px), subtitle, 2 CTAs, product screenshot below
3. Company logos: 'Trusted by 35 million users at...' colored logos strip
4. Feature trio: 3-column icon + headline + body, clean white section
5. Product demo block: actual product GIF/screenshot showing block editing
6. Use-case tabs: 'For teams', 'For personal', 'For startups' — each shows different view
7. Templates gallery: card grid, hover reveals template preview
8. Social proof: quote + avatar + company
9. Footer: 5-col link grid on white

==================================================================
ANTI-PATTERNS (what NOT to do -- these break theme authenticity)
==================================================================
  X No dark hero sections — Notion is always light/white first
  X No gradient backgrounds or gradient text
  X No heavy shadows on cards — use very subtle shadows (0 1px 3px rgba(0,0,0,0.08))
  X No rounded corners above 6px on structural containers
  X No animations beyond simple fade/slide reveals
  X No bold color accents except in CTA buttons

==================================================================
🛡️ DESIGN FIDELITY GUARDRAILS
==================================================================
- MUST ADOPT & REUSE:
  * 1px glowing border cards
  * Keyboard shortcut UI badges
  * Obsidian color system
  * Radial hero glow spotlight
- DO NOT COPY (Proprietary / Brand Specific):
  * Proprietary Notion brand logos
  * Exact Notion copyrighted assets
  * Direct company trademarks
- TECHNICAL IMPLEMENTATION GUIDANCE:
  Development Guide: Use Tailwind bg-[#08090a], border-white/10, hover:border-white/20, font-inter with -tracking-[0.02em] and lucide-react icons.

==================================================================
🛠️ STEP-BY-STEP REFACTORING INSTRUCTIONS
==================================================================
1. READ the user's current project files, identify domain, existing components, and tech stack.
2. INJECT the CSS custom properties above into the global stylesheet or Tailwind config.
3. RE-ARCHITECT each layout section to match the page architecture scaffold above.
4. RE-ENGINEER every UI component (nav, hero, cards, buttons, inputs, footer) into the Notion visual language while keeping the user's real content, data, and workflows intact.
5. APPLY motion physics (transitions, hover states, scroll reveals) as specified above.
6. WRITE all page copy in the Copy Voice defined above -- match the tone, not the brand name.
7. VERIFY: The output should feel unmistakably like Notion's design aesthetic applied to the user's own project domain.

==================================================================
📦 DELIVERABLE DEFINITION
==================================================================
Keep the palette clean and restrained. The power is in the whitespace and typography, not color.
```
