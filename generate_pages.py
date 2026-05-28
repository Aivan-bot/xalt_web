#!/usr/bin/env python3
"""Generate all xalt.de 11ty page files."""
import os

BASE = "/home/aivan/.hermes/workspace/xalt_web/src/pages"
U = "{{ site.url }}"  # template variable for site.url

def make_layout(title, description, content_md):
    return f"---\nlayout: base\ntitle: \"{title}\"\ndescription: \"{description}\"\n---\n\n{content_md}\n"

def card_link(url, title, desc, icon):
    return f"""    <div class="card-link">
      <div class="card-icon" aria-hidden="true">{icon}</div>
      <h3><a href="{{{{ site.url }}}}{url}/">{title}</a></h3>
      <p>{desc}</p>
    </div>
"""

def create(path, title, description, content):
    full = os.path.join(BASE, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    fm = make_layout(title, description, content)
    with open(full, "w", encoding="utf-8") as f:
        f.write(fm)
    print(f"  Created {path}")

# ===========================
# LEISTUNGEN
# ===========================
print("=== Leistungen ===")

create("leistungen/index.md",
    "Leistungen - Atlassian Beratung",
    "XALT bietet umfassende Atlassian-Beratung für digitale Transformation, Agile Coaching und Platform Engineering.",
    f"""<!-- ===== HERO ===== -->
<section class="hero" aria-label="Leistungen">
  <div class="si">
    <div class="hc">
      <div class="ht">
        <span class="htag">LEISTUNGEN</span>
        <h1>Unsere Leistungen</h1>
        <p class="hdesc">XALT bietet umfassende Beratung und Lösungsarchitektur für Unternehmen, die ihre Arbeitsprozesse mit Atlassian-Tools optimieren möchten – von der Strategie bis zur Umsetzung.</p>
        <a href="{U}/kontakt/" class="hcta"><span>Kontakt aufnehmen</span><span class="arr" aria-hidden="true">→</span></a>
      </div>
      <div class="hg" aria-hidden="true">
        <div class="chart-ph">🏗️</div>
      </div>
    </div>
  </div>
</section>

<!-- ===== CARD GRID ===== -->
<section class="section" aria-label="Unsere Leistungen">
  <div class="si">
    <div class="bgrid">
{card_link(f"{U}/leistungen/atlassian-beratung/", "Atlassian Beratung", "Experten für zentrale Plattform statt Insellösungen.", "🔧")}
{card_link(f"{U}/loesungen/digital-workplace/", "Digital Workplace", "Moderne digitale Workplace-Lösungen mit Confluence und Jira.", "📚")}
{card_link(f"{U}/loesungen/prozess-digitalisierung/", "Prozess Digitalisierung", "Automatisierung und Digitalisierung mit Jira und der Atlassian Suite.", "⚡")}
{card_link(f"{U}/loesungen/cloud-infrastruktur/", "Cloud Infrastruktur", "Native Cloud Services und Migration auf Atlassian Cloud.", "☁️")}
{card_link(f"{U}/ressourcen/success-stories/", "Success Stories", "Erfolgsberichte unserer Kundenprojekte.", "📈")}
{card_link(f"{U}/ kontakt/", "Projekt starten", "Beratungstermin vereinbaren.", "🚀")}
    </div>
  </div>
</section>
""")

create("leistungen/atlassian-beratung.md",
    "Atlassian Beratung - XALT",
    "Experten für zentrale Plattform statt Insellösungen. XALT optimiert Ihre Jira, Confluence und die gesamte Atlassian-Toolchain.",
    f"""<!-- ===== HERO ===== -->
<section class="hero" aria-label="Atlassian Beratung">
  <div class="si">
    <div class="hc">
      <div class="ht">
        <span class="htag">BERATUNG</span>
        <h1>Atlassian Beratung</h1>
        <p class="hdesc">Experten für zentrale Plattform statt Insellösungen. Wir helfen Unternehmen, die volle Leistungsfähigkeit ihrer Atlassian-Toolchains zu entfalten – von der Analyse bis zur Implementierung.</p>
        <a href="{U}/kontakt/" class="hcta"><span>Beratungstermin buchen</span><span class="arr" aria-hidden="true">→</span></a>
      </div>
      <div class="hg" aria-hidden="true">
        <div class="chart-ph">🔧</div>
      </div>
    </div>
  </div>
</section>

<!-- ===== CONTENT ===== -->
<section class="section" aria-label="Über unsere Atlassian-Beratung">
  <div class="si">
    <div class="sh">
      <span class="st">Unsere Expertise</span>
      <h2>Warum Atlassian-Beratung?</h2>
    </div>
    <div class="bgrid">
      <article class="bcard">
        <div class="bi" aria-hidden="true">🎯</div>
        <div class="bco">
          <div class="bmeta"><span>Strategie</span></div>
          <h3>Atlassian-Strategie-Review</h3>
          <p>Wir analysieren Ihre bestehende Tool-Infrastruktur und entwickeln eine maßgeschneiderte Strategie für den optimalen Einsatz von Jira, Confluence, Bitbucket und der gesamten Atlassian-Suite.</p>
          <a href="{U}/loesungen/cloud-strategie-roadmap/" class="blink">Weiter lesen <span class="arr" aria-hidden="true">→</span></a>
        </div>
      </article>
      <article class="bcard">
        <div class="bi" aria-hidden="true">🔄</div>
        <div class="bco">
          <div class="bmeta"><span>Migration</span></div>
          <h3>Cloud Migration</h3>
          <p>Professionelle Migration Ihrer Server- und Data-Center-Instanzen in die Atlassian Cloud. Sicher, schnell und mit minimalem Risiko.</p>
          <a href="{U}/loesungen/cloud-migration/" class="blink">Weiter lesen <span class="arr" aria-hidden="true">→</span></a>
        </div>
      </article>
      <article class="bcard">
        <div class="bi" aria-hidden="true">🏗️</div>
        <div class="bco">
          <div class="bmeta"><span>Architecture</span></div>
          <h3>Platform Engineering</h3>
          <p>Enterprise-Platform-Architecture und Toolchain-Design. Wir bauen Ihre DevOps-Plattform mit Jira, Bitbucket und GitHub.</p>
          <a href="{U}/loesungen/cloud-service/" class="blink">Weiter lesen <span class="arr" aria-hidden="true">→</span></a>
        </div>
      </article>
    </div>
  </div>
</section>

<!-- ===== BENEFITS ===== -->
<section class="section" aria-label="Nutzen">
  <div class="si" style="text-align:center">
    <span class="st">Nutzen</span>
    <h2>Was Sie von unserer Beratung profitieren</h2>
    <div class="bgrid" style="margin-top:48px">
      <div class="bcard"><div class="bco"><div class="bmeta"><span>Effizienz</span></div><h3>30-50% schnellere Workflows</h3></div></div>
      <div class="bcard"><div class="bco"><div class="bmeta"><span>Kosten</span></div><h3>Bis zu 40% Einsparung bei Lizenzkosten</h3></div></div>
      <div class="bcard"><div class="bco"><div class="bmeta"><span>Transparenz</span></div><h3>Durchgängige Nachverfolgung aller Prozesse</h3></div></div>
    </div>
  </div>
</section>

<!-- ===== RELATED ===== -->
<section class="section"><div class="si">
  <div class="sh"><span class="st">Weiterführende Themen</span></div>
  <div class="bgrid">
    {card_link(f"{U}/loesungen/cloud-adoption-assessment/", "Cloud Adoption Assessment", "Bewertung Ihrer Cloud-Bereitschaft.", "📋")}
    {card_link(f"{U}/loesungen/it-service-management/", "IT Service Management", "ITSM mit Jira Service Management.", "🛡️")}
    {card_link(f"{U}/ressourcen/whitepaper-service/", "Whitepaper: Service & Development Teams", "Abstimmung zwischen Teams optimieren.", "📄")}
  </div>
</div></section>
""")

# ===========================
# LOESUNGEN
# ===========================
print("=== Lösungen ===")

solutions = [
    ("loesungen/index.md",
     "Lösungen - XALT",
     "Umfassende Lösungen für digitale Transformation, Cloud-Migration und digitale Workplace.",
     f"""<!-- ===== HERO ===== -->
<section class="hero" aria-label="Lösungen">
  <div class="si">
    <div class="hc">
      <div class="ht">
        <span class="htag">LÖSUNGEN</span>
        <h1>Unsere Lösungen</h1>
        <p class="hdesc">Maßgeschneiderte Atlassian-Lösungen für mittelständische Unternehmen und Konzerne. Von Digital Workplace über Cloud Migration bis hin zu automatisierten Workflows.</p>
        <a href="{U}/kontakt/" class="hcta"><span>Lösung anfragen</span><span class="arr" aria-hidden="true">→</span></a>
      </div>
      <div class="hg" aria-hidden="true"><div class="chart-ph">💡</div></div>
    </div>
  </div>
</section>
<!-- ===== CARD GRID ===== -->
<section class="section" aria-label="Lösungen">
  <div class="si">
    <div class="sh"><span class="st">Unsere Lösungen</span><h2>Lösungen nach Kategorie</h2></div>
    <div class="bgrid">
{card_link(f"{U}/loesungen/digital-workplace/", "Digital Workplace", "Moderne digitale Workplace-Lösungen mit Confluence und Jira.", "📚")}
{card_link(f"{U}/loesungen/prozess-digitalisierung/", "Prozess Digitalisierung", "Automatisierung und Digitalisierung mit Jira und Atlassian Suite.", "⚡")}
{card_link(f"{U}/loesungen/cloud-infrastruktur/", "Cloud Infrastruktur", "Native Cloud Services und Migration auf Atlassian Cloud.", "☁️")}
{card_link(f"{U}/loesungen/it-service-management/", "IT Service Management", "ITSM-Lösungen mit Jira Service Management.", "🛡️")}
{card_link(f"{U}/loesungen/projektportfoliomanagement/", "Projekt & Portfolio Management", "Projekte und Portfolios mit Jira effizient steuern.", "📊")}
{card_link(f"{U}/loesungen/changemanagement/", "Change Management", "Unternehmen sicher durch digitale Transformation begleiten.", "🔄")}
{card_link(f"{U}/loesungen/digitalisierung/", "Digitalisierung", "Geschäftsprozesse digital und automatisiert gestalten.", "🔍")}
{card_link(f"{U}/loesungen/continuous-integration/", "Continuous Integration & Delivery", "CI/CD mit Atlassian-Bitbucket-Gateway.", "🔄")}
{card_link(f"{U}/loesungen/automated-testing/", "Automated Testing", "Automatisierte Tests für Atlassian-Applikationen.", "🧪")}
{card_link(f"{U}/loesungen/hosting/", "Managed Hosting", "Professionelles Hosting und Betrieb von Atlassian Applikationen.", "🖥️")}
{card_link(f"{U}/loesungen/schulungen/", "Schulungen", "Atlassian-Schulungen für Administratoren und Endanwender.", "🎓")}
{card_link(f"{U}/apps/", "App Marketplace", "Erweiterte Apps und Plugins für Atlassian-Produkte.", "🧩")}
    </div>
  </div>
</section>
"""),

    ("loesungen/digital-workplace.md",
     "Digital Workplace - Confluence & Jira",
     "Ihr moderner Digital Workplace mit Confluence und Jira.",
     f"""<!-- ===== HERO ===== -->
<section class="hero" aria-label="Digital Workplace">
  <div class="si">
    <div class="hc">
      <div class="ht">
        <span class="htag">DIGITAL WORKPLACE</span>
        <h1>Digital Workplace mit Confluence</h1>
        <p class="hdesc">Unsere digitalen Workplace-Lösungen bringen Sie, Ihre Mitarbeiter und Ihre externen Partner zusammen. Egal ob Cloud oder On-Premise, lokal oder im Rechenzentrum.</p>
        <a href="{U}/kontakt/" class="hcta"><span>Kontakt aufnehmen</span><span class="arr" aria-hidden="true">→</span></a>
      </div>
      <div class="hg" aria-hidden="true"><div class="chart-ph">📚</div></div>
    </div>
  </div>
</section>
<section class="section"><div class="si"><div class="sh"><span class="st">Lösung</span><h2>Konfluence-Intranet-Lösungen</h2></div>
    <div class="bgrid">
{card_link(f"{U}/loesungen/confluence-intranet-mit-linchpin/", "Confluence Intranet mit Linchpin", "Modernes Intranet mit dem Linchpin-Theme.", "🎨")}
{card_link(f"loesungen/confluence-intranet-mit-refined/", "Confluence Intranet mit Refined", "Intranet mit Refined Theme.", "🎨")}
{card_link(f"loesungen/jira-bewerber-tool/", "Jira Bewerber-Tool", "Bewerbungsprozesse mit Jira beschleunigen.", "📋")}
    </div></div></section>
"""),

    ("loesungen/prozess-digitalisierung.md",
     "Prozess Digitalisierung",
     "Automatisierung und Digitalisierung mit Jira und der Atlassian Suite.",
     f"""<!-- ===== HERO ===== -->
<section class="hero" aria-label="Prozess Digitalisierung">
  <div class="si">
    <div class="hc">
      <div class="ht">
        <span class="htag">DIGITALISIERUNG</span>
        <h1>Prozess Digitalisierung mit Jira</h1>
        <p class="hdesc">Bringen Sie Ihre Workflows auf das nächste Level. Von der Anforderung bis zur Ausführung – wir digitalisieren Ihre Geschäftsprozesse mit Jira und der gesamten Atlassian Suite.</p>
        <a href="{U}/kontakt/" class="hcta"><span>Beratung starten</span><span class="arr" aria-hidden="true">→</span></a>
      </div>
      <div class="hg" aria-hidden="true"><div class="chart-ph">⚡</div></div>
    </div>
  </div>
</section>
<section class="section"><div class="si"><div class="bgrid">
{card_link(f"{U}/loesungen/it-service-management/", "IT Service Management", "ITSM mit Jira Service Management.", "🛡️")}
{card_link(f"{U}/case-studies/prozessdigitalisierung/", "Case Study: Prozessdigitalisierung", "Erfolgsbericht aus der Prozessdigitalisierung.", "📈")}
{card_link(f"{U}/apps/self-service/", "Self-Service Portal", "Self-Service für Business Teams mit Jira.", "🖥️")}
</div></div></section>
"""),

    ("loesungen/cloud-infrastruktur.md",
     "Cloud Infrastruktur",
     "Cloud Services: Native und Migration auf Atlassian Cloud.",
     f"""<!-- ===== HERO ===== -->
<section class="hero" aria-label="Cloud Infrastruktur">
  <div class="si">
    <div class="hc">
      <div class="ht">
        <span class="htag">CLOUD</span>
        <h1>Cloud Infrastruktur & Services</h1>
        <p class="hdesc">Cloud Services: Native und Migration für maximale Cloud-Reife. Wir begleiten Sie auf dem Weg zur Cloud.</p>
        <a href="{U}/loesungen/cloud-migration/" class="hcta"><span>Cloud Migration</span><span class="arr" aria-hidden="true">→</span></a>
      </div>
      <div class="hg" aria-hidden="true"><div class="chart-ph">☁️</div></div>
    </div>
  </div>
</section>
<section class="section"><div class="si"><div class="sh"><span class="st">Cloud Services</span><h2>Unsere Cloud-Lösungen</h2></div>
    <div class="bgrid">
{card_link(f"{U}/loesungen/cloud-migration/", "Cloud Migration", "Von Server und Data Center in die Cloud.", "🔄")}
{card_link(f"{U}/loesungen/cloud-adoption-assessment/", "Cloud Adoption Assessment", "Bewertung Ihrer Cloud-Bereitschaft.", "📋")}
{card_link(f"{U}/ressourcen/whitepaper-cloud/", "Whitepaper: Cloud Security", "Cloud-Sicherheit mit Zero Trust.", "📄")}
</div></div></section>
"""),

    ("loesungen/cloud-migration.md",
     "Cloud Migration",
     "Atlassian Cloud Migration: Von Server und Data Center in die Cloud.",
     f"""<!-- ===== HERO ===== -->
<section class="hero" aria-label="Cloud Migration">
  <div class="si">
    <div class="hc">
      <div class="ht">
        <span class="htag">CLOUD MIGRATION</span>
        <h1>Cloud Migration von Server & Data Center</h1>
        <p class="hdesc">Professionelle Migration Ihrer Atlassian-Instance in die Cloud. Sicher, schnell und ohne Datenverlust.</p>
        <a href="{U}/kontakt/" class="hcta"><span>Migrationsberatung</span><span class="arr" aria-hidden="true">→</span></a>
      </div>
      <div class="hg" aria-hidden="true"><div class="chart-ph">🔄</div></div>
    </div>
  </div>
</section>
<section class="section"><div class="si"><div class="sh"><span class="st">Migration</span><h2>Migrationsschritte</h2></div>
    <div class="bgrid">
      <div class="bcard"><div class="bco"><div class="bmeta"><span>Schritt 1</span></div><h3>Analyse & Assessment</h3><p>Bewertung der bestehenden Instanz und Planung der Migration.</p></div></div>
      <div class="bcard"><div class="bco"><div class="bmeta"><span>Schritt 2</span></div><h3>Vorbereitung</h3><p>Konfiguration der Cloud-Umgebung und Datenbereinigung.</p></div></div>
      <div class="bcard"><div class="bco"><div class="bmeta"><span>Schritt 3</span></div><h3>Durchführung</h3><p>Durchführung der Migration mit minimalem Downtime.</p></div></div>
    </div></div></section>
<section class="section"><div class="si">
  <div class="sh"><span class="st">Erfolgsgeschichten</span></div>
  <div class="bgrid">
    {card_link(f"{U}/case-studies/cloud-migration/", "Success Story: Weltbild Cloud Migration", "Weltbild migriert zu Atlassian Cloud.", "📈")}
    {card_link(f"{U}/case-studies/atlassian-cloud-migration/", "Success Story: Atlassian Cloud Migration", "Migration von Jira und Confluence.", "📈")}
    {card_link(f"{U}/loesungen/cloud-adoption/", "Cloud Adoption Assessment", "Bewertung Ihrer Cloud-Bereitschaft.", "📋")}
  </div>
</div></section>
"""),

    ("loesungen/cloud-adoption.md",
     "Cloud Adoption Assessment",
     "Atlassian Cloud Adoption Assessment - Bewertung Ihrer Cloud-Bereitschaft.",
     f"""<!-- ===== HERO ===== -->
<section class="hero" aria-label="Cloud Adoption Assessment">
  <div class="si">
    <div class="hc">
      <div class="ht">
        <span class="htag">ASSESSMENT</span>
        <h1>Cloud Adoption Assessment</h1>
        <p class="hdesc">Bewertung Ihrer Cloud-Bereitschaft und Entwicklung einer Roadmap für Ihre Atlassian-Cloud-Migration.</p>
        <a href="{U}/kontakt/" class="hcta"><span>Assessment anfordern</span><span class="arr" aria-hidden="true">→</span></a>
      </div>
      <div class="hg" aria-hidden="true"><div class="chart-ph">📋</div></div>
    </div>
  </div>
</section>
<section class="section"><div class="si"><div class="sh"><span class="st">Assessment</span><h2>Cloud Adoption Framework</h2></div>
    <p style="color:var(--mute);max-width:800px;margin:0 auto 48px;text-align:center;font-size:18px;line-height:1.8">Unser Cloud Adoption Framework bewertet Ihre aktuelle Infrastruktur, identifiziert Risiken und erstellt einen klaren Migrationspfad für Ihre Atlassian-Tools.</p>
    <div class="bgrid">
      <div class="bcard"><div class="bco"><div class="bmeta"><span>Plan</span></div><h3>Planungsphase</h3><p>Definieren Sie Ihr Cloud-Ziel und Ihre Erfolgsmaßstäbe.</p></div></div>
      <div class="bcard"><div class="bco"><div class="bmeta"><span>Assess</span></div><h3>Bewertung</h3><p>Analyse Ihrer bestehenden Infrastruktur und Abhängigkeiten.</p></div></div>
      <div class="bcard"><div class="bco"><div class="bmeta"><span>Migrate</span></div><h3>Migrationspfad</h3><p>Entwicklung einer schrittweisen Migrationsstrategie.</p></div></div>
    </div></div></section>
"""),

    ("loesungen/cloud-strategie.md",
     "Cloud Strategie Roadmap",
     "Atlassian Cloud Strategie und Roadmap Beratung.",
     f"""<!-- ===== HERO ===== -->
<section class="hero" aria-label="Cloud Strategie Roadmap">
  <div class="si">
    <div class="hc">
      <div class="ht">
        <span class="htag">STRATEGIE</span>
        <h1>Cloud Strategie & Roadmap</h1>
        <p class="hdesc">Maßgeschneiderte Cloud-Strategie und Roadmap für Ihre Atlassian-Infrastruktur. Maximieren Sie den ROI Ihres Toolstacks.</p>
        <a href="{U}/kontakt/" class="hcta"><span>Beratungstermin buchen</span><span class="arr" aria-hidden="true">→</span></a>
      </div>
      <div class="hg" aria-hidden="true"><div class="chart-ph">🗺️</div></div>
    </div>
  </div>
</section>
<section class="section"><div class="si"><div class="sh"><span class="st">Strategie</span><h2>Unsere Cloud-Strategie-Ansätze</h2></div>
    <div class="bgrid">
      <div class="bcard"><div class="bco"><div class="bmeta"><span>Review</span></div><h3>Atlassian Strategy Review</h3><p>ROI maximieren durch systematische Analyse Ihrer Atlassian-Instanzen.</p></div></div>
      <div class="bcard"><div class="bco"><div class="bmeta"><span>Roadmap</span></div><h3>Implementierungsplan</h3><p>Schritt-für-Schritt-Plan für Ihre Cloud-Migration.</p></div></div>
      <div class="bcard"><div class="bco"><div class="bmeta"><span>Adoption</span></div><h3>Cloud Adoption</h3><p>Sicherstellung der Nutzerakzeptanz und -akquise.</p></div></div>
    </div></div></section>
"""),

    ("loesungen/it-service-management.md",
     "IT Service Management",
     "IT Service Management mit Jira Service Management.",
     f"""<!-- ===== HERO ===== -->
<section class="hero" aria-label="IT Service Management">
  <div class="si">
    <div class="hc">
      <div class="ht">
        <span class="htag">ITSM</span>
        <h1>IT Service Management mit Jira</h1>
        <p class="hdesc">Effizientes IT Service Management mit Jira Service Management. Von der Anfrage bis zur Lösung – für IT-Teams und Business-Teams.</p>
        <a href="{U}/kontakt/" class="hcta"><span>ITSM-Lösung anfragen</span><span class="arr" aria-hidden="true">→</span></a>
      </div>
      <div class="hg" aria-hidden="true"><div class="chart-ph">🛡️</div></div>
    </div>
  </div>
</section>
<section class="section"><div class="si"><div class="sh"><span class="st">ITSM</span><h2>Jira Service Management</h2></div>
    <div class="bgrid">
      <div class="bcard"><div class="bco"><div class="bmeta"><span>Self-Service</span></div><h3>Self-Service Portal</h3><p>Effizienter Self-Service für Business-Teams und Endanwender.</p></div></div>
      <div class="bcard"><div class="bco"><div class="bmeta"><span>Automation</span></div><h3>Prozessautomatisierung</h3><p>Automatisierte Workflows für wiederkehrende IT-Aufgaben.</p></div></div>
      <div class="bcard"><div class="bco"><div class="bmeta"><span>Suite</span></div><h3>Customer Support Portal</h3><p>Kompromissloser Support für Kunden.</p></div></div>
    </div></div></section>
<section class="section"><div class="si">
  <div class="sh"><span class="st">Success Story</span></div>
  <div class="bgrid">
    {card_link(f"{U}/case-studies/it-service-management/", "Success Story: ITSM Branche Chemie", "IT Service Management in der Chemiebranche.", "📈")}
    {card_link(f"{U}/ressourcen/whitepaper-service/", "Whitepaper: Service & Development Teams", "Abstimmung zwischen Service und Development Teams.", "📄")}
  </div>
</div></section>
"""),

    ("loesungen/projektportfoliomanagement.md",
     "Projekt & Portfolio Management",
     "Agil zum Erfolg: Jira Projektportfoliomanagement im Fokus.",
     f"""<!-- ===== HERO ===== -->
<section class="hero" aria-label="Projekt & Portfolio Management">
  <div class="si">
    <div class="hc">
      <div class="ht">
        <span class="htag">PMM</span>
        <h1>Projekt & Portfolio Management</h1>
        <p class="hdesc">Agil zum Erfolg: Projektportfoliomanagement mit Jira. Behalten Sie den Überblick über alle Projekte und Portfolien.</p>
        <a href="{U}/kontakt/" class="hcta"><span>PMM-Beratung</span><span class="arr" aria-hidden="true">→</span></a>
      </div>
      <div class="hg" aria-hidden="true"><div class="chart-ph">📊</div></div>
    </div>
  </div>
</section>
<section class="section"><div class="si"><div class="sh"><span class="st">Jira PMM</span><h2>Portfolio-basierte Projektsteuerung</h2></div>
    <div class="bgrid">
      <div class="bcard"><div class="bco"><div class="bmeta"><span>Jira Software</span></div><h3>Projektplanung</h3><p>Planung und Verfolgung von Projekten in Jira Software.</p></div></div>
      <div class="bcard"><div class="bco"><div class="bmeta"><span>Jira Align</span></div><h3>Portfolio-Übersicht</h3><p>Übersicht über alle Projekte und Abhängigkeiten.</p></div></div>
      <div class="bcard"><div class="bco"><div class="bmeta"><span>Reports</span></div><h3>Reporting & Dashboards</h3><p>Echtzeit-Reporting für Entscheidungsträger.</p></div></div>
    </div></div></section>
"""),

    ("loesungen/changemanagement.md",
     "Change Management",
     "Change Management für digitale Transformation.",
     f"""<!-- ===== HERO ===== -->
<section class="hero" aria-label="Change Management">
  <div class="si">
    <div class="hc">
      <div class="ht">
        <span class="htag">CHANGE MANAGEMENT</span>
        <h1>Change Management</h1>
        <p class="hdesc">Unternehmen sicher durch digitale Transformation und Change begleiten. Wir schaffen Akzeptanz für neue Prozesse und Tools.</p>
        <a href="{U}/kontakt/" class="hcta"><span>Contact</span><span class="arr" aria-hidden="true">→</span></a>
      </div>
      <div class="hg" aria-hidden="true"><div class="chart-ph">🔄</div></div>
    </div>
  </div>
</section>
<section class="section"><div class="si"><div class="sh"><span class="st">Change</span><h2>Unsere Change-Management-Expertise</h2></div>
    <div class="bgrid">
      <div class="bcard"><div class="bco"><div class="bmeta"><span>Strategie</span></div><h3>Change-Strategie-Entwicklung</h3><p>Entwicklung einer maßgeschneiderten Change-Strategie.</p></div></div>
      <div class="bcard"><div class="bco"><div class="bmeta"><span>Schulung</span></div><h3>Train-the-Trainer</h3><p>Schulung interner Multiplikatoren im Unternehmen.</p></div></div>
      <div class="bcard"><div class="bco"><div class="bmeta"><span>Adoption</span></div><h3>Change Adoption</h3><p>Messung und Optimierung des Change-Erfolgs.</p></div></div>
    </div></div></section>
<section class="section"><div class="si">
  <div class="sh"><span class="st">Case Study</span></div>
  <div class="bgrid">
    {card_link(f"{U}/case-studies/changemanagement/", "Case Study: Change Management", "Erfolgsbericht über Change Management.", "📈")}
    {card_link(f"{U}/ressourcen/whitepaper-5gruende/", "Whitepaper: 5 Gründe in die Cloud", "5 Gründe für den Cloud-Wechsel.", "📄")}
  </div>
</div></section>
"""),

    ("loesungen/digitalisierung.md",
     "Digitalisierung von Geschäftsprozessen",
     "Digitalisierung von Geschäftsprozessen – XALT Business Consulting.",
     f"""<!-- ===== HERO ===== -->
<section class="hero" aria-label="Digitalisierung">
  <div class="si">
    <div class="hc">
      <div class="ht">
        <span class="htag">DIGITALISIERUNG</span>
        <h1>Digitalisierung von Geschäftsprozessen</h1>
        <p class="hdesc">Wir digitalisieren und automatisieren Ihre Geschäftsprozesse mit Jira, Confluence und der gesamten Atlassian-Suite.</p>
        <a href="{U}/kontakt/" class="hcta"><span>Digitalisierungsberatung</span><span class="arr" aria-hidden="true">→</span></a>
      </div>
      <div class="hg" aria-hidden="true"><div class="chart-ph">🔍</div></div>
    </div>
  </div>
</section>
<section class="section"><div class="si"><div class="sh"><span class="st">Digitalisierung</span><h2>Geschäftsprozesse revolutionieren</h2></div>
    <div class="bgrid">
      <div class="bcard"><div class="bco"><div class="bmeta"><span>Process Mining</span></div><h3>Prozessanalyse</h3><p>Analyse und Optimierung bestehender Geschäftsprozesse.</p></div></div>
      <div class="bcard"><div class="bco"><div class="bmeta"><span>Automation</span></div><h3>Prozessautomatisierung</h3><p>Automatisierung repetitiver Aufgaben und Workflows.</p></div></div>
      <div class="bcard"><div class="bco"><div class="bmeta"><span>Integration</span></div><h3>Systemintegration</h3><p>Anbindung bestehender Systeme an die Atlassian-Suite.</p></div></div>
    </div></div></section>
"""),

    ("loesungen/continuous-integration.md",
     "Continuous Integration & Delivery",
     "Continuous Integration and Delivery mit Atlassian-Tools.",
     f"""<!-- ===== HERO ===== -->
<section class="hero" aria-label="CI/CD">
  <div class="si">
    <div class="hc">
      <div class="ht">
        <span class="htag">CI/CD</span>
        <h1>Continuous Integration & Delivery</h1>
        <p class="hdesc">Continuous Integration and Delivery mit Jira, Bitbucket und der Atlassian-Toolchain für maximale Entwicklungs-Effizienz.</p>
        <a href="{U}/kontakt/" class="hcta"><span>CI/CD-Beratung</span><span class="arr" aria-hidden="true">→</span></a>
      </div>
      <div class="hg" aria-hidden="true"><div class="chart-ph">🔄</div></div>
    </div>
  </div>
</section>
<section class="section"><div class="si"><div class="sh"><span class="st">CI/CD</span><h2>Ihre CI/CD-Pipeline mit Atlassian</h2></div>
    <div class="bgrid">
      <div class="bcard"><div class="bco"><div class="bmeta"><span>Bitbucket</span></div><h3>Source Code Management</h3><p>Zentrales Repository für Ihren Source Code.</p></div></div>
      <div class="bcard"><div class="bco"><div class="bmeta"><span>Bamboo</span></div><h3>Build Automation</h3><p>Automatisierte Builds mit Bamboo.</p></div></div>
      <div class="bcard"><div class="bco"><div class="bmeta"><span>Stash</span></div><h3>Code Reviews</h3><p>Effiziente Code Reviews mit Bitbucket.</p></div></div>
    </div></div></section>
"""),

    ("loesungen/testing.md",
     "Automated Testing",
     "Automated Testing mit Atlassian-Tools.",
     f"""<!-- ===== HERO ===== -->
<section class="hero" aria-label="Automated Testing">
  <div class="si">
    <div class="hc">
      <div class="ht">
        <span class="htag">TESTING</span>
        <h1>Automated Testing</h1>
        <p class="hdesc">Automated Testing mit Atlassian-Tools für höchste Softwarequalität und schnelle Release-Zyklen.</p>
        <a href="{U}/kontakt/" class="hcta"><span>Testing-Beratung</span><span class="arr" aria-hidden="true">→</span></a>
      </div>
      <div class="hg" aria-hidden="true"><div class="chart-ph">🧪</div></div>
    </div>
  </div>
</section>
<section class="section"><div class="si"><div class="sh"><span class="st">Testing</span><h2>Testautomatisierung in der Praxis</h2></div>
    <div class="bgrid">
      <div class="bcard"><div class="bco"><div class="bmeta"><span>Planung</span></div><h3>Teststrategie</h3><p>Entwicklung einer umfassenden Teststrategie.</p></div></div>
      <div class="bcard"><div class="bco"><div class="bmeta"><span>Execution</span></div><h3>Testausführung</h3><p>Automatisierte Testausführung mit Jira.</p></div></div>
      <div class="bcard"><div class="bco"><div class="bmeta"><span>Reporting</span></div><h3>Test-Berichte</h3><p>Umfassende Testberichte und Metriken.</p></div></div>
    </div></div></section>
"""),

    ("loesungen/hosting.md",
     "Managed Hosting",
     "Hosting und Betrieb von Atlassian Applikationen.",
     f"""<!-- ===== HERO ===== -->
<section class="hero" aria-label="Hosting">
  <div class="si">
    <div class="hc">
      <div class="ht">
        <span class="htag">HOSTING</span>
        <h1>Managed Atlassian Hosting</h1>
        <p class="hdesc">Professionelles Hosting und Betrieb von Atlassian-Applikationen. Wir kümmern uns um Infrastruktur, Updates und Sicherheit.</p>
        <a href="{U}/kontakt/" class="hcta"><span>Managed Hosting</span><span class="arr" aria-hidden="true">→</span></a>
      </div>
      <div class="hg" aria-hidden="true"><div class="chart-ph">🖥️</div></div>
    </div>
  </div>
</section>
<section class="section"><div class="si"><div class="sh"><span class="st">Hosting</span><h2>Unsere Hosting-Angebote</h2></div>
    <div class="bgrid">
      <div class="bcard"><div class="bco"><div class="bmeta"><span>Cloud</span></div><h3>Atlassian Cloud Hosting</h3><p>Gemanagtes Hosting auf Atlassian Cloud.</p></div></div>
      <div class="bcard"><div class="bco"><div class="bmeta"><span>On-Premise</span></div><h3>On-Premise Hosting</h3><p>Hosting in Ihrer eigenen Infrastruktur.</p></div></div>
      <div class="bcard"><div class="bco"><div class="bmeta"><span>Support</span></div><h3>24/7 Support</h3><p>Rund-um-die-Uhr Support für kritische Systeme.</p></div></div>
    </div></div></section>
"""),

    ("loesungen/schulungen.md",
     "Atlassian Schulungen",
     "Atlassian Schulungen für Administratoren und Endanwender.",
     f"""<!-- ===== HERO ===== -->
<section class="hero" aria-label="Schulungen">
  <div class="si">
    <div class="hc">
      <div class="ht">
        <span class="htag">SCHULUNGEN</span>
        <h1>Atlassian Schulungen</h1>
        <p class="hdesc">Professionelle Schulungen für Jira, Confluence und die gesamte Atlassian-Plattform. Für Administratoren, Entwickler und Endanwender.</p>
        <a href="{U}/kontakt/" class="hcta"><span>Schulung buchen</span><span class="arr" aria-hidden="true">→</span></a>
      </div>
      <div class="hg" aria-hidden="true"><div class="chart-ph">🎓</div></div>
    </div>
  </div>
</section>
<section class="section"><div class="si"><div class="sh"><span class="st">Schulungen</span><h2>Unsere Schulungsprogramme</h2></div>
    <div class="bgrid">
      <div class="bcard"><div class="bco"><div class="bmeta"><span>Admin</span></div><h3>Jira Admin Schulung</h3><p>Umfassende Schulung für Jira-Administratoren.</p></div></div>
      <div class="bcard"><div class="bco"><div class="bmeta"><span>Basics</span></div><h3>Jira/Confluence Basics</h3><p>Einstiegsschulung für neue Atlassian-Nutzer.</p></div></div>
      <div class="bcard"><div class="bco"><div class="bmeta"><span>Advanced</span></div><h3>Advanced Workflows</h3><p>Fortgeschrittene Jira-Jira-Workflow-Konfiguration.</p></div></div>
    </div></div></section>
"""),
]

for path, title, desc, content in solutions:
    create(path, title, desc, content)

print("=== Done solutions ===")
