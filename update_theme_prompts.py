import json
import os
import re
import glob

with open('dashboard/themes.json', 'r', encoding='utf-8') as f:
    themes = json.load(f)

def clean_domain(url):
    domain = re.sub(r'^https?://(www\.)?', '', url)
    return domain.split('/')[0]

def build_ai_prompt(t):
    tid_clean = str(t['theme_id']).replace('#', '').strip()
    accent_hex = t['primary_colors'][1]['hex'] if len(t.get('primary_colors', [])) > 1 else (t['primary_colors'][0]['hex'] if t.get('primary_colors') else '#0070f3')
    surface_hex = t['secondary_colors'][0]['hex'] if t.get('secondary_colors') else '#151618'
    border_hex = t['secondary_colors'][1]['hex'] if len(t.get('secondary_colors', [])) > 1 else '#222326'
    primary_hex = t['primary_colors'][0]['hex'] if t.get('primary_colors') else '#ffffff'
    domain = clean_domain(t['url'])

    # Color application rules
    car = t.get('color_application_rules', {})
    if car:
        color_rules_str = '\n'.join([hex_val + '  ->  ' + usage for hex_val, usage in car.items()])
    else:
        color_rules_str = '\n'.join(
            ['  * ' + c['hex'] + ' -> ' + c['role'] for c in t.get('primary_colors', [])] +
            ['  * ' + c['hex'] + ' -> ' + c['role'] for c in t.get('secondary_colors', [])]
        )

    # Anti-patterns
    anti = t.get('anti_patterns', [])
    anti_str = '\n'.join(['  X ' + p for p in anti]) if anti else '  X Do not mix styles from other themes\n  X Do not use generic Bootstrap/Material components'

    # Page architecture
    arch = t.get('page_architecture', [])
    arch_str = '\n'.join(arch) if arch else '1. Nav -> 2. Hero -> 3. Features -> 4. Social proof -> 5. CTA -> 6. Footer'

    reuse_items = '\n'.join(['  * ' + r for r in t.get('things_to_reuse', [])])
    not_copy_items = '\n'.join(['  * ' + n for n in t.get('things_not_to_copy', [])])

    css_vars = t.get('css_variables', f':root {{ --accent: {accent_hex}; --bg: {primary_hex}; --surface: {surface_hex}; --border: {border_hex}; }}')
    tw_tokens = t.get('tailwind_tokens', f"colors: {{ accent: '{accent_hex}', bg: '{primary_hex}', surface: '{surface_hex}' }}")
    copy_voice = t.get('copy_voice', 'Professional, benefit-focused, clear. Short declarative headlines. Action CTAs.')
    icon_system = t.get('icon_system', 'Lucide Icons, clean stroke style, monochrome')
    image_treatment = t.get('image_treatment', 'Product screenshots or lifestyle photography appropriate to the project domain')
    signature = t.get('signature_visual_element', t.get('design_principles', ''))
    emotional = t.get('emotional_intent', t.get('design_principles', ''))
    mode = t.get('mode', 'light')
    deliverable = t.get('deliverable_note', 'Output the complete reskinned project files. Apply theme tokens via CSS custom properties globally, then rework component markup. Preserve all business logic and domain data.')

    return f"""[SYSTEM INSTRUCTION: SINGLE-SOURCE THEME DESIGN ADAPTER]
You are a Principal UI/UX Architect & Frontend Design System Engineer.
Your task is to analyze the user's current project / objective, and TRANSFORM / REDESIGN its entire frontend style, visual aesthetic, UX feeling, and component architecture strictly using the design system DNA of THEME #{tid_clean} ({t['name']} - {t['url']}).

Maintain 100% strict theme isolation: extract and apply ONLY this reference theme's design language, tokens, and aesthetic principles.

==================================================================
🎯 CORE OBJECTIVE: ADAPT THEME TO USER'S PROJECT (NOT A BLIND CLONE)
==================================================================
1. ANALYZE CURRENT PROJECT & GOAL:
   - Carefully inspect the user's current project codebase, wireframes, or feature requirements (e.g. e-commerce clothing store selling shirts, SaaS tool, personal portfolio, marketplace, dashboard, etc.).
   - Preserve the user's core project purpose, domain data, functional workflows, and business logic.

2. TRANSLATE DESIGN DNA (DO NOT COPY PROPRIETARY CONTENT):
   - Do NOT blindly copy placeholder copy, trademarks, or unrelated product catalog from {t['name']} (e.g., do not insert "{t['name']}" branding or unrelated product listings).
   - DO extract and adopt 100% of {t['name']}'s visual craft, color palette, typography hierarchy, card structures, spacing rhythm, surface depth, micro-interactions, and UX feeling.

3. ELEVATE & RESKIN EVERY COMPONENT:
   - Reskin the user's existing components (navbars, heroes, product/feature cards, buttons, filters, inputs, modals, footers) into the authentic visual language of THEME #{tid_clean}.
   - Example: If the user's project is an apparel store selling shirts, design a high-craft shirt catalog with {t['name']}'s signature layouts, typography scale, lighting, and button styles.

==================================================================
🧬 THEME #{tid_clean} IDENTITY & EMOTIONAL BRIEF
==================================================================
- Permanent Theme ID: THEME #{tid_clean}
- Reference Design Source: {t['name']} ({t['url']})
- Mode: {mode}
- Archetype / Category: {t['category']}
- Design Style: {t['design_style']}
- Visual Personality: {t['visual_personality']}
- Core Design DNA: {t['overall_design_dna']}

THE SIGNATURE VISUAL ELEMENT (What makes this theme unmistakably {t['name']}):
{signature}

EMOTIONAL INTENT (How the user should FEEL when they see this design):
{emotional}

==================================================================
🎨 COLOR SYSTEM & APPLICATION RULES
==================================================================
{color_rules_str}

CSS Custom Properties (paste into :root {{}}):
{css_vars}

Tailwind Config Extension (add inside extend: {{}}):
{tw_tokens}

==================================================================
🔤 TYPOGRAPHY & TEXT RHYTHM
==================================================================
- Display / Headline Font: {t['typography']['font_family_display']}
- Body Copy Font: {t['typography']['font_family_body']}
- Monospace / Data Font: {t['typography']['font_family_mono']}
- Optical Tracking (Letter Spacing): {t['typography']['letter_spacing']}
- Scale & Proportions: {t['typography']['scale']}
- Font Weights: {t['typography']['weights']}

Copy Voice & Tone (match this style in ALL generated text content):
{copy_voice}

==================================================================
📐 SPACING, GRID & GEOMETRY
==================================================================
- Container Max-Width & Grid: {t['spacing']['grid_system']}
- Vertical Padding Scale: {t['spacing']['padding_scale']}
- Whitespace Philosophy: {t['spacing']['whitespace_philosophy']}

==================================================================
🧩 COMPONENT ARCHETYPE MAPPING
==================================================================
- Buttons (Primary, Secondary, Ghost): {t['components']['buttons']}
- Cards, Modules & Bento Grids: {t['components']['cards']}
- Header & Navigation System: {t['components']['navigation']}
- Hero / Showcase Composition: {t['components']['hero_section']}
- Forms, Filters & Pill Selectors: {t['components']['forms']}
- Footer & System Status: {t['components']['footer']}

Icon System: {icon_system}
Image Treatment: {image_treatment}

==================================================================
⚡ MOTION PHYSICS & MICRO-INTERACTIONS
==================================================================
- Transitions & Easing: {t['motion']['transitions']}
  Apply as: transition: all 150ms cubic-bezier(0.16, 1, 0.3, 1) on all interactive elements
- Card Hover: transform: translateY(-2px) + box-shadow escalation
- Button Press: transform: scale(0.97), transition: 80ms ease-in
- Modal Entry: opacity 0 to 1 + translateY(8px to 0px), 200ms
- Scroll Reveals: IntersectionObserver threshold 0.1, staggered 60ms per sibling
- Scroll Behavior: {t['motion']['scroll_effects']}
- Micro-Interactions: {t['motion']['micro_interactions']}

==================================================================
📱 RESPONSIVE ADAPTATION
==================================================================
- Mobile Layout Strategy: {t['responsive']['mobile_strategy']}
- Desktop Ergonomics: {t['responsive']['desktop_strategy']}

==================================================================
🏗️ PAGE ARCHITECTURE (ordered section scaffold for a typical page)
==================================================================
{arch_str}

==================================================================
ANTI-PATTERNS (what NOT to do -- these break theme authenticity)
==================================================================
{anti_str}

==================================================================
🛡️ DESIGN FIDELITY GUARDRAILS
==================================================================
- MUST ADOPT & REUSE:
{reuse_items}
- DO NOT COPY (Proprietary / Brand Specific):
{not_copy_items}
- TECHNICAL IMPLEMENTATION GUIDANCE:
  {t['implementation_notes']}

==================================================================
🛠️ STEP-BY-STEP REFACTORING INSTRUCTIONS
==================================================================
1. READ the user's current project files, identify domain, existing components, and tech stack.
2. INJECT the CSS custom properties above into the global stylesheet or Tailwind config.
3. RE-ARCHITECT each layout section to match the page architecture scaffold above.
4. RE-ENGINEER every UI component (nav, hero, cards, buttons, inputs, footer) into the {t['name']} visual language while keeping the user's real content, data, and workflows intact.
5. APPLY motion physics (transitions, hover states, scroll reveals) as specified above.
6. WRITE all page copy in the Copy Voice defined above -- match the tone, not the brand name.
7. VERIFY: The output should feel unmistakably like {t['name']}'s design aesthetic applied to the user's own project domain.

==================================================================
📦 DELIVERABLE DEFINITION
==================================================================
{deliverable}"""


