# 01 Einleitung HKA: Integration von Digitalen Zwillingen (AAS) und CAD (Siemens NX)

Im Rahmen dieses Entwicklungsprojekts wird die informationstechnische und konzeptionelle Brücke zwischen der Asset Administration Shell (AAS – Verwaltungsschale) und dem CAD-System Siemens NX geschlagen. Ziel ist es, das Arbeiten mit Digitalen Zwillingen über Systemgrenzen hinweg zu ermöglichen und eine durchgängige Datennutzung über den gesamten Produktlebenszyklus zu gewährleisten. 

Das Projekt gliedert sich methodisch in zwei aufeinander aufbauende Phasen:

## Phase 1: Grundlagen und Anwendungsszenarien im Produktlebenszyklus

In der ersten Projektphase wurden die theoretischen Grundlagen der AAS erarbeitet und evaluiert, welche konkreten Mehrwerte und Anwendungsszenarien die Anbindung eines CAD-Systems an die Verwaltungsschale bietet. 

Zur Veranschaulichung der Konzepte dient das praxisnahe Beispiel einer **Spülmaschine**. Entlang ihres Produktlebenszyklus entstehen in jeder Phase stark variierende Anforderungen an die Bereitstellung, Aktualisierung und Strukturierung von Daten aus dem Digitalen Zwilling. 

Der betrachtete Lebenszyklus umfasst die folgenden sechs Phasen:

1.  Entwicklung (CAD & Engineering)
2.  Teilebeschaffung (Procurement)
3.  **Produktion (Manufacturing)**
4.  Sales (Vertrieb)
5.  Service / After-Sales
6.  **Recycling (End-of-Life)**

*Wie im nachfolgenden Diagramm dargestellt, bilden diese Phasen einen fortlaufenden Kreislauf. Im Rahmen dieses Projekts wurden insbesondere die Phasen **Produktion** und **Recycling** tiefgehend ausgearbeitet. Die detaillierte Ausarbeitung dieser Use-Cases ist Gegenstand der nachfolgenden Kapitel.*

![Produktlebenszyklus einer Spülmaschine](bilder/Eng_AAS_CAD_Lifecycle.drawio.svg)

## Phase 2: Technische Umsetzung und Schnittstellenfunktionen

Basierend auf den konzeptionellen Vorarbeiten der ersten Phase lag der Fokus der zweiten Projektphase auf der technischen Implementierung. Hierbei wurden die zentralen Kernfunktionen identifiziert und entwickelt, die für das praktische Arbeiten mit AASX-Datenpaketen und dem CAD-Programm Siemens NX zwingend erforderlich sind. 

---

> **Hinweis zur Dokumentation ("Living Document"):**
> Da an diesem Repository auch in Zukunft weitergeforscht und gearbeitet wird, ist diese Dokumentation direkt als Struktur für das GitHub-Repository (`README.md` und verknüpfte Markdown-Dateien) konzipiert. Auf eine redundante, separat geführte Dokumentation wurde bewusst verzichtet. Dies stellt sicher, dass Code-Änderungen und Dokumentation stets synchron, transparent versioniert und an einem zentralen Ort für nachfolgende Entwickler zugänglich bleiben.

---

## 3. Szenario: Produktion (Manufacturing)

### 3.1 Detailed description of the scenario
Lena Müller arbeitet als Produktionsplanerin und Montageleiterin in der Endmontage. Sie ist verantwortlich für die korrekte Ausführung der Montageprozesse sowie für die Qualitätssicherung der montierten Baugruppen. Lena überprüft die Anzugsdrehmomente der einzelnen Verschraubungen und montiert die zugehörigen Blechbauteile. Dabei stellt sie sicher, dass alle Montagevorgaben exakt eingehalten werden, um Funktionsfähigkeit, Sicherheit und Qualität des Produkts zu gewährleisten. 

Die relevanten Montageinformationen werden Lena digital bereitgestellt. Eine Montagezeichnung, die über die Asset Administration Shell (AAS) mit dem jeweiligen physischen Asset verknüpft ist, ist im CAD-Modell hinterlegt. Über ein digitales Endgerät (z. B. Industrie-Tablet oder HMI) kann Lena kontextbezogen auf diese Informationen zugreifen.

### 3.2 Process flow description

