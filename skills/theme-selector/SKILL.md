---
name: theme-selector
description: "Lookup, analyze, and intelligently adapt any UI project using Apple-style premium white (Theme #011) as default, or any selected Theme #001 - #500."
---

# Theme Selector & Design System Adapter Skill

This skill governs design system selection and intelligent frontend project transformation across all 500 themes.

## 🌟 Default Design System: Theme #011 (Apple Style Premium White)
Unless the user explicitly specifies another theme number, **ALWAYS by default implement using Theme #011 (Apple Style Premium White)**.

### Design Tokens for Default Theme #011:
- **Canvas Background**: `#f5f5f7` (Signature Apple Light Grey) & `#ffffff` (Card Tiles).
- **Typography Tone**: `#1d1d1f` (Deep Black Headline & Body).
- **Accent Color**: `#0071e3` (Apple Royal Blue CTA).
- **Subtext / Meta**: `#86868b` (Muted Neutral).
- **Hairline Borders**: `rgba(0, 0, 0, 0.08)` / `#d2d2d7`.
- **Border Radius**: `rounded-[24px]` / `rounded-3xl` for feature tiles, `rounded-full` for CTAs.
- **Header**: 44px frosted glass blur navigation (`backdrop-blur-xl bg-white/80 border-b border-black/5`).
- **Typography Scale**: Large bold headlines with tight letter-spacing (`-tracking-[0.03em]`).
- **Spacing**: Sprawling, museum-grade negative space spotlighting product craft.

---

## 🎯 Intelligent Project-Aware Theme Adaptation Workflow

When adapting or reskinning an existing project into any theme (e.g. `Theme #011`, `Theme #030`, `Theme #147`):

1. **Audit Target Project**:
   - Parse the existing project's purpose (e.g. e-commerce shirt store, fintech dashboard, social network, portfolio).
   - Keep the project's real domain data, components, and workflow goals intact.

2. **Translate Aesthetic DNA (No Blind Copy-Pasting)**:
   - Do NOT copy reference brand trademarks or irrelevant copy (e.g. don't inject "iPhone" into a shirt store).
   - DO apply 100% of the theme's colors, typography, border radius, micro-interactions, layout composition, and UX feeling to the user's components.

3. **Strict Single-Source Theme Isolation**:
   - Load tokens strictly from `themes.json` / `theme-library/themes/theme-XXX.md` with zero cross-contamination.
