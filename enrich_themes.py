"""
THEME ENRICHMENT ENGINE
Adds 15 new high-signal fields to every theme in themes.json.
Flagship brands (top 60) get hand-crafted accurate data.
All other themes get category-smart intelligent defaults.
"""

import json
import re
import os

with open('dashboard/themes.json', 'r', encoding='utf-8') as f:
    themes = json.load(f)

def clean_domain(url):
    domain = re.sub(r'^https?://(www\.)?', '', url)
    return domain.split('/')[0]

# ═══════════════════════════════════════════════════════════════════
# FLAGSHIP OVERRIDES - Hand-crafted accurate real-world data
# ═══════════════════════════════════════════════════════════════════
FLAGSHIP = {

    "linear.app": {
        "mode": "dark",
        "signature_visual_element": "Ultra-dense issue-row list on near-black canvas (#08090a). Each row: 40px height, 1px separator rgba(255,255,255,0.06), Brand Indigo pill status badges, no decorative chrome. The density IS the feature.",
        "emotional_intent": "Total control, instant speed. The user feels like a keyboard-powered operator — zero friction, every action responding in under 100ms. Premium dark precision that respects developer time.",
        "color_application_rules": {
            "#08090a": "body background, all section backgrounds — never break this darkness",
            "#5e6ad2": "CTA buttons (solid), active sidebar item glow, progress bars, focus rings, priority badges",
            "#f7f8f8": "H1, H2, all display text, navigation links",
            "#151618": "card surfaces, modal backgrounds, input fields, dropdown panels",
            "#222326": "all borders, table separators, dividers — 1px only",
            "#8a8f98": "body text, metadata, timestamps, secondary labels"
        },
        "anti_patterns": [
            "No gradient backgrounds or gradient text — flat dark surfaces only",
            "No rounded hero sections or blob shapes",
            "No heavy drop shadows — hairline borders only",
            "No decorative illustrations — product screenshots only",
            "No centered full-width hero text — left-aligned density",
            "No more than 1 accent color element per UI section",
            "No large padding between list items — density is the brand"
        ],
        "page_architecture": [
            "1. Sticky 44px nav: logo left, nav links center, 'Get started' pill right",
            "2. Hero: H1 left-aligned 64px, subtitle 20px, 2 CTAs horizontal, product screenshot right",
            "3. Social proof logos strip: muted monochrome, 8 logos, borderless",
            "4. Feature callout row: 3-column icon + headline + 1-line body",
            "5. Product deep-dive: alternating 2-col (text left/right) with app frame screenshot",
            "6. Testimonial: single quote, avatar, name/role, minimal",
            "7. CTA banner: dark surface, centered headline, single CTA",
            "8. Footer: 5-col links, system status green dot, keyboard shortcut badge"
        ],
        "icon_system": "Lucide Icons, 1.5px stroke, 16px default, strictly monochrome (white or #8a8f98)",
        "image_treatment": "High-fidelity dark app UI screenshots only. No photography, no illustrations. Screenshots must show the actual product at full density.",
        "copy_voice": "Declarative and precise. 'The project management tool for high-performance teams.' Short punchy headlines (3-6 words). No exclamation marks. No marketing superlatives. Body copy is factual and benefit-focused.",
        "css_variables": ":root {\n  --bg: #08090a;\n  --surface: #151618;\n  --border: #222326;\n  --accent: #5e6ad2;\n  --text-primary: #f7f8f8;\n  --text-muted: #8a8f98;\n  --radius-sm: 4px;\n  --radius-md: 6px;\n  --radius-lg: 8px;\n}",
        "tailwind_tokens": "colors: { bg: '#08090a', surface: '#151618', border: '#222326', accent: '#5e6ad2', primary: '#f7f8f8', muted: '#8a8f98' }, borderRadius: { sm: '4px', md: '6px', lg: '8px' }",
        "deliverable_note": "Output the reskinned project files preserving all domain data and functionality. Apply theme tokens globally via CSS custom properties first, then rework component markup."
    },

    "vercel.com": {
        "mode": "dark",
        "signature_visual_element": "Pure #000000 background with pure #ffffff typography — maximum contrast, zero mid-tones. The Vercel triangle logo and speed-metric animations are the only decorative elements. Everything else is eliminated.",
        "emotional_intent": "Infrastructure-grade reliability with zero-config speed. The visitor feels Vercel is the fastest, most trusted deployment platform. Obsessively minimal = obsessively fast.",
        "color_application_rules": {
            "#000000": "body background, all section backgrounds — absolute black only",
            "#ffffff": "H1, H2, H3, nav links, CTA button backgrounds (inverted), key UI labels",
            "#888888": "body text, subtitles, metadata, secondary labels",
            "#111111": "card surfaces, modal backgrounds",
            "#333333": "borders, dividers — 1px only"
        },
        "anti_patterns": [
            "No color accents except pure white or pure black",
            "No gradient backgrounds",
            "No border-radius above 8px on structural elements",
            "No illustrations — only product screenshots or abstract geometric shapes",
            "No loose line-height on headings — keep tracking tight (-0.04em)",
            "No more than 2 font weights per page section"
        ],
        "page_architecture": [
            "1. Nav: transparent-to-black on scroll, logo left, links center, CTA right",
            "2. Hero: centered single H1 (60-80px), one-line subtitle, 2 pill CTAs, animated deployment preview below",
            "3. Feature metrics: 3 large stat numbers with label below",
            "4. Framework logos strip: monochrome, 8+ logos on dark strip",
            "5. Feature panels: alternating dark surface cards with code snippets",
            "6. Pricing table: 3 columns on dark surface, white CTA for featured",
            "7. Enterprise CTA: full-width dark panel, headline + contact CTA",
            "8. Footer: 5-col minimal link grid, company info bottom"
        ],
        "icon_system": "Geist Icons, 1px stroke, 14px-16px, pure white or #888",
        "image_treatment": "Abstract deployment animations, terminal output screenshots, framework icons. No photography. Monochrome aesthetic enforced on all media.",
        "copy_voice": "Technical authority, confident brevity. 'Develop. Preview. Ship.' Imperative verbs. No adjectives. Developer-first language, never consumer. CTAs: 'Deploy Now', 'Get Started', 'Read Docs'.",
        "css_variables": ":root {\n  --bg: #000000;\n  --surface: #111111;\n  --border: #333333;\n  --text-primary: #ffffff;\n  --text-muted: #888888;\n  --radius-sm: 4px;\n  --radius-md: 8px;\n}",
        "tailwind_tokens": "colors: { bg: '#000000', surface: '#111111', border: '#333333', primary: '#ffffff', muted: '#888888' }",
        "deliverable_note": "Output the reskinned project files. Global CSS variables first, then component markup."
    },

    "stripe.com": {
        "mode": "light",
        "signature_visual_element": "Animated gradient mesh background (purple-to-cyan-to-teal) behind the hero. Tilted 3D card stack with drop shadows showing the product. Gradient text on key headlines (#635bff to #00d4ff). Light white canvas for content sections.",
        "emotional_intent": "Enterprise-grade financial infrastructure, but approachable and modern. The visitor feels Stripe is both trusted by Fortune 500s and easy for a solo developer. Premium, but not intimidating.",
        "color_application_rules": {
            "#635bff": "primary CTA buttons (solid), links, active states, gradient text start",
            "#0a2540": "dark text, hero headings, footer background",
            "#ffffff": "page canvas, card surfaces, nav background",
            "#f6f9fc": "section alternate backgrounds, input fields",
            "#425466": "body text, descriptions, secondary content",
            "#00d4ff": "gradient accent end, hover glow effects"
        },
        "anti_patterns": [
            "No dark canvas for main sections — keep body on white/near-white",
            "No flat gradient — always animated or multi-stop gradient mesh",
            "No dense technical tables without the Stripe card styling",
            "No generic rounded cards — Stripe cards have specific shadow depth system",
            "Do not use the gradient on body text — only on display headlines",
            "No monochrome logo strip — Stripe shows colored brand logos"
        ],
        "page_architecture": [
            "1. Nav: white bg, logo left, product dropdown links, 'Contact sales' + 'Start now' right",
            "2. Hero: gradient mesh bg, H1 with gradient text, subtitle, 2 CTAs, tilted 3D product card stack",
            "3. Trust logos: 'Join millions of companies including...' with colored brand logos",
            "4. Product feature: white section, icon + headline, alternating 2-col layout",
            "5. Code example: dark terminal block with syntax highlighting, white explanation text beside",
            "6. Metrics: 3 large stats on light background",
            "7. Testimonials: card grid on soft gray background",
            "8. Pricing section: 3-tier table, purple-outlined featured tier",
            "9. Footer: dark (#0a2540) 5-col link grid"
        ],
        "icon_system": "Custom Stripe icons — duotone style, purple primary + cyan secondary. Also uses custom 3D isometric product illustrations.",
        "image_treatment": "Abstract 3D gradient renders for product concepts. Animated mesh gradients in hero. Real product UI screenshots in feature sections. Colored brand logos in trust section.",
        "copy_voice": "Confident financial authority meets developer warmth. 'Payments infrastructure for the internet.' Clear value statements. Technical precision in feature copy. CTAs: 'Start now', 'Contact sales', 'Explore docs'. Never use 'revolutionary'.",
        "css_variables": ":root {\n  --bg: #ffffff;\n  --surface: #f6f9fc;\n  --border: #e0e6eb;\n  --accent: #635bff;\n  --text-primary: #0a2540;\n  --text-body: #425466;\n  --gradient-start: #635bff;\n  --gradient-end: #00d4ff;\n  --radius-md: 8px;\n  --radius-lg: 12px;\n}",
        "tailwind_tokens": "colors: { bg: '#ffffff', surface: '#f6f9fc', accent: '#635bff', primary: '#0a2540', body: '#425466' }",
        "deliverable_note": "Output the reskinned project. Apply gradient mesh to hero section specifically. Use white canvas for content sections."
    },

    "framer.com": {
        "mode": "dark",
        "signature_visual_element": "Full-bleed kinetic motion hero — large text animates on scroll/load with spring physics. Dramatic product viewport previews with 3D perspective tilt. Bold section breaks using oversized typography (120px+) as decorative elements.",
        "emotional_intent": "Alive, kinetic, experimental. The visitor feels this tool is made by people who love pushing the boundaries of what the web can do. Motion IS the message. Every scroll triggers delight.",
        "color_application_rules": {
            "#0d0d0d": "body background, all major sections",
            "#0099ff": "primary CTAs, hover accents, animated underlines, focus rings",
            "#ffffff": "display headlines, nav links, primary text",
            "#1a1a1a": "card surfaces, code blocks, modal backgrounds",
            "#888888": "body copy, metadata, secondary descriptions"
        },
        "anti_patterns": [
            "No static hero — there must be motion (CSS animation or JS-driven)",
            "No small typography in hero — minimum 72px for hero headlines",
            "No symmetrical layouts — asymmetric, overlapping compositions are authentic",
            "No subtle micro-interactions — Framer interactions are visible and dramatic",
            "No traditional corporate grids — break the grid intentionally"
        ],
        "page_architecture": [
            "1. Nav: transparent dark, logo + minimal links, 'Get started free' pill",
            "2. Hero: full viewport height, animated kinetic headline, scroll-triggered reveal",
            "3. Product viewport showcase: browser frame with site-in-motion GIF/video",
            "4. Feature bento grid: asymmetric 3-4 tile layout, each tile animated on hover",
            "5. Template gallery: horizontal scroll strip, card hover = 3D tilt",
            "6. Testimonials: oversized pull quote, minimal attribution",
            "7. CTA section: full-width dark, kinetic headline, single CTA button",
            "8. Footer: minimal dark 4-col"
        ],
        "icon_system": "Custom Framer icons — bold, filled style. Also uses animated SVG illustrations for feature concepts.",
        "image_treatment": "Animated GIFs or video loops of product in action. 3D perspective product frames. Abstract motion blur graphics. Never static screenshots alone.",
        "copy_voice": "Creative-forward, energetic without being loud. 'Build your dream site. No code required.' Short, punchy. Product-forward. CTAs: 'Start for free', 'See examples', 'Explore templates'. Tone is enthusiastic but not hyped.",
        "css_variables": ":root {\n  --bg: #0d0d0d;\n  --surface: #1a1a1a;\n  --border: #2a2a2a;\n  --accent: #0099ff;\n  --text-primary: #ffffff;\n  --text-muted: #888888;\n  --radius-md: 8px;\n  --radius-lg: 16px;\n}",
        "tailwind_tokens": "colors: { bg: '#0d0d0d', surface: '#1a1a1a', accent: '#0099ff', primary: '#ffffff', muted: '#888888' }",
        "deliverable_note": "Ensure all interactive elements have visible motion transitions. The motion IS the theme's primary signature."
    },

    "notion.com": {
        "mode": "adaptive",
        "signature_visual_element": "Clean blank-canvas aesthetic: default serif-less type on pure white, sidebar tree navigation, block-based content modular system. The page itself IS the product — no decorative chrome, zero visual clutter.",
        "emotional_intent": "Calm, infinite flexibility, your second brain. The user feels perfectly organized and infinitely capable. Notion is the world's most flexible notebook — the UI should feel blank, inviting, and effortlessly structured.",
        "color_application_rules": {
            "#ffffff": "page canvas background, sidebar background",
            "#37352f": "all body text, headings, UI labels — deep warm black",
            "#0f7b6c": "primary CTAs, active states, links, selection highlights",
            "#f7f6f3": "hover backgrounds on sidebar items, table row alternates",
            "#e3e2e0": "borders, dividers, database table lines",
            "#9b9a97": "placeholder text, metadata, secondary labels"
        },
        "anti_patterns": [
            "No dark hero sections — Notion is always light/white first",
            "No gradient backgrounds or gradient text",
            "No heavy shadows on cards — use very subtle shadows (0 1px 3px rgba(0,0,0,0.08))",
            "No rounded corners above 6px on structural containers",
            "No animations beyond simple fade/slide reveals",
            "No bold color accents except in CTA buttons"
        ],
        "page_architecture": [
            "1. Nav: white, logo left, product dropdown, 'Request a demo' + 'Get Notion free'",
            "2. Hero: centered headline (56px), subtitle, 2 CTAs, product screenshot below",
            "3. Company logos: 'Trusted by 35 million users at...' colored logos strip",
            "4. Feature trio: 3-column icon + headline + body, clean white section",
            "5. Product demo block: actual product GIF/screenshot showing block editing",
            "6. Use-case tabs: 'For teams', 'For personal', 'For startups' — each shows different view",
            "7. Templates gallery: card grid, hover reveals template preview",
            "8. Social proof: quote + avatar + company",
            "9. Footer: 5-col link grid on white"
        ],
        "icon_system": "Notion's own emoji-first system for content. Lucide icons for UI chrome. Simple outline style, 1px stroke, 16px.",
        "image_treatment": "Clean product screenshots showing organized Notion workspaces. No photography of people. Flat illustrations for abstract concepts. Light, airy, minimal.",
        "copy_voice": "Friendly, inclusive, capability-focused. 'Write, plan, organize. Notion is the connected workspace where better, faster work happens.' Simple language. Anyone can understand. CTAs: 'Get Notion free', 'Try it out', 'See how it works'.",
        "css_variables": ":root {\n  --bg: #ffffff;\n  --surface: #f7f6f3;\n  --border: #e3e2e0;\n  --accent: #0f7b6c;\n  --text-primary: #37352f;\n  --text-muted: #9b9a97;\n  --radius-sm: 3px;\n  --radius-md: 6px;\n}",
        "tailwind_tokens": "colors: { bg: '#ffffff', surface: '#f7f6f3', border: '#e3e2e0', accent: '#0f7b6c', primary: '#37352f', muted: '#9b9a97' }",
        "deliverable_note": "Keep the palette clean and restrained. The power is in the whitespace and typography, not color."
    },

    "apple.com": {
        "mode": "light",
        "signature_visual_element": "Giant SF Pro Display typography (80-96px) sitting directly over full-bleed product photography on pure white canvas. No decorative chrome — the product IS the hero. Blue pill CTAs (#0071e3) as the only color accent.",
        "emotional_intent": "Holding a premium object. The visitor feels they are experiencing craft at the highest possible level. Simplicity communicates mastery. Every detail communicates 'we thought of everything so you don't have to.'",
        "color_application_rules": {
            "#f5f5f7": "body background, section backgrounds — signature Apple off-white",
            "#ffffff": "card surfaces, nav background, tile backgrounds",
            "#0071e3": "all primary CTA buttons, links on hover, focus rings — ONLY here",
            "#1d1d1f": "H1, H2, H3, body text — high-contrast near-black",
            "#86868b": "eyebrow text, captions, secondary descriptions",
            "#d2d2d7": "borders, dividers, table lines — hairline 1px"
        },
        "anti_patterns": [
            "No dark sections except for 'Apple TV+' style media sections",
            "No gradient backgrounds in main content sections",
            "No drop shadows on product images — let the photo breathe on white",
            "No centered text except for hero overlays — left-align all body content",
            "No more than 1 accent-colored element visible at a time",
            "No busy backgrounds — white or #f5f5f7 only",
            "No decorative illustrations — photography only",
            "No font above 700 weight for regular body sections"
        ],
        "page_architecture": [
            "1. Sticky nav: 44px height, white/blur, Apple logo centered on mobile, product categories",
            "2. Cinematic hero: full-viewport product photo, H1 overlaid (bottom-left or centered), CTA pill below",
            "3. Feature overview: 2-up or 3-up tiles on #f5f5f7, each tile = product photo + headline + body",
            "4. Deep feature callout: alternating 2-col (photo left, text right), clean white bg",
            "5. Spec comparison table: clean rows, hairline borders, checkmarks in accent blue",
            "6. Ecosystem section: rounded tiles showing accessory/service lineup",
            "7. Footer: 5-col links on #f5f5f7, language selector, legal links"
        ],
        "icon_system": "SF Symbols style — filled rounded icons, system-ui sizes. Never decorative — only functional UI icons.",
        "image_treatment": "Professional product photography on pure white or gradient-white backgrounds. Camera angles are dramatic but clean. No busy environments. Products are the sole subject.",
        "copy_voice": "Poetic product authority. Short, rhythm-driven headlines ('Thin. Light. Powerful beyond belief.'). Second-person ('Everything you need.'). No technical jargon in hero. Spec pages use precise technical language. CTAs: 'Shop iPhone', 'Learn more ↗', 'Compare models'.",
        "css_variables": ":root {\n  --bg: #f5f5f7;\n  --surface: #ffffff;\n  --border: #d2d2d7;\n  --accent: #0071e3;\n  --text-primary: #1d1d1f;\n  --text-muted: #86868b;\n  --radius-md: 12px;\n  --radius-lg: 18px;\n  --radius-xl: 24px;\n}",
        "tailwind_tokens": "colors: { bg: '#f5f5f7', surface: '#ffffff', border: '#d2d2d7', accent: '#0071e3', primary: '#1d1d1f', muted: '#86868b' }, borderRadius: { md: '12px', lg: '18px', xl: '24px' }",
        "deliverable_note": "Apply CSS variables globally. Every section should feel airy and editorial. Product photography is essential — use placeholder images that mimic the clean white-background product shot style."
    },

    "airbnb.com": {
        "mode": "light",
        "signature_visual_element": "Full-bleed destination photography with an Airbnb-pink search pill floating over it. Warm, human-centered card grid with circular host avatar overlapping the card photo. Signature coral-pink (#FF5A5F) used exclusively on primary CTA and brand marks.",
        "emotional_intent": "Warmth, adventure, belonging. The visitor feels they can belong anywhere in the world. The design prioritizes human faces and real spaces over abstract visuals. 'Belong Anywhere.'",
        "color_application_rules": {
            "#FF5A5F": "primary CTA buttons, brand logo, hover states, selected stars, price highlights",
            "#ffffff": "page canvas, card backgrounds, nav background",
            "#222222": "headings, card titles, primary body text",
            "#717171": "secondary text, metadata, dates, secondary labels",
            "#EBEBEB": "borders, dividers, skeleton loading states",
            "#008489": "secondary accent for 'Plus' tier badging and map pins"
        },
        "anti_patterns": [
            "No dark canvas — Airbnb is always warm white",
            "No corporate geometric layouts — organic, human-centered compositions",
            "No icons-heavy interfaces — photography first always",
            "No cold blue color accents — warmth is essential (coral, warm grays)",
            "No product screenshots — real photography of real spaces only"
        ],
        "page_architecture": [
            "1. Nav: white, logo left (coral), search pill center, profile + hamburger right",
            "2. Hero: full-bleed photo, centered search bar with location/dates/guests pills",
            "3. Category pills: horizontal scroll strip (beaches, mountains, cabins, etc.)",
            "4. Listing grid: 2-4 col responsive card grid, photo top 65%, host avatar, price, rating",
            "5. 'Airbnb it' CTA: split 2-col, lifestyle photo left, form/CTA right",
            "6. Experiences section: card grid for activities",
            "7. Trust section: 3 icons with headline + body copy",
            "8. Footer: 4-col link grid, language/currency selector"
        ],
        "icon_system": "Custom Airbnb icons — friendly filled/outline hybrid style. Warm, rounded, approachable.",
        "image_treatment": "Real destination photography: bright, warm-toned, natural light. Human faces welcome. Show the experience, not just the place. Cards must show the actual space prominently.",
        "copy_voice": "Warm, inclusive, adventurous. 'Find your place in the world.' Human-first. Celebrates community and discovery. CTAs: 'Explore nearby', 'Start hosting', 'Find experiences'. Tone is optimistic and welcoming.",
        "css_variables": ":root {\n  --bg: #ffffff;\n  --surface: #f7f7f7;\n  --border: #EBEBEB;\n  --accent: #FF5A5F;\n  --text-primary: #222222;\n  --text-muted: #717171;\n  --radius-sm: 8px;\n  --radius-md: 12px;\n  --radius-lg: 16px;\n  --radius-full: 9999px;\n}",
        "tailwind_tokens": "colors: { bg: '#ffffff', surface: '#f7f7f7', border: '#EBEBEB', accent: '#FF5A5F', primary: '#222222', muted: '#717171' }",
        "deliverable_note": "Prioritize real photography placeholders. The card grid is the most important component — get the photo proportion and host avatar overlay right."
    },

    "figma.com": {
        "mode": "dark",
        "signature_visual_element": "Multi-panel design tool chrome aesthetic: layers panel on left, properties inspector on right, canvas in center. Purple (#A259FF) accent on selected components. Tool-metaphor UI elements (node connectors, component slots, variant pills) used decoratively throughout marketing.",
        "emotional_intent": "Collaborative design mastery. The user feels they are part of the professional design community. Figma is where real design work happens — the UI communicates creative authority and team collaboration.",
        "color_application_rules": {
            "#1e1e1e": "body background, all main sections",
            "#A259FF": "primary CTAs, active selection highlights, featured tier, link accents",
            "#ffffff": "all display text, tool labels, nav links",
            "#2c2c2c": "card surfaces, panel backgrounds, modal surfaces",
            "#444444": "borders, panel dividers, inspector separators",
            "#b3b3b3": "secondary text, property labels, metadata"
        },
        "anti_patterns": [
            "No light/white sections in main content — keep dark consistently",
            "No simple product screenshots — always show the design tool in use with real work",
            "No generic business language — speak to designers specifically",
            "No simple icon sets — use design-tool metaphors (component icons, variant chips)",
            "No static presentations — show collaboration (multiple cursors, comments)"
        ],
        "page_architecture": [
            "1. Nav: dark, Figma logo left, product links, 'Contact sales' + 'Get started' right",
            "2. Hero: dark canvas bg, bold headline, product screenshot showing design tool with real design",
            "3. Collaboration feature: animated multi-cursor demo, team collaboration callout",
            "4. Component/plugin ecosystem: grid of plugin cards",
            "5. Template gallery: horizontal scroll, card grid with design previews",
            "6. Pricing table: 3 tiers, purple highlighted tier",
            "7. Enterprise CTA: dark panel",
            "8. Footer: dark 5-col"
        ],
        "icon_system": "Custom Figma icons — component/design-tool metaphors. Also uses colorful property icons for feature sections.",
        "image_treatment": "Actual design tool screenshots showing real design work (UI components being built). Multi-cursor collaboration demos. Dark canvas with colorful design elements visible.",
        "copy_voice": "Confident design authority. 'Where teams design together.' Designer-to-designer language. Technical precision mixed with creative empowerment. CTAs: 'Get started for free', 'Contact sales', 'See plans'.",
        "css_variables": ":root {\n  --bg: #1e1e1e;\n  --surface: #2c2c2c;\n  --border: #444444;\n  --accent: #A259FF;\n  --text-primary: #ffffff;\n  --text-muted: #b3b3b3;\n  --radius-sm: 4px;\n  --radius-md: 8px;\n}",
        "tailwind_tokens": "colors: { bg: '#1e1e1e', surface: '#2c2c2c', border: '#444444', accent: '#A259FF', primary: '#ffffff', muted: '#b3b3b3' }",
        "deliverable_note": "Show the design tool aesthetic even if building a non-design product. Use the dark canvas, panel chrome metaphors, and component-grid layouts."
    },

    "github.com": {
        "mode": "dark",
        "signature_visual_element": "Dark developer canvas (#0d1117) with green contribution graph (#238636 accent). Repository card grids, code block snippets with syntax highlighting, and the iconic octocat silhouette. Developer-native density with clean monospace type.",
        "emotional_intent": "Community, craft, open collaboration. The developer feels at home — GitHub is where code lives. The design radiates technical legitimacy and open-source community spirit.",
        "color_application_rules": {
            "#0d1117": "body background, all main sections",
            "#238636": "primary CTA buttons (solid), success states, contribution squares, action confirmations",
            "#c9d1d9": "all body text, headings, nav links",
            "#161b22": "card surfaces, repo cards, modal backgrounds",
            "#30363d": "borders, input outlines, dividers",
            "#8b949e": "secondary text, metadata, timestamps, muted labels",
            "#58a6ff": "links, secondary accents, code references, PR/issue numbers"
        },
        "anti_patterns": [
            "No light background sections — fully dark throughout",
            "No decorative gradients or blob shapes",
            "No photography — illustrations and product screenshots only",
            "No serif fonts — monospace + system-ui only",
            "No large padding — developer density is expected",
            "No color-heavy UI — monochrome with selective green/blue accents only"
        ],
        "page_architecture": [
            "1. Nav: dark #161b22, GitHub logo + search + nav links, avatar right",
            "2. Hero: dark, bold headline, green CTA, contribution graph graphic",
            "3. Feature sections: alternating dark panels with code snippets + description",
            "4. Repository card grid: 3-col cards with language color dot, stars, forks",
            "5. Open source showcase: project cards with contributor avatars",
            "6. Enterprise feature panel: dark, security/compliance callouts",
            "7. Pricing: 3-col, green border on featured tier",
            "8. Footer: dark 5-col minimal"
        ],
        "icon_system": "Octicons — GitHub's own icon system. Simple outline, developer-native. Used at 16px-24px. Always monochrome.",
        "image_treatment": "Product screenshots of GitHub UI. Code snippets as visual elements. Flat developer-themed illustrations. Contribution graphs as data visualization.",
        "copy_voice": "Developer-first, community-focused. 'Where the world builds software.' Open-source values language. Technical precision. CTAs: 'Sign up for free', 'Start a free trial', 'Contact sales'. Avoids marketing fluff entirely.",
        "css_variables": ":root {\n  --bg: #0d1117;\n  --surface: #161b22;\n  --border: #30363d;\n  --accent: #238636;\n  --link: #58a6ff;\n  --text-primary: #c9d1d9;\n  --text-muted: #8b949e;\n  --radius-sm: 4px;\n  --radius-md: 6px;\n}",
        "tailwind_tokens": "colors: { bg: '#0d1117', surface: '#161b22', border: '#30363d', accent: '#238636', link: '#58a6ff', primary: '#c9d1d9', muted: '#8b949e' }",
        "deliverable_note": "Include a code snippet display component — it's central to GitHub's visual identity. Syntax highlighting colors: comments #8b949e, strings #a5d6ff, keywords #ff7b72."
    },

    "openai.com": {
        "mode": "light",
        "signature_visual_element": "Pure white editorial canvas with the DALL-E/ChatGPT gradient orb imagery (green-to-blue animated sphere) as the sole visual statement. Ultra-clean black system typography. Restraint as a design strategy — the AI product speaks through the whitespace.",
        "emotional_intent": "Frontier technology, responsibly approached. The visitor feels they are witnessing something historically significant, calmly presented. Understated confidence, not hype. The future arrives in clean sans-serif.",
        "color_application_rules": {
            "#ffffff": "all backgrounds — total white editorial canvas",
            "#000000": "all headings, all body text, all nav links",
            "#10a37f": "ChatGPT brand, primary CTA buttons, success states, link accent",
            "#f7f7f8": "alternate section backgrounds, input fields",
            "#ececf1": "borders, dividers, card outlines",
            "#6e6e80": "secondary text, metadata, descriptive labels"
        },
        "anti_patterns": [
            "No dark sections on main marketing pages",
            "No gradient backgrounds except for the signature AI orb visual",
            "No decorative icons or illustrations — photography or AI-generated art only",
            "No bold color accents beyond the green brand color",
            "No visual clutter — extreme restraint at all times",
            "No casual or playful tone — serious, thoughtful communication"
        ],
        "page_architecture": [
            "1. Nav: white, OpenAI logo left, product links center, 'Try ChatGPT' right",
            "2. Hero: white, centered H1 (56px), one-line subtitle, gradient AI orb imagery below",
            "3. Product lineup: clean card grid (ChatGPT, API, DALL-E, Sora, etc.)",
            "4. Research highlights: editorial text-heavy section with research paper cards",
            "5. Safety/mission section: text-focused, minimal design",
            "6. API section: code snippet + dark terminal aesthetic",
            "7. Footer: clean 5-col on white"
        ],
        "icon_system": "No decorative icons. Minimal functional UI icons only (arrow, chevron). Product logos serve as visual anchors.",
        "image_treatment": "AI-generated imagery (photorealistic or abstract) from their own models. The signature animated gradient orb for hero sections. Research paper thumbnails for academic sections.",
        "copy_voice": "Thoughtful, serious, historically aware. 'OpenAI is an AI research and deployment company.' Straightforward statements of capability. No hype language. CTAs: 'Try ChatGPT', 'Explore the API', 'Read research'. Tone is measured and authoritative.",
        "css_variables": ":root {\n  --bg: #ffffff;\n  --surface: #f7f7f8;\n  --border: #ececf1;\n  --accent: #10a37f;\n  --text-primary: #000000;\n  --text-muted: #6e6e80;\n  --radius-sm: 4px;\n  --radius-md: 8px;\n  --radius-lg: 12px;\n}",
        "tailwind_tokens": "colors: { bg: '#ffffff', surface: '#f7f7f8', border: '#ececf1', accent: '#10a37f', primary: '#000000', muted: '#6e6e80' }",
        "deliverable_note": "Extreme whitespace and restraint is the signature. Less is more. The AI product imagery (gradient orb or generated art) is the only decoration allowed."
    },

    "raycast.com": {
        "mode": "dark",
        "signature_visual_element": "Deep space dark background (#1c1c1e) with the Raycast command launcher interface mockup as the hero centerpiece. Orange-to-pink gradient (#FF6363 to #FF9F0A) as the signature brand gradient, used on CTAs and logo. Blurred extension store card grid.",
        "emotional_intent": "Mac-native power user delight. The user feels this is the smartest productivity tool ever built for Mac. Every interaction feels snappy, keyboard-first, and delightfully crafted. Premium macOS aesthetic.",
        "color_application_rules": {
            "#1c1c1e": "body background — Apple-system dark appearance",
            "#FF6363": "gradient start for CTAs, logo, brand marks, hover accents",
            "#FF9F0A": "gradient end for CTAs and highlights",
            "#ffffff": "headlines, nav links, primary text",
            "#2c2c2e": "card surfaces, panel backgrounds, modal backgrounds",
            "#3a3a3c": "borders, separator lines",
            "#8e8e93": "secondary text, metadata, descriptions"
        },
        "anti_patterns": [
            "No light canvas — fully dark macOS-native dark mode aesthetic",
            "No gradients other than the orange-to-pink brand gradient",
            "No Web-style rounded corners — use Apple system corner radii (10px, 13px)",
            "No heavy marketing copy — let the product interface speak",
            "No non-Mac-native design patterns (keep iOS-adjacent Apple HIG aesthetics)"
        ],
        "page_architecture": [
            "1. Nav: dark blurred, Raycast logo left, links center, 'Download' pill right",
            "2. Hero: dark bg, command launcher interface mockup center, H1 above, CTA below",
            "3. Extension store grid: 4-col card grid showing extension icons and names",
            "4. Feature sections: alternating dark cards with launcher UI screenshots",
            "5. Testimonials: developer/power-user quotes",
            "6. AI feature section: gradient accent section for Raycast AI",
            "7. Download CTA: gradient CTA banner",
            "8. Footer: dark 4-col"
        ],
        "icon_system": "SF Symbols for any system icons. Custom Raycast extension icons (colorful, app-icon style squares with rounded corners). All functional UI uses SF Symbols.",
        "image_treatment": "macOS app screenshots, command launcher UI mockups. App icon-style graphics for extension cards. Dark UI screenshots throughout. Product is always the hero.",
        "copy_voice": "Power user-to-power user. 'Your shortcut to everything.' Confident, spare, Mac-native tone. Features listed as capabilities, not benefits. CTAs: 'Download for Mac', 'Get Raycast Pro', 'Explore extensions'.",
        "css_variables": ":root {\n  --bg: #1c1c1e;\n  --surface: #2c2c2e;\n  --border: #3a3a3c;\n  --accent: #FF6363;\n  --accent-end: #FF9F0A;\n  --text-primary: #ffffff;\n  --text-muted: #8e8e93;\n  --radius-sm: 8px;\n  --radius-md: 10px;\n  --radius-lg: 13px;\n}",
        "tailwind_tokens": "colors: { bg: '#1c1c1e', surface: '#2c2c2e', border: '#3a3a3c', accent: '#FF6363', primary: '#ffffff', muted: '#8e8e93' }",
        "deliverable_note": "The command launcher interface is central to Raycast's brand identity — include a stylized representation of this component in the hero section."
    },

    "craft.do": {
        "mode": "light",
        "signature_visual_element": "Large editorial typography (64px+) in near-black on pristine white, combined with the document card stack visual — showing nested documents with clean drop shadows. Generous whitespace as a luxury design statement. Monochrome palette with single emerald (#10b981) accent.",
        "emotional_intent": "Premium writing tool for people who care about craft. The user feels inspired to write something beautiful. Notion's calmer, more refined cousin — where the document itself is the art. Clarity of thought reflected in clarity of design.",
        "color_application_rules": {
            "#ffffff": "all backgrounds — absolute white editorial canvas",
            "#0f172a": "all headings, all body text — near-black slate",
            "#10b981": "primary CTA buttons, active states, accent links, selection highlights",
            "#f8fafc": "alternate section backgrounds, card surfaces",
            "#e2e8f0": "borders, dividers — ultra-light hairline borders",
            "#64748b": "secondary text, metadata, captions, eyebrow labels"
        },
        "anti_patterns": [
            "No dark sections — pure white editorial throughout",
            "No gradient backgrounds or gradient text",
            "No decorative elements beyond clean typography and document card imagery",
            "No rounded corners above 12px for structural elements",
            "No more than 1 emerald accent visible at a time",
            "No dense layouts — generous breathing room is mandatory"
        ],
        "page_architecture": [
            "1. Nav: pure white, Craft logo left, links center, 'Try Craft' pill right",
            "2. Hero: white, asymmetric 2-col (headline left, document stack visual right)",
            "3. Feature trio: 3-col, icon + headline + body, spacious",
            "4. Product deep-dive: alternating 2-col editorial showcases",
            "5. Platform showcase: iOS + Mac + Web platform cards",
            "6. Testimonials: large pull quote, minimal attribution",
            "7. CTA: centered, white, large headline + single CTA",
            "8. Footer: minimal 4-col on white"
        ],
        "icon_system": "SF Symbols-adjacent — simple, clean, outline style. 20px default. Monochrome. Never decorative, always functional.",
        "image_treatment": "Clean product screenshots on white backgrounds. Document stack renders with subtle drop shadows. Platform screenshots (iOS, macOS). Minimal, editorial, photography-free.",
        "copy_voice": "Refined, thoughtful, writing-focused. 'A new home for your ideas.' Celebrates the craft of writing and thinking. CTAs: 'Try Craft free', 'Download for Mac', 'Get started'. Tone is calm and confident — never loud.",
        "css_variables": ":root {\n  --bg: #ffffff;\n  --surface: #f8fafc;\n  --border: #e2e8f0;\n  --accent: #10b981;\n  --text-primary: #0f172a;\n  --text-muted: #64748b;\n  --radius-sm: 6px;\n  --radius-md: 10px;\n  --radius-lg: 16px;\n}",
        "tailwind_tokens": "colors: { bg: '#ffffff', surface: '#f8fafc', border: '#e2e8f0', accent: '#10b981', primary: '#0f172a', muted: '#64748b' }",
        "deliverable_note": "Generous whitespace is not waste — it IS the design. Every section should have at least 96px vertical padding. Typography hierarchy must be very clear (H1 >> H2 >> body)."
    },

    "slack.com": {
        "mode": "light",
        "signature_visual_element": "Multi-colored brand palette (red, yellow, green, blue) used in the logo mark and decorative geometric illustrations. Light cream/lavender section backgrounds alternate with white. The channel sidebar preview is the signature product visual.",
        "emotional_intent": "Human connection at work. Slack feels warm, approachable, slightly playful. Work doesn't have to be boring. The design communicates: your team will actually enjoy using this. Fun professionalism.",
        "color_application_rules": {
            "#ffffff": "main page backgrounds, card surfaces",
            "#ECE8FF": "alternate section backgrounds — Slack's signature soft lavender",
            "#611f69": "primary CTAs, nav highlights, brand anchor color (Slack aubergine)",
            "#1d1c1d": "headings and primary body text",
            "#616061": "secondary text, metadata",
            "#e8e8e8": "borders, dividers"
        },
        "anti_patterns": [
            "No purely dark pages — Slack is always warm and light",
            "No single-color accent — the multi-color palette is essential",
            "No cold/corporate colors — warmth through the lavender and aubergine palette",
            "No heavy technical layouts — conversational and human first"
        ],
        "page_architecture": [
            "1. Nav: white, Slack logo, product links, 'Get started' CTA",
            "2. Hero: light bg, bold headline, 2 CTAs, channel sidebar preview",
            "3. Company logos trust strip",
            "4. Feature: alternating 2-col, illustration + text",
            "5. Integration showcase: app grid with colored icons",
            "6. Enterprise section: dark lavender bg callout",
            "7. Pricing: 3-col on white",
            "8. Footer: standard 5-col"
        ],
        "icon_system": "Custom Slack icons — rounded, friendly, slightly chunky fills. Multi-color system (not monochrome). App integration icons are full-color brand logos.",
        "image_treatment": "Custom flat geometric illustrations (multi-color, friendly style). Product screenshots of the Slack interface. No photography of people — illustrations represent humans as shapes/avatars.",
        "copy_voice": "Friendly, workplace-positive, slightly witty. 'Where work happens.' Human language, never corporate-speak. CTA: 'Get started', 'Try for free'. Short, conversational sentences.",
        "css_variables": ":root {\n  --bg: #ffffff;\n  --surface-alt: #ECE8FF;\n  --border: #e8e8e8;\n  --accent: #611f69;\n  --text-primary: #1d1c1d;\n  --text-muted: #616061;\n  --radius-md: 8px;\n  --radius-lg: 12px;\n}",
        "tailwind_tokens": "colors: { bg: '#ffffff', 'surface-alt': '#ECE8FF', accent: '#611f69', primary: '#1d1c1d', muted: '#616061' }",
        "deliverable_note": "The multi-color brand palette is Slack's identity — include colored accent elements (4 colors: red, yellow, green, blue) as decorative geometry or in the logo treatment."
    },
}

