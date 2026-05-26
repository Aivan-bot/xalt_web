# XALT Website Redesign — 11ty → GitHub Pages

## Kontext
- Alte Seite: xalt.de (WordPress) → unnötiger Wartungsaufwand
- Neue Seite: 11ty (statisch, schnell, sicher, null Dependencies)
- Hosting: GitHub Pages (GH Actions CI/CD)
- Design: Übernomme vom Stil von xalt.de/ai (Dark Mode UI)

## Design-Spezifikation (von xalt.de/ai übernommen)

### Farben
- Background: `#0B0F1A` (Deep Dark Blue, fast Schwarz)
- Card Background: `#111827`
- Primary Accent: `#00E5FF` (Cyan/Turquoise)
- Secondary Accent: `#00B4D8`
- Headlines: `#FFFFFF`
- Body Text: `#E5E7EB`
- Meta/Tags: `#6B7280`
- Border: `#1E293B`
- Hover Card: `#1E293B`

### Typography
- Font: Inter (Google Fonts)
- H1: 48px/58px Bold
- H2: 32px/40px Bold
- H3: 24px/32px Medium
- Body: 16px/26px Regular
- Small: 14px/20px Regular
- Navigation: 15px/24px Medium

### Layout-Prinzipien
- Card-based Design mit 8-12px Border-Radius
- 3-spaltiges Grid auf Desktop, 1-column mobil
- Sticky Header mit Logo + Navigation
- Smooth Scroll
- Responsive First

## Seite-Struktur

```
xalt_web/
├── package.json          # 11ty + Dependencies
├── .eleventy.js          # 11ty Konfiguration
├── plan.md               # Dieser Plan
├── .github/
│   └── workflows/
│       └── deploy.yml    # GH Pages CI/CD
├── _data/
│   └── site.json         # Globale Site-Config
├── _includes/
│   ├── layouts/
│   │   └── base.njk      # Base Layout (Header/Footer/Footer)
│   ├── components/
│   │   ├── header.njk    # Sticky Header
│   │   ├── footer.njk    # Footer
│   │   ├── hero.njk      # Hero Section
│   │   ├── card-grid.njk # Karten-Grid Component
│   │   └── section.njk   # Reusable Section
├── css/
│   └── main.css          # Globales Stylesheet
├── js/
│   └── main.js           # Mobile Menu + Smooth Scroll
├── src/
│   ├── index.md          # Startseite (via Template)
│   └── pages/
│       ├── index.md
│       ├── leistungen.md
│       ├── loesungen.md
│       ├── blog.md
│       ├── ressourcen.md
│       ├── unternehmen.md
│       └── apps.md
└── README.md
```

## MVP Scope (Phase 1)
- [x] Repository xalt_web erstellt auf GitHub
- [x] Plan erstellt
- [ ] 11ty Projektstruktur
- [ ] Startseite mit AI-Design
- [ ] GH Actions Workflow
- [ ] Erster Commit & Push
- [ ] GH Pages deployed

## Phase 2 (nacho MVP)
- [ ] Vollständige Seite mit allen Sektionen von xalt.de
- [ ] Animations (Scroll-Reveal, Hover-Effekte)
- [ ] Case Studies
- [ ] Partner-Logos
- [ ] Blog
- [ ] Kontaktformular
- [ ] Impressum & Datenschutz

## Phase 3 (spötere)
- [ ] SEO-Optimierung
- [ ] Analytics
- [ ] Performance-Monitoring
- [ ] A/B Testing
- [ ] CMS-Integration (optional, mit StaticCMS)

## Deployment
- Branch `main` → GH Pages → https://<username>.github.io/xalt_web

## Technologien
- 11ty v3 (eleventy)
- Vanilla CSS (keine Frameworks)
- Vanilla JS (minimales)
- GitHub Pages
- GitHub Actions (CI/CD)
