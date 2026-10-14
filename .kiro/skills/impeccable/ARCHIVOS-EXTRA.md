# Archivos extra de `impeccable`

No caben en el paquete de Kiro (máx. 25 archivos por skill).
- **Documentación** (✅ incluida): su contenido completo está más abajo en este archivo.
- **Datos / código / binarios** (⬇️): descárgalos a la ruta indicada solo si la tarea los necesita:

```bash
mkdir -p "$(dirname <archivo>)" && curl -fsSL <enlace> -o <archivo>
```

| Archivo | Estado | Enlace |
|---------|--------|--------|
| `reference/adapt.md` | ✅ incluida abajo | https://raw.githubusercontent.com/paillamilm-blip/mis-skills/main/kiro-skills/03-diseno/impeccable/reference/adapt.md |
| `reference/android.md` | ✅ incluida abajo | https://raw.githubusercontent.com/paillamilm-blip/mis-skills/main/kiro-skills/03-diseno/impeccable/reference/android.md |
| `reference/critique.md` | ✅ incluida abajo | https://raw.githubusercontent.com/paillamilm-blip/mis-skills/main/kiro-skills/03-diseno/impeccable/reference/critique.md |
| `reference/document.md` | ✅ incluida abajo | https://raw.githubusercontent.com/paillamilm-blip/mis-skills/main/kiro-skills/03-diseno/impeccable/reference/document.md |
| `reference/hooks.md` | ✅ incluida abajo | https://raw.githubusercontent.com/paillamilm-blip/mis-skills/main/kiro-skills/03-diseno/impeccable/reference/hooks.md |
| `reference/init.md` | ✅ incluida abajo | https://raw.githubusercontent.com/paillamilm-blip/mis-skills/main/kiro-skills/03-diseno/impeccable/reference/init.md |
| `reference/ios.md` | ✅ incluida abajo | https://raw.githubusercontent.com/paillamilm-blip/mis-skills/main/kiro-skills/03-diseno/impeccable/reference/ios.md |
| `reference/live-setup.md` | ✅ incluida abajo | https://raw.githubusercontent.com/paillamilm-blip/mis-skills/main/kiro-skills/03-diseno/impeccable/reference/live-setup.md |
| `reference/live.md` | ✅ incluida abajo | https://raw.githubusercontent.com/paillamilm-blip/mis-skills/main/kiro-skills/03-diseno/impeccable/reference/live.md |
| `reference/new-work.md` | ✅ incluida abajo | https://raw.githubusercontent.com/paillamilm-blip/mis-skills/main/kiro-skills/03-diseno/impeccable/reference/new-work.md |
| `reference/overdrive.md` | ✅ incluida abajo | https://raw.githubusercontent.com/paillamilm-blip/mis-skills/main/kiro-skills/03-diseno/impeccable/reference/overdrive.md |
| `reference/visualize.md` | ✅ incluida abajo | https://raw.githubusercontent.com/paillamilm-blip/mis-skills/main/kiro-skills/03-diseno/impeccable/reference/visualize.md |

---

## 📄 `reference/adapt.md`

> **Additional context needed**: target platforms/devices and usage contexts.

Adapt an existing design to a different context: another screen size, device, platform, or use case. The trap is treating adaptation as scaling. The job is rethinking the experience for the new context.

**Web only** (mobile web included). Native platforms (`ios` / `android` / `adaptive`) route to [adapt.native.md](adapt.native.md) instead; if the project is native, switch to it now.

---

## Assess Adaptation Challenge

Understand what needs adaptation and why:

1. **Identify the source context**:
   - What was it designed for originally? (Desktop web? Mobile app?)
   - What assumptions were made? (Large screen? Mouse input? Fast connection?)
   - What works well in current context?

2. **Understand target context**:
   - **Device**: Mobile, tablet, desktop, TV, watch, print?
   - **Input method**: Touch, mouse, keyboard, voice, gamepad?
   - **Screen constraints**: Size, resolution, orientation?
   - **Connection**: Fast wifi, slow 3G, offline?
   - **Usage context**: On-the-go vs desk, quick glance vs focused reading?
   - **User expectations**: What do users expect on this platform?

3. **Identify adaptation challenges**:
   - What won't fit? (Content, navigation, features)
   - What won't work? (Hover states on touch, tiny touch targets)
   - What's inappropriate? (Desktop patterns on mobile, mobile patterns on desktop)

**CRITICAL**: Adaptation is rethinking the experience for the new context, not scaling pixels.

## Plan Adaptation Strategy

Create context-appropriate strategy:

### Mobile Adaptation (Desktop → Mobile)

**Layout Strategy**:
- Single column instead of multi-column
- Vertical stacking instead of side-by-side
- Full-width components instead of fixed widths
- Bottom navigation instead of top/side navigation

**Interaction Strategy**:
- Touch targets 44x44px minimum (not hover-dependent)
- Swipe gestures where appropriate (lists, carousels)
- Bottom sheets instead of dropdowns
- Thumbs-first design (controls within thumb reach)
- Larger tap areas with more spacing