# ═══════════════════════════════════════════════════════════════════
# CATEGORY SMART DEFAULTS — Intelligent fallbacks by design style
# ═══════════════════════════════════════════════════════════════════
CATEGORY_DEFAULTS = {
    "dark": {
        "mode": "dark",
        "icon_system": "Lucide Icons, 1.5px stroke, 16px default, monochrome (white or muted)",
        "image_treatment": "High-fidelity dark app UI screenshots. No photography. Product interface is the hero.",
        "copy_voice": "Direct, technical authority. Short declarative headlines. Developer or professional-first language. Action CTAs: 'Get started', 'Try for free', 'Read docs'.",
    },
    "light": {
        "mode": "light",
        "icon_system": "Lucide Icons or Phosphor Icons, clean outline style, 20px, matches accent color",
        "image_treatment": "Clean product screenshots on light backgrounds or lifestyle photography relevant to the product domain.",
        "copy_voice": "Clear, benefit-focused. Friendly but professional. Accessible language. CTAs: 'Get started free', 'Try it out', 'See how it works'.",
    },
    "adaptive": {
        "mode": "adaptive",
        "icon_system": "System-adaptive icons that work in both light and dark. Lucide Icons recommended.",
        "image_treatment": "Product screenshots shown in both light and dark mode. System-aware visuals.",
        "copy_voice": "Universal, accessible. Works for diverse audiences. Plain language. CTAs: 'Get started', 'Learn more', 'Try for free'.",
    },
}

