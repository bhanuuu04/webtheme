# THEME #070 --- OpenAI

- **Website URL:** [https://openai.com/](https://openai.com/)
- **Category:** AI
- **Design Style:** Minimalist Prompt-First Canvas
- **Mode:** light
- **Tags:** `ai`, `dark`, `minimal`

---

## 🧬 Theme DNA Summary
> **OpenAI design DNA: Dark void canvas, iridescent neon glow accents, prompt-first conversational UI, and live generative canvas modules.**

---

## 🔑 Signature Visual Element
Pure white editorial canvas with the DALL-E/ChatGPT gradient orb imagery (green-to-blue animated sphere) as the sole visual statement. Ultra-clean black system typography. Restraint as a design strategy — the AI product speaks through the whitespace.

---

## 🎭 Emotional Intent
Frontier technology, responsibly approached. The visitor feels they are witnessing something historically significant, calmly presented. Understated confidence, not hype. The future arrives in clean sans-serif.

---

## 🎯 Design Principles ("Why does this look like this?")
Why OpenAI looks like this: Engineered to evoke machine intelligence, boundless creativity, and real-time generative wonder.

---

## 🎨 Color System

### Primary Palette
- **`#050505`** --- Deep Void Canvas
- **`#a855f7`** --- Neural Purple Accent
- **`#ffffff`** --- Bright Text

### Secondary & Surface Palette
- **`#18181b`** --- Card Surface
- **`#3f3f46`** --- Border
- **`#71717a`** --- Muted

### CSS Custom Properties
```css
:root {
  --bg: #ffffff;
  --surface: #f7f7f8;
  --border: #ececf1;
  --accent: #10a37f;
  --text-primary: #000000;
  --text-muted: #6e6e80;
  --radius-sm: 4px;
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

**Copy Voice:** Thoughtful, serious, historically aware. 'OpenAI is an AI research and deployment company.' Straightforward statements of capability. No hype language. CTAs: 'Try ChatGPT', 'Explore the API', 'Read research'. Tone is measured and authoritative.

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
1. Nav: white, OpenAI logo left, product links center, 'Try ChatGPT' right
2. Hero: white, centered H1 (56px), one-line subtitle, gradient AI orb imagery below
3. Product lineup: clean card grid (ChatGPT, API, DALL-E, Sora, etc.)
4. Research highlights: editorial text-heavy section with research paper cards
5. Safety/mission section: text-focused, minimal design
6. API section: code snippet + dark terminal aesthetic
7. Footer: clean 5-col on white

---

## 🚫 Anti-Patterns (What NOT to do)
- No dark sections on main marketing pages
- No gradient backgrounds except for the signature AI orb visual
- No decorative icons or illustrations — photography or AI-generated art only
- No bold color accents beyond the green brand color
- No visual clutter — extreme restraint at all times
- No casual or playful tone — serious, thoughtful communication

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
- Generative AI tools
- LLM chat interfaces
- AI image/audio studios
- Model playgrounds
- OpenAI-inspired applications
- AI platforms

---

## ✅ Things To Reuse
  * Omni-prompt bar design
  * Neon gradient glow borders
  * Token streaming text animation
  * Model status pill

---

## ❌ Things NOT To Copy
  * Proprietary OpenAI brand logos
  * Exact OpenAI copyrighted assets
  * Direct company trademarks

---

## 🛠️ Implementation Notes
Development Guide: Use Tailwind bg-black, radial gradient glows (blur-3xl bg-purple-500/10), and glassmorphism.

---

## 🤖 Deep Comprehensive AI Prompt
```text
[SYSTEM INSTRUCTION: SINGLE-SOURCE THEME DESIGN ADAPTER]
You are a Principal UI/UX Architect & Frontend Design System Engineer.
Your task is to analyze the user's current project / objective, and TRANSFORM / REDESIGN its entire frontend style, visual aesthetic, UX feeling, and component architecture strictly using the design system DNA of THEME #070 (OpenAI - https://openai.com/).

Maintain 100% strict theme isolation: extract and apply ONLY this reference theme's design language, tokens, and aesthetic principles.

==================================================================
🎯 CORE OBJECTIVE: ADAPT THEME TO USER'S PROJECT (NOT A BLIND CLONE)
==================================================================
1. ANALYZE CURRENT PROJECT & GOAL:
   - Carefully inspect the user's current project codebase, wireframes, or feature requirements (e.g. e-commerce clothing store selling shirts, SaaS tool, personal portfolio, marketplace, dashboard, etc.).
   - Preserve the user's core project purpose, domain data, functional workflows, and business logic.

2. TRANSLATE DESIGN DNA (DO NOT COPY PROPRIETARY CONTENT):
   - Do NOT blindly copy placeholder copy, trademarks, or unrelated product catalog from OpenAI (e.g., do not insert "OpenAI" branding or unrelated product listings).
   - DO extract and adopt 100% of OpenAI's visual craft, color palette, typography hierarchy, card structures, spacing rhythm, surface depth, micro-interactions, and UX feeling.

3. ELEVATE & RESKIN EVERY COMPONENT:
   - Reskin the user's existing components (navbars, heroes, product/feature cards, buttons, filters, inputs, modals, footers) into the authentic visual language of THEME #070.
   - Example: If the user's project is an apparel store selling shirts, design a high-craft shirt catalog with OpenAI's signature layouts, typography scale, lighting, and button styles.

==================================================================
🧬 THEME #070 IDENTITY & EMOTIONAL BRIEF
==================================================================
- Permanent Theme ID: THEME #070
- Reference Design Source: OpenAI (https://openai.com/)
- Mode: light
- Archetype / Category: AI
- Design Style: Minimalist Prompt-First Canvas
- Visual Personality: OpenAI signature design: minimalist prompt-first canvas, engineered with high-craft aesthetics, structured hierarchy, and platform-native ergonomics.
- Core Design DNA: OpenAI design DNA: Dark void canvas, iridescent neon glow accents, prompt-first conversational UI, and live generative canvas modules.

THE SIGNATURE VISUAL ELEMENT (What makes this theme unmistakably OpenAI):
Pure white editorial canvas with the DALL-E/ChatGPT gradient orb imagery (green-to-blue animated sphere) as the sole visual statement. Ultra-clean black system typography. Restraint as a design strategy — the AI product speaks through the whitespace.

EMOTIONAL INTENT (How the user should FEEL when they see this design):
Frontier technology, responsibly approached. The visitor feels they are witnessing something historically significant, calmly presented. Understated confidence, not hype. The future arrives in clean sans-serif.

==================================================================
🎨 COLOR SYSTEM & APPLICATION RULES
==================================================================
#ffffff  ->  all backgrounds — total white editorial canvas
#000000  ->  all headings, all body text, all nav links
#10a37f  ->  ChatGPT brand, primary CTA buttons, success states, link accent
#f7f7f8  ->  alternate section backgrounds, input fields
#ececf1  ->  borders, dividers, card outlines
#6e6e80  ->  secondary text, metadata, descriptive labels

CSS Custom Properties (paste into :root {}):
:root {
  --bg: #ffffff;
  --surface: #f7f7f8;
  --border: #ececf1;
  --accent: #10a37f;
  --text-primary: #000000;
  --text-muted: #6e6e80;
  --radius-sm: 4px;
  --radius-md: 8px;
  --radius-lg: 12px;
}

Tailwind Config Extension (add inside extend: {}):
colors: { bg: '#ffffff', surface: '#f7f7f8', border: '#ececf1', accent: '#10a37f', primary: '#000000', muted: '#6e6e80' }

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
Thoughtful, serious, historically aware. 'OpenAI is an AI research and deployment company.' Straightforward statements of capability. No hype language. CTAs: 'Try ChatGPT', 'Explore the API', 'Read research'. Tone is measured and authoritative.

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
1. Nav: white, OpenAI logo left, product links center, 'Try ChatGPT' right
2. Hero: white, centered H1 (56px), one-line subtitle, gradient AI orb imagery below
3. Product lineup: clean card grid (ChatGPT, API, DALL-E, Sora, etc.)
4. Research highlights: editorial text-heavy section with research paper cards
5. Safety/mission section: text-focused, minimal design
6. API section: code snippet + dark terminal aesthetic
7. Footer: clean 5-col on white

==================================================================
ANTI-PATTERNS (what NOT to do -- these break theme authenticity)
==================================================================
  X No dark sections on main marketing pages
  X No gradient backgrounds except for the signature AI orb visual
  X No decorative icons or illustrations — photography or AI-generated art only
  X No bold color accents beyond the green brand color
  X No visual clutter — extreme restraint at all times
  X No casual or playful tone — serious, thoughtful communication

==================================================================
🛡️ DESIGN FIDELITY GUARDRAILS
==================================================================
- MUST ADOPT & REUSE:
  * Omni-prompt bar design
  * Neon gradient glow borders
  * Token streaming text animation
  * Model status pill
- DO NOT COPY (Proprietary / Brand Specific):
  * Proprietary OpenAI brand logos
  * Exact OpenAI copyrighted assets
  * Direct company trademarks
- TECHNICAL IMPLEMENTATION GUIDANCE:
  Development Guide: Use Tailwind bg-black, radial gradient glows (blur-3xl bg-purple-500/10), and glassmorphism.

==================================================================
🛠️ STEP-BY-STEP REFACTORING INSTRUCTIONS
==================================================================
1. READ the user's current project files, identify domain, existing components, and tech stack.
2. INJECT the CSS custom properties above into the global stylesheet or Tailwind config.
3. RE-ARCHITECT each layout section to match the page architecture scaffold above.
4. RE-ENGINEER every UI component (nav, hero, cards, buttons, inputs, footer) into the OpenAI visual language while keeping the user's real content, data, and workflows intact.
5. APPLY motion physics (transitions, hover states, scroll reveals) as specified above.
6. WRITE all page copy in the Copy Voice defined above -- match the tone, not the brand name.
7. VERIFY: The output should feel unmistakably like OpenAI's design aesthetic applied to the user's own project domain.

==================================================================
📦 DELIVERABLE DEFINITION
==================================================================
Extreme whitespace and restraint is the signature. Less is more. The AI product imagery (gradient orb or generated art) is the only decoration allowed.
```
