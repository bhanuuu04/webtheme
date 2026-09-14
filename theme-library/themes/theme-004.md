# THEME #004 --- Framer

- **Website URL:** [https://www.framer.com/](https://www.framer.com/)
- **Category:** SaaS / Product
- **Design Style:** Vibrant Multi-Layered Product Hub
- **Mode:** dark
- **Tags:** `saas-product`, `dark`, `saas`

---

## 🧬 Theme DNA Summary
> **Framer design DNA: Large typography, generous whitespace, monochrome palette, subtle borders, restrained motion, asymmetric hero composition and strong product-focused visual hierarchy.**

---

## 🔑 Signature Visual Element
Full-bleed kinetic motion hero — large text animates on scroll/load with spring physics. Dramatic product viewport previews with 3D perspective tilt. Bold section breaks using oversized typography (120px+) as decorative elements.

---

## 🎭 Emotional Intent
Alive, kinetic, experimental. The visitor feels this tool is made by people who love pushing the boundaries of what the web can do. Motion IS the message. Every scroll triggers delight.

---

## 🎯 Design Principles ("Why does this look like this?")
Why Framer looks like this: Built to communicate speed, craft, and keyboard-first productivity by removing clutter and focusing on high contrast, micro-details, and crisp dark backgrounds.

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
  --bg: #0d0d0d;
  --surface: #1a1a1a;
  --border: #2a2a2a;
  --accent: #0099ff;
  --text-primary: #ffffff;
  --text-muted: #888888;
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

**Copy Voice:** Creative-forward, energetic without being loud. 'Build your dream site. No code required.' Short, punchy. Product-forward. CTAs: 'Start for free', 'See examples', 'Explore templates'. Tone is enthusiastic but not hyped.

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
1. Nav: transparent dark, logo + minimal links, 'Get started free' pill
2. Hero: full viewport height, animated kinetic headline, scroll-triggered reveal
3. Product viewport showcase: browser frame with site-in-motion GIF/video
4. Feature bento grid: asymmetric 3-4 tile layout, each tile animated on hover
5. Template gallery: horizontal scroll strip, card hover = 3D tilt
6. Testimonials: oversized pull quote, minimal attribution
7. CTA section: full-width dark, kinetic headline, single CTA button
8. Footer: minimal dark 4-col

---

## 🚫 Anti-Patterns (What NOT to do)
- No static hero — there must be motion (CSS animation or JS-driven)
- No small typography in hero — minimum 72px for hero headlines
- No symmetrical layouts — asymmetric, overlapping compositions are authentic
- No subtle micro-interactions — Framer interactions are visible and dramatic
- No traditional corporate grids — break the grid intentionally

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
- Framer-inspired applications
- SaaS / Product platforms

---

## ✅ Things To Reuse
  * 1px glowing border cards
  * Keyboard shortcut UI badges
  * Obsidian color system
  * Radial hero glow spotlight

---

## ❌ Things NOT To Copy
  * Proprietary Framer brand logos
  * Exact Framer copyrighted assets
  * Direct company trademarks

---

## 🛠️ Implementation Notes
Development Guide: Use Tailwind bg-[#08090a], border-white/10, hover:border-white/20, font-inter with -tracking-[0.02em] and lucide-react icons.

---

## 🤖 Deep Comprehensive AI Prompt
```text
[SYSTEM INSTRUCTION: SINGLE-SOURCE THEME DESIGN ADAPTER]
You are a Principal UI/UX Architect & Frontend Design System Engineer.
Your task is to analyze the user's current project / objective, and TRANSFORM / REDESIGN its entire frontend style, visual aesthetic, UX feeling, and component architecture strictly using the design system DNA of THEME #004 (Framer - https://www.framer.com/).

Maintain 100% strict theme isolation: extract and apply ONLY this reference theme's design language, tokens, and aesthetic principles.

==================================================================
🎯 CORE OBJECTIVE: ADAPT THEME TO USER'S PROJECT (NOT A BLIND CLONE)
==================================================================
1. ANALYZE CURRENT PROJECT & GOAL:
   - Carefully inspect the user's current project codebase, wireframes, or feature requirements (e.g. e-commerce clothing store selling shirts, SaaS tool, personal portfolio, marketplace, dashboard, etc.).
   - Preserve the user's core project purpose, domain data, functional workflows, and business logic.

2. TRANSLATE DESIGN DNA (DO NOT COPY PROPRIETARY CONTENT):
   - Do NOT blindly copy placeholder copy, trademarks, or unrelated product catalog from Framer (e.g., do not insert "Framer" branding or unrelated product listings).
   - DO extract and adopt 100% of Framer's visual craft, color palette, typography hierarchy, card structures, spacing rhythm, surface depth, micro-interactions, and UX feeling.

3. ELEVATE & RESKIN EVERY COMPONENT:
   - Reskin the user's existing components (navbars, heroes, product/feature cards, buttons, filters, inputs, modals, footers) into the authentic visual language of THEME #004.
   - Example: If the user's project is an apparel store selling shirts, design a high-craft shirt catalog with Framer's signature layouts, typography scale, lighting, and button styles.

==================================================================
🧬 THEME #004 IDENTITY & EMOTIONAL BRIEF
==================================================================
- Permanent Theme ID: THEME #004
- Reference Design Source: Framer (https://www.framer.com/)
- Mode: dark
- Archetype / Category: SaaS / Product
- Design Style: Vibrant Multi-Layered Product Hub
- Visual Personality: Framer signature design: vibrant multi-layered product hub, engineered with high-craft aesthetics, structured hierarchy, and platform-native ergonomics.
- Core Design DNA: Framer design DNA: Large typography, generous whitespace, monochrome palette, subtle borders, restrained motion, asymmetric hero composition and strong product-focused visual hierarchy.

THE SIGNATURE VISUAL ELEMENT (What makes this theme unmistakably Framer):
Full-bleed kinetic motion hero — large text animates on scroll/load with spring physics. Dramatic product viewport previews with 3D perspective tilt. Bold section breaks using oversized typography (120px+) as decorative elements.

EMOTIONAL INTENT (How the user should FEEL when they see this design):
Alive, kinetic, experimental. The visitor feels this tool is made by people who love pushing the boundaries of what the web can do. Motion IS the message. Every scroll triggers delight.

==================================================================
🎨 COLOR SYSTEM & APPLICATION RULES
==================================================================
#0d0d0d  ->  body background, all major sections
#0099ff  ->  primary CTAs, hover accents, animated underlines, focus rings
#ffffff  ->  display headlines, nav links, primary text
#1a1a1a  ->  card surfaces, code blocks, modal backgrounds
#888888  ->  body copy, metadata, secondary descriptions

CSS Custom Properties (paste into :root {}):
:root {
  --bg: #0d0d0d;
  --surface: #1a1a1a;
  --border: #2a2a2a;
  --accent: #0099ff;
  --text-primary: #ffffff;
  --text-muted: #888888;
  --radius-md: 8px;
  --radius-lg: 16px;
}

Tailwind Config Extension (add inside extend: {}):
colors: { bg: '#0d0d0d', surface: '#1a1a1a', accent: '#0099ff', primary: '#ffffff', muted: '#888888' }

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
Creative-forward, energetic without being loud. 'Build your dream site. No code required.' Short, punchy. Product-forward. CTAs: 'Start for free', 'See examples', 'Explore templates'. Tone is enthusiastic but not hyped.

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
1. Nav: transparent dark, logo + minimal links, 'Get started free' pill
2. Hero: full viewport height, animated kinetic headline, scroll-triggered reveal
3. Product viewport showcase: browser frame with site-in-motion GIF/video
4. Feature bento grid: asymmetric 3-4 tile layout, each tile animated on hover
5. Template gallery: horizontal scroll strip, card hover = 3D tilt
6. Testimonials: oversized pull quote, minimal attribution
7. CTA section: full-width dark, kinetic headline, single CTA button
8. Footer: minimal dark 4-col

==================================================================
ANTI-PATTERNS (what NOT to do -- these break theme authenticity)
==================================================================
  X No static hero — there must be motion (CSS animation or JS-driven)
  X No small typography in hero — minimum 72px for hero headlines
  X No symmetrical layouts — asymmetric, overlapping compositions are authentic
  X No subtle micro-interactions — Framer interactions are visible and dramatic
  X No traditional corporate grids — break the grid intentionally

==================================================================
🛡️ DESIGN FIDELITY GUARDRAILS
==================================================================
- MUST ADOPT & REUSE:
  * 1px glowing border cards
  * Keyboard shortcut UI badges
  * Obsidian color system
  * Radial hero glow spotlight
- DO NOT COPY (Proprietary / Brand Specific):
  * Proprietary Framer brand logos
  * Exact Framer copyrighted assets
  * Direct company trademarks
- TECHNICAL IMPLEMENTATION GUIDANCE:
  Development Guide: Use Tailwind bg-[#08090a], border-white/10, hover:border-white/20, font-inter with -tracking-[0.02em] and lucide-react icons.

==================================================================
🛠️ STEP-BY-STEP REFACTORING INSTRUCTIONS
==================================================================
1. READ the user's current project files, identify domain, existing components, and tech stack.
2. INJECT the CSS custom properties above into the global stylesheet or Tailwind config.
3. RE-ARCHITECT each layout section to match the page architecture scaffold above.
4. RE-ENGINEER every UI component (nav, hero, cards, buttons, inputs, footer) into the Framer visual language while keeping the user's real content, data, and workflows intact.
5. APPLY motion physics (transitions, hover states, scroll reveals) as specified above.
6. WRITE all page copy in the Copy Voice defined above -- match the tone, not the brand name.
7. VERIFY: The output should feel unmistakably like Framer's design aesthetic applied to the user's own project domain.

==================================================================
📦 DELIVERABLE DEFINITION
==================================================================
Ensure all interactive elements have visible motion transitions. The motion IS the theme's primary signature.
```
