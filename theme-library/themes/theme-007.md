# THEME #007 --- Raycast

- **Website URL:** [https://www.raycast.com/](https://www.raycast.com/)
- **Category:** SaaS / Product
- **Design Style:** High-Density Productivity Workspace
- **Mode:** dark
- **Tags:** `saas-product`, `dark`, `saas`

---

## 🧬 Theme DNA Summary
> **Raycast design DNA: Large typography, generous whitespace, monochrome palette, subtle borders, restrained motion, asymmetric hero composition and strong product-focused visual hierarchy.**

---

## 🔑 Signature Visual Element
Deep space dark background (#1c1c1e) with the Raycast command launcher interface mockup as the hero centerpiece. Orange-to-pink gradient (#FF6363 to #FF9F0A) as the signature brand gradient, used on CTAs and logo. Blurred extension store card grid.

---

## 🎭 Emotional Intent
Mac-native power user delight. The user feels this is the smartest productivity tool ever built for Mac. Every interaction feels snappy, keyboard-first, and delightfully crafted. Premium macOS aesthetic.

---

## 🎯 Design Principles ("Why does this look like this?")
Why Raycast looks like this: Built to communicate speed, craft, and keyboard-first productivity by removing clutter and focusing on high contrast, micro-details, and crisp dark backgrounds.

---

## 🎨 Color System

### Primary Palette
- **`#08090a`** --- Obsidian Dark Canvas
- **`#5e6ad2`** --- Brand Indigo Accent
- **`#f7f8f8`** --- Primary Text

### Secondary & Surface Palette
- **`#151618`** --- Card Surface
- **`#222326`** --- Subtle Border
- **`#8a8f98`** --- Muted Secondary Text

### CSS Custom Properties
```css
:root {
  --bg: #1c1c1e;
  --surface: #2c2c2e;
  --border: #3a3a3c;
  --accent: #FF6363;
  --accent-end: #FF9F0A;
  --text-primary: #ffffff;
  --text-muted: #8e8e93;
  --radius-sm: 8px;
  --radius-md: 10px;
  --radius-lg: 13px;
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

**Copy Voice:** Power user-to-power user. 'Your shortcut to everything.' Confident, spare, Mac-native tone. Features listed as capabilities, not benefits. CTAs: 'Download for Mac', 'Get Raycast Pro', 'Explore extensions'.

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
1. Nav: dark blurred, Raycast logo left, links center, 'Download' pill right
2. Hero: dark bg, command launcher interface mockup center, H1 above, CTA below
3. Extension store grid: 4-col card grid showing extension icons and names
4. Feature sections: alternating dark cards with launcher UI screenshots
5. Testimonials: developer/power-user quotes
6. AI feature section: gradient accent section for Raycast AI
7. Download CTA: gradient CTA banner
8. Footer: dark 4-col

---

## 🚫 Anti-Patterns (What NOT to do)
- No light canvas — fully dark macOS-native dark mode aesthetic
- No gradients other than the orange-to-pink brand gradient
- No Web-style rounded corners — use Apple system corner radii (10px, 13px)
- No heavy marketing copy — let the product interface speak
- No non-Mac-native design patterns (keep iOS-adjacent Apple HIG aesthetics)

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
- Raycast-inspired applications
- SaaS / Product platforms

---

## ✅ Things To Reuse
  * 1px glowing border cards
  * Keyboard shortcut UI badges
  * Obsidian color system
  * Radial hero glow spotlight

---

## ❌ Things NOT To Copy
  * Proprietary Raycast brand logos
  * Exact Raycast copyrighted assets
  * Direct company trademarks

---

## 🛠️ Implementation Notes
Development Guide: Use Tailwind bg-[#08090a], border-white/10, hover:border-white/20, font-inter with -tracking-[0.02em] and lucide-react icons.

---

## 🤖 Deep Comprehensive AI Prompt
```text
[SYSTEM INSTRUCTION: SINGLE-SOURCE THEME DESIGN ADAPTER]
You are a Principal UI/UX Architect & Frontend Design System Engineer.
Your task is to analyze the user's current project / objective, and TRANSFORM / REDESIGN its entire frontend style, visual aesthetic, UX feeling, and component architecture strictly using the design system DNA of THEME #007 (Raycast - https://www.raycast.com/).

Maintain 100% strict theme isolation: extract and apply ONLY this reference theme's design language, tokens, and aesthetic principles.

==================================================================
🎯 CORE OBJECTIVE: ADAPT THEME TO USER'S PROJECT (NOT A BLIND CLONE)
==================================================================
1. ANALYZE CURRENT PROJECT & GOAL:
   - Carefully inspect the user's current project codebase, wireframes, or feature requirements (e.g. e-commerce clothing store selling shirts, SaaS tool, personal portfolio, marketplace, dashboard, etc.).
   - Preserve the user's core project purpose, domain data, functional workflows, and business logic.

2. TRANSLATE DESIGN DNA (DO NOT COPY PROPRIETARY CONTENT):
   - Do NOT blindly copy placeholder copy, trademarks, or unrelated product catalog from Raycast (e.g., do not insert "Raycast" branding or unrelated product listings).
   - DO extract and adopt 100% of Raycast's visual craft, color palette, typography hierarchy, card structures, spacing rhythm, surface depth, micro-interactions, and UX feeling.

3. ELEVATE & RESKIN EVERY COMPONENT:
   - Reskin the user's existing components (navbars, heroes, product/feature cards, buttons, filters, inputs, modals, footers) into the authentic visual language of THEME #007.
   - Example: If the user's project is an apparel store selling shirts, design a high-craft shirt catalog with Raycast's signature layouts, typography scale, lighting, and button styles.

==================================================================
🧬 THEME #007 IDENTITY & EMOTIONAL BRIEF
==================================================================
- Permanent Theme ID: THEME #007
- Reference Design Source: Raycast (https://www.raycast.com/)
- Mode: dark
- Archetype / Category: SaaS / Product
- Design Style: High-Density Productivity Workspace
- Visual Personality: Raycast signature design: high-density productivity workspace, engineered with high-craft aesthetics, structured hierarchy, and platform-native ergonomics.
- Core Design DNA: Raycast design DNA: Large typography, generous whitespace, monochrome palette, subtle borders, restrained motion, asymmetric hero composition and strong product-focused visual hierarchy.

THE SIGNATURE VISUAL ELEMENT (What makes this theme unmistakably Raycast):
Deep space dark background (#1c1c1e) with the Raycast command launcher interface mockup as the hero centerpiece. Orange-to-pink gradient (#FF6363 to #FF9F0A) as the signature brand gradient, used on CTAs and logo. Blurred extension store card grid.

EMOTIONAL INTENT (How the user should FEEL when they see this design):
Mac-native power user delight. The user feels this is the smartest productivity tool ever built for Mac. Every interaction feels snappy, keyboard-first, and delightfully crafted. Premium macOS aesthetic.

==================================================================
🎨 COLOR SYSTEM & APPLICATION RULES
==================================================================
#1c1c1e  ->  body background — Apple-system dark appearance
#FF6363  ->  gradient start for CTAs, logo, brand marks, hover accents
#FF9F0A  ->  gradient end for CTAs and highlights
#ffffff  ->  headlines, nav links, primary text
#2c2c2e  ->  card surfaces, panel backgrounds, modal backgrounds
#3a3a3c  ->  borders, separator lines
#8e8e93  ->  secondary text, metadata, descriptions

CSS Custom Properties (paste into :root {}):
:root {
  --bg: #1c1c1e;
  --surface: #2c2c2e;
  --border: #3a3a3c;
  --accent: #FF6363;
  --accent-end: #FF9F0A;
  --text-primary: #ffffff;
  --text-muted: #8e8e93;
  --radius-sm: 8px;
  --radius-md: 10px;
  --radius-lg: 13px;
}

Tailwind Config Extension (add inside extend: {}):
colors: { bg: '#1c1c1e', surface: '#2c2c2e', border: '#3a3a3c', accent: '#FF6363', primary: '#ffffff', muted: '#8e8e93' }

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
Power user-to-power user. 'Your shortcut to everything.' Confident, spare, Mac-native tone. Features listed as capabilities, not benefits. CTAs: 'Download for Mac', 'Get Raycast Pro', 'Explore extensions'.

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
1. Nav: dark blurred, Raycast logo left, links center, 'Download' pill right
2. Hero: dark bg, command launcher interface mockup center, H1 above, CTA below
3. Extension store grid: 4-col card grid showing extension icons and names
4. Feature sections: alternating dark cards with launcher UI screenshots
5. Testimonials: developer/power-user quotes
6. AI feature section: gradient accent section for Raycast AI
7. Download CTA: gradient CTA banner
8. Footer: dark 4-col

==================================================================
ANTI-PATTERNS (what NOT to do -- these break theme authenticity)
==================================================================
  X No light canvas — fully dark macOS-native dark mode aesthetic
  X No gradients other than the orange-to-pink brand gradient
  X No Web-style rounded corners — use Apple system corner radii (10px, 13px)
  X No heavy marketing copy — let the product interface speak
  X No non-Mac-native design patterns (keep iOS-adjacent Apple HIG aesthetics)

==================================================================
🛡️ DESIGN FIDELITY GUARDRAILS
==================================================================
- MUST ADOPT & REUSE:
  * 1px glowing border cards
  * Keyboard shortcut UI badges
  * Obsidian color system
  * Radial hero glow spotlight
- DO NOT COPY (Proprietary / Brand Specific):
  * Proprietary Raycast brand logos
  * Exact Raycast copyrighted assets
  * Direct company trademarks
- TECHNICAL IMPLEMENTATION GUIDANCE:
  Development Guide: Use Tailwind bg-[#08090a], border-white/10, hover:border-white/20, font-inter with -tracking-[0.02em] and lucide-react icons.

==================================================================
🛠️ STEP-BY-STEP REFACTORING INSTRUCTIONS
==================================================================
1. READ the user's current project files, identify domain, existing components, and tech stack.
2. INJECT the CSS custom properties above into the global stylesheet or Tailwind config.
3. RE-ARCHITECT each layout section to match the page architecture scaffold above.
4. RE-ENGINEER every UI component (nav, hero, cards, buttons, inputs, footer) into the Raycast visual language while keeping the user's real content, data, and workflows intact.
5. APPLY motion physics (transitions, hover states, scroll reveals) as specified above.
6. WRITE all page copy in the Copy Voice defined above -- match the tone, not the brand name.
7. VERIFY: The output should feel unmistakably like Raycast's design aesthetic applied to the user's own project domain.

==================================================================
📦 DELIVERABLE DEFINITION
==================================================================
The command launcher interface is central to Raycast's brand identity — include a stylized representation of this component in the hero section.
```
