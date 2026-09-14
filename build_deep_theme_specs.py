import json
import os
import re

with open('dashboard/themes.json', 'r', encoding='utf-8') as f:
    themes = json.load(f)

# Comprehensive deep specification profiles for all 39 design styles
STYLE_SPECS = {
    "Dark Precision Keyboard-First SaaS": {
        "mode": "dark",
        "typography": {
            "font_family_display": "'Inter', -apple-system, BlinkMacSystemFont, sans-serif",
            "font_family_body": "'Inter', -apple-system, BlinkMacSystemFont, sans-serif",
            "font_family_mono": "'JetBrains Mono', 'SF Mono', monospace",
            "scale": "Hero: 56-72px (-0.035em), H1: 36-40px, H2: 24-28px, Body: 14-15px, Mono: 12-13px",
            "weights": "400 Regular, 500 Medium, 600 SemiBold",
            "letter_spacing": "-0.03em for display headings, -0.01em for body text, 0 for mono"
        },
        "spacing": {
            "grid_system": "12-column responsive grid, max-width 1240px, 20px gutters",
            "padding_scale": "2px (hairline), 4px, 8px, 16px, 24px (cards), 48px, 96px (sections)",
            "whitespace_philosophy": "High information density balanced by structured syntax blocks and generous vertical margins."
        },
        "motion": {
            "transitions": "120ms-180ms cubic-bezier(0.16, 1, 0.3, 1) ease-out",
            "scroll_effects": "Staggered fade-up reveal on scroll with 40ms index delay, zero parallax blur.",
            "micro_interactions": "Instant 80ms active scale down (0.98), keyboard shortcut badge pulse, active row highlight."
        },
        "components": {
            "buttons": "6px rounded micro-pills with 1px border (#222326), solid primary accent with white text, or frosted translucent glass.",
            "cards": "Subtle 1px border (rgba(255,255,255,0.08)), obsidian dark surface (#151618), radial hover glow spotlight.",
            "forms": "Minimal dark inputs with 1px border (#28282c), focus ring in primary accent with 2px offset.",
            "navigation": "44px sticky frosted header (backdrop-blur-md, bg-black/60), minimal logo left, keyboard shortcuts right.",
            "hero_section": "Asymmetric hero with glowing radial gradient spotlight, high-impact headline, interactive app viewport mockup.",
            "footer": "Structured 4-5 column dark footer with system status indicator dot and keyboard shortcut badge."
        },
        "responsive": {
            "mobile_strategy": "Bottom sheet drawers, collapsible sidebars, single column stacked cards, 44px touch targets.",
            "desktop_strategy": "Full keyboard navigation (⌘K command palette), multi-pane issue columns, split view inspect."
        },
        "icon_system": "Lucide Icons, 1.5px stroke, 16px default, strictly monochrome",
        "image_treatment": "High-fidelity dark app UI screenshots and interactive canvas viewports only. No stock photography.",
        "copy_voice": "Declarative, technical authority, zero marketing fluff. 'The issue tracker built for speed.'",
        "anti_patterns": [
            "No colorful gradient text or playful blobs",
            "No large rounded corners (>8px on cards)",
            "No soft blurred shadows — use hairline borders and surface elevation only",
            "No centered full-width body text"
        ]
    },

    "Clean Minimal Enterprise Product": {
        "mode": "light",
        "typography": {
            "font_family_display": "'Geist Sans', 'Plus Jakarta Sans', 'Inter', sans-serif",
            "font_family_body": "'Geist Sans', 'Inter', sans-serif",
            "font_family_mono": "'Geist Mono', 'Fira Code', monospace",
            "scale": "Hero: 60-84px (-0.04em), H1: 40px, H2: 28px, Body: 15-16px",
            "weights": "400 Regular, 500 Medium, 600 SemiBold, 700 Bold",
            "letter_spacing": "-0.035em for headings, -0.01em for body text"
        },
        "spacing": {
            "grid_system": "12-column grid, max-width 1200px, 24px gutters",
            "padding_scale": "4px, 8px, 16px, 24px, 40px, 80px, 120px",
            "whitespace_philosophy": "Pristine white canvas with generous negative space spotlighting typography clarity."
        },
        "motion": {
            "transitions": "150ms ease-out",
            "scroll_effects": "Clean reveal transitions with crisp 100ms timing, zero blur lag.",
            "micro_interactions": "Subtle border color shift on hover (#e5e7eb to #111827), button ripple effect."
        },
        "components": {
            "buttons": "Pill buttons with 6-8px radius, solid black with white text or pure white with 1px border.",
            "cards": "Pure white cards with 1px hairline border (#e5e7eb), subtle shadow on hover (0 4px 20px rgba(0,0,0,0.05)).",
            "forms": "Crisp white inputs with light grey borders and blue or black focus rings.",
            "navigation": "Clean top bar with logo, dropdown menus, and CTA on right.",
            "hero_section": "Centered large bold statement, 2-line subtitle, primary & secondary CTA pills, framework/tech logos.",
            "footer": "Clean 5-column link directory with copyright and status indicator."
        },
        "responsive": {
            "mobile_strategy": "Clean slide-down mobile nav, single column feature cards, full-width buttons.",
            "desktop_strategy": "1200px container, multi-column grid, hover card previews."
        },
        "icon_system": "Geist Icons / Lucide Icons, 1.25px stroke, 16px-20px",
        "image_treatment": "Clean terminal mockups, component cards, and vector diagrams with crisp borders.",
        "copy_voice": "Precise, confident, developer/enterprise-ready. 'Develop. Preview. Ship.'",
        "anti_patterns": [
            "No messy shadows or multicolored backgrounds",
            "No rounded corners above 10px on structural cards",
            "No cluttered copy blocks"
        ]
    },

    "High-Density Productivity Workspace": {
        "mode": "light",
        "typography": {
            "font_family_display": "'SF Pro Display', -apple-system, BlinkMacSystemFont, 'Plus Jakarta Sans', sans-serif",
            "font_family_body": "'SF Pro Text', -apple-system, BlinkMacSystemFont, sans-serif",
            "font_family_mono": "'SF Mono', 'JetBrains Mono', monospace",
            "scale": "Hero: 64-96px (-0.035em), H1: 44px, H2: 32px, Body: 17px, Caption: 13px",
            "weights": "400 Regular, 500 Medium, 600 SemiBold, 700 Bold",
            "letter_spacing": "-0.03em display, -0.015em body"
        },
        "spacing": {
            "grid_system": "12-column grid, max-width 1024px/1280px, 24px gutters",
            "padding_scale": "4px, 8px, 16px, 24px, 48px, 96px, 140px",
            "whitespace_philosophy": "Museum-grade expansive negative space where product photography commands attention."
        },
        "motion": {
            "transitions": "200ms-300ms cubic-bezier(0.25, 0.1, 0.25, 1) smooth Apple physics",
            "scroll_effects": "Smooth scroll scrubbing, sticky device frames with video playback synchronization.",
            "micro_interactions": "Smooth 1.02x scale zoom on hover, buttery pill button color transitions."
        },
        "components": {
            "buttons": "Fully rounded pill buttons (`rounded-full`), solid royal blue (#0071e3) with white text, or clean text links with chevron.",
            "cards": "Large rounded bento tiles (24px-30px radius), subtle 1px border or soft drop shadow.",
            "forms": "Rounded floating pill inputs with frosted glass backdrop blur.",
            "navigation": "44px sticky frosted navbar (`backdrop-blur-xl bg-white/80 border-b border-black/5`), centered logo, clean minimal links.",
            "hero_section": "Cinematic full-bleed product hero with giant headline, elegant subtitle, and dual pill CTAs.",
            "footer": "Structured 5-column directory on off-white (#f5f5f7) with legal terms and language selector."
        },
        "responsive": {
            "mobile_strategy": "Full-bleed cards, horizontal snap carousels, sticky bottom CTAs, centered logo header.",
            "desktop_strategy": "Expansive 1024px reading container, bento grid showcases, alternating feature rows."
        },
        "icon_system": "SF Symbols style rounded icons, 18px-24px",
        "image_treatment": "Studio-lit hardware and product photography on pure white or off-white studio backdrops.",
        "copy_voice": "Editorial, poetic, product-first. 'Thin. Light. Powerful beyond belief.'",
        "anti_patterns": [
            "No dark backgrounds for main content (off-white #f5f5f7 canvas)",
            "No aggressive drop shadows or saturated gradients on cards",
            "No square buttons — always pill rounded"
        ]
    },

    "Dark Opulent Luxury Maison": {
        "mode": "dark",
        "typography": {
            "font_family_display": "'Canela', 'Cinzel', 'Playfair Display', serif",
            "font_family_body": "'Italiana', 'Inter', -apple-system, sans-serif",
            "font_family_mono": "'Courier New', monospace",
            "scale": "Hero: 64-100px (0.05em letter spacing), H1: 48px, H2: 32px, Body: 15px",
            "weights": "300 Light, 400 Regular, 600 SemiBold",
            "letter_spacing": "0.08em for uppercase display headings, 0.02em for body text"
        },
        "spacing": {
            "grid_system": "8-column or 12-column editorial grid, max-width 1440px, 32px gutters",
            "padding_scale": "8px, 16px, 32px, 64px, 128px, 180px",
            "whitespace_philosophy": "Extravagant, atmospheric negative space communicating exclusivity and luxury."
        },
        "motion": {
            "transitions": "500ms-700ms cubic-bezier(0.19, 1, 0.22, 1) slow luxury ease",
            "scroll_effects": "Parallax image reveals, slow zoom-in on hover, curtain-style page transitions.",
            "micro_interactions": "Delicate underline expansion from center, golden shimmer border on hover."
        },
        "components": {
            "buttons": "Square or subtly rounded (2px) button with gold/white hairline border, uppercase tracked text.",
            "cards": "Border-less photo-dominant cards with floating gold typography and subtle vignette.",
            "forms": "Underline-only inputs with floating serif labels.",
            "navigation": "Ultra-minimal transparent navbar with centered luxury monogram and tracked links.",
            "hero_section": "Full-bleed editorial campaign video/photography with slow vertical title reveal.",
            "footer": "Monochrome dark footer with boutique locator, newsletter sign-up, and heritage mark."
        },
        "responsive": {
            "mobile_strategy": "Full-screen vertical swipe lookbooks, minimal hamburger menu, sticky inquiry pill.",
            "desktop_strategy": "Asymmetric editorial spreads, oversized imagery, mouse-follow cursor spotlight."
        },
        "icon_system": "Custom hairline icons, 1px stroke, gold/white",
        "image_treatment": "High-fashion editorial photography, high-contrast monochrome and warm film grain.",
        "copy_voice": "Haute, understated, poetic. 'A heritage of timeless craftsmanship.'",
        "anti_patterns": [
            "No bright neon colors or bouncy animations",
            "No dense tables or technical SaaS badges",
            "No pill buttons"
        ]
    },

    "Terminal-Centric Dark DevTools": {
        "mode": "dark",
        "typography": {
            "font_family_display": "'JetBrains Mono', 'Fira Code', monospace",
            "font_family_body": "'Inter', -apple-system, sans-serif",
            "font_family_mono": "'JetBrains Mono', 'Courier New', monospace",
            "scale": "Hero: 48-64px (-0.02em), H1: 36px, H2: 24px, Body: 14px, Code: 13px",
            "weights": "400 Regular, 500 Medium, 700 Bold",
            "letter_spacing": "-0.01em display, 0 for code"
        },
        "spacing": {
            "grid_system": "12-column grid, max-width 1200px, 16px gutters",
            "padding_scale": "4px, 8px, 12px, 16px, 24px, 48px, 80px",
            "whitespace_philosophy": "Command-line density with structured code blocks and ASCII art accents."
        },
        "motion": {
            "transitions": "100ms-150ms linear or fast ease-out",
            "scroll_effects": "Terminal line-by-line typing simulation, instant tabs.",
            "micro_interactions": "Cursor blink animation, green terminal glow on hover, copy-command click feedback."
        },
        "components": {
            "buttons": "Sharp 4px rectangular buttons with terminal prefix `$ npm i` and click-to-copy icon.",
            "cards": "Terminal window cards with MacOS traffic light dots (red, yellow, green) and tab headers.",
            "forms": "Dark terminal input with green `>` prompt indicator.",
            "navigation": "Dark header with branch selector, CLI version badge, and GitHub star counter.",
            "hero_section": "Split hero: left command-line value prop, right live interactive terminal emulator.",
            "footer": "Terminal status row: `● All systems operational - v4.18.2`"
        },
        "responsive": {
            "mobile_strategy": "Horizontal scroll code blocks, collapsible command drawer, tap-to-copy buttons.",
            "desktop_strategy": "Interactive multi-tab terminal, split view documentation, keyboard shortcut tooltips."
        },
        "icon_system": "Octicons & Devicons, 16px crisp monochrome",
        "image_treatment": "Interactive terminal sandboxes and ASCII architecture diagrams. No stock photos.",
        "copy_voice": "Direct, technical, engineer-to-engineer. 'Postgres in the cloud with instant replication.'",
        "anti_patterns": [
            "No decorative marketing illustrations",
            "No rounded pill buttons (>4px)",
            "No light mode defaults"
        ]
    },

    "Modern Institutional FinTech": {
        "mode": "light",
        "typography": {
            "font_family_display": "'Söhne', 'Plus Jakarta Sans', 'Inter', sans-serif",
            "font_family_body": "'Inter', -apple-system, sans-serif",
            "font_family_mono": "'JetBrains Mono', monospace",
            "scale": "Hero: 56-80px (-0.03em), H1: 40px, H2: 28px, Body: 16px, Metric: 48px",
            "weights": "400 Regular, 500 Medium, 600 SemiBold, 700 Bold",
            "letter_spacing": "-0.025em for headings, -0.01em for body"
        },
        "spacing": {
            "grid_system": "12-column grid, max-width 1280px, 24px gutters",
            "padding_scale": "4px, 8px, 16px, 24px, 48px, 96px, 128px",
            "whitespace_philosophy": "Institutional clarity, structured financial ledger grids, and prominent metric callouts."
        },
        "motion": {
            "transitions": "200ms cubic-bezier(0.16, 1, 0.3, 1)",
            "scroll_effects": "Animated metric counters counting up from 0 on viewport entry.",
            "micro_interactions": "Card elevate 4px with subtle shadow on hover, currency tab switch."
        },
        "components": {
            "buttons": "8px rounded rectangular buttons with solid navy/emerald accent, crisp typography.",
            "cards": "Structured cards with 1px border (#e2e8f0), header badge, and clean numerical data tables.",
            "forms": "Financial input fields with currency symbol prefix, real-time validation checkmarks.",
            "navigation": "Clean institutional navbar with product mega-menu, compliance badge, and 'Sign In'.",
            "hero_section": "Bold financial headline, dual CTAs, live transaction card mockup with security badges.",
            "footer": "Comprehensive institutional footer with regulatory disclosures, FDIC notices, and security seals."
        },
        "responsive": {
            "mobile_strategy": "Mobile banking drawer, bottom tab bar for key actions, condensed financial summaries.",
            "desktop_strategy": "Multi-pane dashboard previews, split-screen ledger views, live rate tickers."
        },
        "icon_system": "Lucide / Phosphor Icons, 1.5px stroke, clean corporate styling",
        "image_treatment": "High-fidelity titanium card mockups, clean charts, and enterprise office photography.",
        "copy_voice": "Authoritative, trustworthy, modern financial language. 'Global payments built for modern business.'",
        "anti_patterns": [
            "No cartoon illustrations",
            "No dark hacker terminal aesthetics",
            "No ambiguous pricing or hidden fee language"
        ]
    }
}