* **Identifikation des Produkts / Assets:** Lena identifiziert das zu montierende Produkt anhand einer Seriennummer oder eines QR-Codes.
* **Aufruf der AAS:** Über das Fertigungssystem wird die zugehörige Asset Administration Shell geladen.
* **Zugriff auf die Montageinformationen:** Die AAS verweist auf das verknüpfte CAD-Modell und die zugehörige Montagezeichnung.
* **Anzeige der Montageschritte:** Die einzelnen Montageschritte werden sequenziell dargestellt, inklusive der benötigter Werkzeuge.
* **Prüfung der Anzugsdrehmomente:** Für jede Schraubverbindung werden die Soll-Drehmomente angezeigt und mit dem eingesetzten Drehmomentwerkzeug überprüft.
* **Montage der Blechbauteile:** Lena montiert die Blechkomponenten gemäß der Zeichnung und den definierten Prozessschritten.
* **Dokumentation und Rückmeldung:** Die erfolgte Montage und die geprüften Drehmomente werden im System dokumentiert und ggf. an übergeordnete Systeme zurückgemeldet.

### 3.3 Required files and resources
* **CAD-Modelle** (z. B. STEP, JT, native CAD-Formate)
* **Montagezeichnungen** (2D/3D, z. B. PDF oder direkt im CAD)
* **Drehmoment-Spezifikationen** (z. B. Tabellen oder Metadaten)
* **Asset Administration Shell** (AAS-Modell im JSON- oder XML-Format)
* **Digitale Endgeräte** (Tablet, Industrie-PC, HMI)
* **Drehmomentwerkzeuge** (idealerweise mit digitaler Schnittstelle)
* **MES-/PLM-Systeme** zur Datenverwaltung

### 3.4 Technical implementation

#### 3.4.1 Implementation in the Asset Administration Shell (AAS)
Die Asset Administration Shell dient als zentraler Daten-Hub für montage- und qualitätsrelevante Informationen. Technisch erfolgt die Umsetzung über klar definierte `SubmodelElements`, die Montagewissen, CAD-Referenzen und Drehmomentvorgaben standardisiert abbilden.

**Montage- und Drehmomentdaten**
* **Submodell „AssemblyInformation“:** Enthält die vollständige Beschreibung der Montageschritte als strukturierte `SubmodelElements` (z. B. `Operation`, `Sequence`, `StepNumber`).
* **Anzugsdrehmomente:** Jede Schraubverbindung wird durch ein `Property`-Element beschrieben:
    * `FastenerID`
    * `TorqueNominal` (z. B. 12 Nm)
    * `TorqueTolerance` (z. B. ±10 %)
    * `ToolType` (z. B. elektronischer Drehmomentschlüssel)

> **Beispiel:** Die Verschraubung der Seitenwand besitzt das Attribut `TorqueNominal = 12 Nm`, `TorqueTolerance = ±1,2 Nm`.

#### 3.4.2 Implementation in the CAD environment
Die CAD-Umgebung (Viewer oder Montage-Frontend an Lenas Arbeitsplatz) fungiert als visuelle und interaktive Schnittstelle zwischen Werkerin und digitalem Produktzwilling.

* Jedes Bauteil und jede Schraubverbindung im CAD-Modell ist mit der `InstanceId` der entsprechenden AAS-Komponente verknüpft.
* Klickt Lena auf eine Schraube im 3D-Modell, werden **Soll-Drehmoment**, **Toleranz** und **Werkzeugtyp** direkt aus der AAS geladen und angezeigt.

**Feedback- und Rückmeldekanal (As-Planned vs. As-Built)**
Lena kann direkt im CAD-Interface Abweichungen melden, z. B.:
* Schraube nicht zugänglich
* Bauteil passt nicht spannungsfrei
* Drehmoment konstruktiv nicht erreichbar

Diese Rückmeldungen werden als `Event` oder `Annotation` direkt in der AAS gespeichert und stehen Konstruktion und Arbeitsvorbereitung zur Verfügung.

---

## 6. Szenario: Recycling (End-of-Life)

### 6.1 Detailed description of the scenario
Im Jahr 2026 ist die lineare Wirtschaft („Produzieren, Nutzen, Wegwerfen“) durch die *Ecodesign for Sustainable Products Regulation* (ESPR) gesetzlich beendet worden. Jede in der EU verkaufte Spülmaschine muss nun über einen Digitalen Produktpass (DPP) verfügen, der technisch als Verwaltungsschale (Asset Administration Shell, AAS) realisiert ist. 