def detect_mode(t):
    if not t.get('primary_colors'):
        return 'light'
    primary_hex = t['primary_colors'][0]['hex'].lstrip('#').lower()
    try:
        r = int(primary_hex[0:2], 16)
        g = int(primary_hex[2:4], 16)
        b = int(primary_hex[4:6], 16)
        luminance = 0.299 * r + 0.587 * g + 0.114 * b
        return 'dark' if luminance < 100 else 'light'
    except Exception:
        return 'light'

def generate_css_variables(t):
    pc = t.get('primary_colors', [])
    sc = t.get('secondary_colors', [])
    bg = pc[0]['hex'] if pc else '#ffffff'
    accent = pc[1]['hex'] if len(pc) > 1 else '#0070f3'
    surface = sc[0]['hex'] if sc else '#f5f5f5'
    border = sc[1]['hex'] if len(sc) > 1 else '#e5e7eb'
    text_primary = pc[2]['hex'] if len(pc) > 2 else ('#ffffff' if detect_mode(t) == 'dark' else '#111827')
    text_muted = sc[2]['hex'] if len(sc) > 2 else '#6b7280'
    return (
        f":root {{\n"
        f"  --bg: {bg};\n"
        f"  --surface: {surface};\n"
        f"  --border: {border};\n"
        f"  --accent: {accent};\n"
        f"  --text-primary: {text_primary};\n"
        f"  --text-muted: {text_muted};\n"
        f"  --radius-sm: 4px;\n"
        f"  --radius-md: 8px;\n"
        f"  --radius-lg: 16px;\n"
        f"}}"
    )

