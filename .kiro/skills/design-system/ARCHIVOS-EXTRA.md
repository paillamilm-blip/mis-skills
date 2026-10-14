# Archivos extra de `design-system`

No caben en el paquete de Kiro (máx. 25 archivos por skill).
- **Documentación** (✅ incluida): su contenido completo está más abajo en este archivo.
- **Datos / código / binarios** (⬇️): descárgalos a la ruta indicada solo si la tarea los necesita:

```bash
mkdir -p "$(dirname <archivo>)" && curl -fsSL <enlace> -o <archivo>
```

| Archivo | Estado | Enlace |
|---------|--------|--------|
| `references/component-specs.md` | ✅ incluida abajo | https://raw.githubusercontent.com/paillamilm-blip/mis-skills/main/kiro-skills/03-diseno/design-system/references/component-specs.md |
| `references/tailwind-integration.md` | ✅ incluida abajo | https://raw.githubusercontent.com/paillamilm-blip/mis-skills/main/kiro-skills/03-diseno/design-system/references/tailwind-integration.md |
| `references/token-architecture.md` | ✅ incluida abajo | https://raw.githubusercontent.com/paillamilm-blip/mis-skills/main/kiro-skills/03-diseno/design-system/references/token-architecture.md |

---

## 📄 `references/component-specs.md`

# Component Specifications

Detailed specs for core components with states and variants.

## Button

### Variants

| Variant | Background | Text | Border | Use Case |
|---------|------------|------|--------|----------|
| default | primary | white | none | Primary actions |
| secondary | gray-100 | gray-900 | none | Secondary actions |
| outline | transparent | foreground | border | Tertiary actions |
| ghost | transparent | foreground | none | Subtle actions |
| link | transparent | primary | none | Navigation |
| destructive | red-600 | white | none | Dangerous actions |

### Sizes

| Size | Height | Padding X | Padding Y | Font Size | Icon Size |
|------|--------|-----------|-----------|-----------|-----------|
| sm | 32px | 12px | 6px | 14px | 16px |
| default | 40px | 16px | 8px | 14px | 18px |
| lg | 48px | 24px | 12px | 16px | 20px |
| icon | 40px | 0 | 0 | - | 18px |

### States

| State | Background | Text | Opacity | Cursor |
|-------|------------|------|---------|--------|
| default | token | token | 1 | pointer |
| hover | darker | token | 1 | pointer |
| active | darkest | token | 1 | pointer |
| focus | token | token | 1 | pointer |
| disabled | muted | muted-fg | 0.5 | not-allowed |
| loading | token | token | 0.7 | wait |

### Anatomy

```
┌─────────────────────────────────────┐
│  [icon]  Label Text  [icon]         │
└─────────────────────────────────────┘
     ↑                      ↑
  leading icon         trailing icon
```

---

## Input

### Variants

| Variant | Description |
|---------|-------------|
| default | Standard text input |
| textarea | Multi-line text |
| select | Dropdown selection |
| checkbox | Boolean toggle |
| radio | Single selection |
| switch | Toggle switch |

### Sizes

| Size | Height | Padding | Font Size |
|------|--------|---------|-----------|
| sm | 32px | 8px 12px | 14px |
| default | 40px | 8px 12px | 14px |
| lg | 48px | 12px 16px | 16px |

### States

| State | Border | Background | Ring |
|-------|--------|------------|------|
| default | gray-300 | white | none |
| hover | gray-400 | white | none |
| focus | primary | white | primary/20% |
| error | red-500 | white | red/20% |
| disabled | gray-200 | gray-100 | none |

### Anatomy

```
Label (optional)
┌─────────────────────────────────────┐
│ [icon] Placeholder/Value   [action] │
└─────────────────────────────────────┘
Helper text or error message
```

---

## Card

### Variants

| Variant | Shadow | Border | Use Case |
|---------|--------|--------|----------|
| default | sm | 1px | Standard card |
| elevated | lg | none | Prominent content |
| outline | none | 1px | Subtle container |
| interactive | sm→md | 1px | Clickable card |

### Anatomy

```
┌─────────────────────────────────────┐
│ Card Header                         │
│   Title                             │
│   Description                       │
├─────────────────────────────────────┤
│ Card Content                        │
│   Main content area                 │
│                                     │
├─────────────────────────────────────┤
│ Card Footer                         │
│   Actions                           │
└─────────────────────────────────────┘
```

### Spacing

| Area | Padding |
|------|---------|
| header | 24px 24px 0 |
| content | 24px |
| footer | 0 24px 24px |
| gap | 16px |

---

## Badge

### Variants

