# THEME #081 --- Luma

- **Website URL:** [https://lumalabs.ai/](https://lumalabs.ai/)
- **Category:** AI
- **Design Style:** Dark Cosmic AI Interface
- **Mode:** dark
- **Tags:** `ai`, `dark`

---

## 🧬 Theme DNA Summary
> **Luma design DNA: Dark void canvas, iridescent neon glow accents, prompt-first conversational UI, and live generative canvas modules.**

---

## 🔑 Signature Visual Element
Deep dark canvas (#121113) with #f59e0b accent used exclusively on primary actions. Product screenshots or interface mockups as the primary visual element. High contrast between surface (#surface) and text creates the premium feel characteristic of Luma.

---

## 🎭 Emotional Intent
Technical precision and professional authority. The user feels Luma is built by people who understand their craft deeply. The dark aesthetic communicates focus, speed, and zero compromise on quality.

---

## 🎯 Design Principles ("Why does this look like this?")
Why Luma looks like this: Engineered to evoke machine intelligence, boundless creativity, and real-time generative wonder.

---

## 🎨 Color System

### Primary Palette
- **`#121113`** --- Charcoal Canvas
- **`#f59e0b`** --- Warm Amber Intelligence
- **`#fafafa`** --- Text

### Secondary & Surface Palette
- **`#121216`** --- Container Surface
- **`#27272a`** --- Luminescent Border
- **`#a1a1aa`** --- Subtext

### CSS Custom Properties
```css
:root {
  --bg: #121113;
  --surface: #121216;
  --border: #27272a;
  --accent: #f59e0b;
  --text-primary: #fafafa;
  --text-muted: #a1a1aa;
  --radius-sm: 4px;
  --radius-md: 8px;
  --radius-lg: 16px;
}
```

---

## 🔤 Typography System
- **Display Font:** `'Plus Jakarta Sans', 'Inter', sans-serif`
- **Body Font:** `'Inter', sans-serif`
- **Monospace Font:** `'JetBrains Mono', monospace`
- **Hierarchy & Scale:** Hero: 56-80px (-0.03em), H1: 40px, H2: 28px, Body: 15px, Prompt: 14px
- **Weights:** 400 Regular, 500 Medium, 600 SemiBold, 700 Bold
- **Letter Spacing:** -0.03em for headlines, -0.01em for body

**Copy Voice:** Direct, technical authority. Short declarative headlines. Developer or professional-first language. Action CTAs: 'Get started', 'Try for free', 'Read docs'.

---

## 📐 Spacing & Layout Structure
- **Grid System:** 12-column grid, max-width 1240px, 24px gutters
- **Padding Scale:** 4px, 8px, 16px, 24px, 48px, 96px
- **Whitespace Philosophy:** Atmospheric cosmic dark canvas with glowing radial neon spotlights.

---

## 🧩 Component Language

### Buttons
Pill buttons with iridescent gradient border or glowing primary accent.

### Cards
Dark translucent glass cards (`backdrop-blur-lg bg-white/5 border border-white/10`).

### Forms & Inputs
Multi-line AI prompt bar with token counter, model selector, and run button.

### Navigation & Header
Frosted glass floating header with model status and token usage meter.

### Hero Section
Glowing neural orb visual, prompt-first interaction bar, generated art showcase.

### Footer
Dark 4-column footer with API status, documentation links, and Discord community badge.

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
- **Transitions:** 200ms cubic-bezier(0.16, 1, 0.3, 1)
- **Scroll Behavior:** Glowing orb background pulse, particle mesh floating on scroll.
- **Micro-Interactions:** Multicolor border shimmer, prompt input focus neon glow.

---

## 📱 Responsive Strategy
- **Mobile:** Bottom-docked prompt input, single-column generation feed, touch pinch-to-zoom.
- **Desktop:** Split canvas with prompt parameters on left, generation canvas on right.

---

## 🚀 Best Use Cases
- Generative AI tools
- LLM chat interfaces
- AI image/audio studios
- Model playgrounds
- Luma-inspired applications
- AI platforms

---

## ✅ Things To Reuse
  * Omni-prompt bar design
  * Neon gradient glow borders
  * Token streaming text animation
  * Model status pill

---

## ❌ Things NOT To Copy
  * Proprietary Luma brand logos
  * Exact Luma copyrighted assets
  * Direct company trademarks

---

## 🛠️ Implementation Notes
Development Guide: Use Tailwind bg-black, radial gradient glows (blur-3xl bg-purple-500/10), and glassmorphism.

---

## 🤖 Deep Comprehensive AI Prompt
```text
[SYSTEM INSTRUCTION: SINGLE-SOURCE THEME DESIGN ADAPTER]
You are a Principal UI/UX Architect & Frontend Design System Engineer.
Your task is to analyze the user's current project / objective, and TRANSFORM / REDESIGN its entire frontend style, visual aesthetic, UX feeling, and component architecture strictly using the design system DNA of THEME #081 (Luma - https://lumalabs.ai/).

Maintain 100% strict theme isolation: extract and apply ONLY this reference theme's design language, tokens, and aesthetic principles.

==================================================================
🎯 CORE OBJECTIVE: ADAPT THEME TO USER'S PROJECT (NOT A BLIND CLONE)
==================================================================
1. ANALYZE CURRENT PROJECT & GOAL:
   - Carefully inspect the user's current project codebase, wireframes, or feature requirements (e.g. e-commerce clothing store selling shirts, SaaS tool, personal portfolio, marketplace, dashboard, etc.).
   - Preserve the user's core project purpose, domain data, functional workflows, and business logic.

2. TRANSLATE DESIGN DNA (DO NOT COPY PROPRIETARY CONTENT):
   - Do NOT blindly copy placeholder copy, trademarks, or unrelated product catalog from Luma (e.g., do not insert "Luma" branding or unrelated product listings).
   - DO extract and adopt 100% of Luma's visual craft, color palette, typography hierarchy, card structures, spacing rhythm, surface depth, micro-interactions, and UX feeling.

3. ELEVATE & RESKIN EVERY COMPONENT:
   - Reskin the user's existing components (navbars, heroes, product/feature cards, buttons, filters, inputs, modals, footers) into the authentic visual language of THEME #081.
   - Example: If the user's project is an apparel store selling shirts, design a high-craft shirt catalog with Luma's signature layouts, typography scale, lighting, and button styles.

==================================================================
🧬 THEME #081 IDENTITY & EMOTIONAL BRIEF
==================================================================
- Permanent Theme ID: THEME #081
- Reference Design Source: Luma (https://lumalabs.ai/)
- Mode: dark
- Archetype / Category: AI
- Design Style: Dark Cosmic AI Interface
- Visual Personality: Luma signature design: dark cosmic ai interface, engineered with high-craft aesthetics, structured hierarchy, and platform-native ergonomics.
- Core Design DNA: Luma design DNA: Dark void canvas, iridescent neon glow accents, prompt-first conversational UI, and live generative canvas modules.

THE SIGNATURE VISUAL ELEMENT (What makes this theme unmistakably Luma):
Deep dark canvas (#121113) with #f59e0b accent used exclusively on primary actions. Product screenshots or interface mockups as the primary visual element. High contrast between surface (#surface) and text creates the premium feel characteristic of Luma.

EMOTIONAL INTENT (How the user should FEEL when they see this design):
Technical precision and professional authority. The user feels Luma is built by people who understand their craft deeply. The dark aesthetic communicates focus, speed, and zero compromise on quality.

==================================================================
🎨 COLOR SYSTEM & APPLICATION RULES
==================================================================
#121113  ->  page background, all section backgrounds
#f59e0b  ->  primary CTA buttons, links on hover, focus rings, selected states, brand accents
#fafafa  ->  all headings (H1-H3), body text, primary UI labels
#121216  ->  card surfaces, modal backgrounds, input field backgrounds
#27272a  ->  borders, dividers, separator lines — 1px only
#a1a1aa  ->  secondary body text, metadata, timestamps, captions

CSS Custom Properties (paste into :root {}):
:root {
  --bg: #121113;
  --surface: #121216;
  --border: #27272a;
  --accent: #f59e0b;
  --text-primary: #fafafa;
  --text-muted: #a1a1aa;
  --radius-sm: 4px;
  --radius-md: 8px;
  --radius-lg: 16px;
}

Tailwind Config Extension (add inside extend: {}):
colors: { bg: '#121113', surface: '#121216', accent: '#f59e0b', primary: '#fafafa', muted: '#a1a1aa' }

==================================================================
🔤 TYPOGRAPHY & TEXT RHYTHM
==================================================================
- Display / Headline Font: 'Plus Jakarta Sans', 'Inter', sans-serif
- Body Copy Font: 'Inter', sans-serif
- Monospace / Data Font: 'JetBrains Mono', monospace
- Optical Tracking (Letter Spacing): -0.03em for headlines, -0.01em for body
- Scale & Proportions: Hero: 56-80px (-0.03em), H1: 40px, H2: 28px, Body: 15px, Prompt: 14px
- Font Weights: 400 Regular, 500 Medium, 600 SemiBold, 700 Bold

Copy Voice & Tone (match this style in ALL generated text content):
Direct, technical authority. Short declarative headlines. Developer or professional-first language. Action CTAs: 'Get started', 'Try for free', 'Read docs'.

==================================================================
📐 SPACING, GRID & GEOMETRY
==================================================================
- Container Max-Width & Grid: 12-column grid, max-width 1240px, 24px gutters
- Vertical Padding Scale: 4px, 8px, 16px, 24px, 48px, 96px
- Whitespace Philosophy: Atmospheric cosmic dark canvas with glowing radial neon spotlights.

==================================================================
🧩 COMPONENT ARCHETYPE MAPPING
==================================================================
- Buttons (Primary, Secondary, Ghost): Pill buttons with iridescent gradient border or glowing primary accent.
- Cards, Modules & Bento Grids: Dark translucent glass cards (`backdrop-blur-lg bg-white/5 border border-white/10`).
- Header & Navigation System: Frosted glass floating header with model status and token usage meter.
- Hero / Showcase Composition: Glowing neural orb visual, prompt-first interaction bar, generated art showcase.
- Forms, Filters & Pill Selectors: Multi-line AI prompt bar with token counter, model selector, and run button.
- Footer & System Status: Dark 4-column footer with API status, documentation links, and Discord community badge.

Icon System: Lucide Icons, 1.5px stroke, colored neon accents
Image Treatment: High-fidelity AI generated imagery, diffusion model outputs, neural mesh shaders.

==================================================================
⚡ MOTION PHYSICS & MICRO-INTERACTIONS
==================================================================
- Transitions & Easing: 200ms cubic-bezier(0.16, 1, 0.3, 1)
  Apply as: transition: all 150ms cubic-bezier(0.16, 1, 0.3, 1) on all interactive elements
- Card Hover: transform: translateY(-2px) + box-shadow escalation
- Button Press: transform: scale(0.97), transition: 80ms ease-in
- Modal Entry: opacity 0 to 1 + translateY(8px to 0px), 200ms
- Scroll Reveals: IntersectionObserver threshold 0.1, staggered 60ms per sibling
- Scroll Behavior: Glowing orb background pulse, particle mesh floating on scroll.
- Micro-Interactions: Multicolor border shimmer, prompt input focus neon glow.

==================================================================
📱 RESPONSIVE ADAPTATION
==================================================================
- Mobile Layout Strategy: Bottom-docked prompt input, single-column generation feed, touch pinch-to-zoom.
- Desktop Ergonomics: Split canvas with prompt parameters on left, generation canvas on right.

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
  * Omni-prompt bar design
  * Neon gradient glow borders
  * Token streaming text animation
  * Model status pill
- DO NOT COPY (Proprietary / Brand Specific):
  * Proprietary Luma brand logos
  * Exact Luma copyrighted assets
  * Direct company trademarks
- TECHNICAL IMPLEMENTATION GUIDANCE:
  Development Guide: Use Tailwind bg-black, radial gradient glows (blur-3xl bg-purple-500/10), and glassmorphism.

==================================================================
🛠️ STEP-BY-STEP REFACTORING INSTRUCTIONS
==================================================================
1. READ the user's current project files, identify domain, existing components, and tech stack.
2. INJECT the CSS custom properties above into the global stylesheet or Tailwind config.
3. RE-ARCHITECT each layout section to match the page architecture scaffold above.
4. RE-ENGINEER every UI component (nav, hero, cards, buttons, inputs, footer) into the Luma visual language while keeping the user's real content, data, and workflows intact.
5. APPLY motion physics (transitions, hover states, scroll reveals) as specified above.
6. WRITE all page copy in the Copy Voice defined above -- match the tone, not the brand name.
7. VERIFY: The output should feel unmistakably like Luma's design aesthetic applied to the user's own project domain.

==================================================================
📦 DELIVERABLE DEFINITION
==================================================================
Apply CSS custom properties globally first. Then rework each component to match theme tokens. Preserve all domain data and business logic — only the visual layer changes.
```
