# THEME #011 --- Apple

- **Website URL:** [https://www.apple.com/](https://www.apple.com/)
- **Category:** SaaS / Product
- **Design Style:** High-Density Productivity Workspace
- **Mode:** light
- **Tags:** `saas-product`, `light`, `saas`

---

## 🧬 Theme DNA Summary
> **Apple design DNA: Large typography, generous whitespace, monochrome palette, subtle borders, restrained motion, asymmetric hero composition and strong product-focused visual hierarchy.**

---

## 🔑 Signature Visual Element
Giant SF Pro Display typography (80-96px) sitting directly over full-bleed product photography on pure white canvas. No decorative chrome — the product IS the hero. Blue pill CTAs (#0071e3) as the only color accent.

---

## 🎭 Emotional Intent
Holding a premium object. The visitor feels they are experiencing craft at the highest possible level. Simplicity communicates mastery. Every detail communicates 'we thought of everything so you don't have to.'

---

## 🎯 Design Principles ("Why does this look like this?")
Why Apple looks like this: Built to communicate speed, craft, and keyboard-first productivity by removing clutter and focusing on high contrast, micro-details, and crisp dark backgrounds.

---

## 🎨 Color System

### Primary Palette
- **`#ffffff`** --- Light Clean Canvas
- **`#0070f3`** --- Geist Blue Accent
- **`#111827`** --- Deep Charcoal Text

### Secondary & Surface Palette
- **`#151618`** --- Card Surface
- **`#222326`** --- Subtle Border
- **`#8a8f98`** --- Muted Secondary Text

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
- **Display Font:** `'SF Pro Display', -apple-system, BlinkMacSystemFont, 'Plus Jakarta Sans', sans-serif`
- **Body Font:** `'SF Pro Text', -apple-system, BlinkMacSystemFont, sans-serif`
- **Monospace Font:** `'SF Mono', 'JetBrains Mono', monospace`
- **Hierarchy & Scale:** Hero: 64-96px (-0.035em), H1: 44px, H2: 32px, Body: 17px, Caption: 13px
- **Weights:** 400 Regular, 500 Medium, 600 SemiBold, 700 Bold
- **Letter Spacing:** -0.03em display, -0.015em body

**Copy Voice:** Poetic product authority. Short, rhythm-driven headlines ('Thin. Light. Powerful beyond belief.'). Second-person ('Everything you need.'). No technical jargon in hero. Spec pages use precise technical language. CTAs: 'Shop iPhone', 'Learn more ↗', 'Compare models'.

---

## 📐 Spacing & Layout Structure
- **Grid System:** 12-column grid, max-width 1024px/1280px, 24px gutters
- **Padding Scale:** 4px, 8px, 16px, 24px, 48px, 96px, 140px
- **Whitespace Philosophy:** Museum-grade expansive negative space where product photography commands attention.

---

## 🧩 Component Language

### Buttons
Fully rounded pill buttons (`rounded-full`), solid royal blue (#0071e3) with white text, or clean text links with chevron.

### Cards
Large rounded bento tiles (24px-30px radius), subtle 1px border or soft drop shadow.

### Forms & Inputs
Rounded floating pill inputs with frosted glass backdrop blur.

### Navigation & Header
44px sticky frosted navbar (`backdrop-blur-xl bg-white/80 border-b border-black/5`), centered logo, clean minimal links.

### Hero Section
Cinematic full-bleed product hero with giant headline, elegant subtitle, and dual pill CTAs.

### Footer
Structured 5-column directory on off-white (#f5f5f7) with legal terms and language selector.

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
- **Transitions:** 200ms-300ms cubic-bezier(0.25, 0.1, 0.25, 1) smooth Apple physics
- **Scroll Behavior:** Smooth scroll scrubbing, sticky device frames with video playback synchronization.
- **Micro-Interactions:** Smooth 1.02x scale zoom on hover, buttery pill button color transitions.

---

## 📱 Responsive Strategy
- **Mobile:** Full-bleed cards, horizontal snap carousels, sticky bottom CTAs, centered logo header.
- **Desktop:** Expansive 1024px reading container, bento grid showcases, alternating feature rows.

---

## 🚀 Best Use Cases
- Developer tools
- Issue trackers
- Productivity suites
- High-craft B2B SaaS
- Command bar tools
- Apple-inspired applications
- SaaS / Product platforms

---

## ✅ Things To Reuse
  * 1px glowing border cards
  * Keyboard shortcut UI badges
  * Obsidian color system
  * Radial hero glow spotlight

---

## ❌ Things NOT To Copy
  * Proprietary Apple brand logos
  * Exact Apple copyrighted assets
  * Direct company trademarks

---

## 🛠️ Implementation Notes
Development Guide: Use Tailwind bg-[#08090a], border-white/10, hover:border-white/20, font-inter with -tracking-[0.02em] and lucide-react icons.

---

## 🤖 Deep Comprehensive AI Prompt
```text
[SYSTEM INSTRUCTION: SINGLE-SOURCE THEME DESIGN ADAPTER]
You are a Principal UI/UX Architect & Frontend Design System Engineer.
Your task is to analyze the user's current project / objective, and TRANSFORM / REDESIGN its entire frontend style, visual aesthetic, UX feeling, and component architecture strictly using the design system DNA of THEME #011 (Apple - https://www.apple.com/).

Maintain 100% strict theme isolation: extract and apply ONLY this reference theme's design language, tokens, and aesthetic principles.

==================================================================
🎯 CORE OBJECTIVE: ADAPT THEME TO USER'S PROJECT (NOT A BLIND CLONE)
==================================================================
1. ANALYZE CURRENT PROJECT & GOAL:
   - Carefully inspect the user's current project codebase, wireframes, or feature requirements (e.g. e-commerce clothing store selling shirts, SaaS tool, personal portfolio, marketplace, dashboard, etc.).
   - Preserve the user's core project purpose, domain data, functional workflows, and business logic.

2. TRANSLATE DESIGN DNA (DO NOT COPY PROPRIETARY CONTENT):
   - Do NOT blindly copy placeholder copy, trademarks, or unrelated product catalog from Apple (e.g., do not insert "Apple" branding or unrelated product listings).
   - DO extract and adopt 100% of Apple's visual craft, color palette, typography hierarchy, card structures, spacing rhythm, surface depth, micro-interactions, and UX feeling.

3. ELEVATE & RESKIN EVERY COMPONENT:
   - Reskin the user's existing components (navbars, heroes, product/feature cards, buttons, filters, inputs, modals, footers) into the authentic visual language of THEME #011.
   - Example: If the user's project is an apparel store selling shirts, design a high-craft shirt catalog with Apple's signature layouts, typography scale, lighting, and button styles.

==================================================================
🧬 THEME #011 IDENTITY & EMOTIONAL BRIEF
==================================================================
- Permanent Theme ID: THEME #011
- Reference Design Source: Apple (https://www.apple.com/)
- Mode: light
- Archetype / Category: SaaS / Product
- Design Style: High-Density Productivity Workspace
- Visual Personality: Apple signature design: high-density productivity workspace, engineered with high-craft aesthetics, structured hierarchy, and platform-native ergonomics.
- Core Design DNA: Apple design DNA: Large typography, generous whitespace, monochrome palette, subtle borders, restrained motion, asymmetric hero composition and strong product-focused visual hierarchy.

THE SIGNATURE VISUAL ELEMENT (What makes this theme unmistakably Apple):
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
- Display / Headline Font: 'SF Pro Display', -apple-system, BlinkMacSystemFont, 'Plus Jakarta Sans', sans-serif
- Body Copy Font: 'SF Pro Text', -apple-system, BlinkMacSystemFont, sans-serif
- Monospace / Data Font: 'SF Mono', 'JetBrains Mono', monospace
- Optical Tracking (Letter Spacing): -0.03em display, -0.015em body
- Scale & Proportions: Hero: 64-96px (-0.035em), H1: 44px, H2: 32px, Body: 17px, Caption: 13px
- Font Weights: 400 Regular, 500 Medium, 600 SemiBold, 700 Bold

Copy Voice & Tone (match this style in ALL generated text content):
Poetic product authority. Short, rhythm-driven headlines ('Thin. Light. Powerful beyond belief.'). Second-person ('Everything you need.'). No technical jargon in hero. Spec pages use precise technical language. CTAs: 'Shop iPhone', 'Learn more ↗', 'Compare models'.

==================================================================
📐 SPACING, GRID & GEOMETRY
==================================================================
- Container Max-Width & Grid: 12-column grid, max-width 1024px/1280px, 24px gutters
- Vertical Padding Scale: 4px, 8px, 16px, 24px, 48px, 96px, 140px
- Whitespace Philosophy: Museum-grade expansive negative space where product photography commands attention.

==================================================================
🧩 COMPONENT ARCHETYPE MAPPING
==================================================================
- Buttons (Primary, Secondary, Ghost): Fully rounded pill buttons (`rounded-full`), solid royal blue (#0071e3) with white text, or clean text links with chevron.
- Cards, Modules & Bento Grids: Large rounded bento tiles (24px-30px radius), subtle 1px border or soft drop shadow.
- Header & Navigation System: 44px sticky frosted navbar (`backdrop-blur-xl bg-white/80 border-b border-black/5`), centered logo, clean minimal links.
- Hero / Showcase Composition: Cinematic full-bleed product hero with giant headline, elegant subtitle, and dual pill CTAs.
- Forms, Filters & Pill Selectors: Rounded floating pill inputs with frosted glass backdrop blur.
- Footer & System Status: Structured 5-column directory on off-white (#f5f5f7) with legal terms and language selector.

Icon System: SF Symbols style rounded icons, 18px-24px
Image Treatment: Studio-lit hardware and product photography on pure white or off-white studio backdrops.

==================================================================
⚡ MOTION PHYSICS & MICRO-INTERACTIONS
==================================================================
- Transitions & Easing: 200ms-300ms cubic-bezier(0.25, 0.1, 0.25, 1) smooth Apple physics
  Apply as: transition: all 150ms cubic-bezier(0.16, 1, 0.3, 1) on all interactive elements
- Card Hover: transform: translateY(-2px) + box-shadow escalation
- Button Press: transform: scale(0.97), transition: 80ms ease-in
- Modal Entry: opacity 0 to 1 + translateY(8px to 0px), 200ms
- Scroll Reveals: IntersectionObserver threshold 0.1, staggered 60ms per sibling
- Scroll Behavior: Smooth scroll scrubbing, sticky device frames with video playback synchronization.
- Micro-Interactions: Smooth 1.02x scale zoom on hover, buttery pill button color transitions.

==================================================================
📱 RESPONSIVE ADAPTATION
==================================================================
- Mobile Layout Strategy: Full-bleed cards, horizontal snap carousels, sticky bottom CTAs, centered logo header.
- Desktop Ergonomics: Expansive 1024px reading container, bento grid showcases, alternating feature rows.

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
  * 1px glowing border cards
  * Keyboard shortcut UI badges
  * Obsidian color system
  * Radial hero glow spotlight
- DO NOT COPY (Proprietary / Brand Specific):
  * Proprietary Apple brand logos
  * Exact Apple copyrighted assets
  * Direct company trademarks
- TECHNICAL IMPLEMENTATION GUIDANCE:
  Development Guide: Use Tailwind bg-[#08090a], border-white/10, hover:border-white/20, font-inter with -tracking-[0.02em] and lucide-react icons.

==================================================================
🛠️ STEP-BY-STEP REFACTORING INSTRUCTIONS
==================================================================
1. READ the user's current project files, identify domain, existing components, and tech stack.
2. INJECT the CSS custom properties above into the global stylesheet or Tailwind config.
3. RE-ARCHITECT each layout section to match the page architecture scaffold above.
4. RE-ENGINEER every UI component (nav, hero, cards, buttons, inputs, footer) into the Apple visual language while keeping the user's real content, data, and workflows intact.
5. APPLY motion physics (transitions, hover states, scroll reveals) as specified above.
6. WRITE all page copy in the Copy Voice defined above -- match the tone, not the brand name.
7. VERIFY: The output should feel unmistakably like Apple's design aesthetic applied to the user's own project domain.

==================================================================
📦 DELIVERABLE DEFINITION
==================================================================
Apply CSS variables globally. Every section should feel airy and editorial. Product photography is essential — use placeholder images that mimic the clean white-background product shot style.
```
