# 02 Einleitung GitHub

# AAS-CAD Integration: Verbindung zwischen Verwaltungsschale und CAD

Einstiegsdokument für unser Projekt zur AAS-CAD Integration. 

In diesem Projekt arbeiten wir daran, die Asset Administration Shell (AAS) – also den standardisierten digitalen Zwilling – direkt mit unseren CAD-Systemen kommunizieren zu lassen. Ziel ist es, den Datenaustausch in beide Richtungen zu ermöglichen und dafür konkrete Code-Beispiele und Workflows bereitzustellen.

## Worum geht es hier genau?

Stand der Technik ist: Die 3D-Modelle liegen im CAD und der digitale Zwilling lebt völlig isoliert davon in seiner eigenen Software-Umgebung. Wenn wir aber Anwendungsfälle wie intelligentes Recycling oder eine lückenlose Materialverfolgung umsetzen wollen, müssen diese beiden Welten miteinander sprechen. Dieses Repository sammelt Skripte und Plug-ins, um genau diese Brücke zu schlagen.

---

## Kernfunktionen im Überblick

Wir konzentrieren uns auf vier grundlegende Funktionen, um die Interaktion zwischen AAS und CAD aufzubauen. In der Tabelle findest du direkte Links zu den jeweiligen Erklärungen und Umsetzungen für Siemens NX und PTC Creo sowie den aktuellen Entwicklungsstatus für Autodesk Fusion 360.

| # | Funktion | Umsetzung in Siemens NX | Umsetzung in PTC Creo | Umsetzung in Autodesk Fusion 360 |
| :--- | :--- | :--- | :--- | :--- |
| **1** | **Import von 3D-Daten aus der AAS** <br>*(Das Modell aus dem digitalen Zwilling ins CAD laden)* | [NX Part Loader](03_AAS_to_NX_Part_import.md) | [Creo Doku](CREO_DATEINAME.md) | 🚧 In Arbeit |
| **2** | **Zuweisung einer Asset-ID an ein Bauteil** <br>*(Die grundlegende Verknüpfung von 3D-Modell und AAS-Instanz)* | [NX Asset-ID assign](04_NX_PartID_to_AAS.md) | [Creo Doku](CREO_DATEINAME.md) | 🚧 In Arbeit |
| **3** | **Eigenschaften synchronisieren** <br>*(Materialdaten, Metadaten etc. austauschen)* | [NX Sync Properties with AAS](05_NX_Sync_Properties_with_AAS.md) | [Creo Doku](CREO_DATEINAME.md) | 🚧 In Arbeit |
| **4** | **Daten-Export aus dem CAD** <br>*(vorerst als CSV)*  | [NX to AAS Export](06_NX_to_AAS_Export.md) | [Creo Doku](CREO_DATEINAME.md) | 🚧 In Arbeit |

## Detaillierte Beschreibung der Funktionen

Wie genau diese vier Funktionen im Detail funktionieren und wie sie systemseitig gelöst wurden, kannst du direkt den verlinkten Dokumenten aus der obigen Tabelle entnehmen. Dort findest du die ausführlichen Erklärungen und Code-Beispiele für Siemens NX und PTC Creo.

---

## Mitmachen
Wir freuen uns immer über Unterstützung. Wenn du eigene Skripte beisteuern möchtest, eine Lösung für ein anderes CAD-System wie SolidWorks hast oder Fehler findest, erstelle gerne einen Pull Request.

## Lizenz

Das Kernprojekt „Anbindung CAD an Digitale Zwillinge“ ist unter der **Apache License 2.0** lizenziert. Detaillierte Informationen findest du in der [LICENSE.md](LICENSE.md)-Datei.

> **Wichtiger Hinweis zu Siemens NX (UI-Styler):** > Dieses Projekt enthält UI-Code, der mit dem **Siemens NX 2021 UI-Styler** generiert und manuell angepasst wurde. Um diesen Code lauffähig zu kompilieren oder zu nutzen, werden proprietäre NX Open Bibliotheken (DLLs) benötigt, die **nicht** Teil dieses Repositories sind. Die Rechte an diesen Bibliotheken sowie am grundlegenden Framework des generierten Codes verbleiben bei der Siemens AG. Bitte beachte die entsprechenden Lizenzbedingungen (EULA) deiner Siemens NX Installation.

Weitere rechtliche Hinweise sind in der [NOTICE.md](NOTICE.md)-Datei aufgeführt.