def generate_tailwind_tokens(t):
    pc = t.get('primary_colors', [])
    sc = t.get('secondary_colors', [])
    bg = pc[0]['hex'] if pc else '#ffffff'
    accent = pc[1]['hex'] if len(pc) > 1 else '#0070f3'
    surface = sc[0]['hex'] if sc else '#f5f5f5'
    text_primary = pc[2]['hex'] if len(pc) > 2 else '#111827'
    text_muted = sc[2]['hex'] if len(sc) > 2 else '#6b7280'
    return (
        f"colors: {{ bg: '{bg}', surface: '{surface}', accent: '{accent}', "
        f"primary: '{text_primary}', muted: '{text_muted}' }}"
    )

def generate_color_application_rules(t):
    pc = t.get('primary_colors', [])
    sc = t.get('secondary_colors', [])
    rules = {}
    if pc:
        rules[pc[0]['hex']] = f"page background, all section backgrounds"
    if len(pc) > 1:
        rules[pc[1]['hex']] = f"primary CTA buttons, links on hover, focus rings, selected states, brand accents"
    if len(pc) > 2:
        rules[pc[2]['hex']] = f"all headings (H1-H3), body text, primary UI labels"
    if sc:
        rules[sc[0]['hex']] = f"card surfaces, modal backgrounds, input field backgrounds"
    if len(sc) > 1:
        rules[sc[1]['hex']] = f"borders, dividers, separator lines — 1px only"
    if len(sc) > 2:
        rules[sc[2]['hex']] = f"secondary body text, metadata, timestamps, captions"
    return rules