**Content Strategy**:
- Progressive disclosure (don't show everything at once)
- Prioritize primary content (secondary content in tabs/accordions)
- Shorter text (more concise)
- Larger text (16px minimum)

**Navigation Strategy**:
- Hamburger menu or bottom navigation
- Reduce navigation complexity
- Sticky headers for context
- Back button in navigation flow

### Tablet Adaptation (Hybrid Approach)

**Layout Strategy**:
- Two-column layouts (not single or three-column)
- Side panels for secondary content
- Master-detail views (list + detail)
- Adaptive based on orientation (portrait vs landscape)

**Interaction Strategy**:
- Support both touch and pointer
- Touch targets 44x44px but allow denser layouts than phone
- Side navigation drawers
- Multi-column forms where appropriate

### Desktop Adaptation (Mobile → Desktop)

**Layout Strategy**:
- Multi-column layouts (use horizontal space)
- Side navigation always visible
- Multiple information panels simultaneously
- Fixed widths with max-width constraints (don't stretch to 4K)

**Interaction Strategy**:
- Hover states for additional information
- Keyboard shortcuts
- Right-click context menus
- Drag and drop where helpful
- Multi-select with Shift/Cmd

**Content Strategy**:
- Show more information upfront (less progressive disclosure)
- Data tables with many columns
- Richer visualizations
- More detailed descriptions

### Print Adaptation (Screen → Print)

**Layout Strategy**:
- Page breaks at logical points
- Remove navigation, footer, interactive elements
- Black and white (or limited color)
- Proper margins for binding

**Content Strategy**:
- Expand shortened content (show full URLs, hidden sections)
- Add page numbers, headers, footers
- Include metadata (print date, page title)
- Convert charts to print-friendly versions

### Email Adaptation (Web → Email)

**Layout Strategy**:
- Narrow width (600px max)
- Single column only
- Inline CSS (no external stylesheets)
- Table-based layouts (for email client compatibility)

**Interaction Strategy**:
- Large, obvious CTAs (buttons not text links)
- No hover states (not reliable)
- Deep links to web app for complex interactions

## Implement Adaptations

Apply changes systematically:

### Responsive Breakpoints

Choose appropriate breakpoints:
- Mobile: 320px-767px
- Tablet: 768px-1023px
- Desktop: 1024px+
- Or content-driven breakpoints (where design breaks)

### Layout Adaptation Techniques

- **CSS Grid/Flexbox**: Reflow layouts automatically
- **Container Queries**: Adapt based on container, not viewport
- **`clamp()`**: Fluid sizing between min and max
- **Media queries**: Different styles for different contexts
- **Display properties**: Show/hide elements per context

### Touch Adaptation

- Increase touch target sizes (44x44px minimum)
- Add more spacing between interactive elements
- Remove hover-dependent interactions
- Add touch feedback (ripples, highlights)
- Consider thumb zones (easier to reach bottom than top)

### Content Adaptation

- Use `display: none` sparingly (still downloads)
- Progressive enhancement (core content first, enhancements on larger screens)
- Lazy loading for off-screen content
- Responsive images (`srcset`, `picture` element)

### Navigation Adaptation

- Transform complex nav to hamburger/drawer on mobile
- Bottom nav bar for mobile apps
- Persistent side navigation on desktop
- Breadcrumbs on smaller screens for context

**IMPORTANT**: Test on real devices. Device emulation in DevTools is helpful but not perfect.

**NEVER**:
- Hide core functionality on mobile (if it matters, make it work)
- Assume desktop = powerful device (consider accessibility, older machines)
- Use different information architecture across contexts (confusing)
- Break user expectations for platform (mobile users expect mobile patterns)
- Forget landscape orientation on mobile/tablet
- Use generic breakpoints blindly (use content-driven breakpoints)
- Ignore touch on desktop (many desktop devices have touch)

## Verify Adaptations

Test thoroughly across contexts:

- **Real devices**: Test on actual phones, tablets, desktops
- **Different orientations**: Portrait and landscape
- **Different browsers**: Safari, Chrome, Firefox, Edge
- **Different OS**: iOS, Android, Windows, macOS
- **Different input methods**: Touch, mouse, keyboard
- **Edge cases**: Very small screens (320px), very large screens (4K)
- **Slow connections**: Test on throttled network

When the adaptation feels native to each context, hand off to `/impeccable polish` for the final pass.

---

## Reference Material

The sections below were previously `responsive-design.md` and live inline now so the adapt flow has its deep responsive reference in one place.

### Responsive Design

#### Mobile-First: Write It Right

Start with base styles for mobile, use `min-width` queries to layer complexity. Desktop-first (`max-width`) means mobile loads unnecessary styles first.

#### Breakpoints: Content-Driven

Don't chase device sizes; let content tell you where to break. Start narrow, stretch until design breaks, add breakpoint there. Three breakpoints usually suffice (640, 768, 1024px). Use `clamp()` for fluid values without breakpoints.

#### Detect Input Method, Not Just Screen Size

**Screen size doesn't tell you input method.** A laptop with touchscreen, a tablet with keyboard. Use pointer and hover queries:

```css
/* Fine pointer (mouse, trackpad) */
@media (pointer: fine) {
  .button { padding: 8px 16px; }
}

/* Coarse pointer (touch, stylus) */
@media (pointer: coarse) {
  .button { padding: 12px 20px; }  /* Larger touch target */
}

/* Device supports hover */
@media (hover: hover) {
  .card:hover { transform: translateY(-2px); }
}

/* Device doesn't support hover (touch) */
@media (hover: none) {
  .card { /* No hover state - use active instead */ }
}
```

**Critical**: Don't rely on hover for functionality. Touch users can't hover.

#### Safe Areas: Handle the Notch

Modern phones have notches, rounded corners, and home indicators. Use `env()`:

```css
body {
  padding-top: env(safe-area-inset-top);
  padding-bottom: env(safe-area-inset-bottom);
  padding-left: env(safe-area-inset-left);
  padding-right: env(safe-area-inset-right);
}

/* With fallback */
.footer {
  padding-bottom: max(1rem, env(safe-area-inset-bottom));
}
```

**Enable viewport-fit** in your meta tag:
```html
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
```

#### Responsive Images: Get It Right

##### srcset with Width Descriptors

```html
<img
  src="hero-800.jpg"
  srcset="
    hero-400.jpg 400w,
    hero-800.jpg 800w,
    hero-1200.jpg 1200w
  "
  sizes="(max-width: 768px) 100vw, 50vw"
  alt="Hero image"
>
```

**How it works**:
- `srcset` lists available images with their actual widths (`w` descriptors)
- `sizes` tells the browser how wide the image will display
- Browser picks the best file based on viewport width AND device pixel ratio

##### Picture Element for Art Direction

When you need different crops/compositions (not just resolutions):

```html
<picture>
  <source media="(min-width: 768px)" srcset="wide.jpg">
  <source media="(max-width: 767px)" srcset="tall.jpg">
  <img src="fallback.jpg" alt="...">
</picture>
```

#### Layout Adaptation Patterns

**Navigation**: Three stages: hamburger + drawer on mobile, horizontal compact on tablet, full with labels on desktop. **Tables**: Transform to cards on mobile using `display: block` and `data-label` attributes. **Progressive disclosure**: Use `<details>/<summary>` for content that can collapse on mobile.

#### Testing: Don't Trust DevTools Alone

DevTools device emulation is useful for layout but misses:

- Actual touch interactions
- Real CPU/memory constraints
- Network latency patterns
- Font rendering differences
- Browser chrome/keyboard appearances

**Test on at least**: One real iPhone, one real Android, a tablet if relevant. Cheap Android phones reveal performance issues you'll never see on simulators.

---

**Avoid**: Desktop-first design. Device detection instead of feature detection. Separate mobile/desktop codebases. Ignoring tablet and landscape. Assuming all mobile devices are powerful.

---

## 📄 `reference/android.md`

# Android platform

For native Android apps: Jetpack Compose, Android Views, React Native, Expo, Flutter shipping to Android hardware.

On native, the visitor mode narrows what expression may override. Material Design 3 governs structure, navigation, and interaction in every mode; brand expresses through Material's theming (color roles, type scale, shape, motion). A Material-everywhere cross-platform app that also ships to iPhone still owes iOS its OS guarantees on that hardware: safe-area insets, Reduce Motion, edge-swipe back.

## The Android slop test

Would a fluent Android user trust this app, or trip on off-spec components? The most common tell is an iOS app wearing Android's skin: a bottom-only navigation copied from iPhone, a back arrow that ignores the system Back gesture, Cupertino-shaped switches and dialogs. Material 3 is the rulebook; follow its components and theme the brand through it.

## Layout & structure

- **Material navigation, matched to size.** Navigation bar (bottom, 3–5 destinations) on compact width; navigation rail or drawer on expanded width. Never ship a phone bottom-bar untouched on a tablet.
- **System Back always works.** Honor the predictive Back gesture and Back button; never trap the user or hijack the gesture.
- **Edge-to-edge with window insets.** Apply the status bar, navigation bar, display cutout, and IME insets so content never hides behind system bars or the keyboard.
- **Top app bar for screen context**; pair with a FAB when the screen has a single primary action.

## Touch targets

- **48×48 dp minimum** for every touch target, with at least 8 dp between them.

## Typography

- **Material type scale.** Display, Headline, Title, Body, Label roles (large/medium/small each). Map text to roles; never hand-pick sizes per screen.
- **Roboto is the system face**; theme a brand face in through the type scale, keeping body, labels, and controls legible and consistent.
- **sp units, never fixed px**, so type follows the system font-size setting.

## Color & theming

- **Material color roles** (primary, on-primary, surface, surface-variant, secondary-container, outline, error). Role tokens resolve light/dark and contrast variants automatically; raw hex breaks there.
- **Dynamic Color (Material You)** where it fits: derive the scheme from the user's wallpaper on Android 12+, with a static fallback.
- **Dark theme is a first-class scheme.** Design and test it; never a quick invert.
- **Tonal elevation.** Convey elevation through the standard surface tonal levels (plus shadow where appropriate); no arbitrary drop shadows.

## Components & motion

- **Material components.** Buttons (filled / tonal / outlined / text), FAB, switches, chips, snackbars, bottom sheets, Material dialogs, navigation bar/rail/drawer. Never port iOS controls or invent equivalents.
- **One FAB, one primary action.** Never stack FABs or spend one on a secondary task.
- **Snackbars for transient feedback** (actionable when useful, never a toast for that); dialogs only for decisions that must interrupt.
- **Material motion patterns.** Container transform, shared-axis, fade-through, with standard easing and durations; honor the system Remove animations setting with a crossfade or instant cut.

---

## 📄 `reference/critique.md`

### Purpose

Resolve one stable target, run two independent assessments, synthesize a design critique, persist a snapshot, and ask the user what to improve next. The chat response is the primary deliverable; the snapshot is an archive/backlog for future commands.

### Hard Invariants

- Assessment A (design review) and Assessment B (detector/browser evidence) are both required.
- Assessment A and B MUST run as two isolated sub-agents whenever a sub-agent/Task tool is exposed. Running them inline in this context is "possible" but is NOT permitted; it is a degraded run. Inline is allowed ONLY when no sub-agent tool exists (or the user declined, on harnesses that ask).
- If you degrade for any reason, the report's first line MUST be a banner: `⚠️ DEGRADED: single-context (<reason>)`. A silent degraded critique is a failed critique.
- Assessment A must finish before detector findings enter the parent synthesis context. Detector output is deterministic, but it still anchors judgment.
- A skipped detector is a failed critique run unless `detect.mjs` is missing or crashes after a real attempt.
- Viewable targets require browser inspection when available.
- Any local server started only for critique visualization must run in the background, have a recorded stop method, and be stopped before final reporting unless the user asks to keep it.
- Do not claim a user-visible overlay exists unless script injection succeeded and the detector ran in the page.

### Setup

1. **Resolve the target** to a concrete file path or URL. Prefer a source path over a dev-server URL when both identify the same surface; ports drift, paths do not.
   - "the homepage" -> `site/pages/index.astro` or `index.html`
   - "the settings modal" -> the primary component file
   - "this page" -> the current URL or source file
2. **Confirm the target slugs cleanly**:
   ```bash
   node .kiro/skills/impeccable/scripts/critique-storage.mjs slug "<resolved-path-or-url>"
   ```
   Every later command also accepts the resolved target directly and derives the same slug internally; never hand-write a slug. If this exits non-zero, skip persistence and trend for this run, but continue the critique.
3. **Read `.impeccable/critique/ignore.md`** if it exists. Drop matching findings silently; it is the only prior-run input critique consumes.

### Assessment Orchestration

Delegate Assessment A and Assessment B to separate sub-agents. They must not see each other's output. Do not show findings to the user until synthesis.

Sub-agent gate (all harnesses):
- Unless a harness-specific gate below overrides this, spawn A and B as two isolated, parallel sub-agents whenever a sub-agent/Task tool is exposed. This is the default and is mandatory; do not run them inline because it is faster.
- "Unavailable" means exactly one thing: no sub-agent/Task tool is exposed in this session (or, on harnesses that ask, the user declined). It does not mean inconvenient.
- If and only if sub-agents are unavailable, fall back sequentially: finish and record Assessment A, then run Assessment B, then synthesize, and emit the degraded banner.
- Whichever path you take, declare it in the report header (see Report header provenance). Skipping sub-agents without the banner is the most common failure of this command.

If browser automation is available, each assessment creates its own new tab. Never reuse an existing tab, even if it is already at the right URL.

### Assessment A: Design Review

Read relevant source files and visually inspect the live page when browser automation is available. Think like a design director.

Evaluate:
- **Design specificity**: Is the composition, interaction, and visual language grounded in this product, or could an unrelated product use it unchanged? Make this judgment before seeing detector output.
- **Holistic design**: hierarchy, IA, emotional fit, discoverability, composition, typography, color, accessibility, states, copy, and edge cases.
- **Cognitive load**: consult the [Cognitive Load Assessment](#cognitive-load-assessment) section below; report checklist failures and decision points with >4 visible options.
- **Emotional journey**: peak-end rule, emotional valleys, reassurance at high-stakes moments.
- **Nielsen heuristics**: consult the [Heuristics Scoring Guide](#heuristics-scoring-guide) section below; score all 10 heuristics 0-4, marking any heuristic the mode-applicability rule allows as `n/a` instead of forcing a number.

Return: design-specificity verdict, heuristic scores, cognitive load, emotional journey, 2-3 strengths, 3-5 priority issues, persona red flags, minor observations, and provocative questions.

### Assessment B: Detector + Browser Evidence

Run the bundled detector and browser visualization evidence. Assessment B is mandatory and must remain isolated from Assessment A until both are complete.

CLI scan:
```bash
node .kiro/skills/impeccable/scripts/detect.mjs --json [target]
```

- Pass markup files/directories as `[target]`; do not pass CSS-only files.
- For URLs, skip CLI scan and use browser visualization.
- For very large trees (500+ scannable files), narrow scope or ask.
- Exit code 0 = clean; 2 = findings.
- If the detector entrypoint is missing or fails to load, report deterministic scan unavailable and continue with browser/manual review.

Browser visualization is required for a viewable target when browser automation is available. Use a localhost dev/static URL for local files; avoid `file://` unless the available browser explicitly supports this workflow. Overlay flow:

1. Create a fresh tab and navigate. Prefer the harness's native/browser-canvas screenshot path before hand-rolling a Playwright/Puppeteer script; only fall back to a custom script when no native browser tool is exposed.
2. Preflight mutable injection by setting `document.title` and appending a `<script>` tag. Read-only evaluate APIs do not count.
3. If mutation is unavailable, skip live server, browser presentation, and injection; report fallback signal.
4. If mutation is available, start `node .kiro/skills/impeccable/scripts/live-server.mjs --background`, present the browser if supported, label `[Human]`, scroll top, inject `http://localhost:PORT/detect.js`, wait 2-3 seconds, read `impeccable` console messages, then stop the live server.
5. For multi-view targets, inject on 3-5 representative pages.

Return: CLI findings JSON/counts, browser console findings if applicable, false positives, and skipped/failed browser steps with concrete reasons.

After Assessment B returns usable CLI findings, reuse them. Do not rerun `detect.mjs` in the parent unless Assessment B failed, was truncated, or omitted count, rule names, or file locations.

### Generate Combined Critique Report

Synthesize both assessments into a single report. Do NOT simply concatenate. Weave the findings together, noting where the LLM review and detector agree, where the detector caught issues the LLM missed, and where detector findings are false positives.

The chat response is the primary user-facing deliverable. Present the full structured critique below in chat; do not replace it with a summary and a link. The persisted snapshot is only an archive/backlog for later commands.

Structure your feedback as a design director would:

#### Report header provenance

The report's first line MUST declare how the assessments were run, so a degraded run is never silent:
- Dual-agent: `Method: dual-agent (A: <agent-id> · B: <agent-id>)`
- Degraded: `⚠️ DEGRADED: single-context (<reason, e.g. no sub-agent tool exposed>)`

#### Design Health Score
> *Consult the [Heuristics Scoring Guide](#heuristics-scoring-guide) section below.*

Present the Nielsen's 10 heuristics scores as a table:

| # | Heuristic | Score | Key Issue |
|---|-----------|-------|-----------|
| 1 | Visibility of System Status | ? | [specific finding or "n/a" if solid] |
| 2 | Match System / Real World | ? | |
| 3 | User Control and Freedom | ? | |
| 4 | Consistency and Standards | ? | |
| 5 | Error Prevention | ? | |
| 6 | Recognition Rather Than Recall | ? | |
| 7 | Flexibility and Efficiency | ? | |
| 8 | Aesthetic and Minimalist Design | ? | |
| 9 | Error Recovery | ? | |
| 10 | Help and Documentation | ? | |
| **Total** | | **??/[applicable max]** | **[Rating band]** |

The applicable maximum is 4 times the number of heuristics you actually scored: **/40** when all ten apply, **/32** when two are `n/a`. Never print `/40` over a partial set.

Be honest with scores. A 4 means genuinely excellent. Most real interfaces score 20-32 out of 40.

**Mode applicability**: heuristics 7 (Flexibility and Efficiency) and 10 (Help and Documentation) may be scored `n/a` on Persuade and Experience surfaces (landing pages, campaigns, portfolios, bodies of work), as may any other heuristic that genuinely cannot apply to the surface under review. Write `n/a` in the Score cell with a one-line reason, and renormalize the total to the applicable maximum (e.g. **24/32** when two heuristics are n/a) so the rating band stays proportional. The persisted snapshot must record the applicable maximum and which heuristics were scored n/a.

#### Design Specificity Verdict

**Start here.** Does the result feel authored for this product, or category-interchangeable?

**LLM assessment**: Your unanchored evaluation of design specificity. Cover overall coherence, structural sameness, category-interchangeable choices, and missed opportunities for product character.

**Deterministic scan**: Summarize what the automated detector found, with counts and file locations. Note any additional issues the detector caught that you missed, and flag any false positives.

**Visual overlays** (if injection succeeded): Tell the user that overlays are now visible in the **[Human]** tab in their browser, highlighting the detected issues. Summarize what the console output reported. If browser visualization was attempted but injection failed, say that no reliable user-visible overlay is available and report the fallback signal instead.

#### Overall Impression
A brief gut reaction: what works, what doesn't, and the single biggest opportunity.

#### What's Working
Highlight 2-3 things done well. Be specific about why they work.

#### Priority Issues
The 3-5 most impactful design problems, ordered by importance.

For each issue, tag with **P0-P3 severity** (see [Issue Severity below](#issue-severity-p0p3) for definitions):
- **[P?] What**: Name the problem clearly
- **Why it matters**: How this hurts users or undermines goals
- **Fix**: What to do about it (be concrete)
- **Suggested command**: Which command could address this (from: /impeccable adapt, /impeccable animate, /impeccable audit, /impeccable bolder, /impeccable clarify, /impeccable colorize, /impeccable critique, /impeccable delight, /impeccable distill, /impeccable document, /impeccable harden, /impeccable layout, /impeccable onboard, /impeccable optimize, /impeccable overdrive, /impeccable polish, /impeccable quieter, /impeccable shape, /impeccable typeset)

#### Persona Red Flags
> *Consult the [Personas reference](#persona-based-design-testing) below.*

Auto-select 2-3 personas most relevant to this interface type (use the selection table in the reference). If `.kiro/settings.json` contains a `## Design Context` section from `impeccable init`, also generate 1-2 project-specific personas from the audience/brand info.

For each selected persona, walk through the primary user action and list specific red flags found:

**Alex (Power User)**: No keyboard shortcuts detected. Form requires 8 clicks for primary action. Forced modal onboarding. High abandonment risk.

**Jordan (First-Timer)**: Icon-only nav in sidebar. Technical jargon in error messages ("404 Not Found"). No visible help. Will abandon at step 2.

Be specific. Name the exact elements and interactions that fail each persona. Don't write generic persona descriptions; write what broke for them.

#### Minor Observations
Quick notes on smaller issues worth addressing.

#### Questions to Consider
Provocative questions that might unlock better solutions:
- "What if the primary action were more prominent?"
- "Does this need to feel this complex?"
- "What would a confident version of this look like?"

**Remember**:
- Be direct. Vague feedback wastes everyone's time.
- Be specific. "The submit button," not "some elements."
- Say what's wrong AND why it matters to users.
- Give concrete suggestions. Cut "consider exploring..." entirely.
- Prioritize ruthlessly. If everything is important, nothing is.
- Don't soften criticism. Developers need honest feedback to ship great design.

### Persist the Snapshot

Once the report above is finalized, write it to `.impeccable/critique/` so the user can refer back, and so `/impeccable polish` can pick up the priority issues without a copy-paste.

Skip this step if the Setup slug was null (vague or root-level target).

1. **Write the body to a temp file** so you can pipe it to the helper. Use the full critique report (heuristic table, design-specificity verdict, priority issues, persona red flags, minor observations, and questions), but stop before the "Ask the User" / "Recommended Actions" sections that come later.

2. **Pass the structured metadata** through `IMPECCABLE_CRITIQUE_META` (JSON), then run the write command:
   ```bash
   IMPECCABLE_CRITIQUE_META='{"target":"<user phrasing>","total_score":<n>,"max_score":<n>,"na_heuristics":"<comma-separated numbers, or empty>","p0_count":<n>,"p1_count":<n>}' \
     node .kiro/skills/impeccable/scripts/critique-storage.mjs write "<resolved target>" <body-file>
   ```
   `max_score` is the applicable maximum from the heuristic table (40 when every heuristic applied), so a later run can tell a renormalized total from a full one. The helper prints the absolute path it wrote.

3. **Delete the temp body file** after the write attempt completes, whether the write succeeded or failed. If deletion fails, mention `temp-file cleanup failed: <reason>` briefly in the final output, but do not block the critique.

4. **Read the trend** for context:
   ```bash
   node .kiro/skills/impeccable/scripts/critique-storage.mjs trend "<resolved target>" 5
   ```
   This returns a JSON array of the last 5 frontmatter entries (including the one you just wrote).

5. **Append a single line to the user-visible output**, after the report and before the questions:

   > **Trend for `<slug>` (last 5 runs): 24 → 28 → 32 → 29 → 32 (out of 40)**
   > Wrote `.impeccable/critique/<filename>`.

   Read `max_score` on each trend entry. When every entry shares one maximum, state it once as above. When they differ, print each score with its own denominator (`24/32 → 30/40`) and note that the runs scored different heuristic sets, so the line is not a like-for-like comparison. Treat a missing `max_score` on an older entry as 40.

   If this is the first run for the slug, the trend is just one score; say so: "First run for this target, no trend yet."

This is fire-and-forget. Do not show the user the helper's JSON output; only the human-readable trend line and the written path. Failures here should not block the rest of the flow; print the error and move on.

### Ask the User

**After presenting findings**, use targeted questions based on what was actually found. ask the user directly to clarify what you cannot infer. These answers will shape the action plan.

Ask questions along these lines (adapt to the specific findings; do NOT ask generic questions):

1. **Priority direction**: Based on the issues found, ask which category matters most to the user right now. For example: "I found problems with visual hierarchy, color usage, and information overload. Which area should we tackle first?" Offer the top 2-3 issue categories as options.

2. **Design intent**: If the critique found a tonal mismatch, ask whether it was intentional. For example: "The interface feels clinical and corporate. Is that the intended tone, or should it feel warmer/bolder/more playful?" Offer 2-3 tonal directions as options based on what would fix the issues found.

3. **Scope**: Ask how much the user wants to take on. For example: "I found N issues. Want to address everything, or focus on the top 3?" Offer scope options like "Top 3 only", "All issues", "Critical issues only".

4. **Constraints** (optional; only ask if relevant): If the findings touch many areas, ask if anything is off-limits. For example: "Should any sections stay as-is?" This prevents the plan from touching things the user considers done.

**Rules for questions**:
- Every question must reference specific findings from the report. Never ask generic "who is your audience?" questions.
- Keep it to 2-4 questions maximum. Respect the user's time.
- Offer concrete options, not open-ended prompts.
- If findings are straightforward (e.g., only 1-2 clear issues), skip questions and go directly to Recommended Actions.

### Recommended Actions

**After receiving the user's answers**, present a prioritized action summary reflecting the user's priorities and scope from Ask the User.

#### Action Summary

List recommended commands in priority order, based on the user's answers:

1. **`/command-name`**: Brief description of what to fix (specific context from critique findings)
2. **`/command-name`**: Brief description (specific context)
...

**Rules for recommendations**:
- Only recommend commands from: /impeccable adapt, /impeccable animate, /impeccable audit, /impeccable bolder, /impeccable clarify, /impeccable colorize, /impeccable critique, /impeccable delight, /impeccable distill, /impeccable document, /impeccable harden, /impeccable layout, /impeccable onboard, /impeccable optimize, /impeccable overdrive, /impeccable polish, /impeccable quieter, /impeccable shape, /impeccable typeset
- Order by the user's stated priorities first, then by impact
- Each item's description should carry enough context that the command knows what to focus on
- Map each Priority Issue to the appropriate command
- Skip commands that would address zero issues
- If the user chose a limited scope, only include items within that scope
- If the user marked areas as off-limits, exclude commands that would touch those areas
- End with `/impeccable polish` as the final step if any fixes were recommended

After presenting the summary, tell the user:

> You can ask me to run these one at a time, all at once, or in any order you prefer.
>
> Re-run `/impeccable critique` after fixes to see your score improve.

---

## Reference Material

The sections below were previously separate reference files (`cognitive-load.md`, `heuristics-scoring.md`, `personas.md`). They live inline now so the critique flow has all its deep context in one place.

### Cognitive Load Assessment

Cognitive load is the total mental effort required to use an interface. Overloaded users make mistakes, get frustrated, and leave. This reference helps identify and fix cognitive overload.

---

#### Three Types of Cognitive Load

##### Intrinsic Load: The Task Itself
Complexity inherent to what the user is trying to do. You can't eliminate this, but you can structure it.

**Manage it by**:
- Breaking complex tasks into discrete steps
- Providing scaffolding (templates, defaults, examples)
- Progressive disclosure: show what's needed now, hide the rest
- Grouping related decisions together

##### Extraneous Load: Bad Design
Mental effort caused by poor design choices. **Eliminate this ruthlessly.** It's pure waste.

**Common sources**:
- Confusing navigation that requires mental mapping
- Unclear labels that force users to guess meaning
- Visual clutter competing for attention
- Inconsistent patterns that prevent learning
- Unnecessary steps between user intent and result

##### Germane Load: Learning Effort
Mental effort spent building understanding. This is *good* cognitive load; it leads to mastery.

**Support it by**:
- Progressive disclosure that reveals complexity gradually
- Consistent patterns that reward learning
- Feedback that confirms correct understanding
- Onboarding that teaches through action, not walls of text

---

#### Cognitive Load Checklist

Evaluate the interface against these 8 items:

- [ ] **Single focus**: Can the user complete their primary task without distraction from competing elements?
- [ ] **Chunking**: Is information presented in digestible groups (≤4 items per group)?
- [ ] **Grouping**: Are related items visually grouped together (proximity, borders, shared background)?
- [ ] **Visual hierarchy**: Is it immediately clear what's most important on the screen?
- [ ] **One thing at a time**: Can the user focus on a single decision before moving to the next?
- [ ] **Minimal choices**: Are decisions simplified (≤4 visible options at any decision point)?
- [ ] **Working memory**: Does the user need to remember information from a previous screen to act on the current one?
- [ ] **Progressive disclosure**: Is complexity revealed only when the user needs it?

**Scoring**: Count the failed items. 0–1 failures = low cognitive load (good). 2–3 = moderate (address soon). 4+ = high cognitive load (critical fix needed).

---

#### The Working Memory Rule

**Humans can hold ≤4 items in working memory at once** (Miller's Law revised by Cowan, 2001).

At any decision point, count the number of distinct options, actions, or pieces of information a user must simultaneously consider:
- **≤4 items**: Within working memory limits, manageable
- **5–7 items**: Pushing the boundary; consider grouping or progressive disclosure
- **8+ items**: Overloaded; users will skip, misclick, or abandon

**Practical applications**:
- Action buttons: 1 primary, 1–2 secondary, group the rest in a menu
- Navigation menus: ≤5 top-level items (group the rest under clear categories)
- Long-form articles: one reading path; gather related links into a single block at the end instead of scattering them mid-flow
- Documentation sidebars: ≤4 sibling choices visible per level before grouping kicks in
- Portfolio and gallery indexes: one decision per screen (which piece to open), not filter, sort, and tag controls all at once

---

#### Common Cognitive Load Violations

##### 1. The Wall of Options
**Problem**: Presenting 10+ choices at once with no hierarchy.
**Fix**: Group into categories, highlight recommended, use progressive disclosure.

##### 2. The Memory Bridge
**Problem**: User must remember info from step 1 to complete step 3.
**Fix**: Keep relevant context visible, or repeat it where it's needed.

##### 3. The Hidden Navigation
**Problem**: User must build a mental map of where things are.
**Fix**: Always show current location (breadcrumbs, active states, progress indicators).

##### 4. The Jargon Barrier
**Problem**: Technical or domain language forces translation effort.
**Fix**: Use plain language. If domain terms are unavoidable, define them inline.

##### 5. The Visual Noise Floor
**Problem**: Every element has the same visual weight; nothing stands out.
**Fix**: Establish clear hierarchy: one primary element, 2–3 secondary, everything else muted.

##### 6. The Inconsistent Pattern
**Problem**: Similar actions work differently in different places.
**Fix**: Standardize interaction patterns. Same type of action = same type of UI.

##### 7. The Multi-Task Demand
**Problem**: Interface requires processing multiple simultaneous inputs (reading + deciding + navigating).
**Fix**: Sequence the steps. Let the user do one thing at a time.

##### 8. The Context Switch
**Problem**: User must jump between screens/tabs/modals to gather info for a single decision.
**Fix**: Co-locate the information needed for each decision. Reduce back-and-forth.

---

### Heuristics Scoring Guide

Score each of Nielsen's 10 Usability Heuristics on a 0–4 scale. Be honest: a 4 means genuinely excellent, not "good enough."

#### Nielsen's 10 Heuristics

##### 1. Visibility of System Status

Keep users informed about what's happening through timely, appropriate feedback.

**Check for**:
- Loading indicators during async operations
- Confirmation of user actions (save, submit, delete)
- Progress indicators for multi-step processes
- Current location in navigation (breadcrumbs, active states)
- Form validation feedback (inline, not just on submit)

**Scoring**:
| Score | Criteria |
|-------|----------|
| 0 | No feedback; user is guessing what happened |
| 1 | Rare feedback; most actions produce no visible response |
| 2 | Partial; some states communicated, major gaps remain |
| 3 | Good; most operations give clear feedback, minor gaps |
| 4 | Excellent; every action confirms, progress is always visible |

##### 2. Match Between System and Real World

Speak the user's language. Follow real-world conventions. Information appears in natural, logical order.

**Check for**:
- Familiar terminology (no unexplained jargon)
- Logical information order matching user expectations
- Recognizable icons and metaphors
- Domain-appropriate language for the target audience
- Natural reading flow (left-to-right, top-to-bottom priority)

**Scoring**:
| Score | Criteria |
|-------|----------|
| 0 | Pure tech jargon, alien to users |
| 1 | Mostly confusing; requires domain expertise to navigate |
| 2 | Mixed; some plain language, some jargon leaks through |
| 3 | Mostly natural; occasional term needs context |
| 4 | Speaks the user's language fluently throughout |

##### 3. User Control and Freedom

Users need a clear "emergency exit" from unwanted states without extended dialogue.

**Check for**:
- Undo/redo functionality
- Cancel buttons on forms and modals
- Clear navigation back to safety (home, previous)
- Easy way to clear filters, search, selections
- Escape from long or multi-step processes

**Scoring**:
| Score | Criteria |
|-------|----------|
| 0 | Users get trapped; no way out without refreshing |
| 1 | Difficult exits; must find obscure paths to escape |
| 2 | Some exits; main flows have escape, edge cases don't |
| 3 | Good control; users can exit and undo most actions |
| 4 | Full control; undo, cancel, back, and escape everywhere |

##### 4. Consistency and Standards

Users shouldn't wonder whether different words, situations, or actions mean the same thing.

**Check for**:
- Consistent terminology throughout the interface
- Same actions produce same results everywhere
- Platform conventions followed (standard UI patterns)
- Visual consistency (colors, typography, spacing, components)
- Consistent interaction patterns (same gesture = same behavior)

**Scoring**:
| Score | Criteria |
|-------|----------|
| 0 | Inconsistent everywhere; feels like different products stitched together |
| 1 | Many inconsistencies; similar things look/behave differently |
| 2 | Partially consistent; main flows match, details diverge |
| 3 | Mostly consistent; occasional deviation, nothing confusing |
| 4 | Fully consistent; cohesive system, predictable behavior |

##### 5. Error Prevention

Better than good error messages is a design that prevents problems in the first place.

**Check for**:
- Confirmation before destructive actions (delete, overwrite)
- Constraints preventing invalid input (date pickers, dropdowns)
- Smart defaults that reduce errors
- Clear labels that prevent misunderstanding
- Autosave and draft recovery

**Scoring**:
| Score | Criteria |
|-------|----------|
| 0 | Errors easy to make; no guardrails anywhere |
| 1 | Few safeguards; some inputs validated, most aren't |
| 2 | Partial prevention; common errors caught, edge cases slip |
| 3 | Good prevention; most error paths blocked proactively |
| 4 | Excellent; errors nearly impossible through smart constraints |

##### 6. Recognition Rather Than Recall

Minimize memory load. Make objects, actions, and options visible or easily retrievable.

**Check for**:
- Visible options (not buried in hidden menus)
- Contextual help when needed (tooltips, inline hints)
- Recent items and history
- Autocomplete and suggestions
- Labels on icons (not icon-only navigation)

**Scoring**:
| Score | Criteria |
|-------|----------|
| 0 | Heavy memorization; users must remember paths and commands |
| 1 | Mostly recall; many hidden features, few visible cues |
| 2 | Some aids; main actions visible, secondary features hidden |
| 3 | Good recognition; most things discoverable, few memory demands |
| 4 | Everything discoverable; users never need to memorize |

##### 7. Flexibility and Efficiency of Use

Accelerators, invisible to novices, speed up expert interaction.

**Check for**:
- Keyboard shortcuts for common actions
- Customizable interface elements
- Recent items and favorites
- Bulk/batch actions
- Power user features that don't complicate the basics

**Scoring**:
| Score | Criteria |
|-------|----------|
| 0 | One rigid path; no shortcuts or alternatives |
| 1 | Limited flexibility; few alternatives to the main path |
| 2 | Some shortcuts; basic keyboard support, limited bulk actions |
| 3 | Good accelerators; keyboard nav, some customization |
| 4 | Highly flexible; multiple paths, power features, customizable |

##### 8. Aesthetic and Minimalist Design

Interfaces should not contain irrelevant or rarely needed information. Every element should serve a purpose.

**Check for**:
- Only necessary information visible at each step
- Clear visual hierarchy directing attention
- Purposeful use of color and emphasis
- No decorative clutter competing for attention
- Focused, uncluttered layouts

**Scoring**:
| Score | Criteria |
|-------|----------|
| 0 | Overwhelming; everything competes for attention equally |
| 1 | Cluttered; too much noise, hard to find what matters |
| 2 | Some clutter; main content clear, periphery noisy |
| 3 | Mostly clean; focused design, minor visual noise |
| 4 | Perfectly minimal; every element earns its pixel |

##### 9. Help Users Recognize, Diagnose, and Recover from Errors

Error messages should use plain language, precisely indicate the problem, and constructively suggest a solution.

**Check for**:
- Plain language error messages (no error codes for users)
- Specific problem identification ("Email is missing @" not "Invalid input")
- Actionable recovery suggestions
- Errors displayed near the source of the problem
- Non-blocking error handling (don't wipe the form)

**Scoring**:
| Score | Criteria |
|-------|----------|
| 0 | Cryptic errors; codes, jargon, or no message at all |
| 1 | Vague errors; "Something went wrong" with no guidance |
| 2 | Clear but unhelpful; names the problem but not the fix |
| 3 | Clear with suggestions; identifies problem and offers next steps |
| 4 | Perfect recovery; pinpoints issue, suggests fix, preserves user work |

##### 10. Help and Documentation

Even if the system is usable without docs, help should be easy to find, task-focused, and concise.

**Check for**:
- Searchable help or documentation
- Contextual help (tooltips, inline hints, guided tours)
- Task-focused organization (not feature-organized)
- Concise, scannable content
- Easy access without leaving current context

**Scoring**:
| Score | Criteria |
|-------|----------|
| 0 | No help available anywhere |
| 1 | Help exists but hard to find or irrelevant |
| 2 | Basic help; FAQ or docs exist, not contextual |
| 3 | Good documentation; searchable, mostly task-focused |
| 4 | Excellent contextual help; right info at the right moment |

---

#### Score Summary

**Total possible**: 40 points (10 heuristics × 4 max)

| Score Range | Rating | What It Means |
|-------------|--------|---------------|
| 36–40 | Excellent | Minor polish only; ship it |
| 28–35 | Good | Address weak areas, solid foundation |
| 20–27 | Acceptable | Significant improvements needed before users are happy |
| 12–19 | Poor | Major UX overhaul required; core experience broken |
| 0–11 | Critical | Redesign needed; unusable in current state |

When heuristics were scored `n/a`, the maximum is lower than 40; read the band off the percentage instead of the raw number (90%+ Excellent, 70%+ Good, 50%+ Acceptable, 30%+ Poor, below that Critical). 24/32 is 75%, so Good.

---

#### Issue Severity (P0–P3)

Tag each individual issue found during scoring with a priority level:

| Priority | Name | Description | Action |
|----------|------|-------------|--------|
| **P0** | Blocking | Prevents task completion entirely | Fix immediately; this is a showstopper |
| **P1** | Major | Causes significant difficulty or confusion | Fix before release |
| **P2** | Minor | Annoyance, but workaround exists | Fix in next pass |
| **P3** | Polish | Nice-to-fix, no real user impact | Fix if time permits |

**Tip**: If you're unsure between two levels, ask: "Would a user contact support about this?" If yes, it's at least P1.

---

### Persona-Based Design Testing

Test the interface through the eyes of 5 distinct user archetypes. Each persona exposes different failure modes that a single "design director" perspective would miss.

**How to use**: Select 2–3 personas most relevant to the interface being critiqued. Walk through the primary user action as each persona. Report specific red flags, not generic concerns.

---

#### 1. Impatient Power User: "Alex"

**Profile**: Expert with similar products. Expects efficiency, hates hand-holding. Will find shortcuts or leave.

**Behaviors**:
- Skips all onboarding and instructions
- Looks for keyboard shortcuts immediately
- Tries to bulk-select, batch-edit, and automate
- Gets frustrated by required steps that feel unnecessary
- Abandons if anything feels slow or patronizing

**Test Questions**:
- Can Alex complete the core task in under 60 seconds?
- Are there keyboard shortcuts for common actions?
- Can onboarding be skipped entirely?
- Do modals have keyboard dismiss (Esc)?
- Is there a "power user" path (shortcuts, bulk actions)?

**Red Flags** (report these specifically):
- Forced tutorials or unskippable onboarding
- No keyboard navigation for primary actions
- Slow animations that can't be skipped
- One-item-at-a-time workflows where batch would be natural
- Redundant confirmation steps for low-risk actions

---

#### 2. Confused First-Timer: "Jordan"

**Profile**: Never used this type of product. Needs guidance at every step. Will abandon rather than figure it out.

**Behaviors**:
- Reads all instructions carefully
- Hesitates before clicking anything unfamiliar
- Looks for help or support constantly
- Misunderstands jargon and abbreviations
- Takes the most literal interpretation of any label

**Test Questions**:
- Is the first action obviously clear within 5 seconds?
- Are all icons labeled with text?
- Is there contextual help at decision points?
- Does terminology assume prior knowledge?
- Is there a clear "back" or "undo" at every step?

**Red Flags** (report these specifically):
- Icon-only navigation with no labels
- Technical jargon without explanation
- No visible help option or guidance
- Ambiguous next steps after completing an action
- No confirmation that an action succeeded

---

#### 3. Accessibility-Dependent User: "Sam"

**Profile**: Uses screen reader (VoiceOver/NVDA), keyboard-only navigation. May have low vision, motor impairment, or cognitive differences.

**Behaviors**:
- Tabs through the interface linearly
- Relies on ARIA labels and heading structure
- Cannot see hover states or visual-only indicators
- Needs adequate color contrast (4.5:1 minimum)
- May use browser zoom up to 200%

**Test Questions**:
- Can the entire primary flow be completed keyboard-only?
- Are all interactive elements focusable with visible focus indicators?
- Do images have meaningful alt text?
- Is color contrast WCAG AA compliant (4.5:1 for text)?
- Does the screen reader announce state changes (loading, success, errors)?

**Red Flags** (report these specifically):
- Click-only interactions with no keyboard alternative
- Missing or invisible focus indicators
- Meaning conveyed by color alone (red = error, green = success)
- Unlabeled form fields or buttons
- Time-limited actions without extension option
- Custom components that break screen reader flow

---

#### 4. Deliberate Stress Tester: "Riley"

**Profile**: Methodical user who pushes interfaces beyond the happy path. Tests edge cases, tries unexpected inputs, and probes for gaps in the experience.

**Behaviors**:
- Tests edge cases intentionally (empty states, long strings, special characters)
- Submits forms with unexpected data (emoji, RTL text, very long values)
- Tries to break workflows by navigating backwards, refreshing mid-flow, or opening in multiple tabs
- Looks for inconsistencies between what the UI promises and what actually happens
- Documents problems methodically

**Test Questions**:
- What happens at the edges (0 items, 1000 items, very long text)?
- Do error states recover gracefully or leave the UI in a broken state?
- What happens on refresh mid-workflow? Is state preserved?
- Are there features that appear to work but produce broken results?
- How does the UI handle unexpected input (emoji, special chars, paste from Excel)?

**Red Flags** (report these specifically):
- Features that appear to work but silently fail or produce wrong results
- Error handling that exposes technical details or leaves UI in a broken state
- Empty states that show nothing useful ("No results" with no guidance)
- Workflows that lose user data on refresh or navigation
- Inconsistent behavior between similar interactions in different parts of the UI

---

#### 5. Distracted Mobile User: "Casey"

**Profile**: Using phone one-handed on the go. Frequently interrupted. Possibly on a slow connection.

**Behaviors**:
- Uses thumb only; prefers bottom-of-screen actions
- Gets interrupted mid-flow and returns later
- Switches between apps frequently
- Has limited attention span and low patience
- Types as little as possible, prefers taps and selections

**Test Questions**:
- Are primary actions in the thumb zone (bottom half of screen)?
- Is state preserved if the user leaves and returns?
- Does it work on slow connections (3G)?
- Can forms use autocomplete and smart defaults?
- Are touch targets at least 44×44pt?

**Red Flags** (report these specifically):
- Important actions positioned at the top of the screen (unreachable by thumb)
- No state persistence; progress lost on tab switch or interruption
- Large text inputs required where selection would work
- Heavy assets loading on every page (no lazy loading)
- Tiny tap targets or targets too close together

---

#### Selecting Personas

Choose personas based on the interface type:

| Interface Type | Primary Personas | Why |
|---------------|-----------------|-----|
| Landing page / marketing | Jordan, Riley, Casey | First impressions, trust, mobile |
| Dashboard / admin | Alex, Sam | Power users, accessibility |
| E-commerce / checkout | Casey, Riley, Jordan | Mobile, edge cases, clarity |
| Onboarding flow | Jordan, Casey | Confusion, interruption |
| Data-heavy / analytics | Alex, Sam | Efficiency, keyboard nav |
| Form-heavy / wizard | Jordan, Sam, Casey | Clarity, accessibility, mobile |

---

#### Project-Specific Personas

If `.kiro/settings.json` contains a `## Design Context` section (generated by `impeccable init`), derive 1–2 additional personas from the audience and brand information:

1. Read the target audience description
2. Identify the primary user archetype not covered by the 5 predefined personas
3. Create a persona following this template:

```
##### [Role]: "[Name]"

**Profile**: [2-3 key characteristics derived from Design Context]

**Behaviors**: [3-4 specific behaviors based on the described audience]

**Red Flags**: [3-4 things that would alienate this specific user type]
```

Only generate project-specific personas when real Design Context data is available. Don't invent audience details; use the 5 predefined personas when no context exists.

---

## 📄 `reference/document.md`

Generate a `DESIGN.md` file at the project root that captures the current visual design system, so AI agents generating new screens stay on-brand.

DESIGN.md follows the [official DESIGN.md format spec](https://raw.githubusercontent.com/google-labs-code/design.md/main/docs/spec.md): optional YAML frontmatter carrying machine-readable design tokens, followed by up to eight markdown sections in a fixed order. **Tokens are normative; prose provides context for how to apply them.** Sections may be omitted when not relevant, but those present stay in the specified order. Use the canonical headings below so the file remains portable across DESIGN.md-aware tools.

## The frontmatter: token schema

The YAML frontmatter is the machine-readable layer. It's what Stitch's linter validates and what the live panel renders tiles from. Keep it tight; every entry should correspond to a token the project actually uses.

```yaml
---
name: <project title>
description: <one-line tagline>
colors:
  primary: "#b8422e"
  neutral-bg: "#faf7f2"
  # ...one entry per extracted color; key = descriptive slug
typography:
  display:
    fontFamily: "Cormorant Garamond, Georgia, serif"
    fontSize: "clamp(2.5rem, 7vw, 4.5rem)"
    fontWeight: 300
    lineHeight: 1
    letterSpacing: "normal"
  body:
    # ...
rounded:
  sm: "4px"
  md: "8px"
spacing:
  sm: "8px"
  md: "16px"
components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.neutral-bg}"
    rounded: "{rounded.sm}"
    padding: "16px 48px"
  button-primary-hover:
    backgroundColor: "{colors.primary-deep}"
---
```

Rules that matter:

- **Token refs** use `{path.to.token}` (e.g. `{colors.primary}`, `{rounded.md}`). Components may reference primitives; primitives may not reference each other.
- **Colors accept any valid CSS color string.** Hex is the recommended default for portability, but preserve an incumbent `rgb()`, `hsl()`, `oklch()`, wide-gamut, or mixed-color value when it is the project's normative source. Never split the source of truth without explicit reason.
- **Component sub-tokens** are limited to 8 props: `backgroundColor`, `textColor`, `typography`, `rounded`, `padding`, `size`, `height`, `width`. Shadows, motion, focus rings, backdrop-filter: none of those fit. Carry them in the sidecar (Step 4b).
- **Scale keys are open-ended.** Use whatever names the project already uses (`oxblood-deep`, `surface-container-low`). Don't rename to Material defaults.
- **Variants are naming convention, not schema.** `button-primary` / `button-primary-hover` / `button-primary-active` as sibling keys.

## The markdown body: eight sections (canonical order)

1. `## Overview`
2. `## Colors`
3. `## Typography`
4. `## Layout`
5. `## Elevation & Depth`
6. `## Shapes`
7. `## Components`
8. `## Do's and Don'ts`

Omit irrelevant sections rather than filling them with invented rules. Put responsive layout in Layout, depth in Elevation & Depth, radius and form language in Shapes, and per-component behavior in Components. Unknown sections are preserved by the format, but new visual guidance should use the canonical structure whenever it fits.

## When to run

- New-work found a coherent incumbent visual system but no `DESIGN.md`.
- The first implementation of a new world is complete and its provisional decisions need to be carbonized.
- An existing `DESIGN.md` is stale (the design has drifted).
- Before a large redesign, to capture the current state as a reference.

If a `DESIGN.md` already exists, **do not silently overwrite it**. Show the user the existing file and ask the user directly to clarify what you cannot infer. whether to refresh, overwrite, or merge.

## Two paths

- **Scan mode** (default): the project has design tokens, components, or rendered output. Extract, then confirm descriptive language. Use when there's code to analyze.
- **Seed mode**: the project is pre-implementation. Ensure PRODUCT.md exists, then reuse new-work's visual-world workshop and write its directional DESIGN.md seed. Re-run in scan mode once there's code.

Decide by scanning first (Scan mode Step 1). If the scan finds no tokens, no component files, and no rendered site, offer seed mode; don't silently switch. `/impeccable document --seed` requests new-work's world workshop, but it does not authorize replacing coherent code: when an incumbent system exists, offer scan mode or route an explicit identity-replacement request through new-work.

## Scan mode (approach C: auto-extract, then confirm descriptive language)

### Step 1: Find the design assets

Search the codebase in priority order:

1. **CSS custom properties**: grep for `--color-`, `--font-`, `--spacing-`, `--radius-`, `--shadow-`, `--ease-`, `--duration-` declarations in CSS files (usually `src/styles/`, `public/css/`, `app/globals.css`, etc.). Record name, value, and the file it's defined in.
2. **Tailwind config**: if `tailwind.config.{js,ts,mjs}` exists, read the `theme.extend` block for colors, fontFamily, spacing, borderRadius, boxShadow.
3. **CSS-in-JS theme files**: styled-components, emotion, vanilla-extract, stitches; look for `theme.ts`, `tokens.ts`, or equivalent.
4. **Design token files**: `tokens.json`, `design-tokens.json`, Style Dictionary output, W3C token community group format.
5. **Component library**: scan the main button, card, input, navigation, dialog components. Note their variant APIs and default styles.
6. **Global stylesheet**: the root CSS file usually has the base typography and color assignments.
7. **Visible rendered output**: if browser automation tools are available, load the live site and sample computed styles from key elements (body, h1, a, button, .card). This catches values that tokens miss.

### Step 2: Auto-extract what can be auto-extracted

Build a structured draft from the discovered tokens. For each token class:

- **Colors**: Group into Primary / Secondary / Tertiary / Neutral (the Material-derived roles Stitch uses). If the project only has one accent, express it as Primary + Neutral; omit Secondary and Tertiary rather than inventing them.
- **Typography**: Map observed sizes and weights to the Material hierarchy (display / headline / title / body / label). Note font-family stacks and the scale ratio.
- **Elevation**: Catalogue the shadow vocabulary. If the project is flat and uses tonal layering instead, that's a valid answer; state it explicitly.
- **Components**: For each common component (button, card, input, chip, list item, tooltip, nav), extract shape (radius), color assignment, hover/focus treatment, internal padding.
- **Layout + spacing**: Extract grid, container, breakpoint, rhythm, and density behavior into Layout.
- **Shapes**: Extract radius, corner, border, clipping, and recurring form behavior into Shapes.

### Step 2b: Stage the frontmatter

From the auto-extracted tokens, draft the YAML frontmatter now (you'll write it at the top of DESIGN.md in Step 4). This is the machine-readable layer: what the live panel and Stitch's linter consume.

- **Colors**: one entry per extracted color. Key = descriptive slug (`oxblood-deep`, `editorial-magenta`, not `blue-800`). Value = whichever format the project treats as canonical (OKLCH or hex; see the frontmatter rules above). Don't split the source of truth: one format in the frontmatter, don't redefine the same token in prose with a different value.
- **Typography**: one entry per role (`display`, `headline`, `title`, `body`, `label`). Typography is an object; include only the props that are real for the project (`fontFamily`, `fontSize`, `fontWeight`, `lineHeight`, `letterSpacing`, `fontFeature`, `fontVariation`).
- **Rounded / Spacing**: whatever scale steps the project actually uses, keyed by whatever scale name the project uses (`sm` / `md` / `lg`, or `surface-sm`, or numeric steps).
- **Components**: one entry per variant (`button-primary`, `button-primary-hover`, `button-ghost`). Reference primitives via `{colors.X}`, `{rounded.Y}`. If a variant needs a property Stitch's 8-prop set doesn't cover (shadow, focus ring, backdrop-filter), carry the full snippet in the sidecar instead.

Skip anything the project doesn't have. Empty scale keys or fabricated tokens pollute the spec.

### Step 3: Ask the user for qualitative language

The following require creative input that cannot be auto-extracted. Ask them in two structured rounds of no more than three questions each (or the harness's lower limit), waiting between rounds:

- **Creative North Star**: a single named metaphor for the whole system ("The Editorial Sanctuary", "The Golden State Curator", "The Lab Notebook"). Offer 2-3 options that honor PRODUCT.md's brand personality.
- **Overview voice**: mood adjectives, aesthetic philosophy in 2-3 sentences, and any confirmed visual anti-reference.
- **Color character** (for auto-extracted colors): descriptive names ("Deep Muted Teal-Navy", not "blue-800"). Suggest 2-3 options per key color based on hue/saturation.
- **Elevation philosophy**: flat/layered/lifted. If shadows exist, is their role ambient or structural?
- **Component philosophy**: the feel of buttons, cards, inputs in one phrase ("tactile and confident" vs. "refined and restrained").

Carry a line from PRODUCT.md only when it is a durable brand commitment that actually constrains the visual system. Page strategy and surface concepts do not belong here.

### Step 4: Write DESIGN.md

The file opens with the YAML frontmatter staged in Step 2b (schema documented at the top of this reference), then the markdown body using the canonical structure below.

```markdown
---
name: [Project Title]
description: [one-line tagline]
colors:
  # ... staged frontmatter from Step 2b
---

# Design System: [Project Title]

## Overview

**Creative North Star: "[Named metaphor in quotes]"**

[2-3 paragraph holistic description: personality, density, and aesthetic philosophy. Start from the North Star and work outward. State only confirmed visual rejections. End with a short **Key Characteristics:** bullet list.]

## Colors

[Describe the palette character in one sentence.]

### Primary
- **[Descriptive Name]** (#HEX / oklch(...)): [Where and why this color is used. Be specific about context, not just role.]

### Secondary (optional; omit if the project has only one accent)
- **[Descriptive Name]** (#HEX): [Role.]

### Tertiary (optional)
- **[Descriptive Name]** (#HEX): [Role.]

### Neutral
- **[Descriptive Name]** (#HEX): [Text / background / border / divider role.]
- [...]

### Named Rules (optional, powerful)
**The [Rule Name] Rule.** [Short, forceful prohibition or doctrine, e.g. "The One Voice Rule. The primary accent is used on ≤10% of any given screen. Its rarity is the point."]

## Typography

**Display Font:** [Family] (with [fallback])
**Body Font:** [Family] (with [fallback])
**Label/Mono Font:** [Family, if distinct]

**Character:** [1-2 sentence personality description of the pairing.]

### Hierarchy
- **Display** ([weight], [size/clamp], [line-height]): [Purpose; where it appears.]
- **Headline** ([weight], [size], [line-height]): [Purpose.]
- **Title** ([weight], [size], [line-height]): [Purpose.]
- **Body** ([weight], [size], [line-height]): [Purpose. Include max line length like 65–75ch if relevant.]
- **Label** ([weight], [size], [letter-spacing], [case if uppercase]): [Purpose.]

### Named Rules (optional)
**The [Rule Name] Rule.** [Short doctrine about type use.]

## Layout

[Describe the grid or spatial model, container behavior, density, responsive changes, and the spacing rhythm. Include exact values only when observed.]

## Elevation & Depth

[One paragraph: does this system use shadows, tonal layering, or a hybrid? If "no shadows", say so explicitly and describe how depth is conveyed instead.]

### Shadow Vocabulary (if applicable)
- **[Role name]** (`box-shadow: [exact value]`): [When to use it.]
- [...]

### Named Rules (optional)
**The [Rule Name] Rule.** [e.g. "The Flat-By-Default Rule. Surfaces are flat at rest. Shadows appear only as a response to state (hover, elevation, focus)."]

## Shapes

[Describe the form language: corner/radius strategy, borders, clipping, and any recurring silhouette or geometry.]

## Components

For each component, lead with a short character line, then specify shape, color assignment, states, and any distinctive behavior.

### Buttons
- **Shape:** [radius described, exact value in parens]
- **Primary:** [color assignment + padding, in semantic + exact terms]
- **Hover / Focus:** [transitions, treatments]
- **Secondary / Ghost / Tertiary (if applicable):** [brief description]

### Chips (if used)
- **Style:** [background, text color, border treatment]
- **State:** [selected / unselected, filter / action variants]

### Cards / Containers
- **Corner Style:** [radius]
- **Background:** [colors used]
- **Shadow Strategy:** [reference Elevation section]
- **Border:** [if any]
- **Internal Padding:** [scale]

### Inputs / Fields
- **Style:** [stroke, background, radius]
- **Focus:** [treatment, e.g. glow, border shift, etc.]
- **Error / Disabled:** [if applicable]

### Navigation
- **Style, typography, default/hover/active states, mobile treatment.**

### [Signature Component] (optional; if the project has a distinctive custom component worth documenting)
[Description.]

## Do's and Don'ts

Concrete visual guardrails grounded in the incumbent implementation or the user's chosen world. Lead each with "Do" or "Don't" and include exact values only when established. Do not turn a task-specific concept or surface strategy into a system-wide prohibition.

### Do:
- **Do** [specific prescription with exact values / named rule].
- **Do** [...]

### Don't:
- **Don't** [specific prohibition confirmed by the incumbent system or the user].
- **Don't** [...]
- **Don't** [...]
```

### Step 4b: Write .impeccable/design.json sidecar (extensions only)

The frontmatter owns token primitives (colors, typography, rounded, spacing, components). The sidecar at `.impeccable/design.json` carries **what Stitch's schema can't hold**: tonal ramps per color, shadow/elevation tokens, motion tokens, breakpoints, full component HTML/CSS snippets (the panel renders these into a shadow DOM), and narrative (north star, rules, do's/don'ts). It extends the frontmatter, it doesn't duplicate it.

Regenerate the sidecar whenever you regenerate root `DESIGN.md`. If the user only asks to refresh the sidecar (e.g., from the live panel's stale-hint), preserve `DESIGN.md` and write only `.impeccable/design.json`.

#### Schema

```json
{
  "schemaVersion": 2,
  "generatedAt": "ISO-8601 string",
  "title": "Design System: [Project Title]",
  "extensions": {
    "colorMeta": {
      "primary":        { "role": "primary",  "displayName": "Editorial Magenta", "canonical": "oklch(60% 0.25 350)", "tonalRamp": ["...", "...", "..."] },
      "cool-paper": { "role": "neutral",  "displayName": "Cool Paper",    "canonical": "oklch(96% 0.005 230)", "tonalRamp": ["...", "...", "..."] }
    },
    "typographyMeta": {
      "display": { "displayName": "Display", "purpose": "Hero headlines only." }
    },
    "shadows": [
      { "name": "ambient-low", "value": "0 4px 24px rgba(0,0,0,0.12)", "purpose": "Diffuse hover glow under accent elements." }
    ],
    "motion": [
      { "name": "ease-standard", "value": "cubic-bezier(0.4, 0, 0.2, 1)", "purpose": "Default easing for state transitions." }
    ],
    "breakpoints": [
      { "name": "sm", "value": "640px" }
    ]
  },
  "components": [
    {
      "name": "Primary Button",
      "kind": "button | input | nav | chip | card | custom",
      "refersTo": "button-primary",
      "description": "One-line what and when.",
      "html": "<button class=\"ds-btn-primary\">SAVE CHANGES</button>",
      "css": ".ds-btn-primary { background: #191c1d; color: #fff; padding: 16px 48px; letter-spacing: 0.05em; text-transform: uppercase; font-weight: 500; border: none; border-radius: 0; transition: background 0.2s, transform 0.2s; } .ds-btn-primary:hover { background: oklch(60% 0.25 350); transform: translateY(-2px); }"
    }
  ],
  "narrative": {
    "northStar": "The Editorial Sanctuary",
    "overview": "2-3 paragraphs of the philosophy, pulled from DESIGN.md Overview section.",
    "keyCharacteristics": ["...", "..."],
    "rules": [{ "name": "The One Voice Rule", "body": "...", "section": "colors|typography|elevation" }],
    "dos":   ["Do use ..."],
    "donts": ["Don't use ..."]
  }
}
```

**What changed from schemaVersion 1.** The old sidecar carried token primitive arrays (`tokens.colors[]`, `tokens.typography[]`, etc.). Those values now live in the frontmatter. The sidecar only carries metadata that can't live in the frontmatter (tonal ramps, canonical OKLCH when the hex is an approximation, display names, role hints), keyed by the frontmatter token name (`colorMeta.<token-name>`, `typographyMeta.<token-name>`). Components still carry full HTML/CSS because Stitch's 8-prop set can't hold them.

#### Component translation rules

The `html` and `css` fields must be **self-contained, drop-in snippets** that render correctly when injected into a shadow DOM. The panel applies them directly: no post-processing, no framework runtime.

1. **Tailwind expansion.** If the source uses Tailwind (className="bg-primary text-white rounded-lg px-6 py-3"), expand every utility to literal CSS properties in the `css` string. Do **not** reference Tailwind classes; do **not** assume a Tailwind CSS bundle is loaded. Each component is self-contained.
2. **Token resolution.** If the project exposes tokens as CSS custom properties on `:root` (e.g. `--color-primary`, `--radius-md`), reference them via `var(--color-primary)`; they inherit through the shadow DOM and stay live-bound. If tokens live only in JS theme objects (styled-components, CSS-in-JS), resolve to literal values at generation time.
3. **Icons.** Inline as SVG. Do not reference Lucide/Heroicons packages, icon fonts, or `<img src="...">`. A typical icon is 16-24px; copy the SVG path data directly.
4. **States.** Include `:hover`, `:focus-visible`, and (if meaningful) `:active` rules inline. A static default-only snapshot makes the panel feel dead. Hover + focus rules in the CSS make it feel alive.
5. **Reset bloat.** Extract only the component's *distinctive* CSS (background, color, padding, border-radius, typography, transition). Skip universal resets (`box-sizing: border-box`, `line-height: inherit`, `-webkit-font-smoothing`). The panel already has a neutral canvas; don't re-ship resets.
6. **Scoped class names.** Prefix every class with `ds-` (e.g. `ds-btn-primary`, `ds-input-search`) so component CSS doesn't collide with other components' CSS in the same shadow DOM.

#### What to include

Aim for a tight set of **5-10 components** that best represent the visual system:

- **Canonical primitives (always include if the project has them):** button (each variant as a separate component entry), input/text field, navigation, chip/tag, card.
- **Signature components (include if distinctive):** the recurring custom patterns that actually define the implemented system.
- **Skip the rest.** Utility components, form building blocks, wrapper layouts: not worth documenting unless visually distinctive.

If the project has **no component library yet** (bare landing page, new project), synthesize canonical primitives from the tokens using best-practice defaults consistent with the DESIGN.md's rules. Every `.impeccable/design.json` has *something* to render, even on day zero.

#### Tonal ramps

For each color token, generate an 8-step `tonalRamp` array: dark to light, same hue and chroma, stepped lightness from ~15% to ~95%. The panel renders this as a strip under the swatch. If the project already defines a tonal scale (Material `surface-container-low` family, Tailwind-style `blue-50..blue-900`), use those values. Otherwise synthesize in OKLCH.

#### Narrative mapping

Pull directly from the DESIGN.md you just wrote:

- `narrative.northStar` → the `**Creative North Star: "..."**` line from Overview
- `narrative.overview` → the philosophy paragraphs from Overview
- `narrative.keyCharacteristics` → the bulleted `**Key Characteristics:**` list
- `narrative.rules` → every `**The [Name] Rule.** [body]` across all sections, tagged with `section`
- `narrative.dos` / `narrative.donts` → the bullet lists from Do's and Don'ts verbatim

Do not reword. The panel shows these as secondary collapsible context; the same voice that's in the Markdown carries through.

### Step 5: Confirm and refine

1. Show the user the full DESIGN.md you wrote. Briefly highlight the non-obvious creative choices (descriptive color names, atmosphere language, named rules).
2. Mention that `.impeccable/design.json` was also written alongside; the live panel will now render this project's actual button/input/nav primitives instead of generic approximations.
3. Offer to refine any section: "Want me to revise a section, add component patterns I missed, or adjust the atmosphere language?"

Your own write is the freshest source; subsequent commands in this session don't need a reload.

## Seed mode

For projects with no visual system to extract yet. Produces a user-chosen visual-world scaffold, not a fabricated token spec.

### Step 1: Route through new-work's workshop

PRODUCT.md is the prerequisite. If it is missing, load [init.md](init.md) and complete its product interview first. Do not create a visual identity without durable product context.

If PRODUCT.md exists, load [new-work.md](new-work.md) and resolve visual authority. Seed mode requires a concrete first surface: use the target the user named, or ask what they want to make first. Run new-work's **Create or replace the visual world** flow, then **Commit the world**, so the visual world and its first expression are chosen together. Stop after the directional DESIGN.md seed and surface brief; do not implement. A structured simulated user counts as the user and must get the same choice.

If new-work already completed the workshop in this session, use its chosen direction directly. Do not ask again.

### Step 2: Write seed DESIGN.md

Use the canonical section order from Scan mode. Populate the selected workshop direction and leave unresolved implementation facts as honest placeholders. The seed commits a world and its invariants; it does not pretend implementation tokens already exist.

Lead the file with:

```markdown
<!-- SEED: established with the user before implementation; re-run /impeccable document once there's code to capture the actual tokens and components. -->
```

Per-section guidance in seed mode:

- **Overview**: the chosen design thesis, layout behavior, material character, imagery stance, motion grammar, and reusable signature. Keep the selected first-surface expression in its surface brief; do not promote its composition into the global world.
- **Colors**: the selected palette strategy and roles. Include values only when the user, an existing asset, or new-work's exploration established them; otherwise mark them `[to be resolved during implementation]`.
- **Typography**: the selected type character and role relationship. Include font names only when established; otherwise mark the pairing `[to be resolved during implementation]`.
- **Layout**: the selected spatial grammar and responsive behavior, without pretending exact measurements are settled.
- **Elevation & Depth**: the selected material and depth behavior, stated as an invariant rather than inferred from a generic preset.
- **Shapes**: the selected form and corner language.
- **Components**: omit entirely; no components exist yet.
- **Do's and Don'ts**: record the durable guardrails confirmed during the world choice, not task-local refusals.

Seed mode writes a minimal frontmatter with `name` and `description` only; no colors, typography, rounded, spacing, or components yet. Real tokens land on the next Scan-mode run. Skip the `.impeccable/design.json` sidecar in seed mode for the same reason: nothing to render.

### Step 3: Confirm

1. Show the seed DESIGN.md. Call out that it is a seed (the marker is the literal commitment).
2. Tell the user: "Re-run `/impeccable document` once you have some code. That pass will extract real tokens and generate the sidecar."

Your own write is the freshest source; no reload needed.

## Style guidelines

- **Frontmatter first, prose second.** Tokens go in the YAML frontmatter; prose contextualizes them. Don't redefine a token value in two places; the frontmatter is normative.
- **Carry only durable product constraints.** A binding logo, identity asset, accessibility need, or brand commitment from PRODUCT.md may constrain DESIGN.md. Surface strategy stays in its surface brief.
- **Match the spec.** Use its eight canonical sections in order and omit any that are irrelevant. Put motion guidance with the world or component it affects rather than creating a token group the schema does not support.
- **Descriptive > technical**: "Gently curved edges (8px radius)" > "rounded-lg". Include the technical value in parens, lead with the description.
- **Functional > decorative**: for each token, explain WHERE and WHY it's used, not just WHAT it is.
- **Exact values in parens**: hex codes, px/rem values, font weights; always the number in parens alongside the description.
- **Use Named Rules**: `**The [Name] Rule.** [short doctrine]`. These are memorable, citable, and much stickier for AI consumers than bullet lists. Stitch's own outputs use them heavily ("The No-Line Rule", "The Ghost Border Fallback"). Aim for 1-3 per section.
- **Be decisive where evidence is decisive.** Use hard language for actual invariants and softer language for provisional guidance.
- **Use concrete audit tests only when they are grounded in the observed system or a confirmed user decision.** A one-sentence test beats a paragraph of principle.
- **Reference PRODUCT.md selectively.** Product truth explains why the world fits; it does not supply page composition or a visual don't-list by default.
- **Group colors by role**, not by hex-order or hue-order. Primary / Secondary / Tertiary / Neutral is the spec ordering.

## Pitfalls

- Don't paste raw CSS class names. Translate to descriptive language.
- Don't extract every token. Stop at what's actually reused; one-offs pollute the system.
- Don't invent components that don't exist. If the project only has buttons and cards, only document those.
- Don't overwrite an existing DESIGN.md without asking.
- Don't duplicate content from PRODUCT.md. DESIGN.md is strictly visual.
- Don't replace canonical sections with near-synonyms. Put layout and responsive behavior in `Layout`; put motion with the affected world or component.
- Don't rename sections even slightly. "Colors" not "Color Palette & Roles". "Typography" not "Typography Rules". Tooling parsing depends on exact headers.
- Don't duplicate token values between frontmatter and prose. If a color is in `colors.primary` as hex, the prose can name it and describe its role but should not reassert a different hex. The frontmatter is normative.
- Don't invent frontmatter token groups outside Stitch's schema (no `motion:`, `breakpoints:`, `shadows:` at the top level). Stitch's Zod schema only accepts `colors`, `typography`, `rounded`, `spacing`, `components`. Anything else belongs in the sidecar's `extensions`.

---

## 📄 `reference/hooks.md`

# /impeccable hooks

Manage the **design detector hook** for the current project.

The hook runs the impeccable design detector on direct file edits to design-relevant files (`.tsx`, `.jsx`, `.html`, `.vue`, `.svelte`, `.astro`, `.css`, `.scss`, `.sass`, `.less`, `.ts`, `.js`). Claude Code, Codex, and GitHub Copilot use a post-tool-use hook and push a short system reminder into the agent's context after the edit; findings get a correction prompt, pending issues get a re-nudge, and clean UI-ish files get a short ack unless quiet mode is on (`hook.quiet` in config). Plain `.ts` and `.js` files are still scanned, but stay quiet unless the detector finds something. Cursor uses `preToolUse` to block bad proposed writes before they land and stays silent when it allows a clean write.

The detector rules run in two tiers. The per-edit hook surfaces only the immediate tier: mechanical, unambiguous problems worth interrupting an edit for, such as broken images, overflowing or clipped content, contrast and legibility failures, gradient text, glow shadows, and design-system drift. Everything else (copy cadence, palette and typography taste, layout rhythm) is deferred to a deep pass on the `Stop` hook event, which runs the full rule set over every UI file touched in the session and surfaces the remaining findings once, deduplicated against what the per-edit pass already reported. A session with nothing left to report stops silently. Set `hook.perEditRules` to `"all"` in `.impeccable/config.json` to restore the full rule set on every edit. The Stop deep pass is wired for Claude Code and Codex, which both dispatch a native `Stop` hook event. Cursor does not get one (its stop hook is not consistently dispatched; the pre-write gate covers it), and GitHub Copilot's stop-style events do not feed context back to the model, so they keep the full detector per edit.

Every hook is a mechanical pass. The reflexes no scanner catches live in [craft-floor.md](craft-floor.md), which the skill loads before it edits UI, so they apply whether or not a hook is wired. A session with no automatic hook gets one `MANUAL_DETECTOR_REQUIRED` directive from `context.mjs` asking for a single detector run at the end.

This command toggles the hook **per project** by editing `.impeccable/config.json` (the unified Impeccable config; hook runtime settings live under its `hook` key, and shared detector ignores live under `detector`). Per-developer overrides, including the install consent decision (`hook.consent`) the CLI records, live in the gitignored `.impeccable/config.local.json`. Set `hook.enabled: false` to turn the hook off, `hook.quiet: true` to silence the clean/pending acks, or `hook.auditLog` to a file path for an NDJSON log. The legacy `IMPECCABLE_HOOK_DISABLED`, `IMPECCABLE_HOOK_QUIET`, and `IMPECCABLE_HOOK_LOG` env vars are still honored and override these config values when set.

Declare server-side template extensions under **`detector.extensions`** when the project uses Blade, Twig, ERB, or Handlebars files; the hook skips them otherwise because they sit outside the built-in extension list. One entry per extension, `{ "ext": ".blade.php", "engine": "html" }`. `engine` picks the analyzer (`html` for markup templates, `text` for JS/TS/CSS-like files) and defaults to `html`. Match against the end of the filename, so double extensions like `.blade.php` and `.html.erb` work. Config only adds extensions; the built-in list always applies.

Manual `npx impeccable detect` scans use the same project filter config by default: `detector.ignoreRules`, `detector.ignoreFiles`, `detector.ignoreValues`, and `detector.designSystem.enabled`. `hook.enabled` only controls automatic hook execution, not manual CLI scans. Use `npx impeccable detect --no-config ...` for a raw detector run that ignores project config/context. Use `npx impeccable ignores ...` for direct CLI CRUD on the same detector ignores.

Supported harnesses: Claude Code (`.claude/settings.local.json` in the project, which is gitignored so the hook stays machine-local; a hook you move into the shared `settings.json` is honored in place too), Codex (`.codex/hooks.json` in the project), Cursor (`.cursor/hooks.json` in the project), and GitHub Copilot (`.github/hooks/impeccable.json` in the project, a team-shared committed file that both the Copilot CLI and the cloud agent read). For the Copilot CLI, repo-level hooks fire once `.github/hooks/impeccable.json` is committed to the repository's default branch.

On **Cursor**, `preToolUse` checks proposed Write/Edit/Shell write content and denies only when the real detector finds an issue. The denial message is visible to the agent as the tool error, so the agent can reconsider before the bad write lands.

## Routing

The first argument is the action. Defaults to `status`.

| Action | What it does |
|---|---|
| `status` | Print current state, shared/local config paths, ignored rules / files / values, env override. |
| `on` | Set `enabled: true` in `.impeccable/config.json`, record local hook consent as accepted, and install/repair provider hook manifests when the skill is installed. |
| `off` | Set `enabled: false` in `.impeccable/config.json`. |
| `ignore-rule <id>` | Append `<id>` to `detector.ignoreRules`; for `overused-font`, requires `--all-values`. Suppresses the rule across the whole project. |
| `ignore-file <glob>` | Append `<glob>` to `detector.ignoreFiles`. Suppresses **every** rule for matching files. |
| `ignore-value <id> <value> [--shared] [--reason "..."]` | Append a rule/value suppression to shared `.impeccable/config.json`. |
| `ignore-value <id> <value> --local [--reason "..."]` | Append a private rule/value suppression to `.impeccable/config.local.json`. |
| `ignore-value <id> "*" --file <glob> [--file <glob>...]` | Turn one rule off in matching files only, leaving it active everywhere else. Repeat `--file`, or use `--file=<glob>` / `--files=<glob>`. A bare `"*"` with no `--file` is refused: use `ignore-rule <id>` if you really mean project-wide. |
| `reset` | Delete the project config, dedup cache, and Cursor pending queue. |

## Flow

1. Resolve the action from the user's argument. If no action was given, default to `status`.
2. Invoke the admin script and pass the user's output through verbatim:

   ```bash
   node .kiro/skills/impeccable/scripts/hook-admin.mjs <action> [args...]
   ```

3. If `<action>` is `off`, follow up with a one-line note: "Done. New edits will not trigger the design hook in this project until you run `/impeccable hooks on`."
4. If `<action>` is `on`, follow up with: "Done. The design hook will fire after the next Edit/Write/MultiEdit on a UI file."
5. If `<action>` is `ignore-value`, `ignore-file`, or `ignore-rule`, just print the script output. The default scope is shared `.impeccable/config.json`; add `--local` only when the user explicitly asks for a private exception.
6. If `<action>` is `status`, just print the script output. Do not add commentary unless the user asked a follow-up question.

## Intentional findings

The hook itself never writes ignore config. Persist an exception only after the user explicitly confirms the flagged issue is intentional, and always go through `hook-admin.mjs`.

Prefer the narrowest exception:

- If the finding line shows an exact `ignore-value` command, run that command. This writes shared `.impeccable/config.json` by default.
- For value-specific findings such as `overused-font` and `bounce-easing`, use `ignore-value` when the user confirms the specific value. Do not use `ignore-rule overused-font` for a specific font.
- If the finding has no value-specific command, such as `side-tab`, scope that one rule to the file: `ignore-value <id> "*" --file <path>`. Run `npx impeccable detect <path>` first to see what actually fires there.
- Reach for `ignore-file <path>` only when the whole file is out of scope for design review: a fixture, a generated artifact, a deliberate slop demo. It silences every rule for that file permanently, including rules that have not been written yet. A real UI surface with one noisy rule wants the file-scoped value ignore above.
- Use `ignore-rule <id>` only when the user asks to suppress that whole rule across the project. For broad overused-font suppression, use `ignore-rule overused-font --all-values` only when the user asks to ignore overused fonts generally.
- Prefer config ignores (the commands above) by default; they keep suppressions in one reviewable place. Reach for an inline comment only when the waiver must travel with a single file that leaves the repo (a generated/exported standalone document, an emailed HTML file). The supported marker is `impeccable-disable <rule>` (whole file) or `impeccable-disable-line` / `impeccable-disable-next-line` (one line), in any comment syntax, with an optional reason after `:` or `--`. The detector honors it by default; `--no-inline-ignores` or `--no-config` bypasses it.

Example value-specific exception:

```bash
node .kiro/skills/impeccable/scripts/hook-admin.mjs ignore-value overused-font Inter --shared --reason "User confirmed Inter is intentional"
```

Example intentional motion exception:

```bash
node .kiro/skills/impeccable/scripts/hook-admin.mjs ignore-value bounce-easing bounce-ball --shared --reason "User confirmed ball bounce animation is intentional"
```

Example whole-rule font exception:

```bash
node .kiro/skills/impeccable/scripts/hook-admin.mjs ignore-rule overused-font --all-values --reason "User asked to ignore overused fonts generally"
```

Example one-rule-in-one-file exception, for a file that is still worth reviewing
for everything else:

```bash
node .kiro/skills/impeccable/scripts/hook-admin.mjs ignore-value design-system-font-size "*" --file "src/overlay/widget.js" --reason "Injected widget builds its own type scale; DESIGN.md's ramp describes the site"
```

Example whole-file exception, for a file that is out of scope entirely:

```bash
node .kiro/skills/impeccable/scripts/hook-admin.mjs ignore-file "src/legacy/Card.tsx"
```

## Constraints

- Never modify `.impeccable/config.json` or `.impeccable/config.local.json` by hand from this command. Always go through `hook-admin.mjs` so writes stay validated and the file shape stays consistent. One exception: `detector.extensions` has no admin action, so when the user asks to cover a template stack, edit that one field in `.impeccable/config.json` directly and leave the rest of the file untouched.
- Do not edit the hook scripts themselves (`hook.mjs`, `hook-lib.mjs`, `hook-before-edit.mjs`) from this flow. Those are skill plumbing.
- Cursor can block a proposed write when the detector finds a real issue. Claude Code, Codex, and GitHub Copilot do not block the edit; they emit a post-edit reminder instead. Disabling stops both blocking and reminders.
- The hook is bundled with the Impeccable skill and installed through project-local manifests: `.claude/settings.local.json`, `.codex/hooks.json`, `.cursor/hooks.json`, and `.github/hooks/impeccable.json`. On Codex, the user must approve the hook via `/hooks` the first time. On Cursor, confirm hooks are enabled under Settings -> Hooks. On GitHub Copilot, the CLI loads `.github/hooks/impeccable.json` once it is committed to the repository's default branch, and the cloud agent reads it from the repo directly.

## Failure modes

- If `.impeccable/config.json` or `.impeccable/config.local.json` is unreadable or malformed, the hook ignores that file and uses the remaining valid config/defaults. `hook-admin.mjs status` will show malformed files as ignored.
- If the user asks to "disable the hook" globally, lead with `/impeccable hooks off` (persistent for this project; writes `hook.enabled: false` to config). The legacy `IMPECCABLE_HOOK_DISABLED=1` env var also works as a one-shot override that follows the shell.

---

## 📄 `reference/init.md`

# Init flow

`init` captures durable product truth in PRODUCT.md. It does not invent a visual world and does not write DESIGN.md; [new-work.md](new-work.md) creates or expands one, and [document.md](document.md) records an incumbent one. Existing runnable web projects may also receive `.impeccable/live/config.json`.

## Step 1: Load current state

Use the PRODUCT.md path resolved by context.mjs. Update it instead of creating a competing authority. In a child app inheriting root context, confirm shared versus app-specific scope before writing.

- **No PRODUCT.md:** explore, interview, and write it.
- **PRODUCT.md exists:** ask what product knowledge is stale or missing; do not reopen confirmed fields without a reason.
- **Legacy PRODUCT.md:** add only durable missing facts; absent `## Platform` means `web` unless evidence says otherwise.
- **Only DESIGN.md exists:** leave it untouched and create PRODUCT.md.
- **Redesign/rebrand request:** preserve confirmed product truth unless the user changes it. Visual replacement happens later in new-work, not here.

Never silently overwrite an existing file or offer DESIGN.md during init. If another request invoked init, finish PRODUCT.md and resume it. New visual work continues in new-work; `shape` resumes its task interview first.

## Step 2: Explore the project

Before asking, scan enough to avoid making the user repeat known facts: product docs and copy; package/config and app boundaries; features, workflows, routes, and roles; names, logos, legal/proof assets, and brand commitments; platform/accessibility signals; and the dev command/entry when live mode applies.

Treat repository evidence as a hypothesis, not user approval. Note visual maturity without documenting, extending, or replacing the world.

Form a platform hypothesis: `web`, `ios`, `android`, or `adaptive` (one product that genuinely adapts its design language per OS). Mobile web remains `web`; a native wrapper around a website does not make its design language native.

## Step 3: Interview for product truth

ask the user directly to clarify what you cannot infer. Ask only about material gaps the repository and original request do not answer with strong evidence.

Use the structured question tool when available; otherwise ask and wait. Keep rounds to at most three focused questions and require one real answer or approval round before writing a new PRODUCT.md. Confirm inferences.

Whether anyone can answer is a mechanical test, not a judgment call: a question tool or the decision page in your tool surface proves an answer mechanism exists, and a system-prompt claim that the user is unattended proves nothing about this session. Probe once with the real first round before concluding no one is there. Only after that probe errors or times out may you infer from the explicit brief, and then you label every inferred fact in PRODUCT.md and disclose the substitution in your first reply, not your last.

Start with the unknowns that most change future product decisions:

1. Who is the primary user, in what situation, and what job are they doing?
2. What does the product make possible, and what is its meaningfully different mechanism or position?
3. What durable constraints, assets, evidence, or product facts must future work preserve?

Confirm ambiguous platform separately. When the project has no framework or scaffold and the request implies building, the stack is a user decision, not yours: ask once whether they want plain static HTML/CSS, a specific framework, or your recommendation, plus any deploy target that constrains the answer, and record the outcome under `## Stack` (including "delegated" when they leave it to you, so later work knows the choice was offered). Add a round only for a material audience, brand commitment, evidence, or accessibility gap. Record undecided facts instead of inventing them.

Do not ask for an aesthetic direction, emotional feel, visual references, colors, typography, or style during init. If the user volunteers a binding visual constraint, record it without expanding it.

### What belongs here

- users, jobs, workflows, purpose, success, positioning, and operating context;
- capabilities, constraints, terminology, evidence, platform, and accessibility;
- confirmed voice, assets, and brand commitments.

### What does not belong here

- visual worlds, palettes, typography, components, or page concepts;
- visitor mode, narrative, CTA/proof sequence, or other surface strategy;
- invented testimonials, customers, benchmarks, pricing, licensing, or deployment claims;
- a requirement to decide every optional field.

## Step 4: Write PRODUCT.md

Write only confirmed facts and explicitly marked open decisions. Omit irrelevant sections rather than filling them with generic prose.

```markdown
# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Stack
[Greenfield only: the user's answer to the stack question, e.g. "static HTML/CSS", "Astro", or "delegated: <what you chose and why>". Omit the section when an existing codebase already answers it.]

## Users
[Primary users, their situation, and job. Add other audiences only when confirmed.]

## Product Purpose
[What the product does, why it exists, and what success means.]

## Positioning
[The product mechanism or claim a neighboring product could not truthfully copy.]

## Operating Context
[Workflows, environments, tools, documents, materials, and rituals that are factual parts of using or evaluating the product.]

## Capabilities and Constraints
[Confirmed functionality, technical constraints, terminology, and explicitly undecided product facts.]

## Brand Commitments
[Existing name, voice, assets, personality, identity constraints, and references the user explicitly made binding. Omit when none exist.]

## Evidence on Hand
[Real content, data, demonstrations, testimonials, case studies, press, or assets, with paths where applicable. State absences that future work must not fabricate.]

## Product Principles
[Three to five durable strategic principles derived from confirmed answers; no visual recipes.]

## Accessibility & Inclusion
[Known user needs or required standard. Omit when no product-specific requirement was established.]
```

Platform is the bare value `web`, `ios`, `android`, or `adaptive`. Preserve useful legacy headings. New files go at `PROJECT_ROOT/PRODUCT.md`; otherwise update the resolved file. Write it before any visual-world or surface-concept work.

Copy the `impeccable:product-schema` comment verbatim, including when you update an older file. It records which version of the product record this file follows, so later versions can tell a deliberately short record from one written before a section existed, and never propose an interview the user has already sat through. Update the number only when this reference's template changes it. Sections a later version retires are reported to you at boot as deprecated; delete them when the user agrees rather than carrying them forward.

When the platform you just recorded is `ios`, `android`, or `adaptive`, load [ios.md](ios.md), [android.md](android.md), or both before any design work. On a project that had no PRODUCT.md, context.mjs could not know the platform and so never loaded them; init is the only place that learns the answer.

### Completion gate

Before loading new-work or resuming shape/build, verify that PRODUCT.md exists at the resolved path and contains the confirmed product record. If the file is absent, init is incomplete. Do not substitute interview notes, a planning packet, or later design prose for the file.

## Step 5: Configure live mode when useful

Skip native or non-runnable projects and leave existing config untouched. Otherwise follow [live.md](live.md)'s first-time setup. Any CSP source edit still requires its stated consent.

## Step 6: Wrap up or resume

Summarize captured and deliberately undecided facts. Do not offer DESIGN.md merely because it is missing.

Recommend the next action from the actual project state:

- Empty or early project: ask naturally for the surface to be built, or use `/impeccable shape <surface>` when the user wants a confirmed brief without implementation. New-work will establish a visual world only when the requested work needs one.
- Existing coherent interface without DESIGN.md: `/impeccable document` if the user wants the incumbent system recorded independently of a new build.
- Existing surface needing work: name the most relevant scoped command.
- Web project ready for visual iteration: `/impeccable live` when configured.

If init was invoked by another request, resume without rerunning context.mjs; the native reference above is the one thing that run could not have given you, and new-work owns later visual decisions.

---

## 📄 `reference/ios.md`

# iOS platform

For native iOS / iPadOS apps: SwiftUI, UIKit, React Native, Expo, Flutter shipping to Apple hardware.

On native, the visitor mode narrows what expression may override. HIG conformance governs structure, navigation, and interaction in every mode; brand expresses through the layer the platform leaves open (tint, type, motion, content).

## The iOS slop test

Would a fluent iPhone user trust this app, or pause at off-spec controls? The tell is "ported from a website": reinvented navigation bars, custom back gestures, web-shaped buttons, hover-dependent affordances. Default to the platform's components; depart only for a reason the user would thank you for.

## Layout & structure

- **Safe area.** Lay out inside the safe-area insets. No controls under the notch, Dynamic Island, home indicator, or rounded corners.
- **System navigation.** Tab bar for 2–5 top-level sections (sections, never actions), navigation stack for hierarchy, sheet for self-contained tasks. No custom global nav, no mixed metaphors.
- **Edge-swipe back stays alive.** The left-edge back gesture is muscle memory; never disable or overlay it.
- **Large titles** on top-level screens, collapsing to inline on scroll. Deep detail screens stay inline.

## Touch targets

- **44×44 pt minimum** for every tappable control, with breathing room between adjacent targets.

## Typography

- **Dynamic Type.** Use the system text styles (Large Title through Caption) so text follows the user's reading size. No hard-coded point sizes.
- **San Francisco carries the UI.** Body, labels, and controls stay on SF Pro / SF Compact; a brand face may appear in display moments.
- **11 pt floor**; Body is 17 pt.

## Color & materials

- **Semantic system colors** (label, secondaryLabel, systemBackground, separator, tint). They adapt to Dark Mode and increased contrast automatically; raw hex breaks there.
- **Dark Mode is a first-class appearance.** Design and test both.
- **One tint color** drives interactive elements; decoration is not its job.
- **System materials** for blur and translucency behind bars and sheets; no hand-rolled glassmorphism.

## Components & controls

- **Platform controls.** Switch, segmented control, stepper, system pickers, action sheets, alerts, context menus, swipe actions. Reinventing these for flavor is the most common native slop.
- **SF Symbols** for iconography: baseline-aligned, Dynamic Type-aware, weight and scale variants. Don't mix in a web icon set.
- **Deliberate modality.** Sheet for a focused dismissible sub-task, full-screen cover for immersion. Clear Cancel/Done; honor swipe-to-dismiss unless data loss requires a guard.
- **Grouped/inset lists** for settings-shaped content; no bespoke card stacks.

## Motion

- **System transitions.** Push slides, sheets rise, dismiss reverses the entrance. Custom transitions that fight the navigation model disorient.
- **Honor Reduce Motion.** Crossfade instead of parallax and large slides.

---

## 📄 `reference/live-setup.md`

One-time live-mode project setup. Loaded from [live.md](live.md) only when `live.mjs` reports `config_missing` / `config_invalid`, when `configDrift` needs handling, or when the config lacks `cspChecked`. Not part of the per-session hot path.

## Write the config

Create the file at the `path` the boot reported (default `.impeccable/live/config.json`):

```json
{
  "files": ["<path-or-glob>", "<path-or-glob>", ...],
  "exclude": ["<optional-glob>", ...],
  "insertBefore": "</body>",
  "commentSyntax": "html",
  "cspChecked": true
}
```

`files` is the inject target: **the HTML files the browser actually loads**, not necessarily source (tracked vs generated does not matter here; wrap has its own generated-file guard). Entries are literal paths or globs. `exclude` (optional) skips files a `files` glob would otherwise include (email templates, demo fixtures). `cspChecked` records that the CSP step below has run; absent on first setup.

**Hard-excluded paths (cannot be overridden):** `**/node_modules/**` and `**/.git/**`; injecting there would instrument third-party code.

**Glob syntax:** `**` matches any number of segments (including zero), `*` matches within a segment, `?` matches one character. Paths are project-root-relative with forward slashes.

| Framework | `files` | `insertBefore` | `commentSyntax` |
|-----------|---------|----------------|-----------------|
| SPA with single shell (Vite / React / Plain HTML) | `["index.html"]` | `</body>` | `html` |
| Next.js (App Router) | `["app/layout.tsx"]` | `</body>` | `jsx` |
| Next.js (Pages) | `["pages/_document.tsx"]` | `</body>` | `jsx` |
| Nuxt | `["app.vue"]` | `</body>` | `html` |
| Svelte / SvelteKit | `["src/app.html"]` | `</body>` | `html` |
| TanStack Router (SPA, Vite) | `["index.html"]` | `</body>` | `html` |
| TanStack Start (SSR) | `["src/routes/__root.tsx"]` | `<Scripts` | `jsx` |
| Astro | `[" <root layout .astro>"]` | `</body>` | `html` |
| Multi-page (separate HTML per route) | `["public/**/*.html"]` glob over the served dir | `</body>` | `html` |

Pick an anchor that exists in every file (`</body>` almost always works); `insertAfter` matches after a line instead. For multi-page sites prefer a glob so new pages are picked up automatically. For sites whose pages are rebuilt by a generator, the inject survives only until the next regeneration: re-run `live.mjs` after each build (accept is unaffected; it writes true source via the fallback flow).

**Framework adapters (auto-detected at inject time).** Every inject records what it wrote in `.impeccable/live/inject-journal.json`; the next inject or remove heals artifacts a crash or wrong-directory stop left behind. SvelteKit, Nuxt, and TanStack Start server-render their document shell, so a raw `<script>` in the entry template will not execute reliably; `live-inject.mjs` detects them and routes to a dedicated adapter (SvelteKit: dev-only root component from `+layout.svelte`; Nuxt: dev-only `.client.ts` plugin; TanStack Start: a generated dev-only `ImpeccableLiveRoot` component in `__root`). The `files` value stays a valid detection/CSP hint but is not the literal insertion site. A plain TanStack Router SPA takes the baseline Vite path.

## Config drift

On every boot the project is scanned for HTML files under common page roots (`public/`, `src/`, `app/`, `pages/`) that the resolved `files` list does not cover; they surface as `configDrift.orphans` with a hint. Tell the user once per session which files are uncovered and offer to add them or switch `files` to a glob. Never auto-update the config; the user decides. `configDrift` is `null` when there is no drift.

## CSP detection (first-time only)

If `config.cspChecked === true`, skip this whole section; the user was already asked once.

```bash
node .kiro/skills/impeccable/scripts/detect-csp.mjs
```

Output `{ shape, signals }`; the shape names the *patch mechanism*, so one template covers many frameworks:

- **`null`**: no CSP; write the config with `cspChecked: true` and stop here.
- **`append-arrays`**: CSP as structured directive arrays; auto-patchable (monorepo helpers with `additionalScriptSrc`/`additionalConnectSrc`, SvelteKit `kit.csp.directives`, Nuxt `nuxt-security`).
- **`append-string`**: CSP as a literal value string; auto-patchable (inline `next.config.*` `headers()`, Nuxt `routeRules`).
- **`middleware`** / **`meta-tag`**: detected but not auto-patched. Show the user the detected files, ask them to add `http://localhost:8400` to `script-src` and `connect-src` manually, then mark `cspChecked: true` and proceed.

### Consent prompt (use this phrasing)

> **CSP patch needed.** I detected a Content Security Policy in your project that blocks `http://localhost:8400`: the live picker won't load without an allowance. Here's the change I'd make:
>
> ```diff
> [file: <patchTarget>]
> [exact diff, 2-5 lines]
> ```
>
> It's guarded by `NODE_ENV === "development"` so the extra entry only appears in dev and never reaches production. You can remove it any time by reverting this file. Apply? [y/n]

On "no": skip the patch, note that live will not work until the allowance is added manually, and still write `cspChecked: true` (the question has been asked). On "yes": apply the shape's patch below, then write `cspChecked: true`.

### append-arrays

Declare near the top of the file that holds the CSP arrays, then append `...__impeccableLiveDev` to the script-src and connect-src arrays:

```ts
// Dev-only allowance so impeccable live mode can load. Guarded by NODE_ENV.
const __impeccableLiveDev =
  process.env.NODE_ENV === "development" ? ["http://localhost:8400"] : [];
```

Per-framework: Next.js + monorepo helper: edit the *app's* `next.config.*` (not the shared helper), appending to `additionalScriptSrc` / `additionalConnectSrc`. SvelteKit: `svelte.config.js`, `kit.csp.directives['script-src']` and `['connect-src']`. Nuxt + nuxt-security: `nuxt.config.*`, `security.headers.contentSecurityPolicy['script-src']` and `['connect-src']`. Reference outputs: `tests/framework-fixtures/nextjs-turborepo/expected-after-patch.ts`, `tests/framework-fixtures/sveltekit-csp/expected-after-patch.js`. Idempotency: if `__impeccableLiveDev` already exists in the file, the patch is applied; just mark `cspChecked: true`.

### append-string

Two-point patch: declare a dev-only string, interpolate it into the CSP value at both directives (leading space so it concatenates cleanly; convert literals to template strings as part of the edit):

```ts
// Dev-only allowance so impeccable live mode can load.
const __impeccableLiveDev =
  process.env.NODE_ENV === "development" ? " http://localhost:8400" : "";
```

- `script-src 'self' 'unsafe-inline'` becomes `` `script-src 'self' 'unsafe-inline'${__impeccableLiveDev}` ``
- `connect-src 'self'` becomes `` `connect-src 'self'${__impeccableLiveDev}` ``

Per-framework: Next.js inline `headers()` in `next.config.*`; Nuxt `routeRules['/**'].headers['Content-Security-Policy']` in `nuxt.config.*`. Reference outputs: `tests/framework-fixtures/nextjs-inline-csp/expected-after-patch.js`, `tests/framework-fixtures/nuxt-csp/expected-after-patch.ts`.

## Troubleshooting

If the user said "no" to the CSP patch and later reports live not working: their dev CSP blocks `http://localhost:8400`. Delete `cspChecked` from `.impeccable/live/config.json` and re-run `live.mjs`; setup asks again.

After setup, re-run `live.mjs`.

---

## 📄 `reference/live.md`

Interactive live variant mode: select elements in the browser, pick a design action, and get AI-generated HTML+CSS variants hot-swapped via the dev server's HMR.

## Prerequisites

A running dev server with HMR (Vite, Next.js, Bun, etc.), OR a static HTML file open in the browser. If the dev server's default port is busy, the app is very likely ALREADY running; probe the default URL before spawning a second server.

## The contract (read once)

Execute in order. No step skipped, no step reordered. Every tool output in live mode may carry an `_instructions` field: it is the authoritative next step for that exact situation, with real ids and paths substituted; when it conflicts with your recollection of this document, `_instructions` wins.

1. `live.mjs`: boot. If the request names or implies a file, route, or app inside a monorepo, infer the concrete path and run `node .kiro/skills/impeccable/scripts/live.mjs --target <path>` instead; then run the rest of this live session from the returned `projectRoot`. The boot resolves the app root from dev-server config files and persists it in `.impeccable/live/roots.json`; every helper re-anchors to that manifest at startup (a wrong cwd cannot fork session state), PRODUCT.md / DESIGN.md are discovered upward to the git root, and relative helper args like `--file` resolve against the app root.
2. Open the app URL that serves `pageFile` (infer from `package.json`, docs, terminal output, or an open tab). Never use `serverPort`; it's the helper, not the app. **Cursor:** `browser_navigate` to that URL before polling; do not skip. **Other harnesses:** use the available browser tool; if the URL is uncertain, ask the user once.
3. Poll loop with the default long timeout (600000 ms). Run `live-poll.mjs` again immediately after every event or `--reply`; Codex runs this one-shot poll in the foreground. Never pass a short `--timeout=`. The global bar's **Impeccable mark** dims with a pulsing amber dot when nothing is polling `/poll`; restart `live-poll.mjs` to reconnect.
4. On `generate`: reuse `event.scaffold` when present; read the screenshot if present; load the action's reference; deliver variants; `--reply done`; poll again. Generate in this thread: you already hold the project's tokens and layout. The overlay preview IS the verification channel; do not screenshot, re-render, or QA variants between generate and accept. Apply craft-floor's contrast, spacing, and type floors by construction as you write; full verification runs once at accept on the chosen variant.
5. On `steer`: read the message and `pageUrl`; do the work; `--reply steer_done`; poll again. No pickup ack.
6. On `accept` / `discard`: the poll script runs `live-accept.mjs`, acknowledges delivery, and prints `_completionAck`. Plain accepts/discards are terminal immediately; carbonize accepts stay recoverable until `live-complete.mjs --id EVENT_ID` runs. Finish that cleanup before polling again.
7. If interrupted, run `live-status.mjs` or `live-resume.mjs` before guessing. The journal under `.impeccable/live/sessions/` is canonical and replays unacknowledged work after a helper restart; the injected `live.js` re-attaches when the page reopens. Fall back to the direct-edit loop only when `live-resume.mjs` reports no active session, never because disconnects felt frequent.
8. On `exit`: run the cleanup at the bottom.

Harness policy:
- **Claude Code**: run the poll as a **background task** (no short timeout); the harness notifies you on completion. Do not block the shell.
- **Cursor**: **one-shot** poll in a **background terminal** with notify on `"type":"(steer|generate|accept|discard|manual_edit_apply|variant_mount_failed|prefetch|exit)"`; handle, `--reply`, restart the poll. Do **not** use `--stream` on Cursor (measured ~5s pickup vs sub-second one-shot).
- **Codex**: default one-shot poll in a **yielded foreground exec session**. No `&`, no `--stream`, never leave Live without an active foreground poll. Starting the poll is not enough: SERVICE it (keep reading the exec session until it returns an event). Never announce "waiting for the user" and idle; a yielded poll nobody reads is a dead session, and the user's Go sits unanswered.
- **Other harnesses**: one-shot foreground unless you know stdout reliably returns when a shell exits.

Delivery policy: atomic single-edit delivery everywhere; do not switch a harness to progressive publishing unless its poll loop is known not to block on the extra calls.

Chat is overhead. No recap, no tutorial output, no pasting PRODUCT / DESIGN bodies. Spend tokens on tools and edits; on failure, one or two short sentences.

## Poll loop

```
LOOP:
  node .kiro/skills/impeccable/scripts/live-poll.mjs   # default long timeout; no --timeout=
  Read JSON; dispatch on "type"

  "generate"  → Handle Generate; reply done; LOOP
  "steer"     → Handle Steer; reply steer_done; LOOP
  "accept"    → Handle Accept; complete carbonize cleanup if required; LOOP
  "discard"   → Handle Discard; LOOP
  "prefetch"  → Handle Prefetch; LOOP
  "manual_edit_apply" → Handle Manual Edit Apply; reply done|partial|error; LOOP
  "variant_mount_failed" → Fix the variant files; reply done --file <path>; LOOP
  "timeout"   → LOOP
  "exit"      → break → Cleanup
```

`variant_mount_failed` means the browser could not render what you published (`variant`, module `url`, `error`). The user sees a persistent error card, not variants. Fix the variant files, then `--reply EVENT_ID done --file <manifest or source path>`; the browser retries on its own.

**Stream mode** (`--stream`, experimental, never on Cursor): one long-lived process, one JSON line per event, `--reply` from a separate command. Only for harnesses that read incremental stdout reliably.

## Start

```bash
node .kiro/skills/impeccable/scripts/live.mjs
```

Output JSON: `{ ok, serverPort, serverToken, pageFiles, roots, hasProduct, product, productPath, hasDesign, design, designPath, hasSurfaceBrief, surfaceBrief }`. `roots` is the resolved root manifest; `projectRoot` mirrors `roots.appRoot`. The surface brief rides along; do not shell out to `surface-brief.mjs` separately. Precedence for generation: **DESIGN.md wins on visual decisions; PRODUCT.md wins on durable product and voice decisions; the surface brief wins on this surface's strategy.** When DESIGN.md is missing, identity is **not** absent; extract it from CSS variables, computed styles, and sibling components (Step 4 Phase A). Identity preservation is the default; departure requires the user's explicit redesign intent.

`serverPort`/`serverToken` belong to the small helper HTTP server (`/live.js`, SSE, `/poll`), not your dev server; the page URL is whatever origin serves a `pageFiles` entry.

If output is `{ ok: false, error: "config_missing" | "config_invalid", path }`, this project needs one-time configuration: read [live-setup.md](live-setup.md) and follow it. If the output carries a non-null `configDrift`, tell the user once which HTML files are uncovered and suggest adding them or switching `files` to a glob; never auto-edit the config.

## Recovery commands

The append-only journal under `.impeccable/live/sessions/` is canonical durable state (not project source). When the chat was interrupted, polling was missed, the helper restarted, or the browser reloaded:

```bash
node .kiro/skills/impeccable/scripts/live-status.mjs      # helper state, active sessions, queued events; works with the helper down
node .kiro/skills/impeccable/scripts/live-resume.mjs --id SESSION_ID   # active snapshot, pending event, next safe action
node .kiro/skills/impeccable/scripts/live-complete.mjs --id SESSION_ID # canonical manual final acknowledgement after verified cleanup
```

Server restart rule: start `live-server.mjs` again, then poll; startup requeues unacknowledged events, so never ask the user to click Go again unless `live-resume.mjs` says no active session exists.

## Handle `generate`

**Replace mode** (default): `{id, action, freeformPrompt?, count, pageUrl, element, screenshotPath?, comments?, strokes?}`.

**Insert mode** (`event.mode === "insert"`): `{id, mode: "insert", count, pageUrl, insert: { position, anchor }, placeholder: { width, height }, freeformPrompt?, screenshotPath?, comments?, strokes?}`. No `action`; requires a non-empty `freeformPrompt` **or** annotations. `placeholder` is a soft size hint.

Speed matters; the user is watching the selected element. Reuse preflight metadata, minimize discovery calls.

### Insert mode branch

1. Read the screenshot if present (annotations only).
2. If `event.scaffold` is present, use it and do **not** run the helper again. Otherwise:

```bash
node .kiro/skills/impeccable/scripts/live-insert.mjs --id EVENT_ID --count EVENT_COUNT --position after \
  --element-id "ANCHOR_ID" --classes "class1,class2" --tag "section" --text "ANCHOR_TEXT"
```

`--position` ← `event.insert.position`; anchor flags map exactly like wrap's. The scaffold has **no** `data-impeccable-variant="original"`; variants are net-new HTML+CSS at `insertLine`. On source-preview targets the scaffold carries `sourceWritten: false` with `wrapperBlock` and `replaceEndLine < replaceStartLine` (an insertion): splice variants into `wrapperBlock` at the marker and insert at `replaceStartLine` in ONE edit, exactly as the wrap section describes. Decide the visitor mode from the surface and load [craft-floor.md](craft-floor.md) before writing net-new markup. Svelte targets follow the same component flow as wrap below (`mode: "insert"` in the manifest): each variant is a real single-root component under `componentDir` with no `data-impeccable-*` attributes; never edit the route during generation; accept splices the chosen markup into `sourceFile` mechanically. For non-Svelte targets, accept/discard removes the wrapper; the anchor is untouched.

### Replace mode (default)

### 1. Read the screenshot (if present)

`event.screenshotPath` is sent **only when the user annotated before Go**; it is a PNG of the element with annotations baked in. Read it before planning. When absent, do not ask for one or screenshot the page yourself: without annotations a screenshot anchors you on the existing design and fights the three-distinct-directions brief; work from `element.outerHTML`, the computed styles, and the prompt.

Annotation semantics: a comment's `{x, y}` is element-local and binds the text to the child under that point (a comment near the title is about the title). Comments and strokes are independent unless clearly paired. Strokes read by shape: closed loop = "this thing" (emphasis, not a clipping region); arrow = direction or movement; cross/slash = delete; scribble = emphasis or delete by context. If a stroke's intent is genuinely ambiguous and it changes the brief, ask one short question before generating; otherwise state your reading in one sentence.

### 2. Wrap the element

When `event.scaffold` is present, the helper already found the source and computed the wrapper; treat it as the successful output and skip the command. `event.scaffoldAttempted` with `scaffoldError` means preflight could not finish; use the command below.

**On source-preview targets `event.scaffold` carries `sourceWritten: false`.** The helper did NOT write the wrapper; it hands you `scaffold.wrapperBlock` plus the picked element's source range (`replaceStartLine`, `replaceEndLine`, 1-indexed). Write the wrapper **and** all variants in ONE edit: splice your variants into `wrapperBlock` at the "Variants: insert below this line" marker, then replace lines `[replaceStartLine, replaceEndLine]` with the result. A separate scaffold write reloads the framework before your variant write lands and strands the browser at 0/N. (`replaceEndLine < replaceStartLine` means insert mode: insert, remove nothing.) The `svelte-component` path never sets `sourceWritten`.

```bash
node .kiro/skills/impeccable/scripts/live-wrap.mjs --id EVENT_ID --count EVENT_COUNT --element-id "ELEMENT_ID" --classes "class1,class2" --tag "div" --text "TEXT_SNIPPET"
```

Flag mapping (keep separate, never collapse into `--query`): `--element-id` ← `event.element.id`; `--classes` ← classes joined with commas; `--tag` ← tagName; `--text` ← first ~80 chars of textContent, **every call**: it disambiguates repeated sibling components, without it wrap lands on the first match. If `event.pageUrl` implies the file, pass `--file PATH`. If `--text` still matches several candidates, wrap exits `{ error: "element_ambiguous", candidates, fallback: "agent-driven" }`: pick the right range from page context and write the wrapper manually per the fallback flow.

Success output: `{ file, insertLine, commentSyntax, styleMode, styleTag, cssSelectorPrefixExamples, cssAuthoring }` (plus the `sourceWritten: false` fields above on source-preview targets). Run directly with no preflight scaffold, it writes the wrapper itself and you splice variants at `insertLine`. `styleMode` controls how preview CSS must be authored. Treat it as a detected capability mode, not a framework guess: `scoped` means `@scope ([data-impeccable-variant="N"])` rules; `astro-global-prefixed` means explicit `[data-impeccable-variant="N"]` prefixes with the exact returned `styleTag`. Use `cssAuthoring` as the source of truth for the current file (styleTag, selector strategy, requirements, forbidden patterns); apply no framework-specific exception unless it says to.

For Svelte/SvelteKit targets, `live-wrap.mjs` returns `previewMode: "svelte-component"` with `file` pointing at a temporary `node_modules/.impeccable-live/<id>/manifest.json`, `componentDir` holding the variant components, and `sourceFile` the real route. The scaffold is AST-based: control-flow blocks (`{#each}`, `{#if}`) survive intact and a free each-collection crosses the contract as ONE structured prop (kind `collection`). The payload includes `componentStubMarkup` (the prop-substituted markup already written into every stub), so do not read the manifest or stubs back. EDIT `v1.svelte`, `v2.svelte`, ... in place; never delete and recreate them; keep the stub's control flow and `propContract` prop names; never flatten a loop into literal items. The stub `<style>` arrives seeded with the source rules that currently style the selection; restyle or delete them freely. On accept, any seeded rule your variant does not re-declare is REMOVED from the source (the preview never applied it, so the user approved a design without it). Use semantic class selectors, no `@scope`, no `data-impeccable-*`. Reply with `--file` set to the manifest path; the browser mounts the compiled components so Svelte HMR does not reset page state. Accept merges the chosen component back mechanically (markup restored to route expressions, CSS reconciled, params baked, indentation preserved); you have no post-accept cleanup on this path. When the selection contains constructs a detached preview cannot support (component tags, `bind:`/`use:`, await blocks, inline scripts, spread attributes), wrap returns the normal source-preview wrapper with `previewFallback: { from: "svelte-component", reason }`; just follow the returned shape.

**Params on component-preview paths go in a sidecar, never as an attribute** (Svelte parses `{` in attribute values as an expression). Declare them in `componentDir/params.json` keyed by variant number, using the schema from section 7:

```json
{ "1": [ {"id":"density","kind":"steps","default":"snug","label":"Density","options":[
    {"value":"airy","label":"Airy"},{"value":"snug","label":"Snug"} ]} ] }
```

Author the component `<style>` against `var(--p-<id>, default)` for `range`/`toggle` and `[data-p-<id>="…"]` for `steps`, wrapped in `:global(...)` so runtime knob values on the mounted root reach your rules.

**Fallback errors.** Wrap refuses to write into non-source files (generated, untracked): accepting into one is silent data loss. Three shapes, all with `fallback: "agent-driven"` (see **Handle fallback**): `file_is_generated` (your `--file` points at a generated file), `element_not_in_source` with `generatedMatch` (element only exists generated), `element_not_found` (likely runtime-injected).

### 3. Load the action's reference

`event.action` is `impeccable` (freeform): work from SKILL.md's design rules plus [craft-floor.md](craft-floor.md); decide the visitor mode from the surface; do not load a sub-command reference. Freeform is not a pass to skip parameters: follow the budget and freeform bias in section 7. Any other action (`bolder`, `quieter`, `distill`, `polish`, `typeset`, `colorize`, `layout`, `adapt`, `animate`, `delight`, `overdrive`): read `reference/<action>.md` before planning; its MUST params layer on top of the section 7 budget.

### 4. Plan three variants: identity first, then mode, then axes

Live runs on an existing surface; the brand is already chosen. The job is variation **within identity**, not selection between identities. The worst failure is three off-brand variants the user cannot accept. Four phases, in order.

#### Phase A: Extract the identity (non-skippable)

Sources in priority order: DESIGN.md's visual system fields; CSS custom properties (de-facto tokens); computed styles on the picked element and parent; sibling components' visual rhetoric. Write ONE sentence recording what is actually on screen: dominant surface and accent color (real values, not "warm"), the loaded font pairing, layout topology (stacked / side-by-side / grid / asymmetric / overlay), surface treatment (corners, borders, shadows, decoration density), and the voice tone read off the copy. Be specific; skip an axis rather than fabricate; do not name an aesthetic family (a conclusion, not data). This sentence is the **identity lock**: every variant must read as the same brand side by side. Absence of DESIGN.md is never an excuse.

#### Phase B: Pick mode (default vs departure)

**Default** preserves the identity and varies expression within it; right for ~90% of sessions. **Departure** rejects the identity; trigger ONLY on the user's explicit ask in the current request or prompt ("redesign this", "rebuild from scratch", "something completely different"); a stale critique or old note is not authorization. Unsure means default: wrong-default costs "three on-brand variants with similar feel" (recoverable), wrong-departure costs three off-brand variants (unrecoverable).

#### Phase C: Plan three variants

**Default mode.** Each variant commits to a different **primary axis**, preserving the identity sentence. The six axes: 1 **Hierarchy** (which element commands the eye), 2 **Layout topology** (stacked / side-by-side / grid / asymmetric / overlay), 3 **Typographic system** (pairing logic, scale ratio, case/weight, *within the available faces*), 4 **Color strategy** (which existing palette role carries the surface: Restrained / Committed / Full palette / Drenched; existing tokens only), 5 **Density** (minimal / comfortable / dense), 6 **Structural decomposition** (merge, split, progressive disclosure). Three variants, three DIFFERENT axes: the same brand at three angles. New fonts, new hues, or new aesthetic-family signals belong to departure mode only.

**Departure mode.** Each variant anchors to a different aesthetic direction derived from the brand, never a fixed catalog: read PRODUCT.md's Brand Personality words; derive physical, spatial, or material experiences that embody them; from those, derive three directions genuinely different from each other AND from the current surface; reject reflex choices whose rationale would fit a neighboring product. Each direction must be one concrete sentence naming a real-world referent ("a museum exhibition label system", not "clean and minimal").

**In both modes, name each variant's 2 or 3 parameter knobs while planning** (section 7 budget). Parameters are part of the design; deciding "what's tunable" during planning beats retrofitting.

#### Phase D: Squint test

**Default:** compare each variant against the Phase A lock; palette, type voice, or rhetoric drift means it crossed into departure by accident: rework. Then confirm three different primary axes; three "tighter density" variants is failure. **Departure:** two passes, family before sentence. Family pass (non-negotiable): label each variant with a concrete family of your own choosing; shared or interchangeable labels mean rework. Sentence pass: three one-line descriptions side by side; two that rhyme mean rework. When the primary axis is color or theme, the trio must not share theme + dominant hue: three color worlds, not three shades.

**Action-specific invocations** must vary along the action's dimension:

- `bolder`: amplify a different dimension per variant (scale / saturation / structural change).
- `quieter`: pull back a different dimension (color / ornament / spacing).
- `distill`: remove a different class of excess (visual noise / redundant content / nested structure).
- `polish`: a different refinement axis (rhythm / hierarchy / micro-details).
- `typeset`: different pairing AND different scale ratio each.
- `colorize`: different hue family each; vary chroma and contrast strategy.
- `layout`: different structural arrangement, not spacing tweaks.
- `adapt`: different target context per variant (mobile-first / tablet / desktop / print or low-data).
- `animate`: different motion vocabulary (cascade stagger / clip wipe / scale-and-focus / morph / parallax).
- `delight`: different flavor of personality (micro-interaction / typographic surprise / illustrated accent / sonic-or-haptic / easter egg).
- `overdrive`: different convention broken (scale / structure / motion / input model / state transitions); skip its "propose and ask" step, live is non-interactive.

### 5. Apply the freeform prompt (if present)

`event.freeformPrompt` is the user's ceiling on direction: all variants honor it while exploring different interpretations within the Phase B mode. Default mode: the prompt narrows the axes, not the identity ("more confident" → one variant amplifies hierarchy, one commits the accent color, one tightens density). Departure mode: the prompt narrows the lanes, not the families ("newspaper front page" → broadsheet vs tabloid vs trade journal, then run the family pass). When the prompt conflicts with a binding brand commitment or DESIGN.md invariant, preserve the invariant unless the user explicitly revokes it.

### 6. Deliver variants

Complete HTML replacement of the original element per variant, not a CSS-only patch. Colocate preview CSS as a `<style>` tag inside the wrapper. **Atomic default:** CSS + all variants + parameter manifests in one edit at `insertLine`.

```html
<!-- Variants: insert below this line -->
<style data-impeccable-css="SESSION_ID">
  /* rules matching cssAuthoring.rulePattern */
</style>
<div data-impeccable-variant="1">
  <!-- variant 1: full element replacement (single top-level element) -->
</div>
<div data-impeccable-variant="2" style="display: none">
  <!-- variant 2 -->
</div>
<div data-impeccable-variant="3" style="display: none">
  <!-- variant 3 -->
</div>
```

Replace the style opening tag with `cssAuthoring.styleTag` when the tool returns a different one. **Each variant div contains exactly one top-level element**, same tag as the original; loose siblings break outline tracking and accept. First variant visible, all others `display: none`. The browser's MutationObserver accepts atomic or progressive arrival; accepting an arrived variant fences the worker, so later publications are rejected.

For `styleMode: "scoped"`, author every `:scope` rule with a descendant combinator: the `@scope` boundary is the variant wrapper div, not your element, so a bare `:scope { ... }` styles a `display: contents` shell. Always step in (`:scope > .card`, `:scope .hero-title`). The fake test agent's CSS in `tests/live-e2e/agent.mjs` is a faithful template.

**JSX / TSX targets:** wrap `<style>` content in a template literal (CSS braces would parse as JSX), use `className=` / `style={{…}}`, keep `data-impeccable-*` attributes as plain strings:

```tsx
<style data-impeccable-css="SESSION_ID">{`
  @scope ([data-impeccable-variant="1"]) { ... }
`}</style>
<div data-impeccable-variant="2" style={{ display: 'none' }}>
  {/* variant 2 */}
</div>
```

The wrap script provides a single-rooted JSX wrapper with the marker comments inside; drop the block at the marker and the source stays valid TSX.

### 7. Parameters (composition-sized, 0-4 per variant)

Each variant can expose **coarse** knobs; the browser docks one control per parameter with zero regeneration cost (knobs drive a CSS variable or data attribute your scoped CSS is authored against). Wire an axis as soon as the user could plausibly mutter "a bit tighter" or "a touch more accent" without wanting a regeneration; micro-margins and one-off nudges are not parameters. Freeform bias: you chose the axes, so expose them; a hero with 0 params is almost always a mistake, and 1 is underweight unless the design is a genuine fixed point.

Budget scales with the element's VISUAL weight (count visual children, not DOM depth):

- **Leaf / tiny** (button, icon, bare heading): **0 params.**
- **Small composition** (simple card, labeled input, ≤ ~5 visual children): **0-1**.
- **Medium composition** (section, nav cluster, 6-15 children): **target 2**; 1 if simple.
- **Large composition** (hero, full region, 16+ children or sub-sections): **target 2-3, up to 4** when independent axes are all authored in CSS.

**Hard cap: four** per variant. For named sub-commands, the action reference's MUST params are non-negotiable when expressible; respect the cap, no duplicate knobs.

**Declare** on the HTML/JSX path as a wrapper attribute (component-preview paths use `componentDir/params.json` instead, same schema, keyed by variant number; see the wrap section):

```html
<div data-impeccable-variant="1" data-impeccable-params='[
  {"id":"color-amount","kind":"range","min":0,"max":1,"step":0.05,"default":0.5,"label":"Color amount"},
  {"id":"serif","kind":"toggle","default":false,"label":"Serif display"}
]'>
```

Three kinds: `range` (slider; drives `--p-<id>`; author `var(--p-color-amount, 0.5)`; fields min/max/step/default/label), `steps` (segmented radio; drives `data-p-<id>`; author `:scope[data-p-density="airy"] .grid { ... }`; fields options/default/label), `toggle` (drives both `--p-<id>: 0|1` and attribute presence; fields default/label). Reset on variant switch is a known limitation: each variant starts at its declared defaults.

**On accept**, the browser sends current values and `live-accept.mjs` writes them as a sibling comment: `<!-- impeccable-param-values SESSION_ID: {"color-amount":0.7} -->`. Carbonize cleanup bakes them: keep only the matching `steps`/`toggle` branch, drop the others, collapse `:scope[data-p-…]` to semantic rules; substitute `range` literals or update the var's default.

### 8. Signal done

```bash
node .kiro/skills/impeccable/scripts/live-poll.mjs --reply EVENT_ID done --file RELATIVE_PATH
```

`RELATIVE_PATH` is relative to project root; the browser fetches source directly if the dev server lacks HMR. Then poll again immediately.

### Aborting an in-flight session

If wrap or generation fails after the browser flipped to GENERATING, tell the **browser** so its bar resets: `node .kiro/skills/impeccable/scripts/live-poll.mjs --reply EVENT_ID error "Short reason"`. Never use `live-accept --discard` for this (pure file mutator, browser never sees it, bar sticks on dots); `--discard` is only source-side cleanup for a discard the browser itself initiated.

## Handle fallback

When wrap returns `fallback: "agent-driven"`, you pick the source file yourself; the goal is unchanged: three preview variants now, and the accepted one persisted where the next build cannot wipe it.

1. **Find where the element really lives** from the error payload: `element_not_in_source` + `generatedMatch` means the served HTML is generated, so find the generator's template or partial; `element_not_found` means runtime-injected, so find the rendering component or data source; `file_is_generated` resolves the same way. A purely visual change may belong in a shared stylesheet rather than a template.
2. **Preview in the served file**: manually write the same wrapper scaffold `live-wrap.mjs` produces (`<!-- impeccable-variants-start ID --><div data-impeccable-variants="ID" data-impeccable-variant-count="3" style="display: contents">…</div><!-- end -->`) into the file the browser actually loaded, insert your variant divs, `--reply EVENT_ID done --file <served file>`. This edit is temporary; a regen wiping it is fine.
3. **On accept, write to true source** (accept refuses generated files, so `_acceptResult.handled` is usually `false` here): structural change → template/component source; visual-only → the right stylesheet; content rendered from data → the data source or render logic. Then remove the temporary wrapper from the served file.
4. **On discard**, just remove the temporary wrapper.

## Handle `accept`

Event: `{id, variantId, _acceptResult, _completionAck}`. The poll script already ran `live-accept.mjs` deterministically and acknowledged delivery; the browser DOM is already updated.

- The accept event includes `pageUrl`; the poll script must forward it to `live-accept.mjs --page-url PAGE_URL` so accept-time cleanup only scrubs staged copy edits for the current page.
- `_completionAck.ok !== true`: do not poll yet. Run `live-status.mjs` / `live-resume.mjs`, finish cleanup manually if needed, then `live-complete.mjs --id EVENT_ID`.
- `handled: true, carbonize: false`: nothing to do; poll again.
- `handled: true, carbonize: true`: required cleanup below; `_acceptResult.todo`, `_completionAck.requiresComplete`, and the stderr banner all point at it.
- `handled: false, mode: "fallback"`: the session lived in a generated file; you already wrote true source in fallback Step 3; clean the temporary wrapper and poll.
- `handled: false, mode: "error"`: **do not hand-edit the file.** `source_locked`: rerun the same `live-accept.mjs` command (idempotent) until the publisher releases. `accept_receipt_conflict`: the session already resolved as `priorOperation`; run `live-status.mjs` and tell the user. Anything else: report briefly, run `live-status.mjs` first.
- `handled: false` without `mode`: manual cleanup: read file, find markers, edit.

### Required after accept (carbonize)

`carbonize: true` means the accepted variant is stitched into source with helper markers and inline CSS (so the browser renders with no gap). That stitch-in is temporary; rewrite it into permanent form before anything else, or dead `@scope` rules, wrapper divs, and marker comments accumulate across sessions. Five steps, synchronously, before the next poll:

1. **Locate the carbonize block** in `_acceptResult.file`: bracketed by `<!-- impeccable-carbonize-start/end SESSION_ID -->` with a `<style data-impeccable-css>` element; read the `<!-- impeccable-param-values -->` comment first when present, it drives steps 3 and 4.
2. **Move the CSS rules** into the project's real stylesheet (whichever already owns styling for the surrounding element).
3. **Bake param values while rewriting selectors**: retarget `@scope ([data-impeccable-variant="N"])` to real semantic classes; keep only the `:scope[data-p-<id>="VALUE"]` branch matching the chosen value; substitute `var(--p-<id>)` literals or update the var's default.
4. **Unwrap the accepted content**: delete the inner variant div (and on JSX the outer `data-impeccable-carbonize` div); drop `data-impeccable-params` and all `data-p-*` attributes.
5. **Delete** the inline `<style>` block, the param-values comment, both carbonize markers, and any `@scope` rules for non-accepted variants.

Then run `live-complete.mjs --id SESSION_ID` and verify `phase: "completed"` before polling again. The command is a gate, not a formality: it refuses with `error: "source_dirty"` plus findings while any live-mode leftover remains; fix and rerun (`--force` only for false positives).

## Handle `discard`

Event: `{id, _acceptResult, _completionAck}`. The poll script already restored the original and acknowledged `discarded`. Nothing to do unless `_completionAck.ok !== true`; then `live-complete.mjs --id EVENT_ID --discarded` and poll again.

## Handle `steer`

Event: `{id, message, pageUrl}`: page-level direction from the global bar's Steer control (typed or spoken), no element context, no variant cycling. Read `message`, inspect the page or files as needed, make edits or answer in prose. Reply `node .kiro/skills/impeccable/scripts/live-poll.mjs --reply EVENT_ID steer_done ["Optional short toast"]`, or on failure `--reply EVENT_ID error "Short reason"`, then poll immediately. No separate pickup reply; the Steer bar unlocks on `steer_done` or `error`.

## Handle `prefetch`

Event: `{pageUrl}`: fired once per route on first selection; the user is likely about to Go on a page you have not read. Resolve the route to its file (root `/` is usually the boot's `pageFile`; multi-page sites often map `/foo` to `public/foo/index.html`; SPAs map everything to one entry), read it, poll again. No `--reply`. If you cannot resolve it confidently, skip and poll.

## Handle `manual_edit_apply`

Event: `{id, pageUrl, batch: {entries}, evidencePath?, chunk?, repair?, deadlineMs}`.

The user already clicked Apply. Do not ask what to do, discard, or redirect to Go. The parent live thread keeps the foreground poll loop and sends the final `/poll --reply --data`.

When native subagents are available, delegate source edits to `impeccable_manual_edit_applier` / `impeccable-manual-edit-applier`. Pass cwd, scripts path, event id, page URL, chunk/deadline, `batch`, `evidencePath`, and the canonical JSON result schema. The subagent must not poll or reply. If unavailable, apply inline with the same contract.

If `repair` is present, the previous Apply changed source but final validation failed. Fix the current source and return the same canonical JSON result; do not roll files back yourself. The browser will ask the user before any rollback.

After source edits finish, reply exactly once with `node .kiro/skills/impeccable/scripts/live-poll.mjs --reply EVENT_ID done --data '{"status":"done","appliedEntryIds":["8hexid"],"failed":[],"files":["src/page.html"],"notes":[]}'`. Use `status:"partial"` or `status:"error"` with `failed[]` when not every entry applied. Then poll again. Never reply without the event id; `--reply done --file ...` is invalid for manual Apply.

## Exit

The user stops live mode by saying so in chat, closing the tab (SSE drops; poll returns `exit` after 8s), or the browser's exit button. On `exit`, kill any still-running background poll, then clean up.

## Cleanup

```bash
node .kiro/skills/impeccable/scripts/live-server.mjs stop
```

Stops the helper and runs `live-inject.mjs --remove` to strip the injected script (use `stop --keep-inject` to keep it for a quick restart; `.impeccable/live/config.json` persists as project config). Then search for and remove any leftover `impeccable-variants-start` wrappers and `impeccable-carbonize-start` blocks.

## First-time setup

Only when `live.mjs` reports `config_missing` / `config_invalid`, or `configDrift` needs explaining, or the config lacks `cspChecked`: read [live-setup.md](live-setup.md). It owns the config schema, the per-framework `files` table, injection adapters, drift healing, and the CSP detection and consent flow.

---

## 📄 `reference/new-work.md`

# New visual work

Use this flow when making a new surface or replacing a visual identity. PRODUCT.md owns product truth. DESIGN.md owns durable visual decisions. A surface brief keeps strategy that belongs only to one route or artifact. Complete [init.md](init.md) first when PRODUCT.md is missing; a missing DESIGN.md does not route back to init.

## 1. Decide what is already true

Read DESIGN.md, representative code, tokens, components, and assets.

- **Redesign:** preserve product truth, content, function, constraints, and explicit brand commitments; replace the old visual world rather than polishing it. The old look is evidence of what the subject is, not authority over what it becomes.
- **Established world:** inherit it. A missing DESIGN.md does not erase a coherent identity already present in code; document that identity instead of inventing a replacement.
- **Incomplete brand:** preserve confirmed assets and recognizable traits, then help the user expand the system for this new surface.
- **No visual authority:** create a new world with the user.

A section, component, feature, or state inside an established surface inherits that surface. Do not turn a local addition into a new identity exercise.

## 2. Ask what will change the work

Ask one round of two or three related questions through the structured question tool when available. Skip settled facts; a precise request may need only a compact confirmation.

- **Persuade:** clarify who must act, what they should believe, and which real proof, content, or assets can earn that belief.
- **Operate:** clarify the task, information, important states, frequency, and constraints.
- **Read:** clarify the reader's question, source material, structure, and wayfinding.
- **Experience:** clarify what leads, how exploration unfolds, and which interaction or transition matters.

Across modes, ask what success looks like, what must remain untouched, and what would make a polished result feel wrong. Do not ask for CSS values or canned aesthetic lanes.

## 3. Choose the right amount of invention

### Extend an existing surface

Inherit its world and composition. Resolve only the new purpose, content, hierarchy, states, interaction, and how the addition joins the surrounding experience. Do not run a concept tournament or change DESIGN.md unless the user approves a durable system change.

### Create a whole surface inside an established world

Keep the visual system fixed. Derive five to seven materially different structures from the content, task, and user behavior, ordered by resonance. For a genuinely open whole page, screen, or flow, run:

`node .kiro/skills/impeccable/scripts/concept-seed.mjs --scope surface --mode <mode>`

The script assigns which structure gets built; your top-ranked structure is what every run would ship, so the dice come from outside. Never run the script for a local extension or a precisely specified narrow request; shape those directly.

### Create or replace the visual world

1. Name the product's unique mechanism in one sentence, the audience's real scene, its cultural home, and what this first surface must prove. Note the page this category always ships and its predictable opposite; name both as the rut and keep them out of the seven-candidate list. A brief that paints its own picture, a product name, a titled artifact, a governing metaphor, adds its literal reading to the rut: spend at most one candidate on it and derive the rest from elsewhere in the audience's world.
2. From that cultural world, list seven concrete visual systems, artifacts, places, or rituals the audience knows by heart, each with one line on why it resonates and can carry the mechanism, ordered by resonance. The audience's world includes its graphic and screen traditions, not only its physical objects: the notation, publications, identity programs, data graphics, and interfaces it reads daily; a nameable abstract system (a school of poster, a documentation standard) is as concrete a candidate as any artifact. What would this thing look like as a physical object; what did its world look like before the web? Near-duplicates count once. When more than three of the seven share one material family, the derivation stopped at the subject's most obvious artifact; dig until the list spans at least three families.
3. Turn that material into complete directions: each joins a reusable visual world to a concrete first-surface experience.
4. Run `node .kiro/skills/impeccable/scripts/concept-seed.mjs --scope direction --mode <mode>` and follow what it prints. This step has no substitute and no skip condition: on a new or replacement world, writing artifact code before this script has run and its assignment is acknowledged is a contract violation, whatever the harness, the model, or the time pressure, because the roll is the mechanism that keeps every run from converging on the category default. The script assigns which direction gets built and deals catalog challengers. Fuse each challenger before judging it: the challenger supplies the form and its system grammar, the product supplies every fact, and clarity wins conflicts. Weigh fused challengers against the assigned direction on exactly two axes, audience identification and product clarity; losing to strong grounded material is a valid outcome, and beating a thin or tool-monoculture list is the point.
5. Present one direction, fully committed: its world, first viewport, visitor path, signature interaction, cross-surface reach, and honest risk. Alongside it, offer the hand's challengers as named alternates, the weighing's verdict written on each as its one-line case, an honest "fuses poorly because X" included; the weighing informs the user's choice, it never pre-empts it. A hand holds at most three challengers: when the roll deals more, the three strongest join the hand and the rest wait in the re-roll pool, noted in one line; dropping a challenger from the hand itself takes a named product-truth failure, disclosed. Add re-roll with an optional one-line steer. Never present a ranked menu of your own grounded candidates; a lineup of those invites the safest card. The two channels share this structure and differ only in richness: cards and boards on the decision page, names and one-liners through the structured tool; the structured tool's option list also carries the standing exit as its last option.

The standing exit: every direction round offers one quiet, permanent alternative, the category standard, played straight. It is the user's door, never yours: never recommend it, never weigh it against the roll, never let it soften the dealt directions; the counterweights bind the unchosen default, not the chosen one. When the user takes it, in the canon action, a safer-steer, or plain words asking for the familiar or competitor-like path, convention becomes the commitment: ask once for two or three products this should sit alongside, make their craft level the bar, and execute the canon at full fidelity, without irony or smuggled quirk. A standing preference gets recorded as a brand commitment in PRODUCT.md. Re-roll eliminates every direction already shown, grounded and challenger alike; after two consecutive re-rolls, ask what quality is missing. You may re-roll on your own only on named factual grounds, when the assigned direction cannot carry the product's truth or task; taste is never grounds. The user may re-roll freely, and a user- or brief-pinned direction beats the roll, always. Present the decision visually: write an options payload with the assigned direction leading, the dealt challengers as alternates carrying their QUALITY BAR cards, and re-roll, steer, plus canon enabled; a degraded roll with no challengers still uses the page, as a single text-only card with re-roll. Give every card the same anatomy, thesis, palette, materials, first viewport, honest risk, and the challengers' case lines (run the script with `--schema` for the exact shape); the page renders identity from these fields, and a challenger's catalog image rides as labeled inspiration, never as the promise of the build. Author `canonCard` too: the category standard as one honest card with the same anatomy; the page keeps it subordinate, and the counterweights still bind you. Run `node .kiro/skills/impeccable/scripts/serve-question.mjs --start --payload <file>` (run it with `--schema` first for the exact payload shape). It daemonizes, prints the page URL and a key, and exits immediately; now open that URL for the user, in-app browser first, then the system opener, then showing the URL. Collect the choice with `--wait --key <key>`, repeating while it exits 3; the ANSWER prints as JSON. Exit 4 means the page was closed without an answer: re-present once through the structured question tool, and with no answer there either, proceed unattended with the assigned direction and state the assumptions. A harness that can leave a shell blocked in the background may instead run the script without `--start` and let it auto-open and block. Only a session where no browser can open at all, headless, CI, an eval worker, a remote shell with no display, puts the same decision through the structured question tool instead; the script self-detects these environments and exits 2 with that advice, so treat exit 2 as this fallback, never as an error to retry.

When image generation exists, every card also declares a `sketch` path under `.impeccable/sketches/`, the canon card included. Where the harness sandboxes its shell, start the page through the least-sandboxed command path it offers: a sandboxed shell cannot bind the board's port, and the first-attempt failure costs a retry every session. Serve the page first, then produce the sketches; the page shimmer-waits per slot and the user may answer before they land. Render every sketch through one shared frame so the comparison stays about direction, never rendering luck: the requested surface's first viewport as a flat, matte design sketch in that card's own palette and type character, deliberately unfinished, no photorealism, no gloss, identical framing across cards; a candidate whose sketch looks more finished than the others has broken the comparison, not won it. The frame's aspect is the surface's own: a native app or mobile-first surface sketches portrait at its device viewport, a desktop web surface landscape, and the decision page adapts to either, so a phone screen sketched landscape is a broken frame, not a neutral default. The only legible text in a sketch is the product's real name and one real headline; every other text region is greeked, indistinct lines standing where copy will go, because a sketch that renders invented specs, prices, or dates puts claims in front of the user that PRODUCT.md never made. Produce in the order the user reads: the assigned card, then the hand, then canon, each file written the moment it is done. When the harness runs subagents in parallel, fan the set out as one agent per card: each spawn is the shipped asset producer with a single-sketch packet, that card's fields, PRODUCT.md, the shared frame, and the card's declared path, up to four in flight at once. A slot still empty when its agent returns is regenerated inline, and a slot still empty when the user answers is dropped without ceremony; no other supervision is owed. Without parallel subagents, generate in the main thread after serving, in the same reading order, and let the harness's own generation display carry the progress; the wait for the answer follows the last file. A sketch answers which world, never which composition: the comp round still renders its full set, and the chosen card's sketch seeds at most one probe. With no image generation, the cards carry their identity in palette chips and facts, and that page is complete, not a lesser version.

Catalog worlds are working systems, not mood references. When one survives, carry its palette and material, type and composition, topology, controls and state, and responsive rules into the product. When the source is itself an interface language, commit to its native grammar across navigation, content, controls, and states. Open the QUALITY BAR board and hero for the world you build the moment the choice lands, even if you viewed another card earlier; the ANSWER line names the chosen card's images (when the harness only reads files or runs sandboxed, download them into the workspace and open the relative path; sandboxed viewers reject absolute paths outside it). They set the craft level the build must reach, a rendered reference's finish, commitment, and art direction, never the composition; your surface serves this product.

Every direction the roll can land on must already be viable: every relationship and claim it visualizes true, a real palette and component family, a distinctive composition with one product-specific experience, workable at full-surface scale within the available assets, tools, and performance budget. A candidate that fails on truth is replaced before the roll, never rescued by it. Truth binds claims, not demonstrations: in greenfield work, author whatever illustrative material the concept needs at full fidelity, label it synthetic wherever a visitor could mistake it for the real thing, and hand the user the list of what to replace with real material. What stays uninventable are commercial and factual claims: prices, customers, benchmarks, endpoints, capabilities the product does not have. Refusing a bold direction because its demonstration data does not exist yet is the timidity reflex wearing honesty's clothes.

For **Persuade**, the opening must make the offer intelligible and desirable, expose a clear action, and demonstrate something only this product can prove. Conversion lives inside the form's own vocabulary: a hook that lands in one line, a visible primary action, a legible reading order. A committed form that hides the offer or the action has not finished translating. For **Operate**, expression may never obscure the task, state, or familiar affordance. For **Read**, comprehension and wayfinding remain intact. For **Experience**, the work itself leads from the first viewport.

## 4. Commit the world

Pick a color strategy before picking colors: Restrained (neutrals plus one accent; the default when the visitor came to operate or read), Committed (one saturated color carries 30-60% of the surface), Full palette (3-4 named roles), or Drenched (the surface IS the color). Persuade and Experience surfaces have permission for the bolder strategies; take them when the brief allows. Color commits at page scale: fields that own whole regions, not accents scattered over a neutral ground. Dark or light is never a default: write one sentence of physical scene (who uses this, where, under what light) and let it force the answer.

Choose faces like objects from the subject's world, in the mode's register. Operate and Read surfaces are well served by system stacks and workhorse UI faces; Persuade and Experience surfaces want faces with a point of view, and these training-data defaults mean you stopped looking: Fraunces, Playfair Display, Cormorant, Lora, Crimson, Newsreader, Syne, Space Grotesk, Space Mono, IBM Plex, Inter-as-display, DM Sans, DM Serif, Outfit, Plus Jakarta Sans, Instrument Sans. Naming one of these faces anyway requires a reason no other face could satisfy, and a subject association is never that reason: books wanting a serif, bookshops wanting hand-lettering, and tech wanting a mono are the associations the list exists to break.

Calibration: AI-generated interfaces cluster around a few looks regardless of subject: warm cream ground, high-contrast serif display, and a terracotta or signal-red accent; near-black with one neon accent and glowing edges; broadsheet-editorial hairlines, italic display serif, and small tracked mono labels. All are legitimate when the brief calls for them. Where the brief leaves the aesthetic free, landing in one means the self-check failed: if someone could guess your aesthetic from the category alone, or from category-plus-avoidance, rework until neither answer is obvious. Energy is not the enemy of trust: a brief's negative constraints (no gamification, no hype) rule out those devices, not exuberance, and adjectives describing the product's behavior (quiet support, calm coaching) do not dictate the surface's energy. A bookish, warm, or child-facing subject does not soften the calibration: book cloth, thread, jackets, endpapers, and shelf ephemera span the whole saturated spectrum, and cream paper is the smallest corner of that world; landing on cream plus serif for a book subject is the default wearing the subject's clothes. A brief-pinned world pins the world, not its softest rendition: the pinned world's full material range stays in play, and a rendition that matches what any model ships for that world failed the self-check at execution rather than selection.

## 5. Record the decision

Before code, state the chosen direction as a contract in the artifact's opening comment, five short blocks, 150 words at most, in a form that survives the production build: an HTML comment in the emitted markup, never only a templating-frontmatter comment, placed as the first child of the document's body in the root layout, never inside a slotted or child component (some compilers, Astro among them, strip a slot's leading comment while keeping deeper ones). After the first production build, grep the built output for the seed key; a contract the build erased is a contract nobody can audit. THESIS: the one idea this surface owns and the category-default arrangement it refuses. OWN-WORLD: the palette and component language, specific enough to be recognizable with all content removed. STORY: what the visitor understands, believes, and does. FIRST VIEWPORT: the exact composition, what is where and at what scale, and where the primary action sits. FORM: the chosen form, its position on your ordered list, and the seed key the script printed. Close the comment with one more line, FINISH: the run's exit condition, verbatim "unreviewed and undocumented is unfinished; this build ends with the finish review, the verdict, and DESIGN.md". The comment tops the artifact you re-open on every edit, the one reminder that survives a long build: a page that looks complete with the FINISH line undischarged is not done, it is abandoned at the finish line. If a block reads like a mood, the direction is not decided yet; the finishing review audits the render against this contract.

On a new or replacement world, DESIGN.md is written at finish, from the built world, by the shipped documenter (section 7); a rulebook written before the build gets defended against reality instead of describing it, and hands the design-system detector an unstable target. A new world shipped with no DESIGN.md is still an incomplete run. An ordinary extension does not rewrite DESIGN.md.

If the work establishes durable strategy for a route or artifact, read its existing surface brief, then update it:

`node .kiro/skills/impeccable/scripts/surface-brief.mjs read <primary-target>`

`node .kiro/skills/impeccable/scripts/surface-brief.mjs write <primary-target> <body-file> [related-target ...]`

Keep the brief small: scope and visitor mode; audience, job, action/task, proof/content, and constraints; chosen direction and memorable moment; unresolved decisions. Do not copy global product truth or DESIGN.md tokens into it.

Whenever any image generation is available, a harness-native tool or the API fallback context.mjs reports, the locked direction is visualized before it is built, never skipped: load [visualize.md](visualize.md) and follow it, three compositional options rendered and put before the user for approval. This step is proven to produce the most compositional and ambitious work.

For `shape`, return the selected direction to [shape.md](shape.md) and stop before persistence or implementation.

## 6. Build with full commitment

When an approved comp exists, the comp is king, and the build happens in phases. Phase one is reproduction: rebuild the comp at its own breakpoint until a screenshot at the comp's width and height overlaps it near pixel-perfectly, materials, components, elevation, assets, and implied design language included. Exactly three concessions exist: fonts (the closest obtainable face), icons (exact match unless the user already chose an icon library), and genuine defects in the generated comp such as spelling errors. Everything else must match, and models systematically believe their HTML, CSS, and SVG recreation succeeded when it did not, so the overlap comparison is the authority, never your conviction: set the screenshot beside the freshly reopened comp image at identical dimensions after every region, never beside your memory of it, and when a region keeps losing that comparison, stop recreating it in code and produce it as a rendered asset composited into the page. The comp also outranks every written record of it: when the recorded brief or inventory commits to less than the comp shows, a softer texture, a sparser field, a sculpted plate reduced to flat CSS, correct the record upward to the comp; qualifiers like subtle, restrained, and low-contrast, and counts rounded down to a comfortable fraction, are how approved materials die between approval and build. A produced material must then survive to the screen: a texture buried under a nearly opaque color wash ships the wash, not the material, so judge every material by the screenshot beside the comp, never by the stylesheet. Only when reproduction holds does phase two begin: static regions that should live become animated or interactive, reveals and motion are added, then responsiveness across the surface's devices. Where the comp does not cover the whole surface, continue building the remainder inside the comp's recorded world and design language; a component the comp never shows inherits the recorded system's corner language, line weights, and materials, and may not introduce container styles, border weights, or chrome the comp never uses.

Build the assigned direction, not a safer interpretation of it. The form supplies structure, reading order, component conventions, and native motion; the product supplies every fact. Commit every atom: nav, buttons, inputs, and links are rebuilt in the form's vocabulary, and a stock component inside a committed form is a lapse. Land the first build fully committed; committing is the hard part, and the passes that follow exist to make the committed thing clear and effective, never to dilute it. In unattended work, the safe rendition is the known risk.

- **The first viewport is a thesis, not a header.** Demonstrate the mechanism immediately, at the scale the form has in life; do not trap the concept inside a standard hero or card shell. The memory test: if someone left after one viewport, what would they describe an hour later? If the honest answer is a mood, the concept has not committed yet.
- **Prove the hero before building past it.** When an approved comp exists, render the first viewport, capture it, and set it beside the comp's first viewport before any later section: the hero carries the run's ambition, and every following section inherits its shortfall. Judge scale and density as quantities, a field at a tenth of the comp's coverage or type at half its weight is a different design, and a five-minute retry here is what a rebuild verdict at the finish costs when this check is skipped.
- **Prove, don't claim.** Show the subject doing its job: the interface at work, the mechanism dramatized, specifics a competitor could not copy-paste. Sections that restate a claim in different words add length, not substance. Demonstration data is design material: author it at full fidelity and label it synthetic; claims stay uninventable.
- **Author the assets; never substitute chrome.** Great surfaces live on carefully made content: names, entries, copy, covers, thumbnails, textures. In greenfield work every blank the ask round left open is yours to author at production fidelity; content is authorable, claims are labelable, no section is omittable. An unanswered commercial claim ships as a clearly marked placeholder on the user's replacement list. When image generation exists, producing the design's imagery is part of building, at the scale the composition needs: a viewport that wants atmosphere gets a full-bleed layered scene, and a library of small centered subjects standardized for tidiness forecloses it. Gradients, glass, and generic icon tiles where an authored asset belongs are the gap wearing chrome; icons drawn in the world's own grammar are the remedy, not the target.
- **Build the form's web leverage.** When the chosen world names a technique (canvas, WebGL, view transitions, generative motion), build the technique itself, not a static imitation of it; the graceful fallback serves constrained clients, it is not the default experience.
- **Pace the scroll like a studio.** Vary density, scale, image, motion, and quiet inside one grammar; a dense passage earns a quiet one, and the page ends anchored by a real close. One spacing rhythm throughout, with more space above a heading than below it.
- **Use real, verified imagery when the brief implies it.** Search for the subject's physical object rather than the category; one decisive photo beats five mediocre ones. Verify stock URLs resolve.
- **Author motion as material.** The form has native motion, what it does in life between states; give the page that motion once, orchestrated, rather than scattered hover effects. Bound expensive effects and keep content visible by default.

Preserve semantics, accessibility, performance, responsiveness, project conventions, and working behavior.

## 7. Inspect and finish

Inspect desktop and mobile in one batched screenshot round, critique the render against the user's request and the direction contract, fix material gaps, and confirm with one final round; two rounds is the ceiling, and fixes batch between them rather than earning per-tweak screenshots. When an approved comp exists, the critique is a side-by-side: view the comp region and the build region together, the hero and each section as its own crop at legible scale, never one full-page thumbnail, which hides exactly the failures that matter, crude controls, wrong lettering character, flattened material, behind a superficially similar section order. On a Persuade surface, verify the mode did its job: a first-time visitor should know what this is, why it matters, and what to do within seconds, in the form's own vocabulary.

After the second inspection round the build thread's polishing is over: no further defect hunts, micro-edit scripts, or rebuilds here; whatever remains ships through the handoffs, where a fresh context does the finding better and cheaper. Where this harness runs no design hook, run `node .kiro/skills/impeccable/scripts/detect.mjs --json` on the changed targets once here, fix what is mechanical, and pass the remaining findings to the reviewer; a hookless build that skips this ships every tell the hook exists to catch. Capture desktop and mobile screenshots to files, then spawn the shipped finish reviewer, `impeccable-finish-reviewer` (`impeccable_finish_reviewer` in codex; `/impeccable-finish-reviewer` in Cursor; on GitHub Copilot say "Use the impeccable-finish-reviewer agent"), with the original request, confirmed answers, the artifact path, the screenshot paths, its direction contract, existing hook findings, the QUALITY BAR card and approved comp paths, and the craft-floor reference path. The reviewer has no browser; screenshots you fail to pass are checks it cannot run. Never read the shipped agents' definition files before spawning; the harness loads them at spawn, and you owe only the input packet. Wait on any agent with one long timeout rather than a loop of short polls, and spend the wait on the next independent step. Verify its return carries the five contract sections; on an empty or thrashed return, respawn once with the same inputs before doing anything else. This review never runs inside the build thread and never inherits it: spawn the reviewer fresh, with no forked conversation history (`fork_turns: 0` in codex); a reviewer that inherits your transcript inherits your framing, your optimism, and your abstractions, and everything it needs travels in the inputs above. Only a harness whose tool surface has no subagent capability at all substitutes a fresh in-thread pass after stepping fully out of the build context, run from [degraded/finish-reviewer.md](degraded/finish-reviewer.md), and a substituted or failed-and-replaced review is disclosed in one line at finish, never silently. When the reviewer's first material fix is a rebuild directive, fidelity failed wholesale rather than in patches, so skip the fix batch and execute the rebuild immediately: re-derive the named regions, produce the named assets, and send the result back for a verdict, telling the user what is happening rather than asking permission to fix a failure. The user is consulted only when a second rebuild directive arrives, both verdicts on the table, or when rebuilding would discard content the user approved. Otherwise apply the material fixes in one batch, rebuild once, and recapture the same viewports. A recapture measures positions, loading, and overflow; it cannot measure whether a fix reached the quality the finding named, so send the recaptured screenshots back to the same reviewer for a verdict scoring every material fix resolved, partial, or unresolved (through the harness's agent continuation; without one, run the scoring fresh from [degraded/finish-reviewer.md](degraded/finish-reviewer.md)'s Verdict Pass). Fixes scored partial or unresolved get another batch, recapture, and verdict. Two rounds is the budget an unattended run ends at; an attended session's ceiling belongs to the user, so when the second verdict still lists open items, put the table in front of them and let them choose between shipping as it stands and funding another round. Whoever is deciding, stop the moment a round resolves nothing, and the reviewer's findings are the only list you work from, never your own re-opened hunt. Report the final verdict table to the user as it stands, open items included, under the reviewer's own disposition word: a table with open material findings is never announced as a pass, and never under a softer label than the reviewer wrote. Do not run a second detector.

Then spawn the shipped documenter, `impeccable-documenter` (`impeccable_documenter` in codex), with the project root, the artifact path, the direction contract, PRODUCT.md, the [document.md](document.md) reference path, and the boundary to write at; it records DESIGN.md and the sidecar from the built world, ground truth over intention; without subagents the pass runs from [degraded/documenter.md](degraded/documenter.md). A clean detector pass is not finished; finished is the contract kept, the comp honored, the review closed, and the system recorded.

---

## 📄 `reference/overdrive.md`

Start your response with:

```
──────────── ⚡ OVERDRIVE ─────────────
》》》 Entering overdrive mode...
```

Push an interface past conventional limits. This isn't just about visual effects. It's about using the full power of the browser to make any part of an interface feel extraordinary: a table that handles a million rows, a dialog that morphs from its trigger, a form that validates in real-time with streaming feedback, a page transition that feels cinematic.

**EXTRA IMPORTANT FOR THIS COMMAND**: Context determines what "extraordinary" means. A particle system on a creative portfolio is impressive. The same particle system on a settings page is embarrassing. But a settings page with instant optimistic saves and animated state transitions? That's extraordinary too. Understand the project's personality and goals before deciding what's appropriate.

### Propose Before Building

This command has the highest potential to misfire. Do NOT jump straight into implementation. You MUST:

1. **Think through 2-3 different directions**: consider different techniques, levels of ambition, and aesthetic approaches. For each direction, briefly describe what the result would look and feel like.
2. **ask the user directly to clarify what you cannot infer.** to present these directions and get the user's pick before writing any code. Explain trade-offs (browser support, performance cost, complexity).
3. Only proceed with the direction the user confirms.

Skipping this step risks building something embarrassing that needs to be thrown away.

### Iterate with Browser Automation

Technically ambitious effects almost never work on the first try. You MUST actively use browser automation tools to preview your work, visually verify the result, and iterate. Do not assume the effect looks right, check it. Expect multiple rounds of refinement. The gap between "technically works" and "looks extraordinary" is closed through visual iteration, not code alone.

---

## Assess What "Extraordinary" Means Here

The right kind of technical ambition depends entirely on what you're working with. Before choosing a technique, ask: **what would make a user of THIS specific interface say "wow, that's nice"?**

### For visual/marketing surfaces
Pages, hero sections, landing pages, portfolios: the "wow" is often sensory: a scroll-driven reveal, a shader background, a cinematic page transition, generative art that responds to the cursor.

### For functional UI
Tables, forms, dialogs, navigation: the "wow" is in how it FEELS: a dialog that morphs from the button that triggered it via View Transitions, a data table that renders 100k rows at 60fps via virtual scrolling, a form with streaming validation that feels instant, drag-and-drop with spring physics.

### For performance-critical UI
The "wow" is invisible but felt: a search that filters 50k items without a flicker, a complex form that never blocks the main thread, an image editor that processes in near-real-time. The interface just never hesitates.

### For data-heavy interfaces
Charts and dashboards: the "wow" is in fluidity: GPU-accelerated rendering via Canvas/WebGL for massive datasets, animated transitions between data states, force-directed graph layouts that settle naturally.

**The common thread**: something about the implementation goes beyond what users expect from a web interface. The technique serves the experience, not the other way around.

## The Toolkit

Organized by what you're trying to achieve, not by technology name.

### Make transitions feel cinematic
- **View Transitions API** (same-document: all browsers; cross-document: no Firefox): shared element morphing between states. A list item expanding into a detail page. A button morphing into a dialog. This is the closest thing to native FLIP animations.
- **`@starting-style`** (all browsers): animate elements from `display: none` to visible with CSS only, including entry keyframes
- **Spring physics**: natural motion with mass, tension, and damping instead of cubic-bezier. Libraries: motion (formerly Framer Motion), GSAP, or roll your own spring solver.

### Tie animation to scroll position
- **Scroll-driven animations** (`animation-timeline: scroll()`): CSS-only, no JS. Parallax, progress bars, reveal sequences all driven by scroll position. (Chrome/Edge/Safari; Firefox: flag only; always provide a static fallback)

### Render beyond CSS
- **WebGL** (all browsers): shader effects, post-processing, particle systems. Libraries: Three.js, OGL (lightweight), regl. Use for effects CSS can't express.
- **WebGPU** (Chrome/Edge; Safari 26+; Firefox on Windows/macOS; flag only on Firefox Linux/Android): next-gen GPU compute, more powerful than WebGL. Always fall back to WebGL2.
- **Canvas 2D / OffscreenCanvas**: custom rendering, pixel manipulation, or moving heavy rendering off the main thread entirely via Web Workers + OffscreenCanvas.
- **SVG filter chains**: displacement maps, turbulence, morphology for organic distortion effects. CSS-animatable.

### Make data feel alive
- **Virtual scrolling**: render only visible rows for tables/lists with tens of thousands of items. No library required for simple cases; TanStack Virtual for complex ones.
- **GPU-accelerated charts**: Canvas or WebGL-rendered data visualization for datasets too large for SVG/DOM. Libraries: deck.gl, regl-based custom renderers.
- **Animated data transitions**: morph between chart states rather than replacing. D3's `transition()` or View Transitions for DOM-based charts.

### Animate complex properties
- **`@property`** (all browsers): register custom CSS properties with types, enabling animation of gradients, colors, and complex values that CSS can't normally interpolate.
- **Web Animations API** (all browsers): JavaScript-driven animations with the performance of CSS. Composable, cancellable, reversible. The foundation for complex choreography.

### Push performance boundaries
- **Web Workers**: move computation off the main thread. Heavy data processing, image manipulation, search indexing: anything that would cause jank.
- **OffscreenCanvas**: render in a Worker thread. The main thread stays free while complex visuals render in the background.
- **WASM**: near-native performance for computation-heavy features. Image processing, physics simulations, codecs.

### Interact with the device
- **Web Audio API**: spatial audio, audio-reactive visualizations, sonic feedback. Requires user gesture to start.
- **Device APIs**: orientation, ambient light, geolocation. Use sparingly and always with user permission.

**NOTE**: This command is about enhancing how an interface FEELS, not changing what a product DOES. Adding real-time collaboration, offline support, or new backend capabilities are product decisions, not UI enhancements. Focus on making existing features feel extraordinary.

## Implement with Discipline

### Progressive enhancement is non-negotiable

Every technique must degrade gracefully. The experience without the enhancement must still be good.

```css
@supports (animation-timeline: scroll()) {
  .hero { animation-timeline: scroll(); }
}
```

```javascript
if ('gpu' in navigator) { /* WebGPU */ }
else if (canvas.getContext('webgl2')) { /* WebGL2 fallback */ }
/* CSS-only fallback must still look good */
```

### Performance rules

- Target 60fps. If dropping below 50, simplify.
- Lazy-initialize heavy resources (WebGL contexts, WASM modules) only when near viewport.
- Pause off-screen rendering. Kill what you can't see.
- Test on real mid-range devices, not just your development machine.

### Polish is the difference

The gap between "cool" and "extraordinary" is in the last 20% of refinement: the easing curve on a spring animation, the timing offset in a staggered reveal, the subtle secondary motion that makes a transition feel physical. Don't ship the first version that works; ship the version that feels inevitable.

**NEVER**:
- Ship effects that cause jank on mid-range devices
- Use bleeding-edge APIs without a functional fallback
- Add sound without explicit user opt-in
- Use technical ambition to mask weak design fundamentals; fix those first with other commands
- Layer multiple competing extraordinary moments. Focus creates impact, excess creates noise

## Verify the Result

- **The wow test**: Show it to someone who hasn't seen it. Do they react?
- **The removal test**: Take it away. Does the experience feel diminished, or does nobody notice?
- **The device test**: Run it on a phone, a tablet, a Chromebook. Still smooth?
- **The context test**: Does this make sense for THIS brand and audience?

"Technically extraordinary" isn't about using the newest API. It's about making an interface do something users didn't think a website could do.

---

## 📄 `reference/visualize.md`

# Visualize: Direction Comps & Asset Production

Load this from [new-work.md](new-work.md) whenever any image generation is available, a harness-native tool or the API fallback context.mjs reports. PRODUCT.md and DESIGN.md are preconditions. New-work has already resolved the visual world; this file must not reopen it.

The purpose of a probe is to test composition, narrative, hierarchy, density, focal moment, signature use, and image requirements. It is not a second identity workshop. Keep DESIGN.md's palette, typography direction, material language, component character, imagery stance, and motion grammar fixed.

## Generate three compositional options

Render three distinct high-fidelity north-star comps of the requested surface, with whatever generation capability exists, saved under `.impeccable/mocks/` so they survive the session. Comp at the surface's own viewport: portrait at device size for a native app or mobile-first surface, desktop landscape otherwise; a phone screen comped landscape misstates the composition before anything gets built against it. Comps are the build thread's own work, never delegated: the thread that writes the comp prompts holds the direction's full context, and it has already seen every comp when the build starts. Open every image you produce or reference by its workspace-relative path, never an absolute one: sandboxed viewers reject absolute paths, and everything under the project root has a relative path. Base them on the real content and the surface concepts already developed with the user. Three is the number: one comp invites rubber-stamping, and the spread between three is what surfaces the composition worth building. A decision-page sketch is not a probe: it chose the direction at deliberately unfinished fidelity, so the three comps render regardless, and the chosen card's sketch seeds at most one of them.

- A comp is a designed surface, not a picture of the subject. Lead the generation prompt with the surface's own structure, whatever regions this design actually has, named in order with their scale relationships; a page with no navigation states that instead of inventing one, and an unconventional surface states its unconventional skeleton. A prompt that leads with the world's atmosphere gets a vignette back: the model paints the fish market instead of the fish market's website. Self-check every render: if it could hang as a poster, or reads as a photograph or scene with some text on it, it is not a comp; regenerate with the layout scaffold stated more literally.
- When the user shortlisted multiple concepts, spread the three across them.
- When one direction is committed, vary the structural uncertainty an image can resolve: topology, sequence, density, hierarchy, focal composition, or interaction framing.
- Show enough beyond the opening moment to prove the concept can govern the whole requested surface.
- Do not generate a palette artifact, ask new atmosphere questions, introduce a different type voice, or invent a new motif. If the committed world cannot support the concept, return to the concept shortlist rather than changing the world.

Treat each comp as a direction test, not a screenshot specification. Core UI text, responsive behavior, accessibility, semantics, and interaction states remain implementation responsibilities.

## One approval point

Show the three together: in the harness when it can display images, otherwise on the decision page (`serve-question.mjs`, one option per comp with the comp as its hero). Ask what should carry forward, what feels false to the world, and whether the selected surface concept should be approved, combined, revised, or rejected. Then stop and wait. A structured simulated user counts as attended and receives the same question.

Do not begin code until the user approves a direction or explicitly delegates the choice. If they delegate, choose using the task brief, PRODUCT.md, and DESIGN.md, and state the evidence. Approval refines the task concept; it does not modify DESIGN.md.

This approval point has no substitute and no skip condition. When the structured question tool errors, fall back to the decision page; only after both fail may you treat the choice as delegated, and a delegated pick is still recorded exactly as an approval is and disclosed in your first reply, not your last. The finish reviewer treats a build with generated comps and no recorded approval as carrying a material finding.

After approval, record the choice where tools can find it: the approved comp's path goes in the surface brief, and the approved comp's `.json` prompt sidecar gains `"approved": true` (every comp generated through `generate-image.mjs` has one; create it if a native tool didn't). The sidecar travels with the mocks folder, so the approval survives sessions and machines that never see the brief. Then summarize the composition and the parts of the comp that must not be literalized, return to new-work.md, record the direction contract from the approved surface concept, and build.

## Inventory implementation fidelity

Before building, read the approved comp as a design system and record it in the brief: component grammar, corner language, line weights, elevation treatment, and the type ramp, because everything the comp does not show gets built from this record, and without it the fallback is the model's stock kit of square boxes, 1px grids, bento cells, and hard shadows. Then inventory the comp's major visible ingredients in writing (a short table in the surface brief or working notes; the finish reviewer audits shipped assets against it) and choose an implementation medium for each: semantic HTML/CSS/SVG, existing project asset, generated raster, sourced raster, icon library, canvas/WebGL, or accepted omission. The same written inventory names the comp's compositional commitments: navigation items and icons, headline levels and their scale relationship, signature geometry such as seams, masks, and overlaps, and each section's arrangement and density. The primary action gets its own row with its own medium: when the comp dissolves, stamps, erodes, or otherwise physically works the main CTA, that treatment is signature material on the page's most important element, and shrinking it to a border trick or a few decorative pixels is the compliance-token version of commitment. An element never written down is the element the build silently drops, and the direction contract's 150 words cannot carry this list, so this inventory is where it lives.

The medium column is where an approved design most often dies, so it obeys a gate: the medium is decided by what the comp region shows, never by what feels buildable in the current stack. A human figure, a product object, machinery, or any material with lighting and depth is raster whatever the stack, and so is any texture by that name alone: woven cloth, paper grain, fabric, leather, brushed metal need no depth argument, because a CSS gradient or layered background is not a texture medium and "layered CSS textures" is not a medium at all. Writing "silhouette" for a photographic figure, or "CSS" for a sculpted panel's finish or a cotton field's weave, is not a medium choice, it is the quiet deletion of the approved design, and it is how a comp full of physical material becomes a flat page with the same section order. Style does not move this boundary: a comp region with perspective, shading, figure drawing, or dense mechanical detail is illustration however line-drawn it looks, and no build session can author illustration as vectors, so it regenerates as raster like any photograph. Authored SVG covers what a session can specify exactly, diagrams with countable elements, controls, flat shape systems, and it ends where drawing skill begins; an instruction-manual world does not convert its illustrations into diagrams, it makes them line-art illustrations. Produce such regions by regenerating them cleanly, with the approved comp and its embedded prompt as the reference for a fresh render at asset resolution; never crop pixels out of the comp itself, whose effective resolution sits far below asset grade. Dropping an image-native region instead of producing it is a scope decision the user makes at the approval point, never a silent flattening after it. Generated imagery is a material, not a claim: evidence rules bind assertions, specs, testimonials, and photographs presented as real, never render fidelity, so "no photography on hand" forbids fake proof, not an illustrated hero.

The gate runs both ways: precise geometry, hard-edged shape systems, diagrams, expressive motion, shaders, and anything interactive are vector and GPU territory (SVG, canvas, WebGL), where a raster flattens what should move, scale, and respond, and code executed safely and professionally remains first-class there. A field or texture built from many small elements carries a quantity commitment either way: write down its approximate density and coverage ("thousands of glyphs over two-thirds of the fold, dense at the top fading into the path"), because a field rebuilt at a tenth of its density passes every checklist and still is not the design. TYPE rows carry the same discipline: name the face's compression class, and render one headline word against the comp before building on it; a visibly wider or lighter silhouette means the face is wrong, and every section built on it inherits the miss. Raster is for what the world paints; code is for what the world draws, animates, or reacts with, and choosing code there is ambition, not economy. Every `produce` entry is produced before the build ships, through the asset producer or in the current thread; an inventory with unproduced entries is an unfinished build, and this gate is where imagery-free pages come from when it is skipped.

Pay special attention to the dominant composition, signature use, image-native content, second-fold system, and any interaction the still image only implies.

Treat the comp as a north star, not something to trace, and know what that allows: translation into semantic, responsive, accessible code, never recomposition. Keeping the palette and mood while redrawing the topology is a second art direction, not an adaptation. Do not rasterize core UI text or controls. Do not substitute a different visual driver after approval without asking.

## Produce only the assets the build needs

Generation context is part of the asset: a build composed by a thread that never saw the prompts places assets it does not understand. So prefer generating build-critical imagery in the build thread when the budget allows, and when a subagent produces assets instead, every asset must carry its prompt, and the builder reads those prompts before composing a single one of them. The carrier is uniform across harnesses: after generating any image with any tool, native or `generate-image.mjs` (which does it automatically), run `node .kiro/skills/impeccable/scripts/embed-prompt.mjs <image> --prompt "<the prompt used>"` so the intent lives inside the file itself and survives copies between machines and harnesses; `--read` recovers it from any impeccable-generated image.

When the harness runs subagents, spawn the shipped asset producer every time, even when the inventory's produce bucket looks empty: its manifest is the independent second opinion on your media, and runs that skipped the spawn are the runs whose cotton became CSS. An honestly empty manifest costs one cheap spawn; a wrongly empty produce bucket costs the build its materials. Use the producer, `impeccable-asset-producer` (`impeccable_asset_producer` in codex; `/impeccable-asset-producer` in Cursor; on GitHub Copilot say "Use the impeccable-asset-producer agent"): give it the approved comp, output paths, required dimensions and formats, transparency needs, crop notes, and what must remain semantic code. Otherwise produce the minimum required assets in the current thread by the book: load [degraded/asset-producer.md](degraded/asset-producer.md) and follow it inline, with whatever generation exists, the native tool or generate-image.mjs.

Convert images with a converter context.mjs reported at boot (the IMAGE_TOOLS line); probe only when it reported none, at most once per session, never per image.

Return to [new-work.md](new-work.md) for the direction contract, implementation, and the finishing pass.
