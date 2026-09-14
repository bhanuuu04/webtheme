# THEME #473 --- Feastables

- **Website URL:** [https://feastables.com/](https://feastables.com/)
- **Category:** E-commerce / Consumer
- **Design Style:** Minimalist Clean Curation
- **Mode:** light
- **Tags:** `e-commerce-consumer`, `light`, `minimal`

---

## 🧬 Theme DNA Summary
> **Feastables design DNA: Product shelf grids, secondary hover image flips, instant slide-over cart drawer, and high-contrast Add to Cart CTA.**

---

## 🔑 Signature Visual Element
Clean white editorial canvas with #18181b as the single brand accent color. Large display typography and generous whitespace communicate the premium quality of Feastables. Product screenshots or lifestyle imagery on clean white/off-white backgrounds.

---

## 🎭 Emotional Intent
Clarity and trustworthiness. The user feels confident that Feastables is the right choice — professional, accessible, and purpose-built for their needs. The clean light design removes friction and communicates reliability.

---

## 🎯 Design Principles ("Why does this look like this?")
Why Feastables looks like this: Engineered to maximize product desirability, minimize checkout friction, and convey brand lifestyle authenticity.

---

## 🎨 Color System

### Primary Palette
- **`#ffffff`** --- Pure White Canvas
- **`#18181b`** --- Charcoal Typography
- **`#ff4f00`** --- Vibrant D2C Orange

### Secondary & Surface Palette
- **`#f4f4f5`** --- Product Shelf Surface
- **`#e4e4e7`** --- Subtle Shelf Border
- **`#71717a`** --- Product Review Subtext

### CSS Custom Properties
```css
:root {
  --bg: #ffffff;
  --surface: #f4f4f5;
  --border: #e4e4e7;
  --accent: #18181b;
  --text-primary: #ff4f00;
  --text-muted: #71717a;
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
1. Sticky nav: logo, search bar, cart icon, account
2. Hero: full-bleed product imagery, headline overlay, CTA
3. Category pills: horizontal filter strip
4. Product grid: responsive 3-4 col card layout with price + rating
5. Featured collection: large showcase tile
6. Trust signals: shipping, returns, guarantee icons
7. Testimonials/reviews: star-rated quote cards
8. Footer: 4-col links, newsletter, social

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
- D2C e-commerce brands
- Consumer electronics stores
- Apparel & fashion shops
- Subscription boxes
- Feastables-inspired applications
- E-commerce / Consumer platforms

---

## ✅ Things To Reuse
  * Hover image flip product card
  * Slide-over cart drawer
  * Sticky mobile buy bar
  * Announcement marquee bar

---

## ❌ Things NOT To Copy
  * Proprietary Feastables brand logos
  * Exact Feastables copyrighted assets
  * Direct company trademarks

---

## 🛠️ Implementation Notes
Development Guide: Use Tailwind grid system, slide-over drawer modals, and snappy hovers.

---

## 🤖 Deep Comprehensive AI Prompt
```text
[SYSTEM INSTRUCTION: SINGLE-SOURCE THEME DESIGN ADAPTER]
You are a Principal UI/UX Architect & Frontend Design System Engineer.
Your task is to analyze the user's current project / objective, and TRANSFORM / REDESIGN its entire frontend style, visual aesthetic, UX feeling, and component architecture strictly using the design system DNA of THEME #473 (Feastables - https://feastables.com/).

Maintain 100% strict theme isolation: extract and apply ONLY this reference theme's design language, tokens, and aesthetic principles.

==================================================================
🎯 CORE OBJECTIVE: ADAPT THEME TO USER'S PROJECT (NOT A BLIND CLONE)
==================================================================
1. ANALYZE CURRENT PROJECT & GOAL:
   - Carefully inspect the user's current project codebase, wireframes, or feature requirements (e.g. e-commerce clothing store selling shirts, SaaS tool, personal portfolio, marketplace, dashboard, etc.).
   - Preserve the user's core project purpose, domain data, functional workflows, and business logic.

2. TRANSLATE DESIGN DNA (DO NOT COPY PROPRIETARY CONTENT):
   - Do NOT blindly copy placeholder copy, trademarks, or unrelated product catalog from Feastables (e.g., do not insert "Feastables" branding or unrelated product listings).
   - DO extract and adopt 100% of Feastables's visual craft, color palette, typography hierarchy, card structures, spacing rhythm, surface depth, micro-interactions, and UX feeling.

3. ELEVATE & RESKIN EVERY COMPONENT:
   - Reskin the user's existing components (navbars, heroes, product/feature cards, buttons, filters, inputs, modals, footers) into the authentic visual language of THEME #473.
   - Example: If the user's project is an apparel store selling shirts, design a high-craft shirt catalog with Feastables's signature layouts, typography scale, lighting, and button styles.

==================================================================
🧬 THEME #473 IDENTITY & EMOTIONAL BRIEF
==================================================================
- Permanent Theme ID: THEME #473
- Reference Design Source: Feastables (https://feastables.com/)
- Mode: light
- Archetype / Category: E-commerce / Consumer
- Design Style: Minimalist Clean Curation
- Visual Personality: Feastables signature design: minimalist clean curation, engineered with high-craft aesthetics, structured hierarchy, and platform-native ergonomics.
- Core Design DNA: Feastables design DNA: Product shelf grids, secondary hover image flips, instant slide-over cart drawer, and high-contrast Add to Cart CTA.

THE SIGNATURE VISUAL ELEMENT (What makes this theme unmistakably Feastables):
Clean white editorial canvas with #18181b as the single brand accent color. Large display typography and generous whitespace communicate the premium quality of Feastables. Product screenshots or lifestyle imagery on clean white/off-white backgrounds.

EMOTIONAL INTENT (How the user should FEEL when they see this design):
Clarity and trustworthiness. The user feels confident that Feastables is the right choice — professional, accessible, and purpose-built for their needs. The clean light design removes friction and communicates reliability.

==================================================================
🎨 COLOR SYSTEM & APPLICATION RULES
==================================================================
#ffffff  ->  page background, all section backgrounds
#18181b  ->  primary CTA buttons, links on hover, focus rings, selected states, brand accents
#ff4f00  ->  all headings (H1-H3), body text, primary UI labels
#f4f4f5  ->  card surfaces, modal backgrounds, input field backgrounds
#e4e4e7  ->  borders, dividers, separator lines — 1px only
#71717a  ->  secondary body text, metadata, timestamps, captions

CSS Custom Properties (paste into :root {}):
:root {
  --bg: #ffffff;
  --surface: #f4f4f5;
  --border: #e4e4e7;
  --accent: #18181b;
  --text-primary: #ff4f00;
  --text-muted: #71717a;
  --radius-sm: 4px;
  --radius-md: 8px;
  --radius-lg: 16px;
}

Tailwind Config Extension (add inside extend: {}):
colors: { bg: '#ffffff', surface: '#f4f4f5', accent: '#18181b', primary: '#ff4f00', muted: '#71717a' }

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
1. Sticky nav: logo, search bar, cart icon, account
2. Hero: full-bleed product imagery, headline overlay, CTA
3. Category pills: horizontal filter strip
4. Product grid: responsive 3-4 col card layout with price + rating
5. Featured collection: large showcase tile
6. Trust signals: shipping, returns, guarantee icons
7. Testimonials/reviews: star-rated quote cards
8. Footer: 4-col links, newsletter, social

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
  * Hover image flip product card
  * Slide-over cart drawer
  * Sticky mobile buy bar
  * Announcement marquee bar
- DO NOT COPY (Proprietary / Brand Specific):
  * Proprietary Feastables brand logos
  * Exact Feastables copyrighted assets
  * Direct company trademarks
- TECHNICAL IMPLEMENTATION GUIDANCE:
  Development Guide: Use Tailwind grid system, slide-over drawer modals, and snappy hovers.

==================================================================
🛠️ STEP-BY-STEP REFACTORING INSTRUCTIONS
==================================================================
1. READ the user's current project files, identify domain, existing components, and tech stack.
2. INJECT the CSS custom properties above into the global stylesheet or Tailwind config.
3. RE-ARCHITECT each layout section to match the page architecture scaffold above.
4. RE-ENGINEER every UI component (nav, hero, cards, buttons, inputs, footer) into the Feastables visual language while keeping the user's real content, data, and workflows intact.
5. APPLY motion physics (transitions, hover states, scroll reveals) as specified above.
6. WRITE all page copy in the Copy Voice defined above -- match the tone, not the brand name.
7. VERIFY: The output should feel unmistakably like Feastables's design aesthetic applied to the user's own project domain.

==================================================================
📦 DELIVERABLE DEFINITION
==================================================================
Apply CSS custom properties globally first. Then rework each component to match theme tokens. Preserve all domain data and business logic — only the visual layer changes.
```