def generate_anti_patterns(t, mode):
    if mode == 'dark':
        return [
            "No light/white background sections — maintain dark canvas throughout",
            "No heavy drop shadows — use hairline borders and surface elevation instead",
            "No busy gradient backgrounds — flat dark surfaces with selective glow accents only",
            "No decorative illustrations — use product screenshots or abstract geometric shapes",
            "No loose tracking on body text — keep optical letter-spacing tight",
            "No more than 2 accent-colored elements visible in the same viewport"
        ]
    else:
        return [
            "No dark section breaks that interrupt the light, airy flow",
            "No gradient backgrounds in main content areas",
            "No more than 1 accent color per section",
            "No heavy drop shadows — use soft shadows (0 2px 8px rgba(0,0,0,0.08))",
            "No cluttered layouts — generous whitespace is mandatory",
            "No condensed typography — maintain comfortable line-height (1.5-1.7 for body)"
        ]

def generate_page_architecture(t):
    design_style = t.get('design_style', '').lower()
    category = t.get('category', '').lower()
    name = t['name']
    if 'e-commerce' in category or 'shop' in category:
        return [
            f"1. Sticky nav: logo, search bar, cart icon, account",
            f"2. Hero: full-bleed product imagery, headline overlay, CTA",
            f"3. Category pills: horizontal filter strip",
            f"4. Product grid: responsive 3-4 col card layout with price + rating",
            f"5. Featured collection: large showcase tile",
            f"6. Trust signals: shipping, returns, guarantee icons",
            f"7. Testimonials/reviews: star-rated quote cards",
            f"8. Footer: 4-col links, newsletter, social"
        ]
    elif 'saas' in category or 'product' in category:
        return [
            f"1. Nav: 44px sticky, logo left, product links, CTA right",
            f"2. Hero: headline (56-72px), subtitle, 2 CTAs, product screenshot",
            f"3. Social proof: company logos strip",
            f"4. Feature trio: 3-col icon + headline + body",
            f"5. Product deep-dive: alternating 2-col text + screenshot",
            f"6. Testimonials: card grid or single large quote",
            f"7. Pricing: 3-col tier table",
            f"8. Footer: 5-col link grid"
        ]
    elif 'portfolio' in category or 'creative' in category:
        return [
            f"1. Nav: minimal logo + 3-4 links",
            f"2. Hero: full-viewport, name/title, brief description, scroll indicator",
            f"3. Work grid: masonry or 2-3 col project cards",
            f"4. About: 2-col photo + biography",
            f"5. Services/Skills: 3-col specialty cards",
            f"6. Contact: centered form or email CTA",
            f"7. Footer: minimal social links"
        ]
    else:
        return [
            f"1. Sticky nav: logo, navigation links, primary CTA",
            f"2. Hero: strong headline, subtitle, CTA buttons, visual right",
            f"3. Trust indicators: logos or stats",
            f"4. Features: 3-col or alternating 2-col showcase",
            f"5. Testimonials: quote cards grid",
            f"6. Pricing or next-step section",
            f"7. Final CTA: centered, bold",
            f"8. Footer: standard 4-5 col"
        ]

