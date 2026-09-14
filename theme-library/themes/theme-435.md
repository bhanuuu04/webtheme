# THEME #435 --- Apple Store

- **Website URL:** [https://www.apple.com/store/](https://www.apple.com/store/)
- **Category:** E-commerce / Consumer
- **Design Style:** Bold Playful Streetwear Store
- **Mode:** light
- **Tags:** `e-commerce-consumer`, `light`, `playful`

---

## 🧬 Theme DNA Summary
> **Apple Store design DNA: Product shelf grids, secondary hover image flips, instant slide-over cart drawer, and high-contrast Add to Cart CTA.**

---

## 🔑 Signature Visual Element
Giant SF Pro Display typography (80-96px) sitting directly over full-bleed product photography on pure white canvas. No decorative chrome — the product IS the hero. Blue pill CTAs (#0071e3) as the only color accent.

---

## 🎭 Emotional Intent
Holding a premium object. The visitor feels they are experiencing craft at the highest possible level. Simplicity communicates mastery. Every detail communicates 'we thought of everything so you don't have to.'

---

## 🎯 Design Principles ("Why does this look like this?")
Why Apple Store looks like this: Engineered to maximize product desirability, minimize checkout friction, and convey brand lifestyle authenticity.

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
  --bg: #f5f5f7;
  --surface: #ffffff;
  --border: #d2d2d7;
  --accent: #0071e3;
  --text-primary: #1d1d1f;
  --text-muted: #86868b;
  --radius-md: 12px;
  --radius-lg: 18px;
  --radius-xl: 24px;
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

**Copy Voice:** Poetic product authority. Short, rhythm-driven headlines ('Thin. Light. Powerful beyond belief.'). Second-person ('Everything you need.'). No technical jargon in hero. Spec pages use precise technical language. CTAs: 'Shop iPhone', 'Learn more ↗', 'Compare models'.

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
1. Sticky nav: 44px height, white/blur, Apple logo centered on mobile, product categories
2. Cinematic hero: full-viewport product photo, H1 overlaid (bottom-left or centered), CTA pill below
3. Feature overview: 2-up or 3-up tiles on #f5f5f7, each tile = product photo + headline + body
4. Deep feature callout: alternating 2-col (photo left, text right), clean white bg
5. Spec comparison table: clean rows, hairline borders, checkmarks in accent blue
6. Ecosystem section: rounded tiles showing accessory/service lineup
7. Footer: 5-col links on #f5f5f7, language selector, legal links

---

## 🚫 Anti-Patterns (What NOT to do)
- No dark sections except for 'Apple TV+' style media sections
- No gradient backgrounds in main content sections
- No drop shadows on product images — let the photo breathe on white
- No centered text except for hero overlays — left-align all body content
- No more than 1 accent-colored element visible at a time
- No busy backgrounds — white or #f5f5f7 only
- No decorative illustrations — photography only
- No font above 700 weight for regular body sections

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
- Apple Store-inspired applications
- E-commerce / Consumer platforms

---

## ✅ Things To Reuse
  * Hover image flip product card
  * Slide-over cart drawer
  * Sticky mobile buy bar
  * Announcement marquee bar

---

## ❌ Things NOT To Copy
  * Proprietary Apple Store brand logos
  * Exact Apple Store copyrighted assets
  * Direct company trademarks

---

## 🛠️ Implementation Notes
Development Guide: Use Tailwind grid system, slide-over drawer modals, and snappy hovers.

---

## 🤖 Deep Comprehensive AI Prompt
```text
[SYSTEM INSTRUCTION: SINGLE-SOURCE THEME DESIGN ADAPTER]
You are a Principal UI/UX Architect & Frontend Design System Engineer.
Your task is to analyze the user's current project / objective, and TRANSFORM / REDESIGN its entire frontend style, visual aesthetic, UX feeling, and component architecture strictly using the design system DNA of THEME #435 (Apple Store - https://www.apple.com/store/).

Maintain 100% strict theme isolation: extract and apply ONLY this reference theme's design language, tokens, and aesthetic principles.

==================================================================
🎯 CORE OBJECTIVE: ADAPT THEME TO USER'S PROJECT (NOT A BLIND CLONE)
==================================================================
1. ANALYZE CURRENT PROJECT & GOAL:
   - Carefully inspect the user's current project codebase, wireframes, or feature requirements (e.g. e-commerce clothing store selling shirts, SaaS tool, personal portfolio, marketplace, dashboard, etc.).
   - Preserve the user's core project purpose, domain data, functional workflows, and business logic.

2. TRANSLATE DESIGN DNA (DO NOT COPY PROPRIETARY CONTENT):
   - Do NOT blindly copy placeholder copy, trademarks, or unrelated product catalog from Apple Store (e.g., do not insert "Apple Store" branding or unrelated product listings).
   - DO extract and adopt 100% of Apple Store's visual craft, color palette, typography hierarchy, card structures, spacing rhythm, surface depth, micro-interactions, and UX feeling.

3. ELEVATE & RESKIN EVERY COMPONENT:
   - Reskin the user's existing components (navbars, heroes, product/feature cards, buttons, filters, inputs, modals, footers) into the authentic visual language of THEME #435.
   - Example: If the user's project is an apparel store selling shirts, design a high-craft shirt catalog with Apple Store's signature layouts, typography scale, lighting, and button styles.

==================================================================
🧬 THEME #435 IDENTITY & EMOTIONAL BRIEF
==================================================================
- Permanent Theme ID: THEME #435
- Reference Design Source: Apple Store (https://www.apple.com/store/)
- Mode: light
- Archetype / Category: E-commerce / Consumer
- Design Style: Bold Playful Streetwear Store
- Visual Personality: Apple Store signature design: bold playful streetwear store, engineered with high-craft aesthetics, structured hierarchy, and platform-native ergonomics.
- Core Design DNA: Apple Store design DNA: Product shelf grids, secondary hover image flips, instant slide-over cart drawer, and high-contrast Add to Cart CTA.

THE SIGNATURE VISUAL ELEMENT (What makes this theme unmistakably Apple Store):
Giant SF Pro Display typography (80-96px) sitting directly over full-bleed product photography on pure white canvas. No decorative chrome — the product IS the hero. Blue pill CTAs (#0071e3) as the only color accent.

EMOTIONAL INTENT (How the user should FEEL when they see this design):
Holding a premium object. The visitor feels they are experiencing craft at the highest possible level. Simplicity communicates mastery. Every detail communicates 'we thought of everything so you don't have to.'

==================================================================
🎨 COLOR SYSTEM & APPLICATION RULES
==================================================================
#f5f5f7  ->  body background, section backgrounds — signature Apple off-white
#ffffff  ->  card surfaces, nav background, tile backgrounds
#0071e3  ->  all primary CTA buttons, links on hover, focus rings — ONLY here
#1d1d1f  ->  H1, H2, H3, body text — high-contrast near-black
#86868b  ->  eyebrow text, captions, secondary descriptions
#d2d2d7  ->  borders, dividers, table lines — hairline 1px

CSS Custom Properties (paste into :root {}):
:root {
  --bg: #f5f5f7;
  --surface: #ffffff;
  --border: #d2d2d7;
  --accent: #0071e3;
  --text-primary: #1d1d1f;
  --text-muted: #86868b;
  --radius-md: 12px;
  --radius-lg: 18px;
  --radius-xl: 24px;
}

Tailwind Config Extension (add inside extend: {}):
colors: { bg: '#f5f5f7', surface: '#ffffff', border: '#d2d2d7', accent: '#0071e3', primary: '#1d1d1f', muted: '#86868b' }, borderRadius: { md: '12px', lg: '18px', xl: '24px' }

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
Poetic product authority. Short, rhythm-driven headlines ('Thin. Light. Powerful beyond belief.'). Second-person ('Everything you need.'). No technical jargon in hero. Spec pages use precise technical language. CTAs: 'Shop iPhone', 'Learn more ↗', 'Compare models'.

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
1. Sticky nav: 44px height, white/blur, Apple logo centered on mobile, product categories
2. Cinematic hero: full-viewport product photo, H1 overlaid (bottom-left or centered), CTA pill below
3. Feature overview: 2-up or 3-up tiles on #f5f5f7, each tile = product photo + headline + body
4. Deep feature callout: alternating 2-col (photo left, text right), clean white bg
5. Spec comparison table: clean rows, hairline borders, checkmarks in accent blue
6. Ecosystem section: rounded tiles showing accessory/service lineup
7. Footer: 5-col links on #f5f5f7, language selector, legal links

==================================================================
ANTI-PATTERNS (what NOT to do -- these break theme authenticity)
==================================================================
  X No dark sections except for 'Apple TV+' style media sections
  X No gradient backgrounds in main content sections
  X No drop shadows on product images — let the photo breathe on white
  X No centered text except for hero overlays — left-align all body content
  X No more than 1 accent-colored element visible at a time
  X No busy backgrounds — white or #f5f5f7 only
  X No decorative illustrations — photography only
  X No font above 700 weight for regular body sections

==================================================================
🛡️ DESIGN FIDELITY GUARDRAILS
==================================================================
- MUST ADOPT & REUSE:
  * Hover image flip product card
  * Slide-over cart drawer
  * Sticky mobile buy bar
  * Announcement marquee bar
- DO NOT COPY (Proprietary / Brand Specific):
  * Proprietary Apple Store brand logos
  * Exact Apple Store copyrighted assets
  * Direct company trademarks
- TECHNICAL IMPLEMENTATION GUIDANCE:
  Development Guide: Use Tailwind grid system, slide-over drawer modals, and snappy hovers.

==================================================================
🛠️ STEP-BY-STEP REFACTORING INSTRUCTIONS
==================================================================
1. READ the user's current project files, identify domain, existing components, and tech stack.
2. INJECT the CSS custom properties above into the global stylesheet or Tailwind config.
3. RE-ARCHITECT each layout section to match the page architecture scaffold above.
4. RE-ENGINEER every UI component (nav, hero, cards, buttons, inputs, footer) into the Apple Store visual language while keeping the user's real content, data, and workflows intact.
5. APPLY motion physics (transitions, hover states, scroll reveals) as specified above.
6. WRITE all page copy in the Copy Voice defined above -- match the tone, not the brand name.
7. VERIFY: The output should feel unmistakably like Apple Store's design aesthetic applied to the user's own project domain.

==================================================================
📦 DELIVERABLE DEFINITION
==================================================================
Apply CSS variables globally. Every section should feel airy and editorial. Product photography is essential — use placeholder images that mimic the clean white-background product shot style.
```
