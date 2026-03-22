## Werkzeugkasten in NX

Die Anbindung des CAD-Systems Siemens NX an die Asset Administration Shell (AAS) ermöglicht einen durchgängigen, bidirektionalen Informationsfluss. Dadurch wird das statische 3D-Modell zu einem integralen Bestandteil des Digitalen Zwillings. Über die NX Open API lassen sich vielfältige Funktionen realisieren, die den Funktionsumfang für AAS-Anwendungsfälle nahezu unbegrenzt erweitern.

Folgende Kernfunktionen und Workflows sind durch die Integration möglich:

### 1. Automatisierter Import von CAD-Daten aus der AAS
* **AASX-Extraktion:** CAD-Modelle (wie z. B. STEP-Dateien), die in einem AASX-Container referenziert sind, können über externe Python-Skripte gezielt gesucht, extrahiert und in einem temporären Verzeichnis abgelegt werden.
* **Automatisches Laden in NX:** Ein in NX ausgeführtes Launcher-Skript greift diese Daten auf und importiert sie über den NX Step Importer automatisch in die Arbeitsumgebung.
* **Baugruppen und Einzelteile:** Es können sowohl komplexe Baugruppenstrukturen als auch Einzelteile geladen werden. *Hinweis zur Positionierung: Über die NX Open API können den importierten Körpern beim Laden oder in der Baugruppe exakte Transformationsmatrizen (Koordinaten) mitgegeben werden.*

### 2. Zuweisung einer eindeutigen Asset-ID (Digitaler Faden)
* **ID-Verknüpfung:** Um ein CAD-Bauteil eindeutig einer spezifischen AAS-Instanz zuzuordnen, kann dem Modell direkt in NX eine eindeutige ID zugewiesen werden.
* **Attributierung:** Diese Zuweisung erfolgt durch das Schreiben von Metadaten in die Part-Attribute (z. B. Anlage des Attributs `PART_ID`). Wird das Teil später exportiert, bleibt diese ID als Meta-Information im Modell erhalten und kann von Systemen der Industrie 4.0 ausgelesen werden.

### 3. Datenexport für Stücklisten (BOM) und AAS-Synchronisation
* **Eigenschaften auslesen:** Spezifische physikalische Masseneigenschaften eines NX-Teils (wie Volumen, Masse und Oberfläche) können automatisiert über ein Python-Skript ausgelesen werden.
* **BOM-Erstellung:** Diese ausgelesenen CAD-Attribute lassen sich exportieren (z. B. als CSV-Datei). Diese Daten bilden die Grundlage für detaillierte Stücklisten (wie z. B. eine R-BOM für Recycling-Szenarien), die anschließend direkt in die Struktur der AASX-Datei eingehängt werden können.

### 4. UI-Anpassung und Nutzerinteraktion
* **NX Block UI Styler:** Native grafische Benutzeroberflächen (Dialogboxen) können direkt in NX erstellt werden. So kann der Nutzer beispielsweise IDs über ein komfortables Textfeld eingeben, während im Hintergrund Validierungsprüfungen (z. B. ob ein aktives Bauteil geöffnet ist) ablaufen.
* **Nahtlose Integration:** Die Benutzeroberfläche von NX lässt sich anpassen, indem Skripte als interaktive Buttons direkt in der NX-Menüleiste (Ribbon) hinterlegt werden. Dies sorgt für eine hohe Benutzerfreundlichkeit.
* **Grenzenlose Erweiterbarkeit:** Da NX sowohl als Launcher für externe Python-Skripte agieren als auch interne C#/Python-Logik ausführen kann, gibt es für die Automatisierung und Datenverknüpfung mit dem Digitalen Zwilling kaum technische Einschränkungen.