| Variant | Background | Text |
|---------|------------|------|
| default | primary | white |
| secondary | gray-100 | gray-900 |
| outline | transparent | foreground |
| destructive | red-600 | white |
| success | green-600 | white |
| warning | yellow-500 | gray-900 |

### Sizes

| Size | Padding | Font Size | Height |
|------|---------|-----------|--------|
| sm | 4px 8px | 11px | 20px |
| default | 4px 10px | 12px | 24px |
| lg | 6px 12px | 14px | 28px |

---

## Alert

### Variants

| Variant | Icon | Background | Border |
|---------|------|------------|--------|
| default | info | gray-50 | gray-200 |
| destructive | alert | red-50 | red-200 |
| success | check | green-50 | green-200 |
| warning | warning | yellow-50 | yellow-200 |

### Anatomy

```
┌─────────────────────────────────────┐
│ [icon]  Title                    [×]│
│         Description text            │
└─────────────────────────────────────┘
```

---

## Dialog

### Sizes

| Size | Max Width | Use Case |
|------|-----------|----------|
| sm | 384px | Simple confirmations |
| default | 512px | Standard dialogs |
| lg | 640px | Complex forms |
| xl | 768px | Data-heavy dialogs |
| full | 100% - 32px | Full-screen on mobile |

### Anatomy

```
┌───────────────────────────────────────┐
│ Dialog Header                      [×]│
│   Title                               │
│   Description                         │
├───────────────────────────────────────┤
│ Dialog Content                        │
│   Scrollable if needed                │
│                                       │
├───────────────────────────────────────┤
│ Dialog Footer                         │
│                     [Cancel] [Confirm]│
└───────────────────────────────────────┘
```

---

## Table

### Row States

| State | Background | Use Case |
|-------|------------|----------|
| default | white | Normal row |
| hover | gray-50 | Mouse over |
| selected | primary/10% | Selected row |
| striped | gray-50/white | Alternating |

### Cell Alignment

| Content Type | Alignment |
|--------------|-----------|
| Text | Left |
| Numbers | Right |
| Status/Badge | Center |
| Actions | Right |

### Spacing

| Element | Value |
|---------|-------|
| cell padding | 12px 16px |
| header padding | 12px 16px |
| row height (compact) | 40px |
| row height (default) | 48px |
| row height (comfortable) | 56px |

---

## 📄 `references/tailwind-integration.md`

# Tailwind Integration

Map design system tokens to Tailwind CSS configuration.

## CSS Variables Setup

### Base Layer

```css
/* globals.css */
@tailwind base;
@tailwind components;
@tailwind utilities;

@layer base {
  :root {
    /* Primitives */
    --color-blue-600: 37 99 235;  /* HSL: 217 91% 60% */

    /* Semantic */
    --background: 0 0% 100%;
    --foreground: 222 47% 11%;
    --primary: 217 91% 60%;
    --primary-foreground: 0 0% 100%;
    --secondary: 220 14% 96%;
    --secondary-foreground: 222 47% 11%;
    --muted: 220 14% 96%;
    --muted-foreground: 220 9% 46%;
    --accent: 220 14% 96%;
    --accent-foreground: 222 47% 11%;
    --destructive: 0 84% 60%;
    --destructive-foreground: 0 0% 100%;
    --border: 220 13% 91%;
    --input: 220 13% 91%;
    --ring: 217 91% 60%;
    --radius: 0.5rem;
  }

  .dark {
    --background: 222 47% 4%;
    --foreground: 210 40% 98%;
    --primary: 217 91% 60%;
    --primary-foreground: 0 0% 100%;
    --secondary: 217 33% 17%;
    --secondary-foreground: 210 40% 98%;
    --muted: 217 33% 17%;
    --muted-foreground: 215 20% 65%;
    --accent: 217 33% 17%;
    --accent-foreground: 210 40% 98%;
    --destructive: 0 62% 30%;
    --destructive-foreground: 0 0% 100%;
    --border: 217 33% 17%;
    --input: 217 33% 17%;
    --ring: 217 91% 60%;
  }
}
```

## Tailwind Config

### tailwind.config.ts

