# THEME #129 --- WorkOS

- **Website URL:** [https://workos.com/](https://workos.com/)
- **Category:** Developer / Infrastructure
- **Design Style:** Monospace Minimalist CLI Hub
- **Mode:** dark
- **Tags:** `developer-infrastructure`, `dark`, `minimal`, `developer`

---

## 🧬 Theme DNA Summary
> **WorkOS design DNA: Terminal windows, syntax highlighting, monospace metadata, hairline borders, and live developer CLI workflows.**

---

## 🔑 Signature Visual Element
Deep dark canvas (#0b0f19) with #22c55e accent used exclusively on primary actions. Product screenshots or interface mockups as the primary visual element. High contrast between surface (#surface) and text creates the premium feel characteristic of WorkOS.

---

## 🎭 Emotional Intent
Technical precision and professional authority. The user feels WorkOS is built by people who understand their craft deeply. The dark aesthetic communicates focus, speed, and zero compromise on quality.

---

## 🎯 Design Principles ("Why does this look like this?")
Why WorkOS looks like this: Built for instant technical comprehension, zero latency, and engineering credibility.

---

## 🎨 Color System

### Primary Palette
- **`#0b0f19`** --- Deep Console Dark
- **`#22c55e`** --- Terminal Green Accent
- **`#e2e8f0`** --- Primary Text

### Secondary & Surface Palette
- **`#111827`** --- Terminal Block Surface
- **`#1f2937`** --- Code Border
- **`#94a3b8`** --- Comment Muted Text

### CSS Custom Properties
```css
:root {
  --bg: #0b0f19;
  --surface: #111827;
  --border: #1f2937;
  --accent: #22c55e;
  --text-primary: #e2e8f0;
  --text-muted: #94a3b8;
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

**Copy Voice:** Direct, technical authority. Short declarative headlines. Developer or professional-first language. Action CTAs: 'Get started', 'Try for free', 'Read docs'.

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
- **Transitions:** 180ms ease-out
- **Scroll Behavior:** Staggered reveal on scroll, smooth parallax card depth.
- **Micro-Interactions:** Subtle card translateY(-2px), smooth button active scale down.

---

## 📱 Responsive Strategy
- **Mobile:** Bottom sheet drawers, collapsible sidebars, single column stacked cards.
- **Desktop:** Multi-pane grid layout, 1240px max-width container.

---

## 🚀 Best Use Cases
- Cloud infrastructure
- Databases
- APIs & SDKs
- Developer platforms
- CI/CD tools
- WorkOS-inspired applications
- Developer / Infrastructure platforms

---

## ✅ Things To Reuse
  * Terminal snippet cards
  * Interactive API parameter builder
  * Status uptime badge
  * 3-column docs layout

---

## ❌ Things NOT To Copy
  * Proprietary WorkOS brand logos
  * Exact WorkOS copyrighted assets
  * Direct company trademarks

---

## 🛠️ Implementation Notes
Development Guide: Use Prism/Shiki syntax styling, font-mono, bg-slate-950, and border-slate-800.

---

## 🤖 Deep Comprehensive AI Prompt
```text
[SYSTEM INSTRUCTION: SINGLE-SOURCE THEME DESIGN ADAPTER]
You are a Principal UI/UX Architect & Frontend Design System Engineer.
Your task is to analyze the user's current project / objective, and TRANSFORM / REDESIGN its entire frontend style, visual aesthetic, UX feeling, and component architecture strictly using the design system DNA of THEME #129 (WorkOS - https://workos.com/).

Maintain 100% strict theme isolation: extract and apply ONLY this reference theme's design language, tokens, and aesthetic principles.

==================================================================
🎯 CORE OBJECTIVE: ADAPT THEME TO USER'S PROJECT (NOT A BLIND CLONE)
==================================================================
1. ANALYZE CURRENT PROJECT & GOAL:
   - Carefully inspect the user's current project codebase, wireframes, or feature requirements (e.g. e-commerce clothing store selling shirts, SaaS tool, personal portfolio, marketplace, dashboard, etc.).
   - Preserve the user's core project purpose, domain data, functional workflows, and business logic.

2. TRANSLATE DESIGN DNA (DO NOT COPY PROPRIETARY CONTENT):
   - Do NOT blindly copy placeholder copy, trademarks, or unrelated product catalog from WorkOS (e.g., do not insert "WorkOS" branding or unrelated product listings).
   - DO extract and adopt 100% of WorkOS's visual craft, color palette, typography hierarchy, card structures, spacing rhythm, surface depth, micro-interactions, and UX feeling.

3. ELEVATE & RESKIN EVERY COMPONENT:
   - Reskin the user's existing components (navbars, heroes, product/feature cards, buttons, filters, inputs, modals, footers) into the authentic visual language of THEME #129.
   - Example: If the user's project is an apparel store selling shirts, design a high-craft shirt catalog with WorkOS's signature layouts, typography scale, lighting, and button styles.

==================================================================
🧬 THEME #129 IDENTITY & EMOTIONAL BRIEF
==================================================================
- Permanent Theme ID: THEME #129
- Reference Design Source: WorkOS (https://workos.com/)
- Mode: dark
- Archetype / Category: Developer / Infrastructure
- Design Style: Monospace Minimalist CLI Hub
- Visual Personality: WorkOS signature design: monospace minimalist cli hub, engineered with high-craft aesthetics, structured hierarchy, and platform-native ergonomics.
- Core Design DNA: WorkOS design DNA: Terminal windows, syntax highlighting, monospace metadata, hairline borders, and live developer CLI workflows.

THE SIGNATURE VISUAL ELEMENT (What makes this theme unmistakably WorkOS):
Deep dark canvas (#0b0f19) with #22c55e accent used exclusively on primary actions. Product screenshots or interface mockups as the primary visual element. High contrast between surface (#surface) and text creates the premium feel characteristic of WorkOS.

EMOTIONAL INTENT (How the user should FEEL when they see this design):
Technical precision and professional authority. The user feels WorkOS is built by people who understand their craft deeply. The dark aesthetic communicates focus, speed, and zero compromise on quality.

==================================================================
🎨 COLOR SYSTEM & APPLICATION RULES
==================================================================
#0b0f19  ->  page background, all section backgrounds
#22c55e  ->  primary CTA buttons, links on hover, focus rings, selected states, brand accents
#e2e8f0  ->  all headings (H1-H3), body text, primary UI labels
#111827  ->  card surfaces, modal backgrounds, input field backgrounds
#1f2937  ->  borders, dividers, separator lines — 1px only
#94a3b8  ->  secondary body text, metadata, timestamps, captions

CSS Custom Properties (paste into :root {}):
:root {
  --bg: #0b0f19;
  --surface: #111827;
  --border: #1f2937;
  --accent: #22c55e;
  --text-primary: #e2e8f0;
  --text-muted: #94a3b8;
  --radius-sm: 4px;
  --radius-md: 8px;
  --radius-lg: 16px;
}

Tailwind Config Extension (add inside extend: {}):
colors: { bg: '#0b0f19', surface: '#111827', accent: '#22c55e', primary: '#e2e8f0', muted: '#94a3b8' }

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
Direct, technical authority. Short declarative headlines. Developer or professional-first language. Action CTAs: 'Get started', 'Try for free', 'Read docs'.

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
  * Terminal snippet cards
  * Interactive API parameter builder
  * Status uptime badge
  * 3-column docs layout
- DO NOT COPY (Proprietary / Brand Specific):
  * Proprietary WorkOS brand logos
  * Exact WorkOS copyrighted assets
  * Direct company trademarks
- TECHNICAL IMPLEMENTATION GUIDANCE:
  Development Guide: Use Prism/Shiki syntax styling, font-mono, bg-slate-950, and border-slate-800.

==================================================================
🛠️ STEP-BY-STEP REFACTORING INSTRUCTIONS
==================================================================
1. READ the user's current project files, identify domain, existing components, and tech stack.
2. INJECT the CSS custom properties above into the global stylesheet or Tailwind config.
3. RE-ARCHITECT each layout section to match the page architecture scaffold above.
4. RE-ENGINEER every UI component (nav, hero, cards, buttons, inputs, footer) into the WorkOS visual language while keeping the user's real content, data, and workflows intact.
5. APPLY motion physics (transitions, hover states, scroll reveals) as specified above.
6. WRITE all page copy in the Copy Voice defined above -- match the tone, not the brand name.
7. VERIFY: The output should feel unmistakably like WorkOS's design aesthetic applied to the user's own project domain.

==================================================================
📦 DELIVERABLE DEFINITION
==================================================================
Apply CSS custom properties globally first. Then rework each component to match theme tokens. Preserve all domain data and business logic — only the visual layer changes.
```
