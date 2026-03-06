# 02 Einleitung GitHub

# AAS-CAD Integration: Verbindung zwischen Verwaltungsschale und CAD

Einstiegsdokument für unser Projekt zur AAS-CAD Integration. 

In diesem Projekt arbeiten wir daran, die Asset Administration Shell (AAS) – also den standardisierten digitalen Zwilling – direkt mit unseren CAD-Systemen kommunizieren zu lassen. Ziel ist es, den Datenaustausch in beide Richtungen zu ermöglichen und dafür konkrete Code-Beispiele und Workflows bereitzustellen.



## Worum geht es hier genau?

Stand der Technik ist: Die 3D-Modelle liegen im CAD und der digitale Zwilling lebt völlig isoliert davon in seiner eigenen Software-Umgebung. Wenn wir aber Anwendungsfälle wie intelligentes Recycling oder eine lückenlose Materialverfolgung umsetzen wollen, müssen diese beiden Welten miteinander sprechen. Dieses Repository sammelt Skripte und Plug-ins, um genau diese Brücke zu schlagen.

---

## Kernfunktionen im Überblick

Wir konzentrieren uns auf vier grundlegende Funktionen, um die Interaktion zwischen AAS und CAD aufzubauen. In der Tabelle findest du direkte Links zu den jeweiligen Erklärungen und Umsetzungen für Siemens NX und PTC Creo.

| # | Funktion | Umsetzung in Siemens NX | Umsetzung in PTC Creo |
| :--- | :--- | :--- | :--- |
| **1** | **Import von 3D-Daten aus der AAS** <br>*(Das Modell aus dem digitalen Zwilling ins CAD laden)* | [NX Doku](#1-import-von-3d-daten-aus-der-aas) | [Creo Doku](#1-import-von-3d-daten-aus-der-aas) |
| **2** | **Zuweisung einer Asset-ID an ein Bauteil** <br>*(Die grundlegende Verknüpfung von 3D-Modell und AAS-Instanz)* | [NX Doku](#2-zuweisung-einer-asset-id-partid) | [Creo Doku](#2-zuweisung-einer-asset-id-partid) |
| **3** | **Eigenschaften synchronisieren** <br>*(Materialdaten, Metadaten etc. austauschen)* | [NX Doku](#3-eigenschaften-synchronisieren) | [Creo Doku](#3-eigenschaften-synchronisieren) |
| **4** | **Daten aus dem CAD in die AAS exportieren** <br>*(Aktualisierte Daten zurück in die Schale schreiben)* | [NX Doku](#4-daten-aus-dem-cad-in-die-aas-exportieren) | [Creo Doku](#4-daten-aus-dem-cad-in-die-aas-exportieren) |

---

## Detaillierte Beschreibung der Funktionen

Hier erklären wir kurz, was hinter den einzelnen Schritten steckt und wie wir das Ganze systemseitig lösen.

### 1. Import von 3D-Daten aus der AAS
Wenn in der Verwaltungsschale bereits ein Submodell mit CAD-Daten (wie STEP oder JT) liegt, wollen wir dieses nicht manuell heraussuchen müssen. Diese Funktion beschreibt, wie ein Konstrukteur die AAS ansteuert und das darin enthaltene 3D-Modell per Skript direkt in seine aktive CAD-Sitzung lädt.
* **Siemens NX:** 
* **PTC Creo:** 

### 2. Zuweisung einer Asset-ID (PartID)
Das ist der wichtigste erste Schritt. Damit CAD und AAS sich verstehen, muss das CAD-Modell wissen, zu welcher Verwaltungsschale es gehört. Dafür erzeugen wir ein spezifisches Attribut (z.B. PART_ID) im 3D-Modell.
* **Siemens NX:** Wir nutzen hierfür ein C#-Skript in Kombination mit dem NX Block UI Styler, das dem Konstrukteur ein einfaches Eingabefenster bietet. (Siehe Unterordner `/NX_AddPartID/`)
* **PTC Creo:** 

### 3. Eigenschaften synchronisieren
Sobald die ID verknüpft ist, können wir anfangen, Metadaten auszutauschen. Wenn sich in der Verwaltungsschale zum Beispiel die Materialvorgabe ändert, soll unser Skript diese neue Information auslesen und das Material im CAD-Bauteil entsprechend anpassen.
* **Siemens NX:** 
* **PTC Creo:** 

### 4. Daten aus dem CAD in die AAS exportieren
Das ist der Weg zurück. Wenn die Konstruktion abgeschlossen ist oder Geometrien optimiert wurden, müssen diese Änderungen in den digitalen Zwilling gespiegelt werden. Das Skript greift die neuen Parameter ab, erzeugt eventuell ein neues 3D-Austauschformat und aktualisiert das entsprechende Submodell in der Verwaltungsschale.
* **Siemens NX:** 
* **PTC Creo:** 

---

## Mitmachen
Wir freuen uns immer über Unterstützung. Wenn du eigene Skripte beisteuern möchtest, eine Lösung für ein anderes CAD-System wie SolidWorks hast oder Fehler findest, erstelle gerne einen Pull Request. Halte dich dabei einfach grob an die Struktur dieses Dokuments.

## Lizenz

Dieses Projekt ist unter der [GNU General Public License v3.0 (GPLv3)](LICENSE) lizenziert. 
Weitere Details zur Nutzung, Vervielfältigung und Modifikation findest du in der `LICENSE`-Datei in diesem Repository.