```typescript
import type { Config } from 'tailwindcss'

const config: Config = {
  darkMode: ['class'],
  content: ['./src/**/*.{ts,tsx}'],
  theme: {
    extend: {
      colors: {
        background: 'hsl(var(--background))',
        foreground: 'hsl(var(--foreground))',
        primary: {
          DEFAULT: 'hsl(var(--primary))',
          foreground: 'hsl(var(--primary-foreground))',
        },
        secondary: {
          DEFAULT: 'hsl(var(--secondary))',
          foreground: 'hsl(var(--secondary-foreground))',
        },
        muted: {
          DEFAULT: 'hsl(var(--muted))',
          foreground: 'hsl(var(--muted-foreground))',
        },
        accent: {
          DEFAULT: 'hsl(var(--accent))',
          foreground: 'hsl(var(--accent-foreground))',
        },
        destructive: {
          DEFAULT: 'hsl(var(--destructive))',
          foreground: 'hsl(var(--destructive-foreground))',
        },
        border: 'hsl(var(--border))',
        input: 'hsl(var(--input))',
        ring: 'hsl(var(--ring))',
        card: {
          DEFAULT: 'hsl(var(--card))',
          foreground: 'hsl(var(--card-foreground))',
        },
      },
      borderRadius: {
        lg: 'var(--radius)',
        md: 'calc(var(--radius) - 2px)',
        sm: 'calc(var(--radius) - 4px)',
      },
    },
  },
  plugins: [],
}

export default config
```

## HSL Format Benefits

Using HSL without function allows opacity modifiers:

```tsx
// With HSL format (space-separated)
<div className="bg-primary/50">   // 50% opacity
<div className="text-primary/80"> // 80% opacity

// CSS output
background-color: hsl(217 91% 60% / 0.5);
```

## Component Classes

### Button Example

```css
@layer components {
  .btn {
    @apply inline-flex items-center justify-center
           rounded-md font-medium
           transition-colors
           focus-visible:outline-none focus-visible:ring-2
           focus-visible:ring-ring focus-visible:ring-offset-2
           disabled:pointer-events-none disabled:opacity-50;
  }

  .btn-default {
    @apply bg-primary text-primary-foreground
           hover:bg-primary/90;
  }

  .btn-secondary {
    @apply bg-secondary text-secondary-foreground
           hover:bg-secondary/80;
  }

  .btn-outline {
    @apply border border-input bg-background
           hover:bg-accent hover:text-accent-foreground;
  }

  .btn-ghost {
    @apply hover:bg-accent hover:text-accent-foreground;
  }

  .btn-destructive {
    @apply bg-destructive text-destructive-foreground
           hover:bg-destructive/90;
  }

  /* Sizes */
  .btn-sm { @apply h-8 px-3 text-xs; }
  .btn-md { @apply h-10 px-4 text-sm; }
  .btn-lg { @apply h-12 px-6 text-base; }
}
```

## Spacing Integration

```typescript
// tailwind.config.ts
theme: {
  extend: {
    spacing: {
      // Map to CSS variables if needed
      'section': 'var(--spacing-section)',
      'component': 'var(--spacing-component)',
    }
  }
}
```

## Animation Tokens

```typescript
// tailwind.config.ts
theme: {
  extend: {
    transitionDuration: {
      fast: '150ms',
      normal: '200ms',
      slow: '300ms',
    },
    keyframes: {
      'accordion-down': {
        from: { height: '0' },
        to: { height: 'var(--radix-accordion-content-height)' },
      },
      'accordion-up': {
        from: { height: 'var(--radix-accordion-content-height)' },
        to: { height: '0' },
      },
    },
    animation: {
      'accordion-down': 'accordion-down 0.2s ease-out',
      'accordion-up': 'accordion-up 0.2s ease-out',
    },
  }
}
```

## Dark Mode Toggle

```typescript
// Toggle dark mode
function toggleDarkMode() {
  document.documentElement.classList.toggle('dark')
}

// System preference
if (window.matchMedia('(prefers-color-scheme: dark)').matches) {
  document.documentElement.classList.add('dark')
}
```

## shadcn/ui Alignment

This configuration aligns with shadcn/ui conventions:

- Same CSS variable naming
- Same HSL format
- Same color scale structure
- Compatible with `npx shadcn@latest add` commands

### Using with shadcn/ui

```bash
# Initialize (uses same token structure)
npx shadcn@latest init

# Add components (styled with these tokens)
npx shadcn@latest add button card input
```

Components will automatically use your design system tokens.

---

## 📄 `references/token-architecture.md`

# Token Architecture

Three-layer token system for scalable, themeable design systems.

## Layer Overview

```
┌─────────────────────────────────────────┐
│  Component Tokens                       │  Per-component overrides
│  --button-bg, --card-padding            │
├─────────────────────────────────────────┤
│  Semantic Tokens                        │  Purpose-based aliases
│  --color-primary, --spacing-section     │
├─────────────────────────────────────────┤
│  Primitive Tokens                       │  Raw design values
│  --color-blue-600, --space-4            │
└─────────────────────────────────────────┘
```

## Why Three Layers?

| Layer | Purpose | When to Change |
|-------|---------|----------------|
| Primitive | Base values (colors, sizes) | Rarely - foundational |
| Semantic | Meaning assignment | Theme switching |
| Component | Component customization | Per-component needs |