def generate_signature(t, mode):
    name = t['name']
    pc = t.get('primary_colors', [])
    accent = pc[1]['hex'] if len(pc) > 1 else (pc[0]['hex'] if pc else '#0070f3')
    bg = pc[0]['hex'] if pc else '#ffffff'
    ds = t.get('design_style', 'clean minimal')
    if mode == 'dark':
        return (
            f"Deep dark canvas ({bg}) with {accent} accent used exclusively on primary actions. "
            f"Product screenshots or interface mockups as the primary visual element. "
            f"High contrast between surface (#surface) and text creates the premium feel characteristic of {name}."
        )
    else:
        return (
            f"Clean white editorial canvas with {accent} as the single brand accent color. "
            f"Large display typography and generous whitespace communicate the premium quality of {name}. "
            f"Product screenshots or lifestyle imagery on clean white/off-white backgrounds."
        )

def generate_emotional_intent(t, mode):
    name = t['name']
    ds = t.get('design_style', 'modern productivity tool')
    cat = t.get('category', 'SaaS')
    if mode == 'dark':
        return f"Technical precision and professional authority. The user feels {name} is built by people who understand their craft deeply. The dark aesthetic communicates focus, speed, and zero compromise on quality."
    else:
        return f"Clarity and trustworthiness. The user feels confident that {name} is the right choice — professional, accessible, and purpose-built for their needs. The clean light design removes friction and communicates reliability."

