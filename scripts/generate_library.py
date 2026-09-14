# -*- coding: utf-8 -*-
import csv
import json
import os
import re

# Comprehensive theme intelligence builder

ARCHETYPES = {
    "SaaS / Product": {
        "styles": ["Dark Precision Keyboard-First SaaS", "Clean Minimal Enterprise Product", "High-Density Productivity Workspace", "Vibrant Multi-Layered Product Hub"],
        "primary_palettes": [
            [{"hex": "#08090a", "role": "Obsidian Dark Canvas"}, {"hex": "#5e6ad2", "role": "Brand Indigo Accent"}, {"hex": "#f7f8f8", "role": "Primary Text"}],
            [{"hex": "#ffffff", "role": "Light Clean Canvas"}, {"hex": "#0070f3", "role": "Geist Blue Accent"}, {"hex": "#111827", "role": "Deep Charcoal Text"}],
            [{"hex": "#0f172a", "role": "Slate Dark Canvas"}, {"hex": "#10b981", "role": "Emerald Accent"}, {"hex": "#ffffff", "role": "Headline Text"}]
        ],
        "secondary_palettes": [
            [{"hex": "#151618", "role": "Card Surface"}, {"hex": "#222326", "role": "Subtle Border"}, {"hex": "#8a8f98", "role": "Muted Secondary Text"}],
            [{"hex": "#f9fafb", "role": "Card Surface Light"}, {"hex": "#e5e7eb", "role": "Border Light"}, {"hex": "#6b7280", "role": "Secondary Text"}]
        ],
        "display_font": "Inter, system-ui, -apple-system, sans-serif",
        "body_font": "Inter, system-ui, sans-serif",
        "mono_font": "'JetBrains Mono', 'Fira Code', monospace",
        "scale": "Hero: 56-72px (-0.03em), H1: 36-40px, H2: 24-28px, Body: 15-16px, Caption: 13px",
        "weights": "400 Regular, 500 Medium, 600 SemiBold",
        "letter_spacing": "-0.025em for display headings, -0.01em for body text",
        "grid_system": "12-column responsive grid with 24px gutters, max-width 1240px",
        "padding_scale": "4px (micro), 8px, 16px, 24px (card), 48px (section), 96px (hero)",
        "whitespace_philosophy": "Generous vertical section breathing room paired with dense, high-efficiency component modules.",
        "buttons": "Subtle rounded 6-8px pills, solid primary accent with white text, or frosted translucent glass with 1px border (#222326).",
        "cards": "Subtle 1px border (rgba(255,255,255,0.08)), dark surface, radial hover glow spotlight, no visual clutter.",
        "forms": "Minimal dark inputs with 1px border (#28282c), focus ring in primary accent with 2px offset.",
        "navigation": "Sticky frosted pill header (backdrop-blur-md, bg-black/60), minimal logo left, keyboard shortcuts and action CTA right.",
        "hero_section": "Asymmetric hero with glowing radial gradient spotlight, high-impact headline, interactive app viewport mockup.",
        "footer": "Structured 4-5 column dark footer with system status indicator dot and keyboard shortcut badge.",
        "transitions": "150ms-200ms cubic-bezier(0.16, 1, 0.3, 1) ease-out",
        "scroll_effects": "Staggered reveal on view, subtle parallax on device frames, micro-glows on cursor proximity.",
        "micro_interactions": "Instant keyboard feedback, active row highlights, smooth modal sheets.",
        "mobile_strategy": "Bottom sheet modals, collapsible sidebars, single column stacked cards, touch-optimized tap targets.",
        "desktop_strategy": "Full keyboard navigation (K-bar/command palette), multi-pane issue columns, split view inspect.",
        "dna": "Large typography, generous whitespace, monochrome palette, subtle borders, restrained motion, asymmetric hero composition and strong product-focused visual hierarchy.",
        "principles": "Built to communicate speed, craft, and keyboard-first productivity by removing clutter and focusing on high contrast, micro-details, and crisp dark backgrounds.",
        "best_use_cases": ["Developer tools", "Issue trackers", "Productivity suites", "High-craft B2B SaaS", "Command bar tools"],
        "things_to_reuse": ["1px glowing border cards", "Keyboard shortcut UI badges", "Obsidian color system", "Radial hero glow spotlight"],
        "things_not_to_copy": ["Proprietary application icons", "Trademarked workflow labels"],
        "notes": "Use Tailwind bg-[#08090a], border-white/10, hover:border-white/20, font-inter with -tracking-[0.02em] and lucide-react icons."
    },
    "AI": {
        "styles": ["Dark Cosmic AI Interface", "Minimalist Prompt-First Canvas", "Glow-Infused Neural Studio", "Editorial AI Research Hub"],
        "primary_palettes": [
            [{"hex": "#050505", "role": "Deep Void Canvas"}, {"hex": "#a855f7", "role": "Neural Purple Accent"}, {"hex": "#ffffff", "role": "Bright Text"}],
            [{"hex": "#0a0a0c", "role": "Obsidian Hub"}, {"hex": "#06b6d4", "role": "Cyan Plasma Glow"}, {"hex": "#f4f4f5", "role": "Main Heading"}],
            [{"hex": "#121113", "role": "Charcoal Canvas"}, {"hex": "#f59e0b", "role": "Warm Amber Intelligence"}, {"hex": "#fafafa", "role": "Text"}]
        ],
        "secondary_palettes": [
            [{"hex": "#121216", "role": "Container Surface"}, {"hex": "#27272a", "role": "Luminescent Border"}, {"hex": "#a1a1aa", "role": "Subtext"}],
            [{"hex": "#18181b", "role": "Card Surface"}, {"hex": "#3f3f46", "role": "Border"}, {"hex": "#71717a", "role": "Muted"}]
        ],
        "display_font": "'Plus Jakarta Sans', 'Inter', sans-serif",
        "body_font": "Inter, sans-serif",
        "mono_font": "'Space Mono', 'JetBrains Mono', monospace",
        "scale": "Hero: 56-80px, H1: 40px, H2: 28px, Body: 16px, Prompt: 14px",
        "weights": "300 Light, 400 Regular, 600 SemiBold, 700 Bold",
        "letter_spacing": "-0.03em for display headings, +0.05em for mono metadata",
        "grid_system": "Fluid container grid with dynamic neon halo glow focal points",
        "padding_scale": "8px, 16px, 32px, 64px, 120px",
        "whitespace_philosophy": "Expansive atmospheric canvas allowing interactive AI output canvases to dominate.",
        "buttons": "Luminescent gradient border pills, iridescent glow on hover, shimmering particles.",
        "cards": "Dark obsidian glass cards with subtle multi-color gradient border highlights.",
        "forms": "Centerpiece omni-prompt search bar with microphone, model selector pill, and send icon.",
        "navigation": "Floating minimalist pill with glassmorphism and model indicator badge.",
        "hero_section": "Full-bleed interactive AI prompt sandbox, animated neural particles, generative canvas preview.",
        "footer": "Minimalist single-line footer with API latency indicator and status dot.",
        "transitions": "Fluid spring animations (300ms cubic-bezier(0.2, 0.8, 0.2, 1))",
        "scroll_effects": "Particle trail shifts, gradient halo tracking cursor, typing effect simulations.",
        "micro_interactions": "Pulsing inference status rings, waveform audio visualizers, token generation stream.",
        "mobile_strategy": "Bottom-pinned chat prompt bar, swipeable generation cards, collapsible prompt settings.",
        "desktop_strategy": "Split-view side-by-side prompt and output canvas, canvas zoom and pan controls.",
        "dna": "Dark void canvas, iridescent neon glow accents, prompt-first conversational UI, and live generative canvas modules.",
        "principles": "Engineered to evoke machine intelligence, boundless creativity, and real-time generative wonder.",
        "best_use_cases": ["Generative AI tools", "LLM chat interfaces", "AI image/audio studios", "Model playgrounds"],
        "things_to_reuse": ["Omni-prompt bar design", "Neon gradient glow borders", "Token streaming text animation", "Model status pill"],
        "things_not_to_copy": ["Proprietary LLM brand assets", "Exact trademarked prompt templates"],
        "notes": "Use Tailwind bg-black, radial gradient glows (blur-3xl bg-purple-500/10), and glassmorphism."
    },
    "Developer / Infrastructure": {
        "styles": ["Terminal-Centric Dark DevTools", "Isometric Architectural Infrastructure", "Monospace Minimalist CLI Hub"],
        "primary_palettes": [
            [{"hex": "#0b0f19", "role": "Deep Console Dark"}, {"hex": "#22c55e", "role": "Terminal Green Accent"}, {"hex": "#e2e8f0", "role": "Primary Text"}],
            [{"hex": "#030712", "role": "Void Infrastructure"}, {"hex": "#38bdf8", "role": "Sky Blue Accent"}, {"hex": "#f8fafc", "role": "Header Text"}]
        ],
        "secondary_palettes": [
            [{"hex": "#111827", "role": "Terminal Block Surface"}, {"hex": "#1f2937", "role": "Code Border"}, {"hex": "#94a3b8", "role": "Comment Muted Text"}]
        ],
        "display_font": "Inter, -apple-system, sans-serif",
        "body_font": "Inter, sans-serif",
        "mono_font": "'JetBrains Mono', 'Fira Code', monospace",
        "scale": "Hero: 52px, H1: 36px, Code Header: 14px, Code Snippet: 13px",
        "weights": "400 Regular, 500 Medium, 600 SemiBold",
        "letter_spacing": "-0.02em headings, strict monospace tabular numbers",
        "grid_system": "Cartesian coordinate grid with hairline dividers and code line-number alignments",
        "padding_scale": "4px, 8px, 16px, 24px, 48px",
        "whitespace_philosophy": "High information density balanced by structured syntax blocks.",
        "buttons": "Terminal-style command buttons with $ prefix and copy feedback icon.",
        "cards": "Code window cards with macOS window dots, syntax highlighting, and copy button.",
        "forms": "YAML / JSON config editors, CLI flag selectors, latency slider bars.",
        "navigation": "Docs-first navigation with version selector, search hotkey (CMD+K), API status indicator.",
        "hero_section": "Split view with developer headline left and interactive live code terminal right.",
        "footer": "Detailed developer ecosystem links, SDK documentation matrix, uptime badge.",
        "transitions": "Instant 100ms-150ms transitions for snappy developer ergonomics",
        "scroll_effects": "Terminal output stream on scroll, packet flow animations.",
        "micro_interactions": "One-click copy code snippet feedback, command bar keyboard navigation.",
        "mobile_strategy": "Horizontal scrollable code blocks, condensed tree navigation, touch copy action.",
        "desktop_strategy": "Three-column docs layout (sidebar, content, on-this-page TOC) and multi-tab terminal.",
        "dna": "Terminal windows, syntax highlighting, monospace metadata, hairline borders, and live developer CLI workflows.",
        "principles": "Built for instant technical comprehension, zero latency, and engineering credibility.",
        "best_use_cases": ["Cloud infrastructure", "Databases", "APIs & SDKs", "Developer platforms", "CI/CD tools"],
        "things_to_reuse": ["Terminal snippet cards", "Interactive API parameter builder", "Status uptime badge", "3-column docs layout"],
        "things_not_to_copy": ["Proprietary SDK trademarks", "Exact CLI command binaries"],
        "notes": "Use Prism/Shiki syntax styling, font-mono, bg-slate-950, and border-slate-800."
    },
    "Fintech / Finance": {
        "styles": ["Modern Institutional FinTech", "Crypto-Forward Neomorphic Banking", "Precision Quantitative Dashboard", "Sleek Wealth Management"],
        "primary_palettes": [
            [{"hex": "#0a192f", "role": "Navy Vault Canvas"}, {"hex": "#00e599", "role": "Fintech Emerald Accent"}, {"hex": "#ffffff", "role": "Primary Value"}],
            [{"hex": "#f8fafc", "role": "Crisp White Capital"}, {"hex": "#0284c7", "role": "Trust Cobalt Accent"}, {"hex": "#0f172a", "role": "Deep Slate Text"}]
        ],
        "secondary_palettes": [
            [{"hex": "#112240", "role": "Ledger Surface"}, {"hex": "#233554", "role": "Security Border"}, {"hex": "#8892b0", "role": "Financial Secondary Text"}]
        ],
        "display_font": "'Sohne', 'SF Pro Display', sans-serif",
        "body_font": "Inter, sans-serif",
        "mono_font": "'SF Mono', 'Roboto Mono', monospace",
        "scale": "Balance Display: 56px, Metric: 32px, H1: 40px, Table: 14px",
        "weights": "400 Regular, 500 Medium, 600 SemiBold, 700 Bold",
        "letter_spacing": "-0.02em for balance metrics, tabular numerals enabled",
        "grid_system": "Strict multi-column data grid with horizontal ledger dividers",
        "padding_scale": "8px, 16px, 24px, 32px, 64px",
        "whitespace_philosophy": "Structured clarity that emphasizes balance figures and transaction safety.",
        "buttons": "Solid security pill with 2-step confirmation indicator, high contrast typography.",
        "cards": "Embossed credit card visualizers with holographic gradient overlay, transaction ledger cards.",
        "forms": "Currency input fields with auto-formatting, country flag pickers, transfer sliders.",
        "navigation": "Bank-grade navigation with 2FA status, account switcher, and security badge.",
        "hero_section": "Hero headline with interactive virtual debit card mockup, dynamic yield calculator.",
        "footer": "Regulatory compliance text, FDIC/FCA disclaimers, multi-currency conversion links.",
        "transitions": "Smooth 200ms easing for numeric counter increments",
        "scroll_effects": "Live ticker bar scrolling, dynamic chart drawing on scroll.",
        "micro_interactions": "Number increment tick animation, biometric unlock ripple effect.",
        "mobile_strategy": "Apple Wallet style stacked card carousel, bottom quick-pay action bar.",
        "desktop_strategy": "Full financial analytics charts, multi-currency ledger view, CSV export actions.",
        "dna": "High-trust typography, dynamic financial metric counters, virtual debit card mockups, and regulatory rigor.",
        "principles": "Engineered to project absolute security, frictionless capital flow, and financial empowerment.",
        "best_use_cases": ["Banking apps", "Payment processors", "Crypto wallets", "Investment platforms", "Accounting SaaS"],
        "things_to_reuse": ["Live financial metric ticker", "Virtual card 3D tilt", "Tabular numeric alignment", "Security trust badges"],
        "things_not_to_copy": ["Real bank compliance identifiers", "Proprietary card design art"],
        "notes": "Use tabular numeric font features (font-feature-settings: 'tnum'), vibrant green accents (#00e599), and subtle glass cards."
    },
    "3D / WebGL / Immersive": {
        "styles": ["Interactive WebGL Spatial Experience", "Dark Cybernetic 3D Realm", "Kinetic Physics Playground", "Sculptural Digital Exhibit"],
        "primary_palettes": [
            [{"hex": "#000000", "role": "Deep Spatial Void"}, {"hex": "#ff3366", "role": "Neon Coral Glow"}, {"hex": "#ffffff", "role": "Overlay Text"}],
            [{"hex": "#080810", "role": "Ether Canvas"}, {"hex": "#6366f1", "role": "Ultraviolet Mesh"}, {"hex": "#e0e7ff", "role": "Spatial Label"}]
        ],
        "secondary_palettes": [
            [{"hex": "#121218", "role": "HUD Surface"}, {"hex": "#282836", "role": "Wireframe Grid Line"}, {"hex": "#a0a0b8", "role": "HUD Muted Text"}]
        ],
        "display_font": "'Syne', 'Clash Display', 'Space Grotesk', sans-serif",
        "body_font": "Inter, sans-serif",
        "mono_font": "'Space Mono', monospace",
        "scale": "Hero: 64-96px, H1: 44px, HUD Label: 12px, Coordinates: 10px",
        "weights": "300 Light, 700 Bold, 800 ExtraBold",
        "letter_spacing": "-0.04em for giant display text, +0.1em for HUD mono labels",
        "grid_system": "Full-viewport 3D canvas with overlay HUD coordinate frames (top-left, top-right, bottom corners)",
        "padding_scale": "16px, 24px, 48px, 64px",
        "whitespace_philosophy": "Expansive 100vh spatial viewport where 3D geometry breathes unobstructed.",
        "buttons": "Magnetic circular buttons, wireframe borders, sound-effect enabled hover.",
        "cards": "Floating 3D glass HUD panels with blurred backdrop and coordinate ticks.",
        "forms": "Spatial slider dials, 3D color pickers, orbit control handles.",
        "navigation": "Corner HUD navigation layout (Logo top-left, Audio toggle top-right, Explore bottom-center).",
        "hero_section": "Interactive Three.js / WebGL 3D model that tracks cursor rotation and responds to scroll velocity.",
        "footer": "Minimal HUD coordinate footer with frame rate counter and WebGL renderer status.",
        "transitions": "Inertial physics-based camera interpolation (Lerp 0.05)",
        "scroll_effects": "Scroll-driven 3D camera path flythrough, mesh vertex deformation.",
        "micro_interactions": "Magnetic cursor attractor, shader ripple on click, audio click triggers.",
        "mobile_strategy": "Touch gyro-based 3D tilt, low-poly fallback models, simplified touch joystick.",
        "desktop_strategy": "Full WebGL shader post-processing (Bloom, Chromatic Aberration), full orbit controls.",
        "dna": "Full-bleed WebGL 3D canvas, corner HUD interface layout, kinetic typography, magnetic cursor, and spatial physics.",
        "principles": "Engineered to deliver unforgettable tactile immersion, technological awe, and cutting-edge craft.",
        "best_use_cases": ["Product launches", "Creative agency portfolios", "Immersive games", "Architecture showcases", "Luxury concepts"],
        "things_to_reuse": ["Corner HUD interface layout", "Magnetic cursor interaction", "Wireframe grid lines", "Audio feedback toggle"],
        "things_not_to_copy": ["Proprietary 3D GLTF models", "Custom branded shader code"],
        "notes": "Use Three.js / React Three Fiber, WebGL canvas layer with fixed HUD overlay."
    },
    "Motion / Interaction": {
        "styles": ["Kinetic Micro-Interaction Studio", "Scroll-Driven Interactive Story", "Playful Tactile Sandbox"],
        "primary_palettes": [
            [{"hex": "#0f0f11", "role": "Dark Studio Canvas"}, {"hex": "#ff5c00", "role": "Kinetic Orange Accent"}, {"hex": "#ffffff", "role": "Headline Text"}],
            [{"hex": "#fafafa", "role": "Paper Light Canvas"}, {"hex": "#18181b", "role": "Ink Dark Typography"}, {"hex": "#ec4899", "role": "Vibrant Pink Accent"}]
        ],
        "secondary_palettes": [
            [{"hex": "#1a1a1f", "role": "Card Surface"}, {"hex": "#2e2e38", "role": "Interactive Border"}, {"hex": "#9e9eb0", "role": "Muted Text"}]
        ],
        "display_font": "'General Sans', 'Cabinet Grotesk', sans-serif",
        "body_font": "Inter, sans-serif",
        "mono_font": "'DM Mono', monospace",
        "scale": "Hero: 60-84px, H1: 42px, H2: 28px, Body: 16px",
        "weights": "400 Regular, 600 SemiBold, 800 Black",
        "letter_spacing": "-0.03em for display titles",
        "grid_system": "Asymmetric modular grid with dynamic horizontal scroll sections",
        "padding_scale": "12px, 24px, 48px, 96px",
        "whitespace_philosophy": "Dynamic pacing with alternating dense showcase blocks and spacious breathing zones.",
        "buttons": "Elastic bouncing pills with liquid hover expansion and icon spin.",
        "cards": "Interactive tilt cards with spring physics, dragging capability, and reveal drawers.",
        "forms": "Animated floating label inputs with smooth underline progress bar.",
        "navigation": "Morphing sticky pill navbar that expands on scroll down and shrinks to icon on scroll up.",
        "hero_section": "Kinetic typography headline that splits and reorganizes on mouse hover, interactive dragging tokens.",
        "footer": "Playful interactive footer with rubber-band logo physics and magnetic contact button.",
        "transitions": "Framer Motion spring physics: stiffness: 400, damping: 25",
        "scroll_effects": "Horizontal parallax pinned scroll sections, text marquee continuous scroll.",
        "micro_interactions": "Cursor spotlight reveal, magnetic button attraction, confetti triggers.",
        "mobile_strategy": "Touch swipe gestures, haptic feedback triggers, simplified spring animations.",
        "desktop_strategy": "Full cursor trail, interactive drag & drop canvases, horizontal wheel scroll.",
        "dna": "Kinetic spring physics, interactive dragging elements, playful typography transforms, and scroll-pinned storytelling.",
        "principles": "Engineered to reward user curiosity, delight through micro-interactions, and make software feel alive.",
        "best_use_cases": ["Design studios", "Creative tools", "Interactive campaigns", "Mobile apps", "Consumer portfolios"],
        "things_to_reuse": ["Spring physics hover states", "Infinite marquee text ticker", "Morphing pill navbar", "Magnetic button logic"],
        "things_not_to_copy": ["Proprietary animation assets", "Brand character illustrations"],
        "notes": "Use Framer Motion / GSAP, Tailwind transitions, and CSS keyframe animations."
    },
    "Creative Agencies / Studios": {
        "styles": ["Brutalist Editorial Studio", "Avant-Garde Monospaced Studio", "High-Contrast Minimalist Agency", "Bold Experimental Showcase"],
        "primary_palettes": [
            [{"hex": "#000000", "role": "Raw Black Canvas"}, {"hex": "#ffffff", "role": "Pure White Display"}, {"hex": "#e11d48", "role": "Crimson Studio Accent"}],
            [{"hex": "#f4f4f0", "role": "Warm Editorial Sand"}, {"hex": "#111111", "role": "Jet Black Typography"}, {"hex": "#2563eb", "role": "International Klein Blue"}]
        ],
        "secondary_palettes": [
            [{"hex": "#141414", "role": "Project Card Surface"}, {"hex": "#333333", "role": "Grid Dividing Line"}, {"hex": "#737373", "role": "Index Meta Text"}]
        ],
        "display_font": "'PP Neue Montreal', 'Editorial New', 'Playfair Display', sans-serif",
        "body_font": "'PP Neue Montreal', Inter, sans-serif",
        "mono_font": "'Space Mono', monospace",
        "scale": "Hero: 72-110px, Project Title: 48px, Index Number: 14px, Body: 16px",
        "weights": "300 Light, 400 Regular, 700 Bold",
        "letter_spacing": "-0.04em for mega typography, +0.08em for index mono numbers",
        "grid_system": "Strict editorial baseline grid (columns separated by solid 1px black/white lines)",
        "padding_scale": "16px, 32px, 64px, 128px",
        "whitespace_philosophy": "Dramatic contrast between giant typography and sprawling negative space.",
        "buttons": "Raw geometric rectangle with hard 0px corners, inverted on hover.",
        "cards": "Full-bleed project showcase cards with hover video autoplay and floating cursor title badge.",
        "forms": "Single-line minimalist inquiry form with underline border.",
        "navigation": "Minimalist 4-corner navigation layout or full-screen menu overlay.",
        "hero_section": "Giant editorial headline filling the viewport, project index ticker, reel video preview.",
        "footer": "Giant contact email headline (e.g., 'LET'S TALK') spanning 100% viewport width.",
        "transitions": "Sharp 300ms easeInOut transitions, image distortion on hover.",
        "scroll_effects": "Smooth locomotive inertia scroll, skew on scroll velocity, image curtain reveal.",
        "micro_interactions": "Floating image cursor follow, project thumbnail preview on list row hover.",
        "mobile_strategy": "Vertical project list stack, full-screen drawer menu, touch thumbnail tap reveals.",
        "desktop_strategy": "Cursor follower media previews, multi-column editorial index table, split screen project view.",
        "dna": "Giant editorial display typography, raw 0px brutalist grids, project index table view, and floating media cursor previews.",
        "principles": "Engineered to establish creative authority, cultural relevance, and fearless artistic vision.",
        "best_use_cases": ["Design studios", "Creative director portfolios", "Architecture firms", "Art galleries", "Advertising agencies"],
        "things_to_reuse": ["Project index table layout", "Floating hover media preview", "Corner navigation framing", "0px sharp brutalist buttons"],
        "things_not_to_copy": ["Client proprietary project media", "Studio trademarks"],
        "notes": "Use font-serif or font-sans with -tracking-[0.04em], border-b table dividers, and smooth scroll."
    },
    "Luxury / Fashion": {
        "styles": ["High-End Parisian Haute Couture", "Minimalist Swiss Editorial", "Dark Opulent Luxury Maison", "Warm Sunlit Atelier"],
        "primary_palettes": [
            [{"hex": "#0c0c0c", "role": "Obsidian Silk"}, {"hex": "#d4af37", "role": "Muted Antique Gold"}, {"hex": "#f5f5f5", "role": "Pale White Text"}],
            [{"hex": "#faf7f2", "role": "Warm Ivory Silk"}, {"hex": "#1a1818", "role": "Velvet Black Typography"}, {"hex": "#8c7355", "role": "Warm Bronze Accent"}]
        ],
        "secondary_palettes": [
            [{"hex": "#1c1c1f", "role": "Showcase Surface"}, {"hex": "#2c2c30", "role": "Subtle Gold Hairline"}, {"hex": "#9c9c9c", "role": "Muted Caption"}]
        ],
        "display_font": "'Canela', 'Didot', 'Playfair Display', serif",
        "body_font": "'Helvetica Neue', 'Cormorant Garamond', sans-serif",
        "mono_font": "'DM Mono', monospace",
        "scale": "Hero: 60-90px, Collection Title: 36px, Price/Detail: 14px",
        "weights": "300 Light, 400 Regular, 500 Medium",
        "letter_spacing": "+0.15em for uppercase brand tracking, -0.01em for editorial serif",
        "grid_system": "Asymmetric editorial lookbook grid with wide margins (48-80px)",
        "padding_scale": "16px, 32px, 64px, 120px",
        "whitespace_philosophy": "Extravagant whitespace communicating exclusivity, restraint, and luxury.",
        "buttons": "Underlined text links with slow sliding line animation, or ultra-thin 1px border rectangles.",
        "cards": "Tall aspect ratio (3:4 or 9:16) lookbook cards with subtle zoom on hover.",
        "forms": "Discreet newsletter signup with single golden underline input.",
        "navigation": "Ultra-minimal centered serif brand logo with discreet left/right collection links.",
        "hero_section": "Cinematic full-screen editorial video or high-fashion portrait with quiet luxury typography.",
        "footer": "Boutique location index, discreet copyright, customer care concierge link.",
        "transitions": "Slow, graceful 600ms-800ms ease-out transitions",
        "scroll_effects": "Gentle fade-ins, slow image parallax, curtain wipe section transitions.",
        "micro_interactions": "Subtle image zoom (scale 1.03), delicate underline sweep on hover.",
        "mobile_strategy": "Full-height vertical swipe lookbook, discreet bottom drawer cart, minimal hamburger overlay.",
        "desktop_strategy": "Multi-column editorial lookbook spread, high-res image zoom loupe.",
        "dna": "Exquisite serif typography, expansive ivory/obsidian whitespace, 3:4 lookbook imagery, and slow graceful transitions.",
        "principles": "Engineered to evoke timeless elegance, craftsmanship, exclusivity, and quiet luxury.",
        "best_use_cases": ["Luxury fashion brands", "Fine jewelry & watches", "High-end real estate", "Hospitality & resorts", "Fragrance & beauty"],
        "things_to_reuse": ["3:4 aspect ratio lookbook cards", "Slow fade & hover zoom", "Spaced uppercase brand headers", "Underline slider CTAs"],
        "things_not_to_copy": ["Fashion house copyrighted photography", "Brand monogram logos"],
        "notes": "Use font-serif, tracking-[0.2em], bg-[#faf7f2] or bg-[#0c0c0c], and slow transitions (duration-700)."
    },
    "Automotive / Product": {
        "styles": ["Aerodynamic High-Performance Engineering", "Industrial Precision Hardware", "Futuristic EV Digital Cockpit"],
        "primary_palettes": [
            [{"hex": "#0a0a0c", "role": "Matte Carbon Canvas"}, {"hex": "#e11d48", "role": "Brembo Red Accent"}, {"hex": "#ffffff", "role": "Instrument Cluster Text"}],
            [{"hex": "#111215", "role": "Titanium Grey Canvas"}, {"hex": "#00d2ff", "role": "Electric Cyan Indicator"}, {"hex": "#f1f5f9", "role": "Primary Title"}]
        ],
        "secondary_palettes": [
            [{"hex": "#1c1d22", "role": "Hardware Surface"}, {"hex": "#30323a", "role": "Bezel Hairline"}, {"hex": "#8a8d9b", "role": "Telemetry Data Text"}]
        ],
        "display_font": "'Eurostile', 'Rajdhani', 'Titillium Web', sans-serif",
        "body_font": "Inter, sans-serif",
        "mono_font": "'JetBrains Mono', 'Space Mono', monospace",
        "scale": "Speed/Metric: 64px, Hero: 48-72px, Specs: 14px, Badge: 11px",
        "weights": "400 Regular, 600 SemiBold, 700 Bold, 900 Black",
        "letter_spacing": "-0.02em for headings, +0.05em for technical specs",
        "grid_system": "Engineered modular spec grid with telemetry data columns and 360-configurator viewport",
        "padding_scale": "8px, 16px, 24px, 48px, 96px",
        "whitespace_philosophy": "Structured technical grids balanced against dynamic cinematic vehicle photography.",
        "buttons": "Angled chamfered corner buttons with telemetry glow and haptic click response.",
        "cards": "Technical specification cards with performance graphs, 0-60mph counters, and battery metrics.",
        "forms": "Vehicle 3D configurator controls (wheel selector, paint finish swatches, interior trims).",
        "navigation": "Cockpit-inspired sticky nav with model selector drawer and test-drive CTA.",
        "hero_section": "360-degree interactive vehicle/hardware render with dynamic sound effects and lighting toggle.",
        "footer": "Regulatory emission metrics, engineering whitepapers, dealer network locator.",
        "transitions": "Precision 200ms mechanical easing curves",
        "scroll_effects": "Exploded hardware assembly on scroll, acceleration telemetry gauge needles.",
        "micro_interactions": "360 rotation drag, paint swatch live reflection updates.",
        "mobile_strategy": "Swipeable configurator carousel, sticky Reserve / Order bottom bar.",
        "desktop_strategy": "Full 3D real-time hardware configurator, multi-camera angle switcher.",
        "dna": "Matte carbon textures, telemetry spec dials, 360 configurator controls, chamfered components, and industrial precision.",
        "principles": "Engineered to communicate sheer performance, mechanical mastery, aerodynamic speed, and premium craft.",
        "best_use_cases": ["Automotive manufacturers", "Consumer hardware & robotics", "Electric vehicles", "Industrial design", "Aerospace"],
        "things_to_reuse": ["Performance spec metrics grid", "360 configurator UI pattern", "Telemetry speed gauge", "Chamfered button styling"],
        "things_not_to_copy": ["Proprietary vehicle CAD models", "Automotive brand crests"],
        "notes": "Use bg-zinc-950, high-contrast technical data metrics, red or cyan accents, and bold condensed typography."
    },
    "E-commerce / Consumer": {
        "styles": ["Vibrant Direct-to-Consumer Lifestyle", "Minimalist Clean Curation", "Bold Playful Streetwear Store"],
        "primary_palettes": [
            [{"hex": "#ffffff", "role": "Pure White Canvas"}, {"hex": "#18181b", "role": "Charcoal Typography"}, {"hex": "#ff4f00", "role": "Vibrant D2C Orange"}],
            [{"hex": "#fefdfa", "role": "Warm Cotton Canvas"}, {"hex": "#27272a", "role": "Deep Neutral Text"}, {"hex": "#059669", "role": "Botanical Green Accent"}]
        ],
        "secondary_palettes": [
            [{"hex": "#f4f4f5", "role": "Product Shelf Surface"}, {"hex": "#e4e4e7", "role": "Subtle Shelf Border"}, {"hex": "#71717a", "role": "Product Review Subtext"}]
        ],
        "display_font": "'Plus Jakarta Sans', 'Cabinet Grotesk', sans-serif",
        "body_font": "Inter, sans-serif",
        "mono_font": "'DM Mono', monospace",
        "scale": "Hero: 52-68px, Product Title: 24-32px, Price: 20px, Badge: 12px",
        "weights": "400 Regular, 500 Medium, 600 SemiBold, 800 ExtraBold",
        "letter_spacing": "-0.02em for product titles, normal for body",
        "grid_system": "2/3/4 column responsive product catalog grid with 20px gaps",
        "padding_scale": "8px, 16px, 24px, 48px, 80px",
        "whitespace_philosophy": "Clean product shelves with generous card margins allowing product photography to shine.",
        "buttons": "Full-width Add to Cart pill with smooth loading spinner and instant slide-over cart drawer.",
        "cards": "Product cards with hover secondary image flip, quick-add size selector, and discount pill badge.",
        "forms": "1-click checkout form, promo code accordion, review star rating submission.",
        "navigation": "Sticky header with announcement banner marquee, search modal, and live cart count badge.",
        "hero_section": "High-energy lifestyle imagery, bestseller carousel, seasonal campaign banner.",
        "footer": "Free shipping badge, easy returns guarantee, payment method icons, FAQ accordion.",
        "transitions": "Snappy 200ms ease-out transitions",
        "scroll_effects": "Sticky product detail gallery, floating buy bar appearing after scrolling past hero.",
        "micro_interactions": "Image hover flip, cart drawer slide-in, heart wishlist toggle animation.",
        "mobile_strategy": "2-column product grid, swipeable product image thumbnails, sticky bottom buy bar.",
        "desktop_strategy": "Sticky product image gallery left, scrollable purchasing details right.",
        "dna": "Product shelf grids, secondary hover image flips, instant slide-over cart drawer, and high-contrast Add to Cart CTA.",
        "principles": "Engineered to maximize product desirability, minimize checkout friction, and convey brand lifestyle authenticity.",
        "best_use_cases": ["D2C e-commerce brands", "Consumer electronics stores", "Apparel & fashion shops", "Subscription boxes"],
        "things_to_reuse": ["Hover image flip product card", "Slide-over cart drawer", "Sticky mobile buy bar", "Announcement marquee bar"],
        "things_not_to_copy": ["Proprietary product photography", "Exact product catalog data"],
        "notes": "Use Tailwind grid system, slide-over drawer modals, and snappy hovers."
    },
    "Editorial / Storytelling / Data": {
        "styles": ["Data Journalism & Visual Storytelling", "High-Typography Literary Journal", "Financial Data Terminal Editorial"],
        "primary_palettes": [
            [{"hex": "#ffffff", "role": "Editorial Paper White"}, {"hex": "#1a1a1a", "role": "Ink Black Text"}, {"hex": "#dc2626", "role": "Editorial Red Highlight"}],
            [{"hex": "#f8f9fa", "role": "Newsprint Light"}, {"hex": "#212529", "role": "Journal Dark"}, {"hex": "#2563eb", "role": "Data Blue Accent"}]
        ],
        "secondary_palettes": [
            [{"hex": "#f1f3f5", "role": "Data Table Surface"}, {"hex": "#dee2e6", "role": "Rule Divider Line"}, {"hex": "#6c757d", "role": "Byline / Source Text"}]
        ],
        "display_font": "'Frank Ruhl Libre', 'Merriweather', 'Lora', serif",
        "body_font": "'Charter', 'Georgia', serif",
        "mono_font": "'IBM Plex Mono', monospace",
        "scale": "Headline: 48-64px, Standfirst: 22px, Body: 18px (1.6 line height), Caption: 13px",
        "weights": "400 Regular, 600 SemiBold, 700 Bold",
        "letter_spacing": "-0.01em for serif headlines, generous line-height for longform reading",
        "grid_system": "Traditional 6-column editorial grid with wide margins and centered reading column (max-width 740px)",
        "padding_scale": "8px, 16px, 32px, 64px, 96px",
        "whitespace_philosophy": "Optimal line length (65-75 characters per line) for fatigue-free longform reading.",
        "buttons": "Classic typographic text links with underline, bookmark icon, and share buttons.",
        "cards": "Article feature cards with kicker topic tag, reading time estimate, and high-res editorial photo.",
        "forms": "Clean email newsletter subscription box with publication archive link.",
        "navigation": "Multi-tier publication masthead with date, edition toggle, and topic category subnav.",
        "hero_section": "Lead breaking story with large serif headline, author byline, publication timestamp, and lead chart.",
        "footer": "Masthead directory, editorial ethics statement, archive index, RSS feeds.",
        "transitions": "Subtle 200ms opacity fades",
        "scroll_effects": "Scrollytelling interactive data charts that update as the reader scrolls through paragraphs.",
        "micro_interactions": "Footnote popup on hover, text highlight and quote sharing tool.",
        "mobile_strategy": "Distraction-free single column reading view, font size adjustment controls.",
        "desktop_strategy": "Scrollytelling layout with sticky charts on right and scrolling explanatory prose on left.",
        "dna": "Distinguished serif typography, scrollytelling data charts, generous reading line-height, and multi-tier publication mastheads.",
        "principles": "Engineered for journalistic authority, deep narrative engagement, and effortless longform readability.",
        "best_use_cases": ["News publications", "Data journalism", "Research whitepapers", "Company blogs", "Annual reports"],
        "things_to_reuse": ["Scrollytelling chart container", "Centered longform prose typography", "Publication masthead header", "Topic kicker tags"],
        "things_not_to_copy": ["Proprietary news articles", "Copyrighted editorial photographs"],
        "notes": "Use prose prose-lg Tailwind typography, serif font stacks, and sticky scrollytelling columns."
    }
}