## Layer 1: Primitive Tokens

Raw design values without semantic meaning.

```css
:root {
  /* Colors */
  --color-gray-50: #F9FAFB;
  --color-gray-900: #111827;
  --color-blue-500: #3B82F6;
  --color-blue-600: #2563EB;

  /* Spacing (4px base) */
  --space-1: 0.25rem;  /* 4px */
  --space-2: 0.5rem;   /* 8px */
  --space-4: 1rem;     /* 16px */
  --space-6: 1.5rem;   /* 24px */

  /* Typography */
  --font-size-sm: 0.875rem;
  --font-size-base: 1rem;
  --font-size-lg: 1.125rem;

  /* Radius */
  --radius-sm: 0.25rem;
  --radius-default: 0.5rem;
  --radius-lg: 0.75rem;

  /* Shadows */
  --shadow-sm: 0 1px 2px rgb(0 0 0 / 0.05);
  --shadow-default: 0 1px 3px rgb(0 0 0 / 0.1);
}
```

## Layer 2: Semantic Tokens

Purpose-based aliases that reference primitives.

```css
:root {
  /* Background */
  --color-background: var(--color-gray-50);
  --color-foreground: var(--color-gray-900);

  /* Primary */
  --color-primary: var(--color-blue-600);
  --color-primary-hover: var(--color-blue-700);

  /* Secondary */
  --color-secondary: var(--color-gray-100);
  --color-secondary-foreground: var(--color-gray-900);

  /* Muted */
  --color-muted: var(--color-gray-100);
  --color-muted-foreground: var(--color-gray-500);

  /* Destructive */
  --color-destructive: var(--color-red-600);
  --color-destructive-foreground: white;

  /* Spacing */
  --spacing-component: var(--space-4);
  --spacing-section: var(--space-6);
}
```

## Layer 3: Component Tokens

Component-specific tokens referencing semantic layer.

```css
:root {
  /* Button */
  --button-bg: var(--color-primary);
  --button-fg: white;
  --button-hover-bg: var(--color-primary-hover);
  --button-padding-x: var(--space-4);
  --button-padding-y: var(--space-2);
  --button-radius: var(--radius-default);

  /* Input */
  --input-bg: var(--color-background);
  --input-border: var(--color-gray-300);
  --input-focus-ring: var(--color-primary);
  --input-padding: var(--space-2) var(--space-3);

  /* Card */
  --card-bg: var(--color-background);
  --card-border: var(--color-gray-200);
  --card-padding: var(--space-4);
  --card-radius: var(--radius-lg);
  --card-shadow: var(--shadow-default);
}
```

## Dark Mode

Override semantic tokens for dark theme:

```css
.dark {
  --color-background: var(--color-gray-900);
  --color-foreground: var(--color-gray-50);
  --color-muted: var(--color-gray-800);
  --color-muted-foreground: var(--color-gray-400);
  --color-secondary: var(--color-gray-800);
}
```

## Naming Convention

```
--{category}-{item}-{variant}-{state}

Examples:
--color-primary           # category-item
--color-primary-hover     # category-item-state
--button-bg-hover         # component-property-state
--space-section-sm        # category-semantic-variant
```

## Categories

| Category | Examples |
|----------|----------|
| color | primary, secondary, muted, destructive |
| space | 1, 2, 4, 8, section, component |
| font-size | xs, sm, base, lg, xl |
| radius | sm, default, lg, full |
| shadow | sm, default, lg |
| duration | fast, normal, slow |

## File Organization

```
tokens/
├── primitives.css     # Raw values
├── semantic.css       # Purpose aliases
├── components.css     # Component tokens
└── index.css          # Imports all
```

Or single file with layer comments:

```css
/* === PRIMITIVES === */
:root { ... }

/* === SEMANTIC === */
:root { ... }

/* === COMPONENTS === */
:root { ... }

/* === DARK MODE === */
.dark { ... }
```

## Migration from Flat Tokens

Before (flat):
```css
--button-primary-bg: #2563EB;
--button-secondary-bg: #F3F4F6;
```

After (three-layer):
```css
/* Primitive */
--color-blue-600: #2563EB;
--color-gray-100: #F3F4F6;

/* Semantic */
--color-primary: var(--color-blue-600);
--color-secondary: var(--color-gray-100);

/* Component */
--button-bg: var(--color-primary);
--button-secondary-bg: var(--color-secondary);
```

## W3C DTCG Alignment

Token JSON format (W3C Design Tokens Community Group):

```json
{
  "color": {
    "blue": {
      "600": {
        "$value": "#2563EB",
        "$type": "color"
      }
    }
  }
}
```