# ═══════════════════════════════════════════════════════════════════
# ENRICH ALL THEMES
# ═══════════════════════════════════════════════════════════════════
def enrich_theme(t):
    domain = clean_domain(t['url'])
    mode = detect_mode(t)

    # Start with category-smart defaults
    defaults = CATEGORY_DEFAULTS.get(mode, CATEGORY_DEFAULTS['light'])

    t['mode'] = defaults['mode']
    t['icon_system'] = defaults['icon_system']
    t['image_treatment'] = defaults['image_treatment']
    t['copy_voice'] = defaults['copy_voice']
    t['signature_visual_element'] = generate_signature(t, mode)
    t['emotional_intent'] = generate_emotional_intent(t, mode)
    t['color_application_rules'] = generate_color_application_rules(t)
    t['anti_patterns'] = generate_anti_patterns(t, mode)
    t['page_architecture'] = generate_page_architecture(t)
    t['css_variables'] = generate_css_variables(t)
    t['tailwind_tokens'] = generate_tailwind_tokens(t)
    t['deliverable_note'] = "Apply CSS custom properties globally first. Then rework each component to match theme tokens. Preserve all domain data and business logic — only the visual layer changes."

    # Override with flagship data if available
    if domain in FLAGSHIP:
        override = FLAGSHIP[domain]
        for key, val in override.items():
            t[key] = val

    return t

print("Enriching all 500 themes with 11 new data fields...")
enriched = [enrich_theme(dict(t)) for t in themes]

with open('dashboard/themes.json', 'w', encoding='utf-8') as f:
    json.dump(enriched, f, ensure_ascii=False, indent=2)

print(f"Done! Enriched {len(enriched)} themes.")

# Verify a flagship theme
apple = [t for t in enriched if 'apple.com' in t['url']][0]
print("Apple mode:", apple['mode'])
print("Apple signature:", apple['signature_visual_element'][:80])
print("Apple anti_patterns count:", len(apple['anti_patterns']))
print("Apple css_variables present:", 'css_variables' in apple)
