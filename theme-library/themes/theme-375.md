# THEME #375 --- Rolex

- **Website URL:** [https://www.rolex.com/](https://www.rolex.com/)
- **Category:** Luxury / Fashion
- **Design Style:** Dark Opulent Luxury Maison
- **Mode:** dark
- **Tags:** `luxury-fashion`, `dark`, `luxury`, `ai`

---

## 🧬 Theme DNA Summary
> **Rolex design DNA: Exquisite serif typography, expansive ivory/obsidian whitespace, 3:4 lookbook imagery, and slow graceful transitions.**

---

## 🔑 Signature Visual Element
Deep dark canvas (#0c0c0c) with #d4af37 accent used exclusively on primary actions. Product screenshots or interface mockups as the primary visual element. High contrast between surface (#surface) and text creates the premium feel characteristic of Rolex.

---

## 🎭 Emotional Intent
Technical precision and professional authority. The user feels Rolex is built by people who understand their craft deeply. The dark aesthetic communicates focus, speed, and zero compromise on quality.

---

## 🎯 Design Principles ("Why does this look like this?")
Why Rolex looks like this: Engineered to evoke timeless elegance, craftsmanship, exclusivity, and quiet luxury.

---

## 🎨 Color System

### Primary Palette
- **`#0c0c0c`** --- Obsidian Silk
- **`#d4af37`** --- Muted Antique Gold
- **`#f5f5f5`** --- Pale White Text

### Secondary & Surface Palette
- **`#1c1c1f`** --- Showcase Surface
- **`#2c2c30`** --- Subtle Gold Hairline
- **`#9c9c9c`** --- Muted Caption

### CSS Custom Properties
```css
:root {
  --bg: #0c0c0c;
  --surface: #1c1c1f;
  --border: #2c2c30;
  --accent: #d4af37;
  --text-primary: #f5f5f5;
  --text-muted: #9c9c9c;
  --radius-sm: 4px;
  --radius-md: 8px;
  --radius-lg: 16px;
}
```

---

## 🔤 Typography System
- **Display Font:** `'Canela', 'Cinzel', 'Playfair Display', serif`
- **Body Font:** `'Italiana', 'Inter', -apple-system, sans-serif`
- **Monospace Font:** `'Courier New', monospace`
- **Hierarchy & Scale:** Hero: 64-100px (0.05em letter spacing), H1: 48px, H2: 32px, Body: 15px
- **Weights:** 300 Light, 400 Regular, 600 SemiBold
- **Letter Spacing:** 0.08em for uppercase display headings, 0.02em for body text

**Copy Voice:** Direct, technical authority. Short declarative headlines. Developer or professional-first language. Action CTAs: 'Get started', 'Try for free', 'Read docs'.

---

## 📐 Spacing & Layout Structure
- **Grid System:** 8-column or 12-column editorial grid, max-width 1440px, 32px gutters
- **Padding Scale:** 8px, 16px, 32px, 64px, 128px, 180px
- **Whitespace Philosophy:** Extravagant, atmospheric negative space communicating exclusivity and luxury.

---

## 🧩 Component Language

### Buttons
Square or subtly rounded (2px) button with gold/white hairline border, uppercase tracked text.

### Cards
Border-less photo-dominant cards with floating gold typography and subtle vignette.

### Forms & Inputs
Underline-only inputs with floating serif labels.

### Navigation & Header
Ultra-minimal transparent navbar with centered luxury monogram and tracked links.

### Hero Section
Full-bleed editorial campaign video/photography with slow vertical title reveal.

### Footer
Monochrome dark footer with boutique locator, newsletter sign-up, and heritage mark.

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
- No light/white background sections — maintain dark canvas throughout
- No heavy drop shadows — use hairline borders and surface elevation instead
- No busy gradient backgrounds — flat dark surfaces with selective glow accents only
- No decorative illustrations — use product screenshots or abstract geometric shapes
- No loose tracking on body text — keep optical letter-spacing tight
- No more than 2 accent-colored elements visible in the same viewport

---

## ⚡ Motion & Animation
- **Transitions:** 500ms-700ms cubic-bezier(0.19, 1, 0.22, 1) slow luxury ease
- **Scroll Behavior:** Parallax image reveals, slow zoom-in on hover, curtain-style page transitions.
- **Micro-Interactions:** Delicate underline expansion from center, golden shimmer border on hover.

---

## 📱 Responsive Strategy
- **Mobile:** Full-screen vertical swipe lookbooks, minimal hamburger menu, sticky inquiry pill.
- **Desktop:** Asymmetric editorial spreads, oversized imagery, mouse-follow cursor spotlight.

---

## 🚀 Best Use Cases
- Luxury fashion brands
- Fine jewelry & watches
- High-end real estate
- Hospitality & resorts
- Fragrance & beauty
- Rolex-inspired applications
- Luxury / Fashion platforms

---

## ✅ Things To Reuse
  * 3:4 aspect ratio lookbook cards
  * Slow fade & hover zoom
  * Spaced uppercase brand headers
  * Underline slider CTAs

---

## ❌ Things NOT To Copy
  * Proprietary Rolex brand logos
  * Exact Rolex copyrighted assets
  * Direct company trademarks

---

## 🛠️ Implementation Notes
Development Guide: Use font-serif, tracking-[0.2em], bg-[#faf7f2] or bg-[#0c0c0c], and slow transitions (duration-700).

---

## 🤖 Deep Comprehensive AI Prompt
```text
[SYSTEM INSTRUCTION: SINGLE-SOURCE THEME DESIGN ADAPTER]
You are a Principal UI/UX Architect & Frontend Design System Engineer.
Your task is to analyze the user's current project / objective, and TRANSFORM / REDESIGN its entire frontend style, visual aesthetic, UX feeling, and component architecture strictly using the design system DNA of THEME #375 (Rolex - https://www.rolex.com/).

Maintain 100% strict theme isolation: extract and apply ONLY this reference theme's design language, tokens, and aesthetic principles.

==================================================================
🎯 CORE OBJECTIVE: ADAPT THEME TO USER'S PROJECT (NOT A BLIND CLONE)
==================================================================
1. ANALYZE CURRENT PROJECT & GOAL:
   - Carefully inspect the user's current project codebase, wireframes, or feature requirements (e.g. e-commerce clothing store selling shirts, SaaS tool, personal portfolio, marketplace, dashboard, etc.).
   - Preserve the user's core project purpose, domain data, functional workflows, and business logic.

2. TRANSLATE DESIGN DNA (DO NOT COPY PROPRIETARY CONTENT):
   - Do NOT blindly copy placeholder copy, trademarks, or unrelated product catalog from Rolex (e.g., do not insert "Rolex" branding or unrelated product listings).
   - DO extract and adopt 100% of Rolex's visual craft, color palette, typography hierarchy, card structures, spacing rhythm, surface depth, micro-interactions, and UX feeling.

3. ELEVATE & RESKIN EVERY COMPONENT:
   - Reskin the user's existing components (navbars, heroes, product/feature cards, buttons, filters, inputs, modals, footers) into the authentic visual language of THEME #375.
   - Example: If the user's project is an apparel store selling shirts, design a high-craft shirt catalog with Rolex's signature layouts, typography scale, lighting, and button styles.

==================================================================
🧬 THEME #375 IDENTITY & EMOTIONAL BRIEF
==================================================================
- Permanent Theme ID: THEME #375
- Reference Design Source: Rolex (https://www.rolex.com/)
- Mode: dark
- Archetype / Category: Luxury / Fashion
- Design Style: Dark Opulent Luxury Maison
- Visual Personality: Rolex signature design: dark opulent luxury maison, engineered with high-craft aesthetics, structured hierarchy, and platform-native ergonomics.
- Core Design DNA: Rolex design DNA: Exquisite serif typography, expansive ivory/obsidian whitespace, 3:4 lookbook imagery, and slow graceful transitions.

THE SIGNATURE VISUAL ELEMENT (What makes this theme unmistakably Rolex):
Deep dark canvas (#0c0c0c) with #d4af37 accent used exclusively on primary actions. Product screenshots or interface mockups as the primary visual element. High contrast between surface (#surface) and text creates the premium feel characteristic of Rolex.

EMOTIONAL INTENT (How the user should FEEL when they see this design):
Technical precision and professional authority. The user feels Rolex is built by people who understand their craft deeply. The dark aesthetic communicates focus, speed, and zero compromise on quality.

==================================================================
🎨 COLOR SYSTEM & APPLICATION RULES
==================================================================
#0c0c0c  ->  page background, all section backgrounds
#d4af37  ->  primary CTA buttons, links on hover, focus rings, selected states, brand accents
#f5f5f5  ->  all headings (H1-H3), body text, primary UI labels
#1c1c1f  ->  card surfaces, modal backgrounds, input field backgrounds
#2c2c30  ->  borders, dividers, separator lines — 1px only
#9c9c9c  ->  secondary body text, metadata, timestamps, captions

CSS Custom Properties (paste into :root {}):
:root {
  --bg: #0c0c0c;
  --surface: #1c1c1f;
  --border: #2c2c30;
  --accent: #d4af37;
  --text-primary: #f5f5f5;
  --text-muted: #9c9c9c;
  --radius-sm: 4px;
  --radius-md: 8px;
  --radius-lg: 16px;
}

Tailwind Config Extension (add inside extend: {}):
colors: { bg: '#0c0c0c', surface: '#1c1c1f', accent: '#d4af37', primary: '#f5f5f5', muted: '#9c9c9c' }

==================================================================
🔤 TYPOGRAPHY & TEXT RHYTHM
==================================================================
- Display / Headline Font: 'Canela', 'Cinzel', 'Playfair Display', serif
- Body Copy Font: 'Italiana', 'Inter', -apple-system, sans-serif
- Monospace / Data Font: 'Courier New', monospace
- Optical Tracking (Letter Spacing): 0.08em for uppercase display headings, 0.02em for body text
- Scale & Proportions: Hero: 64-100px (0.05em letter spacing), H1: 48px, H2: 32px, Body: 15px
- Font Weights: 300 Light, 400 Regular, 600 SemiBold

Copy Voice & Tone (match this style in ALL generated text content):
Direct, technical authority. Short declarative headlines. Developer or professional-first language. Action CTAs: 'Get started', 'Try for free', 'Read docs'.

==================================================================
📐 SPACING, GRID & GEOMETRY
==================================================================
- Container Max-Width & Grid: 8-column or 12-column editorial grid, max-width 1440px, 32px gutters
- Vertical Padding Scale: 8px, 16px, 32px, 64px, 128px, 180px
- Whitespace Philosophy: Extravagant, atmospheric negative space communicating exclusivity and luxury.

==================================================================
🧩 COMPONENT ARCHETYPE MAPPING
==================================================================
- Buttons (Primary, Secondary, Ghost): Square or subtly rounded (2px) button with gold/white hairline border, uppercase tracked text.
- Cards, Modules & Bento Grids: Border-less photo-dominant cards with floating gold typography and subtle vignette.
- Header & Navigation System: Ultra-minimal transparent navbar with centered luxury monogram and tracked links.
- Hero / Showcase Composition: Full-bleed editorial campaign video/photography with slow vertical title reveal.
- Forms, Filters & Pill Selectors: Underline-only inputs with floating serif labels.
- Footer & System Status: Monochrome dark footer with boutique locator, newsletter sign-up, and heritage mark.

Icon System: Custom hairline icons, 1px stroke, gold/white
Image Treatment: High-fashion editorial photography, high-contrast monochrome and warm film grain.

==================================================================
⚡ MOTION PHYSICS & MICRO-INTERACTIONS
==================================================================
- Transitions & Easing: 500ms-700ms cubic-bezier(0.19, 1, 0.22, 1) slow luxury ease
  Apply as: transition: all 150ms cubic-bezier(0.16, 1, 0.3, 1) on all interactive elements
- Card Hover: transform: translateY(-2px) + box-shadow escalation
- Button Press: transform: scale(0.97), transition: 80ms ease-in
- Modal Entry: opacity 0 to 1 + translateY(8px to 0px), 200ms
- Scroll Reveals: IntersectionObserver threshold 0.1, staggered 60ms per sibling
- Scroll Behavior: Parallax image reveals, slow zoom-in on hover, curtain-style page transitions.
- Micro-Interactions: Delicate underline expansion from center, golden shimmer border on hover.

==================================================================
📱 RESPONSIVE ADAPTATION
==================================================================
- Mobile Layout Strategy: Full-screen vertical swipe lookbooks, minimal hamburger menu, sticky inquiry pill.
- Desktop Ergonomics: Asymmetric editorial spreads, oversized imagery, mouse-follow cursor spotlight.

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
  * 3:4 aspect ratio lookbook cards
  * Slow fade & hover zoom
  * Spaced uppercase brand headers
  * Underline slider CTAs
- DO NOT COPY (Proprietary / Brand Specific):
  * Proprietary Rolex brand logos
  * Exact Rolex copyrighted assets
  * Direct company trademarks
- TECHNICAL IMPLEMENTATION GUIDANCE:
  Development Guide: Use font-serif, tracking-[0.2em], bg-[#faf7f2] or bg-[#0c0c0c], and slow transitions (duration-700).

==================================================================
🛠️ STEP-BY-STEP REFACTORING INSTRUCTIONS
==================================================================
1. READ the user's current project files, identify domain, existing components, and tech stack.
2. INJECT the CSS custom properties above into the global stylesheet or Tailwind config.
3. RE-ARCHITECT each layout section to match the page architecture scaffold above.
4. RE-ENGINEER every UI component (nav, hero, cards, buttons, inputs, footer) into the Rolex visual language while keeping the user's real content, data, and workflows intact.
5. APPLY motion physics (transitions, hover states, scroll reveals) as specified above.
6. WRITE all page copy in the Copy Voice defined above -- match the tone, not the brand name.
7. VERIFY: The output should feel unmistakably like Rolex's design aesthetic applied to the user's own project domain.

==================================================================
📦 DELIVERABLE DEFINITION
==================================================================
Apply CSS custom properties globally first. Then rework each component to match theme tokens. Preserve all domain data and business logic — only the visual layer changes.
```