# Generic generator for other design styles
def generate_style_spec(style_name, mode):
    is_dark = (mode == "dark")
    
    if "Creative" in style_name or "Studio" in style_name or "Avant-Garde" in style_name or "Brutalist" in style_name:
        return {
            "mode": mode,
            "typography": {
                "font_family_display": "'Syne', 'Monument Extended', 'Cabinet Grotesk', sans-serif",
                "font_family_body": "'Inter', -apple-system, sans-serif",
                "font_family_mono": "'Space Mono', monospace",
                "scale": "Hero: 64-110px (-0.04em), H1: 48px, H2: 32px, Body: 16px",
                "weights": "500 Medium, 700 Bold, 900 Black",
                "letter_spacing": "-0.04em for giant headlines, 0.05em for uppercase pills"
            },
            "spacing": {
                "grid_system": "12-column asymmetric broken grid, max-width 1400px",
                "padding_scale": "8px, 16px, 32px, 64px, 120px, 160px",
                "whitespace_philosophy": "Bold contrasting whitespace paired with oversized typography and overlapping visual modules."
            },
            "motion": {
                "transitions": "300ms cubic-bezier(0.2, 0, 0, 1) magnetic easing",
                "scroll_effects": "Kinetic typography marquee, smooth locomotive scroll, distorted image shaders on hover.",
                "micro_interactions": "Magnetic cursor attractor, inverted text color mask on hover."
            },
            "components": {
                "buttons": "Chunky pill or brutalist bordered rectangle with magnetic hover physics.",
                "cards": "Asymmetric bento cards with bold hairline borders and high-contrast typography.",
                "forms": "Large typography inputs with custom stylized focus underlines.",
                "navigation": "Floating minimalist pill navbar with animated hamburger overlay.",
                "hero_section": "Giant kinetic headline, video reel viewport, animated badge stamp.",
                "footer": "Massive display typography footer with 'Let's Work Together' CTA."
            },
            "responsive": {
                "mobile_strategy": "Vertical card stack, full-screen touch menu, smooth touch dragging.",
                "desktop_strategy": "Horizontal scroll portfolios, custom cursor trail, WebGL canvas."
            },
            "icon_system": "Custom geometric SVG icons, 2px stroke",
            "image_treatment": "High-concept studio photography, experimental 3D renders, video showreels.",
            "copy_voice": "Bold, avant-garde, provocative. 'We craft digital experiences that defy convention.'",
            "anti_patterns": ["No generic SaaS templates", "No boring standard grids", "No flat boring text"]
        }
    elif "AI" in style_name or "Neural" in style_name or "Cybernetic" in style_name:
        return {
            "mode": "dark",
            "typography": {
                "font_family_display": "'Plus Jakarta Sans', 'Inter', sans-serif",
                "font_family_body": "'Inter', sans-serif",
                "font_family_mono": "'JetBrains Mono', monospace",
                "scale": "Hero: 56-80px (-0.03em), H1: 40px, H2: 28px, Body: 15px, Prompt: 14px",
                "weights": "400 Regular, 500 Medium, 600 SemiBold, 700 Bold",
                "letter_spacing": "-0.03em for headlines, -0.01em for body"
            },
            "spacing": {
                "grid_system": "12-column grid, max-width 1240px, 24px gutters",
                "padding_scale": "4px, 8px, 16px, 24px, 48px, 96px",
                "whitespace_philosophy": "Atmospheric cosmic dark canvas with glowing radial neon spotlights."
            },
            "motion": {
                "transitions": "200ms cubic-bezier(0.16, 1, 0.3, 1)",
                "scroll_effects": "Glowing orb background pulse, particle mesh floating on scroll.",
                "micro_interactions": "Multicolor border shimmer, prompt input focus neon glow."
            },
            "components": {
                "buttons": "Pill buttons with iridescent gradient border or glowing primary accent.",
                "cards": "Dark translucent glass cards (`backdrop-blur-lg bg-white/5 border border-white/10`).",
                "forms": "Multi-line AI prompt bar with token counter, model selector, and run button.",
                "navigation": "Frosted glass floating header with model status and token usage meter.",
                "hero_section": "Glowing neural orb visual, prompt-first interaction bar, generated art showcase.",
                "footer": "Dark 4-column footer with API status, documentation links, and Discord community badge."
            },
            "responsive": {
                "mobile_strategy": "Bottom-docked prompt input, single-column generation feed, touch pinch-to-zoom.",
                "desktop_strategy": "Split canvas with prompt parameters on left, generation canvas on right."
            },
            "icon_system": "Lucide Icons, 1.5px stroke, colored neon accents",
            "image_treatment": "High-fidelity AI generated imagery, diffusion model outputs, neural mesh shaders.",
            "copy_voice": "Futuristic, capability-focused, visionary. 'Generative intelligence at the speed of thought.'",
            "anti_patterns": ["No pure white corporate backgrounds", "No low-res pixelated assets", "No clunky forms"]
        }
    else:
        # Balanced high-craft fallback
        return {
            "mode": mode,
            "typography": {
                "font_family_display": "'Plus Jakarta Sans', 'Inter', -apple-system, sans-serif",
                "font_family_body": "'Inter', -apple-system, sans-serif",
                "font_family_mono": "'JetBrains Mono', monospace",
                "scale": "Hero: 56-72px (-0.03em), H1: 36-40px, H2: 24-28px, Body: 15-16px",
                "weights": "400 Regular, 500 Medium, 600 SemiBold, 700 Bold",
                "letter_spacing": "-0.025em display, -0.01em body"
            },
            "spacing": {
                "grid_system": "12-column responsive grid, max-width 1240px, 24px gutters",
                "padding_scale": "4px, 8px, 16px, 24px, 48px, 96px",
                "whitespace_philosophy": "Balanced, generous vertical rhythm spotlighting structured visual hierarchy."
            },
            "motion": {
                "transitions": "180ms ease-out",
                "scroll_effects": "Staggered reveal on scroll, smooth parallax card depth.",
                "micro_interactions": "Subtle card translateY(-2px), smooth button active scale down."
            },
            "components": {
                "buttons": "8px rounded pills with solid accent or 1px hairline border.",
                "cards": "Structured cards with 1px border (rgba(255,255,255,0.08) or #e5e7eb) and subtle hover glow.",
                "forms": "Clean inputs with 1px border, focus ring in primary accent.",
                "navigation": "Sticky frosted pill header with minimal logo and action CTA.",
                "hero_section": "Asymmetric hero with high-impact headline, subtitle, and interactive mockup.",
                "footer": "Structured 4-5 column footer with system status and social links."
            },
            "responsive": {
                "mobile_strategy": "Bottom sheet drawers, collapsible sidebars, single column stacked cards.",
                "desktop_strategy": "Multi-pane grid layout, 1240px max-width container."
            },
            "icon_system": "Lucide Icons, 1.5px stroke",
            "image_treatment": "High-craft product screenshots and crisp vector mockups.",
            "copy_voice": "Clear, professional, benefit-focused. Short punchy headlines.",
            "anti_patterns": ["No inconsistent border radii", "No un-styled raw HTML inputs", "No generic templates"]
        }

print("Updating all 500 themes with deep typography, motion, spacing, and component specs...")

count = 0
for t in themes:
    ds = t.get('design_style', '')
    mode = t.get('mode', 'light')
    
    if ds in STYLE_SPECS:
        spec = STYLE_SPECS[ds]
    else:
        spec = generate_style_spec(ds, mode)
    
    # Inject deep typography, motion, spacing, components, responsive specs
    t['typography'] = spec['typography']
    t['spacing'] = spec['spacing']
    t['motion'] = spec['motion']
    t['components'] = spec['components']
    t['responsive'] = spec['responsive']
    t['icon_system'] = spec['icon_system']
    t['image_treatment'] = spec['image_treatment']
    if 'anti_patterns' in spec and not t.get('anti_patterns'):
        t['anti_patterns'] = spec['anti_patterns']
    
    count += 1

with open('dashboard/themes.json', 'w', encoding='utf-8') as f:
    json.dump(themes, f, ensure_ascii=False, indent=2)

print(f"Updated all {count} themes in themes.json successfully!")
