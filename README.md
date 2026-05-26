# XALT Website v2

> xalt.de — Modern, statisch & wartungsarm

## Über dieses Projekt

Die xalt.de Website wurde von WordPress migriert und mit **11ty** (Eleventy) neu aufgebaut. Das Ergebnis:

- ⚡ **Blitzschnell** — Statisch generiert, CDN-fähig
- 🔒 **Sicher** — Keine Datenbank, kein PHP, keine Plugins
- 🎨 **Modern** — Dark Mode Design (inspiriert von xalt.de/ai)
- 📱 **Responsive** — Mobile-first, alle Geräte
- 🔄 **CI/CD** — Automatisch deployed via GitHub Pages

## Technologien

- **11ty (Eleventy)** — Statische Website-Engine
- **Vanilla CSS** — Kein Framework, komplett maßgeschneidert
- **Vanilla JS** — Minimal, nur für mobile Menu & Animationen
- **GitHub Actions** —全自动 CI/CD Pipeline
- **GitHub Pages** — Hosting

## Entwicklung

### Voraussetzungen

- Node.js ≥ 18
- npm

### Lokal starten

```bash
# Dependencies installieren
npm install

# Development Server starten (Live Reload)
npm run dev

# ODER
npx eleventy --serve --incremental
```

Öffne dann http://localhost:8080 in deinem Browser.

### Build für Produktion

```bash
npm run build
# Ausgabe: dist/
```

## Struktur

```
xalt_web/
├── .eleventy.js          # 11ty Konfiguration
├── package.json          # Dependencies & Scripts
├── plan.md               # Projektplan
├── .github/
│   └── workflows/
│       └── deploy.yml    # GH Actions CI/CD
├── _data/
│   └── site.json         # Globale Site-Config
├── _includes/
│   ├── layouts/
│   │   └── base.njk      # Base Layout
│   └── components/
│       ├── header.njk    # Sticky Header
│       └── footer.njk    # Footer
├── css/
│   └── main.css          # Globales CSS
├── js/
│   └── main.js           # Mobile Menu + Animationen
├── src/
│   └── pages/
│       ├── index.md      # Startseite
│       │
│       └── ...           # Weitere Seiten
└── dist/                 # Build-Ausgabe (wird ignoriert)
```

## Deployment

Das Projekt wird automatisch bei jedem Push auf `main` deployed:

1. Push auf `main` triggerd GitHub Actions
2. 11ty baut die statischen Dateien
3. GitHub Pages stellt die Seite live

Manuelles Deployment möglich:
```bash
git push origin main
# oder
gh workflow run "Deploy to GitHub Pages"
```

## Design

### Farben

| Farbe | Hex | Verwendung |
|---|---|---|
| Background | `#0B0F1A` | Main Background |
| Card | `#111827` | Cards, Panels |
| Accent | `#00E5FF` | CTA, Links, Highlights |
| Text | `#E5E7EB` | Body Text |
| Headlines | `#FFFFFF` | Überschriften |
| Meta | `#6B7280` | Untertitel, Labels |

### Schriftarten

- **Inter** (Google Fonts) — Hauptfont
- Weights: 300, 400, 500, 600, 700, 800

### Design-Prinzipien

- Card-based Layout mit hover Effects
- Sticky Header mit Blur-Effekt
- Responsive Grid (3 → 2 → 1 Spalten)
- Subtile Animationen (fade-in, hover transforms)
- Clean, professionell, tech-lastig

## Zukunft (Roadmap)

### Phase 2
- [ ] Vollständige Seite mit allen Sektionen
- [ ] Case Studies
- [ ] Partner-Logos (SVG)
- [ ] Animationen (Scroll-Reveal)
- [ ] Kontaktformular
- [ ] Impressum & Datenschutz

### Phase 3
- [ ] SEO-Optimierung (Meta, Schema, Open Graph)
- [ ] Analytics Integration
- [ ] Performance-Monitoring
- [ ] A/B Testing
- [ ] StaticCMS (optional für Content-Updates)

## License

© 2026 XALT. Alle Rechte vorbehalten.
