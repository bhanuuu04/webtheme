# THEME #212 --- Stripe Atlas

- **Website URL:** [https://stripe.com/atlas](https://stripe.com/atlas)
- **Category:** Fintech / Finance
- **Design Style:** Sleek Wealth Management
- **Mode:** light
- **Tags:** `fintech-finance`, `light`, `fintech`

---

## 🧬 Theme DNA Summary
> **Stripe Atlas design DNA: High-trust typography, dynamic financial metric counters, virtual debit card mockups, and regulatory rigor.**

---

## 🔑 Signature Visual Element
Animated gradient mesh background (purple-to-cyan-to-teal) behind the hero. Tilted 3D card stack with drop shadows showing the product. Gradient text on key headlines (#635bff to #00d4ff). Light white canvas for content sections.

---

## 🎭 Emotional Intent
Enterprise-grade financial infrastructure, but approachable and modern. The visitor feels Stripe is both trusted by Fortune 500s and easy for a solo developer. Premium, but not intimidating.

---

## 🎯 Design Principles ("Why does this look like this?")
Why Stripe Atlas looks like this: Engineered to project absolute security, frictionless capital flow, and financial empowerment.

---

## 🎨 Color System

### Primary Palette
- **`#f8fafc`** --- Crisp White Capital
- **`#0284c7`** --- Trust Cobalt Accent
- **`#0f172a`** --- Deep Slate Text

### Secondary & Surface Palette
- **`#112240`** --- Ledger Surface
- **`#233554`** --- Security Border
- **`#8892b0`** --- Financial Secondary Text

### CSS Custom Properties
```css
:root {
  --bg: #ffffff;
  --surface: #f6f9fc;
  --border: #e0e6eb;
  --accent: #635bff;
  --text-primary: #0a2540;
  --text-body: #425466;
  --gradient-start: #635bff;
  --gradient-end: #00d4ff;
  --radius-md: 8px;
  --radius-lg: 12px;
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

**Copy Voice:** Confident financial authority meets developer warmth. 'Payments infrastructure for the internet.' Clear value statements. Technical precision in feature copy. CTAs: 'Start now', 'Contact sales', 'Explore docs'. Never use 'revolutionary'.

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
1. Nav: white bg, logo left, product dropdown links, 'Contact sales' + 'Start now' right
2. Hero: gradient mesh bg, H1 with gradient text, subtitle, 2 CTAs, tilted 3D product card stack
3. Trust logos: 'Join millions of companies including...' with colored brand logos
4. Product feature: white section, icon + headline, alternating 2-col layout
5. Code example: dark terminal block with syntax highlighting, white explanation text beside
6. Metrics: 3 large stats on light background
7. Testimonials: card grid on soft gray background
8. Pricing section: 3-tier table, purple-outlined featured tier
9. Footer: dark (#0a2540) 5-col link grid

---

## 🚫 Anti-Patterns (What NOT to do)
- No dark canvas for main sections — keep body on white/near-white
- No flat gradient — always animated or multi-stop gradient mesh
- No dense technical tables without the Stripe card styling
- No generic rounded cards — Stripe cards have specific shadow depth system
- Do not use the gradient on body text — only on display headlines
- No monochrome logo strip — Stripe shows colored brand logos

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
- Banking apps
- Payment processors
- Crypto wallets
- Investment platforms
- Accounting SaaS
- Stripe Atlas-inspired applications
- Fintech / Finance platforms

---

## ✅ Things To Reuse
  * Live financial metric ticker
  * Virtual card 3D tilt
  * Tabular numeric alignment
  * Security trust badges

---

## ❌ Things NOT To Copy
  * Proprietary Stripe Atlas brand logos
  * Exact Stripe Atlas copyrighted assets
  * Direct company trademarks

---

## 🛠️ Implementation Notes
Development Guide: Use tabular numeric font features (font-feature-settings: 'tnum'), vibrant green accents (#00e599), and subtle glass cards.

---

## 🤖 Deep Comprehensive AI Prompt
```text
[SYSTEM INSTRUCTION: SINGLE-SOURCE THEME DESIGN ADAPTER]
You are a Principal UI/UX Architect & Frontend Design System Engineer.
Your task is to analyze the user's current project / objective, and TRANSFORM / REDESIGN its entire frontend style, visual aesthetic, UX feeling, and component architecture strictly using the design system DNA of THEME #212 (Stripe Atlas - https://stripe.com/atlas).

Maintain 100% strict theme isolation: extract and apply ONLY this reference theme's design language, tokens, and aesthetic principles.

==================================================================
🎯 CORE OBJECTIVE: ADAPT THEME TO USER'S PROJECT (NOT A BLIND CLONE)
==================================================================
1. ANALYZE CURRENT PROJECT & GOAL:
   - Carefully inspect the user's current project codebase, wireframes, or feature requirements (e.g. e-commerce clothing store selling shirts, SaaS tool, personal portfolio, marketplace, dashboard, etc.).
   - Preserve the user's core project purpose, domain data, functional workflows, and business logic.

2. TRANSLATE DESIGN DNA (DO NOT COPY PROPRIETARY CONTENT):
   - Do NOT blindly copy placeholder copy, trademarks, or unrelated product catalog from Stripe Atlas (e.g., do not insert "Stripe Atlas" branding or unrelated product listings).
   - DO extract and adopt 100% of Stripe Atlas's visual craft, color palette, typography hierarchy, card structures, spacing rhythm, surface depth, micro-interactions, and UX feeling.

3. ELEVATE & RESKIN EVERY COMPONENT:
   - Reskin the user's existing components (navbars, heroes, product/feature cards, buttons, filters, inputs, modals, footers) into the authentic visual language of THEME #212.
   - Example: If the user's project is an apparel store selling shirts, design a high-craft shirt catalog with Stripe Atlas's signature layouts, typography scale, lighting, and button styles.

==================================================================
🧬 THEME #212 IDENTITY & EMOTIONAL BRIEF
==================================================================
- Permanent Theme ID: THEME #212
- Reference Design Source: Stripe Atlas (https://stripe.com/atlas)
- Mode: light
- Archetype / Category: Fintech / Finance
- Design Style: Sleek Wealth Management
- Visual Personality: Stripe Atlas signature design: sleek wealth management, engineered with high-craft aesthetics, structured hierarchy, and platform-native ergonomics.
- Core Design DNA: Stripe Atlas design DNA: High-trust typography, dynamic financial metric counters, virtual debit card mockups, and regulatory rigor.

THE SIGNATURE VISUAL ELEMENT (What makes this theme unmistakably Stripe Atlas):
Animated gradient mesh background (purple-to-cyan-to-teal) behind the hero. Tilted 3D card stack with drop shadows showing the product. Gradient text on key headlines (#635bff to #00d4ff). Light white canvas for content sections.

EMOTIONAL INTENT (How the user should FEEL when they see this design):
Enterprise-grade financial infrastructure, but approachable and modern. The visitor feels Stripe is both trusted by Fortune 500s and easy for a solo developer. Premium, but not intimidating.

==================================================================
🎨 COLOR SYSTEM & APPLICATION RULES
==================================================================
#635bff  ->  primary CTA buttons (solid), links, active states, gradient text start
#0a2540  ->  dark text, hero headings, footer background
#ffffff  ->  page canvas, card surfaces, nav background
#f6f9fc  ->  section alternate backgrounds, input fields
#425466  ->  body text, descriptions, secondary content
#00d4ff  ->  gradient accent end, hover glow effects

CSS Custom Properties (paste into :root {}):
:root {
  --bg: #ffffff;
  --surface: #f6f9fc;
  --border: #e0e6eb;
  --accent: #635bff;
  --text-primary: #0a2540;
  --text-body: #425466;
  --gradient-start: #635bff;
  --gradient-end: #00d4ff;
  --radius-md: 8px;
  --radius-lg: 12px;
}

Tailwind Config Extension (add inside extend: {}):
colors: { bg: '#ffffff', surface: '#f6f9fc', accent: '#635bff', primary: '#0a2540', body: '#425466' }

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
Confident financial authority meets developer warmth. 'Payments infrastructure for the internet.' Clear value statements. Technical precision in feature copy. CTAs: 'Start now', 'Contact sales', 'Explore docs'. Never use 'revolutionary'.

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
1. Nav: white bg, logo left, product dropdown links, 'Contact sales' + 'Start now' right
2. Hero: gradient mesh bg, H1 with gradient text, subtitle, 2 CTAs, tilted 3D product card stack
3. Trust logos: 'Join millions of companies including...' with colored brand logos
4. Product feature: white section, icon + headline, alternating 2-col layout
5. Code example: dark terminal block with syntax highlighting, white explanation text beside
6. Metrics: 3 large stats on light background
7. Testimonials: card grid on soft gray background
8. Pricing section: 3-tier table, purple-outlined featured tier
9. Footer: dark (#0a2540) 5-col link grid

==================================================================
ANTI-PATTERNS (what NOT to do -- these break theme authenticity)
==================================================================
  X No dark canvas for main sections — keep body on white/near-white
  X No flat gradient — always animated or multi-stop gradient mesh
  X No dense technical tables without the Stripe card styling
  X No generic rounded cards — Stripe cards have specific shadow depth system
  X Do not use the gradient on body text — only on display headlines
  X No monochrome logo strip — Stripe shows colored brand logos

==================================================================
🛡️ DESIGN FIDELITY GUARDRAILS
==================================================================
- MUST ADOPT & REUSE:
  * Live financial metric ticker
  * Virtual card 3D tilt
  * Tabular numeric alignment
  * Security trust badges
- DO NOT COPY (Proprietary / Brand Specific):
  * Proprietary Stripe Atlas brand logos
  * Exact Stripe Atlas copyrighted assets
  * Direct company trademarks
- TECHNICAL IMPLEMENTATION GUIDANCE:
  Development Guide: Use tabular numeric font features (font-feature-settings: 'tnum'), vibrant green accents (#00e599), and subtle glass cards.

==================================================================
🛠️ STEP-BY-STEP REFACTORING INSTRUCTIONS
==================================================================
1. READ the user's current project files, identify domain, existing components, and tech stack.
2. INJECT the CSS custom properties above into the global stylesheet or Tailwind config.
3. RE-ARCHITECT each layout section to match the page architecture scaffold above.
4. RE-ENGINEER every UI component (nav, hero, cards, buttons, inputs, footer) into the Stripe Atlas visual language while keeping the user's real content, data, and workflows intact.
5. APPLY motion physics (transitions, hover states, scroll reveals) as specified above.
6. WRITE all page copy in the Copy Voice defined above -- match the tone, not the brand name.
7. VERIFY: The output should feel unmistakably like Stripe Atlas's design aesthetic applied to the user's own project domain.

==================================================================
📦 DELIVERABLE DEFINITION
==================================================================
Output the reskinned project. Apply gradient mesh to hero section specifically. Use white canvas for content sections.
```
