# THEME #012 --- Airbnb

- **Website URL:** [https://www.airbnb.com/](https://www.airbnb.com/)
- **Category:** SaaS / Product
- **Design Style:** Vibrant Multi-Layered Product Hub
- **Mode:** light
- **Tags:** `saas-product`, `light`, `saas`, `ai`

---

## 🧬 Theme DNA Summary
> **Airbnb design DNA: Large typography, generous whitespace, monochrome palette, subtle borders, restrained motion, asymmetric hero composition and strong product-focused visual hierarchy.**

---

## 🔑 Signature Visual Element
Full-bleed destination photography with an Airbnb-pink search pill floating over it. Warm, human-centered card grid with circular host avatar overlapping the card photo. Signature coral-pink (#FF5A5F) used exclusively on primary CTA and brand marks.

---

## 🎭 Emotional Intent
Warmth, adventure, belonging. The visitor feels they can belong anywhere in the world. The design prioritizes human faces and real spaces over abstract visuals. 'Belong Anywhere.'

---

## 🎯 Design Principles ("Why does this look like this?")
Why Airbnb looks like this: Built to communicate speed, craft, and keyboard-first productivity by removing clutter and focusing on high contrast, micro-details, and crisp dark backgrounds.

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
  --surface: #f7f7f7;
  --border: #EBEBEB;
  --accent: #FF5A5F;
  --text-primary: #222222;
  --text-muted: #717171;
  --radius-sm: 8px;
  --radius-md: 12px;
  --radius-lg: 16px;
  --radius-full: 9999px;
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

**Copy Voice:** Warm, inclusive, adventurous. 'Find your place in the world.' Human-first. Celebrates community and discovery. CTAs: 'Explore nearby', 'Start hosting', 'Find experiences'. Tone is optimistic and welcoming.

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
1. Nav: white, logo left (coral), search pill center, profile + hamburger right
2. Hero: full-bleed photo, centered search bar with location/dates/guests pills
3. Category pills: horizontal scroll strip (beaches, mountains, cabins, etc.)
4. Listing grid: 2-4 col responsive card grid, photo top 65%, host avatar, price, rating
5. 'Airbnb it' CTA: split 2-col, lifestyle photo left, form/CTA right
6. Experiences section: card grid for activities
7. Trust section: 3 icons with headline + body copy
8. Footer: 4-col link grid, language/currency selector

---

## 🚫 Anti-Patterns (What NOT to do)
- No dark canvas — Airbnb is always warm white
- No corporate geometric layouts — organic, human-centered compositions
- No icons-heavy interfaces — photography first always
- No cold blue color accents — warmth is essential (coral, warm grays)
- No product screenshots — real photography of real spaces only

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
- Airbnb-inspired applications
- SaaS / Product platforms

---

## ✅ Things To Reuse
  * 1px glowing border cards
  * Keyboard shortcut UI badges
  * Obsidian color system
  * Radial hero glow spotlight

---

## ❌ Things NOT To Copy
  * Proprietary Airbnb brand logos
  * Exact Airbnb copyrighted assets
  * Direct company trademarks

---

## 🛠️ Implementation Notes
Development Guide: Use Tailwind bg-[#08090a], border-white/10, hover:border-white/20, font-inter with -tracking-[0.02em] and lucide-react icons.

---

## 🤖 Deep Comprehensive AI Prompt
```text
[SYSTEM INSTRUCTION: SINGLE-SOURCE THEME DESIGN ADAPTER]
You are a Principal UI/UX Architect & Frontend Design System Engineer.
Your task is to analyze the user's current project / objective, and TRANSFORM / REDESIGN its entire frontend style, visual aesthetic, UX feeling, and component architecture strictly using the design system DNA of THEME #012 (Airbnb - https://www.airbnb.com/).

Maintain 100% strict theme isolation: extract and apply ONLY this reference theme's design language, tokens, and aesthetic principles.

==================================================================
🎯 CORE OBJECTIVE: ADAPT THEME TO USER'S PROJECT (NOT A BLIND CLONE)
==================================================================
1. ANALYZE CURRENT PROJECT & GOAL:
   - Carefully inspect the user's current project codebase, wireframes, or feature requirements (e.g. e-commerce clothing store selling shirts, SaaS tool, personal portfolio, marketplace, dashboard, etc.).
   - Preserve the user's core project purpose, domain data, functional workflows, and business logic.

2. TRANSLATE DESIGN DNA (DO NOT COPY PROPRIETARY CONTENT):
   - Do NOT blindly copy placeholder copy, trademarks, or unrelated product catalog from Airbnb (e.g., do not insert "Airbnb" branding or unrelated product listings).
   - DO extract and adopt 100% of Airbnb's visual craft, color palette, typography hierarchy, card structures, spacing rhythm, surface depth, micro-interactions, and UX feeling.

3. ELEVATE & RESKIN EVERY COMPONENT:
   - Reskin the user's existing components (navbars, heroes, product/feature cards, buttons, filters, inputs, modals, footers) into the authentic visual language of THEME #012.
   - Example: If the user's project is an apparel store selling shirts, design a high-craft shirt catalog with Airbnb's signature layouts, typography scale, lighting, and button styles.

==================================================================
🧬 THEME #012 IDENTITY & EMOTIONAL BRIEF
==================================================================
- Permanent Theme ID: THEME #012
- Reference Design Source: Airbnb (https://www.airbnb.com/)
- Mode: light
- Archetype / Category: SaaS / Product
- Design Style: Vibrant Multi-Layered Product Hub
- Visual Personality: Airbnb signature design: vibrant multi-layered product hub, engineered with high-craft aesthetics, structured hierarchy, and platform-native ergonomics.
- Core Design DNA: Airbnb design DNA: Large typography, generous whitespace, monochrome palette, subtle borders, restrained motion, asymmetric hero composition and strong product-focused visual hierarchy.

THE SIGNATURE VISUAL ELEMENT (What makes this theme unmistakably Airbnb):
Full-bleed destination photography with an Airbnb-pink search pill floating over it. Warm, human-centered card grid with circular host avatar overlapping the card photo. Signature coral-pink (#FF5A5F) used exclusively on primary CTA and brand marks.

EMOTIONAL INTENT (How the user should FEEL when they see this design):
Warmth, adventure, belonging. The visitor feels they can belong anywhere in the world. The design prioritizes human faces and real spaces over abstract visuals. 'Belong Anywhere.'

==================================================================
🎨 COLOR SYSTEM & APPLICATION RULES
==================================================================
#FF5A5F  ->  primary CTA buttons, brand logo, hover states, selected stars, price highlights
#ffffff  ->  page canvas, card backgrounds, nav background
#222222  ->  headings, card titles, primary body text
#717171  ->  secondary text, metadata, dates, secondary labels
#EBEBEB  ->  borders, dividers, skeleton loading states
#008489  ->  secondary accent for 'Plus' tier badging and map pins

CSS Custom Properties (paste into :root {}):
:root {
  --bg: #ffffff;
  --surface: #f7f7f7;
  --border: #EBEBEB;
  --accent: #FF5A5F;
  --text-primary: #222222;
  --text-muted: #717171;
  --radius-sm: 8px;
  --radius-md: 12px;
  --radius-lg: 16px;
  --radius-full: 9999px;
}

Tailwind Config Extension (add inside extend: {}):
colors: { bg: '#ffffff', surface: '#f7f7f7', border: '#EBEBEB', accent: '#FF5A5F', primary: '#222222', muted: '#717171' }

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
Warm, inclusive, adventurous. 'Find your place in the world.' Human-first. Celebrates community and discovery. CTAs: 'Explore nearby', 'Start hosting', 'Find experiences'. Tone is optimistic and welcoming.

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
1. Nav: white, logo left (coral), search pill center, profile + hamburger right
2. Hero: full-bleed photo, centered search bar with location/dates/guests pills
3. Category pills: horizontal scroll strip (beaches, mountains, cabins, etc.)
4. Listing grid: 2-4 col responsive card grid, photo top 65%, host avatar, price, rating
5. 'Airbnb it' CTA: split 2-col, lifestyle photo left, form/CTA right
6. Experiences section: card grid for activities
7. Trust section: 3 icons with headline + body copy
8. Footer: 4-col link grid, language/currency selector

==================================================================
ANTI-PATTERNS (what NOT to do -- these break theme authenticity)
==================================================================
  X No dark canvas — Airbnb is always warm white
  X No corporate geometric layouts — organic, human-centered compositions
  X No icons-heavy interfaces — photography first always
  X No cold blue color accents — warmth is essential (coral, warm grays)
  X No product screenshots — real photography of real spaces only

==================================================================
🛡️ DESIGN FIDELITY GUARDRAILS
==================================================================
- MUST ADOPT & REUSE:
  * 1px glowing border cards
  * Keyboard shortcut UI badges
  * Obsidian color system
  * Radial hero glow spotlight
- DO NOT COPY (Proprietary / Brand Specific):
  * Proprietary Airbnb brand logos
  * Exact Airbnb copyrighted assets
  * Direct company trademarks
- TECHNICAL IMPLEMENTATION GUIDANCE:
  Development Guide: Use Tailwind bg-[#08090a], border-white/10, hover:border-white/20, font-inter with -tracking-[0.02em] and lucide-react icons.

==================================================================
🛠️ STEP-BY-STEP REFACTORING INSTRUCTIONS
==================================================================
1. READ the user's current project files, identify domain, existing components, and tech stack.
2. INJECT the CSS custom properties above into the global stylesheet or Tailwind config.
3. RE-ARCHITECT each layout section to match the page architecture scaffold above.
4. RE-ENGINEER every UI component (nav, hero, cards, buttons, inputs, footer) into the Airbnb visual language while keeping the user's real content, data, and workflows intact.
5. APPLY motion physics (transitions, hover states, scroll reveals) as specified above.
6. WRITE all page copy in the Copy Voice defined above -- match the tone, not the brand name.
7. VERIFY: The output should feel unmistakably like Airbnb's design aesthetic applied to the user's own project domain.

==================================================================
📦 DELIVERABLE DEFINITION
==================================================================
Prioritize real photography placeholders. The card grid is the most important component — get the photo proportion and host avatar overlay right.
```