def generate_markdown(t):
    tid_clean = str(t['theme_id']).replace('#', '').strip()
    ai_prompt = build_ai_prompt(t)
    tags_str = ', '.join(['`' + tag + '`' for tag in t.get('tags', [])])
    prim_colors_md = '\n'.join(['- **`' + c['hex'] + '`** --- ' + c['role'] for c in t.get('primary_colors', [])])
    sec_colors_md = '\n'.join(['- **`' + c['hex'] + '`** --- ' + c['role'] for c in t.get('secondary_colors', [])])
    use_cases_md = '\n'.join(['- ' + u for u in t.get('best_use_cases', [])])
    reuse_md = '\n'.join(['  * ' + r for r in t.get('things_to_reuse', [])])
    not_copy_md = '\n'.join(['  * ' + n for n in t.get('things_not_to_copy', [])])
    mode = t.get('mode', 'light')
    signature = t.get('signature_visual_element', '')
    emotional = t.get('emotional_intent', '')
    anti = t.get('anti_patterns', [])
    anti_md = '\n'.join(['- ' + p for p in anti]) if anti else ''
    arch = t.get('page_architecture', [])
    arch_md = '\n'.join(arch) if arch else ''
    css_vars = t.get('css_variables', '')
    copy_voice = t.get('copy_voice', '')

    md_content = f"""# THEME #{tid_clean} --- {t['name']}

- **Website URL:** [{t['url']}]({t['url']})
- **Category:** {t['category']}
- **Design Style:** {t['design_style']}
- **Mode:** {mode}
- **Tags:** {tags_str}

---

## 🧬 Theme DNA Summary
> **{t['overall_design_dna']}**

---

## 🔑 Signature Visual Element
{signature}

---

## 🎭 Emotional Intent
{emotional}

---

## 🎯 Design Principles ("Why does this look like this?")
{t['design_principles']}

---

## 🎨 Color System

### Primary Palette
{prim_colors_md}

### Secondary & Surface Palette
{sec_colors_md}

### CSS Custom Properties
```css
{css_vars}
```

---

## 🔤 Typography System
- **Display Font:** `{t['typography']['font_family_display']}`
- **Body Font:** `{t['typography']['font_family_body']}`
- **Monospace Font:** `{t['typography']['font_family_mono']}`
- **Hierarchy & Scale:** {t['typography']['scale']}
- **Weights:** {t['typography']['weights']}
- **Letter Spacing:** {t['typography']['letter_spacing']}

**Copy Voice:** {copy_voice}

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

## 🏗️ Page Architecture
{arch_md}

---

## 🚫 Anti-Patterns (What NOT to do)
{anti_md}

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
{use_cases_md}

---

## ✅ Things To Reuse
{reuse_md}

---

## ❌ Things NOT To Copy
{not_copy_md}

---

## 🛠️ Implementation Notes
{t['implementation_notes']}

---

## 🤖 Deep Comprehensive AI Prompt
```text
{ai_prompt}
```
"""
    return md_content


def main():
    target_dir = 'theme-library/themes'
    os.makedirs(target_dir, exist_ok=True)

    # Remove stale files
    for old_file in glob.glob(os.path.join(target_dir, '*.md')):
        try:
            os.remove(old_file)
        except Exception:
            pass

    for t in themes:
        tid_clean = str(t['theme_id']).replace('#', '').strip()
        filename = f'{target_dir}/theme-{tid_clean}.md'
        content = generate_markdown(t)
        with open(filename, 'w', encoding='utf-8') as mf:
            mf.write(content)

    print(f'Successfully regenerated all {len(themes)} theme markdown files with full enriched prompts!')


if __name__ == '__main__':
    main()
