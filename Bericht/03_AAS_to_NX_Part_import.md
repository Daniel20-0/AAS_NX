# 03 NX AASX to STEP Import Tool

Dieses Projekt beinhaltet ein Python-Skript, das über die **NX Open Python API** ausgeführt wird.  
Das Tool dient dazu, eine **AASX-Datei (Asset Administration Shell)** auszuwählen, daraus automatisch ein enthaltenes **STEP-Modell** zu extrahieren und dieses anschließend in **Siemens NX** zu importieren.

Die Anwendung verbindet damit eine **Asset Administration Shell (AAS)** mit einem CAD-System, indem sie ein in der AAS referenziertes STEP-Modell direkt in NX öffnet.

---

## Überblick

Der **NX Part Loader** stellt einen vereinfachten Workflow zum schnellen Auffinden und Öffnen von Bauteilen bereit.

Funktionen:

- Automatische Prüfung auf vorhandenes Work Part
- Erstellung eines neuen Parts, falls keines existiert
- Dialogbasierte Dateinameneingabe
- Rekursive Suche nach `.prt` Dateien
- Automatisches Öffnen der ersten gefundenen Datei
- Fehlerausgabe über NX MessageBox

---

# Grundlegende Funktionsweise (Import eines STEP-Modells aus einer AASX)

Um digitale Zwillinge oder Industrie-4.0-Modelle in CAD-Systeme zu integrieren, müssen CAD-Daten aus der Verwaltungsschale extrahiert und in die CAD-Umgebung geladen werden.

Dieses Skript automatisiert diesen Workflow:

1. **Start des NX-Skripts**

   Der Benutzer startet das Skript direkt in Siemens NX.  
   Das Skript fungiert als **Launcher** und startet ein externes Python-Skript.

2. **Auswahl einer AASX-Datei**

   Das externe Skript öffnet einen Dateiauswahldialog.  
   Der Benutzer wählt eine `.aasx` Datei aus.

3. **Extraktion des STEP-Modells**

   Das externe Skript durchsucht die AAS nach referenzierten Modellen und extrahiert eine enthaltene STEP-Datei.

4. **Zwischenspeicherung**

   Die STEP-Datei wird temporär gespeichert.

5. **Import in Siemens NX**

   Das NX-Skript erkennt die erzeugte STEP-Datei und importiert sie automatisch in NX.

---

# Code-Struktur und die einzelnen Funktionen

Der Code besteht aus zwei Skripten:

- **NX Launcher Skript** (führt den Import in NX aus)
- **Externes AAS-Skript** (extrahiert das STEP-Modell aus der AASX)

---

# NX Launcher Skript

Dieses Skript wird direkt in Siemens NX ausgeführt und steuert den gesamten Workflow.

---

## `main()`

Der Einstiegspunkt des NX-Skripts.

Funktionen:

- Öffnet das NX Listing Window zur Ausgabe von Statusmeldungen
- Startet das externe Python-Skript über `subprocess`
- Prüft, ob die STEP-Datei erzeugt wurde
- Stellt sicher, dass ein aktives NX-Part existiert
- Importiert die STEP-Datei in NX

---
## `ensure_work_part()`

Diese Funktion stellt sicher, dass ein aktives NX-Part vorhanden ist.

Falls kein Work Part existiert:

- wird ein neues Part erstellt
- ein eventuell vorhandenes altes Part wird gelöscht
- das neue Part wird als **Work Part** gesetzt

Dadurch wird verhindert, dass NXOpen-Funktionen ohne gültiges Zielpart ausgeführt werden.

---

## `import_step_into_nx()`

Diese Funktion übernimmt den Import der STEP-Datei in NX.

Dafür wird der **NX Step242Importer** verwendet.

Konfiguration des Importers:

- Geometrieoptimierung aktiviert
- Kurven, Flächen und Volumenkörper werden importiert
- PMI-Daten werden ebenfalls übernommen
- Import erfolgt direkt aus dem Dateisystem

Der Import wird anschließend automatisch ausgeführt.
---
# Externes Skript (AAS_TO_NX.py)

Dieses Skript extrahiert ein STEP-Modell aus einer AASX-Datei.

---

## `main()`

Der Einstiegspunkt des externen Skripts.

Ablauf:

1. Öffnet einen Dateiauswahldialog
2. Benutzer wählt eine `.aasx` Datei
3. Die Datei wird analysiert
4. Ein STEP-Modell wird extrahiert
5. Die STEP-Datei wird lokal gespeichert

---

## `select_aasx_file()`

Diese Funktion öffnet einen Dateidialog über **Tkinter**.

Der Benutzer kann eine `.aasx` Datei auswählen.

Falls keine Datei ausgewählt wird, wird der Prozess beendet.

---

## `extract_step_from_aasx()`

Diese Funktion durchsucht die AASX-Datei nach enthaltenen CAD-Modellen.

Ablauf:

1. Import der AASX-Datei
2. Suche nach Asset Administration Shells
3. Durchsuchen der Modelle
4. Prüfen der Dateiformate
5. Finden einer STEP-Datei
6. Extraktion der STEP-Datei aus dem File Store
7. Schreiben der Datei in das temporäre Verzeichnis

---

# Installation & Ausführung in NX

1. Stelle sicher, dass Python installiert ist.
2. Stelle sicher, dass die NX Python API verfügbar ist.
3. Lege beide Skripte in dein Projektverzeichnis.

Benötigte Skripte:

- NX Launcher Skript
- `AAS_TO_NX.py`

4. Öffne Siemens NX.
5. Starte das NX-Skript über

Das Skript startet anschließend automatisch den vollständigen Workflow.

---

# Konfiguration

Aktuell sind mehrere Pfade im Code fest definiert.

Beispiele:

script_path = C:\Users\chris\AAS-Creo-Bridge\src\AAS_TO_NX.py

step_path = C:\Users\chris\AAS-Creo-Bridge\temp_model.step

---

# Troubleshooting (Fehlerbehebung)

## STEP-Datei wird nicht erzeugt
Mögliche Ursachen:

- Die AASX-Datei enthält kein STEP-Modell
- Das Modellformat ist nicht STEP
- Der Zugriff auf den File Store ist fehlgeschlagen

---

## Externes Skript startet nicht

Mögliche Ursachen:

- Falscher Python-Pfad
- Skriptpfad falsch
- Python-Abhängigkeiten fehlen

---

## Import in NX schlägt fehl

Mögliche Ursachen:

- STEP-Datei beschädigt
- NX Step Importer nicht korrekt initialisiert
- Kein Work Part vorhanden


