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
| **1** | **Import von 3D-Daten aus der AAS** <br>*(Das Modell aus dem digitalen Zwilling ins CAD laden)* | [NX Part Loader](03_AAS_to_NX_Part_import.md) | [Creo Doku](CREO_DATEINAME.md) |
| **2** | **Zuweisung einer Asset-ID an ein Bauteil** <br>*(Die grundlegende Verknüpfung von 3D-Modell und AAS-Instanz)* | [NX Asset-ID assign](04_NX_PartID_to_AAS.md) | [Creo Doku](CREO_DATEINAME.md) |
| **3** | **Eigenschaften synchronisieren** <br>*(Materialdaten, Metadaten etc. austauschen)* | [NX Sync Properties with AAS](05_NX_Sync_Properties_with_AAS.md) | [Creo Doku](CREO_DATEINAME.md) |
| **4** | **Daten aus dem CAD in die AAS exportieren** <br>*(Aktualisierte Daten zurück in die Schale schreiben)* | [NX to AAS Export](06_NX_to_AAS_Export.md) | [Creo Doku](CREO_DATEINAME.md) |

---

## Detaillierte Beschreibung der Funktionen

Wie genau diese vier Funktionen im Detail funktionieren und wie sie systemseitig gelöst wurden, kannst du direkt den verlinkten Dokumenten aus der obigen Tabelle entnehmen. Dort findest du die ausführlichen Erklärungen und Code-Beispiele für Siemens NX und PTC Creo.

---

## Mitmachen
Wir freuen uns immer über Unterstützung. Wenn du eigene Skripte beisteuern möchtest, eine Lösung für ein anderes CAD-System wie SolidWorks hast oder Fehler findest, erstelle gerne einen Pull Request. Halte dich dabei einfach grob an die Struktur dieses Dokuments.

## Lizenz

Dieses Projekt ist unter der [GNU General Public License v3.0 (GPLv3)](LICENSE) lizenziert. 
Weitere Details zur Nutzung, Vervielfältigung und Modifikation findest du in der `LICENSE`-Datei in diesem Repository.