Markus Mustermann, ein spezialisierter Mitarbeiter in einem zertifizierten Demontagezentrum, steht vor einer Herausforderung: Eine moderne Spülmaschine besteht aus über 150 verschiedenen Materialien, darunter wertvoller Edelstahl, kupferhaltige Motoren, Elektronik mit Seltenen Erden und problematische Bitumen-Dämmmatten.

Ohne die AAS wäre die Spülmaschine für Markus eine „Blackbox“. Er müsste sie schreddern, was die Materialreinheit extrem verschlechtert. Dank der AAS wird Markus zum Urban Miner: Er greift auf den digitalen Zwilling zu, der ihm nicht nur sagt, was verbaut ist, sondern auch, wie er es zerstörungsfrei trennen kann, um die Rückführungsgewinne zu maximieren.

### 6.2 Process flow description
Der Workflow ist in fünf Phasen unterteilt:

1.  **Erfassung & Initialisierung:** Markus scannt den am Gehäuserahmen gelaserten QR-Code. Die AAS öffnet dazu das entsprechende Modell.
2.  **Status- & Sicherheitsanalyse:** Bevor Markus das Werkzeug ansetzt, prüft das System das Submodell „Safety“. Es wird angezeigt, ob Kondensatoren entladen werden müssen oder ob chemische Rückstände (z. B. Klarspüler-Reste) in Schläuchen vorhanden sind.
3.  **Virtuelle Exploration:** Markus bekommt in der AAS die Demontagezeichnungen und zerlegt basierend darauf die Maschine. Ihm wird angezeigt, welches Teil aus welchem Material ist. Am Ende trägt er ein, wie viel Masse er von welchem Material sortenrein getrennt hat.
4.  **Geführte Demontage:** Markus folgt den in der AAS hinterlegten Schritten. Das System gibt vor:
    * *Schritt 1:* Lösen der Torx-Schrauben (T15) an der Rückwand.
    * *Schritt 2:* Abklemmen des Kabelbaums.
    * *Schritt 3:* Entnahme der Isolierung.

### 6.3 Required files and resources
Für die Implementierung werden folgende Punkte benötigt:

* **Das AASX-Container-File:** Beinhaltet die logische Struktur und alle Verweise.
* **Identification:** Eindeutige ID.
* **DigitalProductPassport (DPP):** Enthält die rechtlich geforderten Daten der ESPR (CO2-Fußabdruck, Rezyklatanteil).
* **Bill of Materials (R-BOM):** Die hierarchische Liste sowie Eigenschaften für das Recycling aller Komponenten.
* **TechnicalProperties:** Materialdatenblätter pro Komponente, von den jeweiligen Herstellern bereitgestellt und in der AAS der Spülmaschine zusammengeführt.
* **CAD-Ressourcen:** Demontagezeichnungen und 3D-Modell zur Demontage.

### 6.4 Technical implementation

#### 6.4.1 Implementation in the Asset Administration Shell (AAS)
Die AAS dient als Daten-Hub. Alle verbauten Komponenten haben von den jeweiligen Herstellern die Eigenschaften hinterlegt und diese werden zu einer Spülmaschine zusammengebaut.

* **Material-Identifikation:** Jedes Bauteil in der Spülmaschine erhält ein `Property`-Element mit der Material-ID.
    * *Beispiel:* Die Verkleidungselemente erhalten das Attribut `Material: V2A (Edelstahl)`.
* **API-Schnittstelle:** Die AAS stellt eine REST-API bereit, über die die Recycling-Software Abfragen stellt (z. B. `GET /submodels/MaterialComposition/submodel-elements/CopperWeight`).

#### 6.4.2 Implementation in the CAD environment
Die CAD-Umgebung dient als zentrale Datenquelle für die Erstellung der Verwaltungsschale (AAS). Der Prozess gestaltet sich wie folgt:

* **Bereitstellung von Dokumenten:** Direkt aus dem CAD-System werden Demontagezeichnungen im PDF-Format generiert und der AAS zur Verfügung gestellt.
* **Stoffstromanalyse:** Es wird eine automatisierte Liste generiert, die alle Bauteile inklusive deren Volumina und Materialien erfasst. Daraus lassen sich die exakten Massen der verschiedenen Rohstoffe ableiten. 
* **Soll-Ist-Vergleich im Recycling-Prozess:** Im Rahmen des Recycling-Prozesses werden diese Daten für jede Spülmaschinen-Variante berechnet und in der AAS als Soll-Werte hinterlegt.
* **Nachweispflicht:** Nach der Zerlegung ist der Recycler verpflichtet, die tatsächlich gewonnenen Massen der unterschiedlichen Stoffe als Ist-Werte in die AAS einzutragen.
* **Rückfluss zum Hersteller:** Diese Daten werden an den Hersteller zurückgeführt. Dieser erhält dadurch einen lückenlosen Nachweis darüber, zu wie viel Prozent die Maschine sortenrein zerlegt wurde.
* **Visualisierung:** Bei hoher Komplexität der Anlage kann dem Recycler zusätzlich ein 3D-Modell zur Verfügung gestellt werden.
* **Zusätzliche Visualisierung:** Das System berechnet die Recycling-Priorität auf Grundlage der hinterlegten Materialeigenschaften. Bauteile, die Schadstoffe enthalten, werden rot blinkend dargestellt.

### 6.5 Vorgaben und gesetzliche Richtlinien (Additional Requirements)

1.  **ESPR (Ecodesign for Sustainable Products Regulation)**
    * **Standardwerkzeuge & Zerlegbarkeit:** Bereits die bestehende Verordnung (EU) 2019/2022 für Spülmaschinen legt fest, dass bestimmte Teile (wie Pumpen oder Motoren) mit „allgemein verfügbaren Werkzeugen“ und ohne dauerhafte Beschädigung des Geräts austauschbar sein müssen.
    * **Demontagezeit:** Die neue ESPR (Verordnung (EU) 2024/1781) erlaubt es der EU, in produktspezifischen "Delegierten Rechtsakten" explizite Leistungsanforderungen zu stellen. Für die Überarbeitung der Spülmaschinen-Regeln (geplant ab 2026) wird diskutiert, die Demontagezeit als Metrik für die Recyclingfähigkeit aufzunehmen. *(Quelle: Verordnung (EU) 2019/2022, Anhang II, Punkt 3 sowie Verordnung (EU) 2024/1781 (ESPR), Artikel 5).*
2.  **EU-Batterieverordnung (2023/1542)**
    * **Entnehmbarkeit:** Ab dem 18. Februar 2027 müssen Gerätebatterien so konstruiert sein, dass sie vom Endnutzer oder Fachpersonal leicht entnommen und ausgetauscht werden können.
    * **Batteriepass:** Während der volle „Batteriepass“ primär für Industrie- (>2 kWh) und Traktionsbatterien gilt, müssen Informationen zur chemischen Zusammensetzung und zum sicheren Ausbau bei kleinen Batterien im Digitalen Produktpass (DPP) des Hauptgeräts (hier die AAS der Spülmaschine) hinterlegt sein. *(Quelle: Verordnung (EU) 2023/1542, Artikel 11 und Artikel 77).*
3.  **WEEE-Richtlinie (Waste Electrical and Electronic Equipment)**
    * Die WEEE regelt den Umgang mit dem Elektroschrott nach der Nutzung. 
    * **Sammel- und Verwertungsquoten:** Für Großgeräte (Kategorie 1), zu denen Spülmaschinen gehören, schreibt die Richtlinie eine Verwertungsquote von 85 % und eine Quote für Vorbereitung zur Wiederverwendung und Recycling von 80 % vor. 
    * **Rolle der AAS:** Die AAS ist das Werkzeug, um die "Materialhygiene" zu garantieren. Nur durch sortenreine Trennung (z. B. Edelstahl der Güte 1.4301 statt Mischschrott) können diese hohen Quoten wirtschaftlich erreicht werden. *(Quelle: Richtlinie 2012/19/EU, Anhang V).*
4.  **Substances of Concern (REACH & SCIP)**
    * **Informationspflicht:** Seit Januar 2021 müssen Hersteller Informationen über besonders besorgniserregende Stoffe (SVHC) in der SCIP-Datenbank der ECHA hinterlegen, wenn die Konzentration über 0,1 % liegt.
    * **AAS-Integration:** Die AAS dient als Schnittstelle, um diese komplexen Chemikaliendaten für Markus Mustermann direkt am Arbeitsplatz visualisierbar zu machen (z. B. Warnhinweis auf Bitumenmatten oder Flammschutzmittel in Platinen), ohne dass er manuell in Datenbanken suchen muss. *(Quelle: Abfallrahmenrichtlinie (2008/98/EG), Artikel 9(1)i und REACH-Verordnung (EG) Nr. 1907/2006).*