# 06 Attribute Export Skript

Dieses Python-Skript nutzt die **NXOpen Python API**, um bestimmte Attribute eines geöffneten NX-Bauteils auszulesen und diese in eine **CSV-Datei** zu exportieren.

Die CSV-Datei enthält ausgewählte **Masseneigenschaften** eines Parts, z.B.:

- Volumen
- Masse
- Oberfläche

Die Datei wird automatisch im gleichen Verzeichnis wie das NX-Part gespeichert.

---

# Grundlegende Funktionsweise

Das Skript führt folgenden Ablauf aus:

1. Verbindung zur aktuellen **NX-Session** herstellen  
2. Zugriff auf das **aktive Work Part**  
3. Definition der auszulesenden Attribute  
4. Durchsuchen aller Attribute des Parts  
5. Extraktion der gewünschten Werte  
6. Schreiben der Daten in eine **CSV-Datei**

---

# Code-Struktur und Funktionen

## main()

Der Einstiegspunkt des Skripts.

Funktionen:

- Zugriff auf die aktuelle NX-Session
- Zugriff auf das aktive Work Part
- Definition der gewünschten Attribute
- Auslesen aller Part-Attribute
- Filtern der relevanten Attribute
- Export der Werte in eine CSV-Datei

## Definition der gewünschten Attribute

Die folgenden Attribute werden exportiert:

wanted_attributes = [
    "MassPropVolume",
    "MassPropMass",
    "MassPropArea"
]

Diese Attribute entsprechen Masseneigenschaften eines NX-Bauteils.

| Attribut        | Bedeutung                |
|-----------------|--------------------------|
| MassPropVolume  | Volumen des Bauteils     |
| MassPropMass    | Masse des Bauteils       |
| MassPropArea    | Oberfläche des Bauteils  |

## Erstellen des Export-Dateipfades

Der Dateipfad der CSV-Datei wird automatisch erzeugt:

filePath = workPart.FullPath.replace(".prt", "_selected_attributes.csv")

---

## Installation & Ausführung in NX

Stelle sicher, dass Siemens NX mit NX Open Python API installiert ist. Speichere das Skript in einem NX-Skriptverzeichnis oder einem Projektordner. Öffne ein Bauteil in Siemens NX. Führe das Skript über folgendes Menü aus:
- Datei → Ausführen → NX Open
- Wähle das Python-Skript aus
- Nach der Ausführung wird automatisch eine CSV-Datei erzeugt

---

## Troubleshooting (Fehlerbehebung)
Keine CSV-Datei wird erstellt
Mögliche Ursachen:
- Kein aktives Work Part vorhanden
- Das Bauteil besitzt keine entsprechenden Attribute
- Schreibrechte im Zielverzeichnis fehlen

Attribute werden nicht gefunden
Mögliche Ursachen:

- Attribute besitzen andere Namen
- Attribute sind nicht als User Attributes gespeichert
- Alias und Titel unterscheiden sich