# THEME #003 --- Stripe

- **Website URL:** [https://stripe.com/](https://stripe.com/)
- **Category:** SaaS / Product
- **Design Style:** High-Density Productivity Workspace
- **Mode:** light
- **Tags:** `saas-product`, `light`, `saas`

---

## 🧬 Theme DNA Summary
> **Stripe design DNA: Large typography, generous whitespace, monochrome palette, subtle borders, restrained motion, asymmetric hero composition and strong product-focused visual hierarchy.**

---

## 🔑 Signature Visual Element
Animated gradient mesh background (purple-to-cyan-to-teal) behind the hero. Tilted 3D card stack with drop shadows showing the product. Gradient text on key headlines (#635bff to #00d4ff). Light white canvas for content sections.

---

## 🎭 Emotional Intent
Enterprise-grade financial infrastructure, but approachable and modern. The visitor feels Stripe is both trusted by Fortune 500s and easy for a solo developer. Premium, but not intimidating.

---

## 🎯 Design Principles ("Why does this look like this?")
Why Stripe looks like this: Built to communicate speed, craft, and keyboard-first productivity by removing clutter and focusing on high contrast, micro-details, and crisp dark backgrounds.

---

## 🎨 Color System

### Primary Palette
- **`#0f172a`** --- Slate Dark Canvas
- **`#10b981`** --- Emerald Accent
- **`#ffffff`** --- Headline Text

### Secondary & Surface Palette
- **`#151618`** --- Card Surface
- **`#222326`** --- Subtle Border
- **`#8a8f98`** --- Muted Secondary Text

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
- **Display Font:** `'SF Pro Display', -apple-system, BlinkMacSystemFont, 'Plus Jakarta Sans', sans-serif`
- **Body Font:** `'SF Pro Text', -apple-system, BlinkMacSystemFont, sans-serif`
- **Monospace Font:** `'SF Mono', 'JetBrains Mono', monospace`
- **Hierarchy & Scale:** Hero: 64-96px (-0.035em), H1: 44px, H2: 32px, Body: 17px, Caption: 13px
- **Weights:** 400 Regular, 500 Medium, 600 SemiBold, 700 Bold
- **Letter Spacing:** -0.03em display, -0.015em body

**Copy Voice:** Confident financial authority meets developer warmth. 'Payments infrastructure for the internet.' Clear value statements. Technical precision in feature copy. CTAs: 'Start now', 'Contact sales', 'Explore docs'. Never use 'revolutionary'.

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
- Stripe-inspired applications
- SaaS / Product platforms

---

## ✅ Things To Reuse
  * 1px glowing border cards
  * Keyboard shortcut UI badges
  * Obsidian color system
  * Radial hero glow spotlight

---

## ❌ Things NOT To Copy
  * Proprietary Stripe brand logos
  * Exact Stripe copyrighted assets
  * Direct company trademarks

---

## 🛠️ Implementation Notes
Development Guide: Use Tailwind bg-[#08090a], border-white/10, hover:border-white/20, font-inter with -tracking-[0.02em] and lucide-react icons.

---

## 🤖 Deep Comprehensive AI Prompt
```text
[SYSTEM INSTRUCTION: SINGLE-SOURCE THEME DESIGN ADAPTER]
You are a Principal UI/UX Architect & Frontend Design System Engineer.
Your task is to analyze the user's current project / objective, and TRANSFORM / REDESIGN its entire frontend style, visual aesthetic, UX feeling, and component architecture strictly using the design system DNA of THEME #003 (Stripe - https://stripe.com/).

Maintain 100% strict theme isolation: extract and apply ONLY this reference theme's design language, tokens, and aesthetic principles.

==================================================================
🎯 CORE OBJECTIVE: ADAPT THEME TO USER'S PROJECT (NOT A BLIND CLONE)
==================================================================
1. ANALYZE CURRENT PROJECT & GOAL:
   - Carefully inspect the user's current project codebase, wireframes, or feature requirements (e.g. e-commerce clothing store selling shirts, SaaS tool, personal portfolio, marketplace, dashboard, etc.).
   - Preserve the user's core project purpose, domain data, functional workflows, and business logic.

2. TRANSLATE DESIGN DNA (DO NOT COPY PROPRIETARY CONTENT):
   - Do NOT blindly copy placeholder copy, trademarks, or unrelated product catalog from Stripe (e.g., do not insert "Stripe" branding or unrelated product listings).
   - DO extract and adopt 100% of Stripe's visual craft, color palette, typography hierarchy, card structures, spacing rhythm, surface depth, micro-interactions, and UX feeling.

3. ELEVATE & RESKIN EVERY COMPONENT:
   - Reskin the user's existing components (navbars, heroes, product/feature cards, buttons, filters, inputs, modals, footers) into the authentic visual language of THEME #003.
   - Example: If the user's project is an apparel store selling shirts, design a high-craft shirt catalog with Stripe's signature layouts, typography scale, lighting, and button styles.

==================================================================
🧬 THEME #003 IDENTITY & EMOTIONAL BRIEF
==================================================================
- Permanent Theme ID: THEME #003
- Reference Design Source: Stripe (https://stripe.com/)
- Mode: light
- Archetype / Category: SaaS / Product
- Design Style: High-Density Productivity Workspace
- Visual Personality: Stripe signature design: high-density productivity workspace, engineered with high-craft aesthetics, structured hierarchy, and platform-native ergonomics.
- Core Design DNA: Stripe design DNA: Large typography, generous whitespace, monochrome palette, subtle borders, restrained motion, asymmetric hero composition and strong product-focused visual hierarchy.

THE SIGNATURE VISUAL ELEMENT (What makes this theme unmistakably Stripe):
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
- Display / Headline Font: 'SF Pro Display', -apple-system, BlinkMacSystemFont, 'Plus Jakarta Sans', sans-serif
- Body Copy Font: 'SF Pro Text', -apple-system, BlinkMacSystemFont, sans-serif
- Monospace / Data Font: 'SF Mono', 'JetBrains Mono', monospace
- Optical Tracking (Letter Spacing): -0.03em display, -0.015em body
- Scale & Proportions: Hero: 64-96px (-0.035em), H1: 44px, H2: 32px, Body: 17px, Caption: 13px
- Font Weights: 400 Regular, 500 Medium, 600 SemiBold, 700 Bold

Copy Voice & Tone (match this style in ALL generated text content):
Confident financial authority meets developer warmth. 'Payments infrastructure for the internet.' Clear value statements. Technical precision in feature copy. CTAs: 'Start now', 'Contact sales', 'Explore docs'. Never use 'revolutionary'.

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
  * 1px glowing border cards
  * Keyboard shortcut UI badges
  * Obsidian color system
  * Radial hero glow spotlight
- DO NOT COPY (Proprietary / Brand Specific):
  * Proprietary Stripe brand logos
  * Exact Stripe copyrighted assets
  * Direct company trademarks
- TECHNICAL IMPLEMENTATION GUIDANCE:
  Development Guide: Use Tailwind bg-[#08090a], border-white/10, hover:border-white/20, font-inter with -tracking-[0.02em] and lucide-react icons.

==================================================================
🛠️ STEP-BY-STEP REFACTORING INSTRUCTIONS
==================================================================
1. READ the user's current project files, identify domain, existing components, and tech stack.
2. INJECT the CSS custom properties above into the global stylesheet or Tailwind config.
3. RE-ARCHITECT each layout section to match the page architecture scaffold above.
4. RE-ENGINEER every UI component (nav, hero, cards, buttons, inputs, footer) into the Stripe visual language while keeping the user's real content, data, and workflows intact.
5. APPLY motion physics (transitions, hover states, scroll reveals) as specified above.
6. WRITE all page copy in the Copy Voice defined above -- match the tone, not the brand name.
7. VERIFY: The output should feel unmistakably like Stripe's design aesthetic applied to the user's own project domain.

==================================================================
📦 DELIVERABLE DEFINITION
==================================================================
Output the reskinned project. Apply gradient mesh to hero section specifically. Use white canvas for content sections.
```
