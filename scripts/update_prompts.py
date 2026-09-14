# -*- coding: utf-8 -*-
import json
import os

with open('themes.json', 'r', encoding='utf-8') as f:
    themes = json.load(f)

for t in themes:
    num_str = f"{t['theme_number']:03d}"
    md_filename = f"theme-library/themes/theme-{num_str}.md"
    
    primaryHex = t['primary_colors'][0]['hex'] if t['primary_colors'] else '#0f172a'
    accentHex = t['primary_colors'][1]['hex'] if len(t['primary_colors']) > 1 else primaryHex
    surfaceHex = t['secondary_colors'][0]['hex'] if t['secondary_colors'] else '#131d31'
    borderHex = t['secondary_colors'][1]['hex'] if len(t['secondary_colors']) > 1 else 'rgba(255,255,255,0.08)'
    domain = t['url'].replace('https://', '').replace('http://', '').replace('www.', '').split('/')[0]

    primary_colors_str = "\n".join([f"  * {c['hex']} → {c['role']}" for c in t['primary_colors']])
    secondary_colors_str = "\n".join([f"  * {c['hex']} → {c['role']}" for c in t['secondary_colors']])
    reuse_str = "\n".join([f"  * {r}" for r in t['things_to_reuse']])
    not_copy_str = "\n".join([f"  * {n}" for n in t['things_not_to_copy']])
    use_cases_str = "\n".join([f"- {uc}" for uc in t['best_use_cases']])
    primary_list_str = "\n".join([f"- **`{c['hex']}`** — {c['role']}" for c in t['primary_colors']])
    secondary_list_str = "\n".join([f"- **`{c['hex']}`** — {c['role']}" for c in t['secondary_colors']])

    ai_prompt = f"""[SYSTEM INSTRUCTION: SINGLE-SOURCE THEME REPLICA]
You are tasked with building a production-ready, pixel-perfect frontend replica strictly adhering to THEME {t['theme_id']} ({t['name']} - {t['url']}). Maintain 100% strict theme isolation: do not combine, blend, or borrow styles from any other theme.

# 1. CORE THEME IDENTITY & ARCHITECTURAL DNA
- Permanent Theme: THEME {t['theme_id']}
- Reference Website: {t['name']} ({t['url']})
- Domain: {domain}
- Primary Category: {t['category']}
- Design Style: {t['design_style']}
- Visual Personality: {t['visual_personality']}
- Design DNA: {t['overall_design_dna']}
- Design Principles ("Why it looks like this"): {t['design_principles']}

# 2. EXACT COLOR TOKEN SYSTEM & LIGHTING
- Base Canvas Background: {primaryHex}
- Container & Card Surface: {surfaceHex}
- Primary Brand / CTA Accent: {accentHex}
- Hairline Border Stroke: {borderHex}
- Primary Color Hierarchy:
{primary_colors_str}
- Secondary & Surface Hierarchy:
{secondary_colors_str}
- Atmospheric Lighting / Glow: radial-gradient(circle, {accentHex}20 0%, transparent 70%) hover glow spotlight

# 3. TYPOGRAPHY & FONT SPECIFICATIONS
- Display / Hero Font: {t['typography']['font_family_display']}
- Body Copy Font: {t['typography']['font_family_body']}
- Monospace / Code Font: {t['typography']['font_family_mono']}
- Optical Letter-Spacing (Tracking): {t['typography']['letter_spacing']}
- Hierarchy Scale & Line-Heights: {t['typography']['scale']}
- Font Weights: {t['typography']['weights']}

# 4. SPACING, GRID & LAYOUT GEOMETRY
- Container Max-Width & Grid: {t['spacing']['grid_system']}
- Vertical Section Rhythm (Padding Scale): {t['spacing']['padding_scale']}
- Whitespace Philosophy: {t['spacing']['whitespace_philosophy']}

# 5. COMPONENT LANGUAGE & MICRO-STATES
- Buttons (CTAs, Secondary, Ghost): {t['components']['buttons']}
- Cards, Tiles & Bento Grid Modules: {t['components']['cards']}
- Header & Navigation System: {t['components']['navigation']}
- Hero Section Architecture: {t['components']['hero_section']}
- Form Inputs & Filter Pills: {t['components']['forms']}
- Footer Layout & System Status: {t['components']['footer']}

# 6. MOTION, PHYSICS & ANIMATION CURVES
- Transitions & Easing Curves: {t['motion']['transitions']}
- Scroll Behavior & Parallax: {t['motion']['scroll_effects']}
- Micro-Interactions & Hover Responses: {t['motion']['micro_interactions']}

# 7. RESPONSIVE STRATEGY
- Mobile Adaptation: {t['responsive']['mobile_strategy']}
- Desktop Ergonomics: {t['responsive']['desktop_strategy']}

# 8. PRECISE EXECUTION GUARDRAILS
- MUST REUSE:
{reuse_str}
- DO NOT COPY (Proprietary/Copyrighted):
{not_copy_str}
- TECHNICAL IMPLEMENTATION NOTES:
  {t['implementation_notes']}

Apply these exact design tokens, typography rules, component styling, and motion parameters to build the requested user deliverable with absolute single-source fidelity."""

    md_content = f"""# {t['theme_display_id']} — {t['name']}

- **Website URL:** [{t['url']}]({t['url']})
- **Category:** {t['category']}
- **Design Style:** {t['design_style']}
- **Tags:** {", ".join([f'`{tag}`' for tag in t['tags']])}

---

## 🧬 Theme DNA Summary
> **{t['overall_design_dna']}**

---

## 🎯 Design Principles ("Why does this look like this?")
{t['design_principles']}

---

## 🎨 Color System

### Primary Palette
{primary_list_str}

### Secondary & Surface Palette
{secondary_list_str}

---

## 🔤 Typography System
- **Display Font:** `{t['typography']['font_family_display']}`
- **Body Font:** `{t['typography']['font_family_body']}`
- **Monospace Font:** `{t['typography']['font_family_mono']}`
- **Hierarchy & Scale:** {t['typography']['scale']}
- **Weights:** {t['typography']['weights']}
- **Letter Spacing:** {t['typography']['letter_spacing']}

---

## 📐 Spacing & Layout Structure
- **Grid System:** {t['spacing']['grid_system']}
- **Padding Scale:** {t['spacing']['padding_scale']}
- **Whitespace Philosophy:** {t['spacing']['whitespace_philosophy']}

---

## 🧩 Component Language

### Buttons
{t['components']['buttons']}

### Cards
{t['components']['cards']}

### Forms & Inputs
{t['components']['forms']}

### Navigation & Header
{t['components']['navigation']}

### Hero Section
{t['components']['hero_section']}

### Footer
{t['components']['footer']}

---

## ⚡ Motion & Animation
- **Transitions:** {t['motion']['transitions']}
- **Scroll Behavior:** {t['motion']['scroll_effects']}
- **Micro-Interactions:** {t['motion']['micro_interactions']}

---

## 📱 Responsive Strategy
- **Mobile:** {t['responsive']['mobile_strategy']}
- **Desktop:** {t['responsive']['desktop_strategy']}

---

## 🚀 Best Use Cases
{use_cases_str}

---

## ✅ Things To Reuse
{reuse_str}

---

## ❌ Things NOT To Copy
{not_copy_str}

---

## 🛠️ Implementation Notes
{t['implementation_notes']}

---

## 🤖 Deep Comprehensive AI Prompt
```text
{ai_prompt}
```
"""
    with open(md_filename, 'w', encoding='utf-8') as mf:
        mf.write(md_content)

print(f"Updated all {len(themes)} markdown theme profiles with deep AI prompts.")