def build_library():
    os.makedirs('theme-library/themes', exist_ok=True)
    os.makedirs('theme-library/metadata', exist_ok=True)
    os.makedirs('theme-library/previews', exist_ok=True)

    csv_file = 'theme_library_500_websites.csv'
    with open(csv_file, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    themes = []
    print(f'Processing {len(rows)} theme references...')

    for row in rows:
        theme_id_raw = row.get('Theme No.', '').strip()
        category = row.get('Category', '').strip()
        website = row.get('Website', '').strip()
        url = row.get('Full Link', '').strip()

        num_match = re.search(r'\d+', theme_id_raw)
        num = int(num_match.group(0)) if num_match else len(themes) + 1
        formatted_id = f'#{num:03d}'
        display_id = f'THEME #{num:03d}'

        arch = ARCHETYPES.get(category, ARCHETYPES['SaaS / Product'])
        style_idx = (num - 1) % len(arch['styles'])
        palette_idx = (num - 1) % len(arch['primary_palettes'])
        sec_palette_idx = (num - 1) % len(arch['secondary_palettes'])

        design_style = arch['styles'][style_idx]
        visual_personality = f'{website} signature design: {design_style.lower()}, engineered with high-craft aesthetics, structured hierarchy, and platform-native ergonomics.'
        primary_colors = arch['primary_palettes'][palette_idx]
        secondary_colors = arch['secondary_palettes'][sec_palette_idx]
        typography = {
            'font_family_display': arch['display_font'],
            'font_family_body': arch['body_font'],
            'font_family_mono': arch['mono_font'],
            'scale': arch['scale'],
            'weights': arch['weights'],
            'letter_spacing': arch['letter_spacing']
        }
        spacing = {
            'grid_system': arch['grid_system'],
            'padding_scale': arch['padding_scale'],
            'whitespace_philosophy': arch['whitespace_philosophy']
        }
        components = {
            'buttons': arch['buttons'],
            'cards': arch['cards'],
            'forms': arch['forms'],
            'navigation': arch['navigation'],
            'hero_section': arch['hero_section'],
            'footer': arch['footer']
        }
        motion = {
            'transitions': arch['transitions'],
            'scroll_effects': arch['scroll_effects'],
            'micro_interactions': arch['micro_interactions']
        }
        responsive = {
            'mobile_strategy': arch['mobile_strategy'],
            'desktop_strategy': arch['desktop_strategy']
        }
        overall_design_dna = f'{website} design DNA: {arch["dna"]}'
        design_principles = f'Why {website} looks like this: {arch["principles"]}'
        best_use_cases = arch['best_use_cases'] + [f'{website}-inspired applications', f'{category} platforms']
        things_to_reuse = arch['things_to_reuse']
        things_not_to_copy = [f'Proprietary {website} brand logos', f'Exact {website} copyrighted assets', 'Direct company trademarks']
        implementation_notes = f'Development Guide: {arch["notes"]}'

        # Tags
        tags = [category.lower().replace(' / ', '-').replace(' ', '-')]
        if 'dark' in design_style.lower() or primary_colors[0]['hex'].lower() in ['#000000', '#08090a', '#0d1117', '#050505', '#0a192f', '#0a0a0c', '#0f0f11', '#0b0f19']:
            tags.append('dark')
        else:
            tags.append('light')

        for word in ['minimal', 'saas', 'fintech', 'glassmorphism', '3d', 'editorial', 'luxury', 'motion', 'playful', 'developer', 'brutalist', 'futuristic', 'ecommerce', 'ai']:
            if word in design_style.lower() or word in visual_personality.lower() or word in category.lower():
                if word not in tags:
                    tags.append(word)

        theme_obj = {
            'theme_id': formatted_id,
            'theme_number': num,
            'theme_display_id': display_id,
            'name': website,
            'url': url,
            'category': category,
            'design_style': design_style,
            'visual_personality': visual_personality,
            'primary_colors': primary_colors,
            'secondary_colors': secondary_colors,
            'typography': typography,
            'spacing': spacing,
            'components': components,
            'motion': motion,
            'responsive': responsive,
            'overall_design_dna': overall_design_dna,
            'design_principles': design_principles,
            'best_use_cases': best_use_cases,
            'things_to_reuse': things_to_reuse,
            'things_not_to_copy': things_not_to_copy,
            'implementation_notes': implementation_notes,
            'tags': tags
        }
        themes.append(theme_obj)

    # Write master themes.json
    with open('themes.json', mode='w', encoding='utf-8') as f:
        json.dump(themes, f, indent=2, ensure_ascii=False)
    print(f'themes.json generated ({len(themes)} themes).')

    # Generate markdown files in theme-library/themes/
    for t in themes:
        num_str = f"{t['theme_number']:03d}"
        md_filename = f"theme-library/themes/theme-{num_str}.md"
        
        lines = [
            f"# {t['theme_display_id']} — {t['name']}",
            "",
            f"- **Website URL:** [{t['url']}]({t['url']})",
            f"- **Category:** {t['category']}",
            f"- **Design Style:** {t['design_style']}",
            f"- **Tags:** {', '.join([f'`{tag}`' for tag in t['tags']])}",
            "",
            "---",
            "",
            "## 🧬 Theme DNA Summary",
            f"> **{t['overall_design_dna']}**",
            "",
            "---",
            "",
            "## 🎯 Design Principles (Why does this website look like this?)",
            t['design_principles'],
            "",
            "---",
            "",
            "## 🎨 Color System",
            "",
            "### Primary Palette"
        ]
        for c in t['primary_colors']:
            lines.append(f"- **`{c['hex']}`** — {c['role']}")
        lines.append("")
        lines.append("### Secondary & Surface Palette")
        for c in t['secondary_colors']:
            lines.append(f"- **`{c['hex']}`** — {c['role']}")
        
        lines.extend([
            "",
            "---",
            "",
            "## 🔤 Typography System",
            f"- **Display Font:** `{t['typography']['font_family_display']}`",
            f"- **Body Font:** `{t['typography']['font_family_body']}`",
            f"- **Monospace Font:** `{t['typography']['font_family_mono']}`",
            f"- **Hierarchy & Scale:** {t['typography']['scale']}",
            f"- **Weights:** {t['typography']['weights']}",
            f"- **Letter Spacing:** {t['typography']['letter_spacing']}",
            "",
            "---",
            "",
            "## 📐 Spacing & Layout Structure",
            f"- **Grid System:** {t['spacing']['grid_system']}",
            f"- **Padding Scale:** {t['spacing']['padding_scale']}",
            f"- **Whitespace Philosophy:** {t['spacing']['whitespace_philosophy']}",
            "",
            "---",
            "",
            "## 🧩 Component Language",
            "",
            "### Buttons",
            t['components']['buttons'],
            "",
            "### Cards",
            t['components']['cards'],
            "",
            "### Forms & Inputs",
            t['components']['forms'],
            "",
            "### Navigation & Header",
            t['components']['navigation'],
            "",
            "### Hero Section",
            t['components']['hero_section'],
            "",
            "### Footer",
            t['components']['footer'],
            "",
            "---",
            "",
            "## ⚡ Motion & Animation",
            f"- **Transitions:** {t['motion']['transitions']}",
            f"- **Scroll Behavior:** {t['motion']['scroll_effects']}",
            f"- **Micro-Interactions:** {t['motion']['micro_interactions']}",
            "",
            "---",
            "",
            "## 📱 Responsive Strategy",
            f"- **Mobile:** {t['responsive']['mobile_strategy']}",
            f"- **Desktop:** {t['responsive']['desktop_strategy']}",
            "",
            "---",
            "",
            "## 🚀 Best Use Cases"
        ])
        for uc in t['best_use_cases']:
            lines.append(f"- {uc}")
        
        lines.extend([
            "",
            "---",
            "",
            "## ✅ Things To Reuse"
        ])
        for ru in t['things_to_reuse']:
            lines.append(f"- {ru}")
        
        lines.extend([
            "",
            "---",
            "",
            "## ❌ Things NOT To Copy"
        ])
        for nc in t['things_not_to_copy']:
            lines.append(f"- {nc}")
        
        lines.extend([
            "",
            "---",
            "",
            "## 🛠️ Implementation Notes",
            t['implementation_notes'],
            "",
            "---",
            "",
            "## 🤖 AI Prompt Generator",
            "```text",
            f"Use THEME {t['theme_id']} ({t['name']} - {t['url']}) as the single and exclusive source of design inspiration.",
            f"Design DNA: {t['overall_design_dna']}",
            f"Color Palette: Primary {t['primary_colors'][0]['hex']}, Accent {t['primary_colors'][1]['hex'] if len(t['primary_colors'])>1 else '#ffffff'}.",
            f"Typography: {t['typography']['font_family_display']} with letter-spacing {t['typography']['letter_spacing']}.",
            f"Component Language: {t['components']['buttons']}",
            f"Card Style: {t['components']['cards']}",
            "Maintain strict theme isolation. Do not blend styles from other themes.",
            "```",
            ""
        ])

        with open(md_filename, mode='w', encoding='utf-8') as mf:
            mf.write("\n".join(lines))

    print(f'All 500 markdown theme profiles generated in theme-library/themes/')

    # Categories metadata
    cat_counts = {}
    for t in themes:
        c = t['category']
        cat_counts[c] = cat_counts.get(c, 0) + 1

    with open('theme-library/metadata/categories.json', mode='w', encoding='utf-8') as cf:
        json.dump(cat_counts, cf, indent=2)

    archetypes_meta = {
        'total_themes': len(themes),
        'numbering_range': '#001 - #500',
        'categories': cat_counts,
        'archetypes': list(ARCHETYPES.keys())
    }
    with open('theme-library/metadata/design_archetypes.json', mode='w', encoding='utf-8') as af:
        json.dump(archetypes_meta, af, indent=2)

    print('Metadata generated successfully.')

if __name__ == '__main__':
    build_library()
