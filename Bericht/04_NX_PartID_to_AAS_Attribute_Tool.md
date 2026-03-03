# NX PartID to AAS Attribute Tool

Dieses Projekt beinhaltet eine Siemens NX Open Anwendung (C#), die über den NX Block UI Styler erstellt wurde. Das Tool ermöglicht es Konstrukteuren, über eine einfache grafische Benutzeroberfläche eine eindeutige ID (Part ID) in ein aktives NX-Bauteil einzutragen. 

Diese ID wird als Part-Attribut (`PART_ID`) gespeichert und dient zur Verknüpfung des 3D-Modells mit der **Asset Administration Shell (AAS / Verwaltungsschale)** für digitale Zwillinge.

---

## Grundlegende Funktionsweise (Das Hinzufügen der PartID für die AAS)

Um ein 3D-Modell in Industrie 4.0-Szenarien nutzbar zu machen, muss es eindeutig identifizierbar sein. Dieses Skript löst das Problem, indem es einen definierten Workflow in NX bereitstellt:

1. **Benutzereingabe:** Der Anwender startet das Skript in NX. Es öffnet sich ein Dialogfeld (definiert durch die `.dlx`-Datei), in dem die gewünschte ID für die Verwaltungsschale eingegeben wird.

2. **Validierung:** Das Tool prüft, ob eine ID eingegeben wurde und ob überhaupt ein Bauteil in NX geöffnet und aktiv (WorkPart) ist.
3. **Attribut-Zuweisung:** Die eingegebene Zeichenfolge wird über die NX Open API direkt in die Metadaten des Bauteils geschrieben. Es wird das Attribut **`PART_ID`** erzeugt bzw. überschrieben.

Sobald das Bauteil gespeichert und beispielsweise als STEP exportiert wird (inklusive Metadaten), kann die AAS diese `PART_ID` auslesen und das Bauteil einem digitalen Zwilling zuordnen.

---

## Code-Struktur und die einzelnen Funktionen

Der Code basiert auf dem Standard-Template des NX Block UI Stylers. Hier ist die detaillierte Beschreibung der wichtigsten Funktionen in der `add_PartID.cs`:

### `Main()`
Der Einstiegspunkt der Anwendung. Hier wird eine neue Instanz der Klasse `add_PartID` erstellt und der Dialog über die Methode `Show()` auf dem Bildschirm des Anwenders aufgerufen. 

### `initialize_cb()`
*(Initialize Callback)*
Diese Methode wird direkt beim Laden des Dialogs ausgeführt. Sie stellt die Verbindung zwischen der C#-Logik und der grafischen Oberfläche (der `.dlx`-Datei) her. Hier wird das Eingabefeld (Blocktyp: String) aus der UI gesucht und der Variablen `string0` zugewiesen, damit im späteren Verlauf darauf zugegriffen werden kann.

### `apply_cb()`
*(Apply Callback)*
Diese Funktion wird ausgelöst, wenn der Nutzer auf "Anwenden" klickt:
* **Werte auslesen:** Zieht den Text aus dem Eingabefeld (`string0.Value`).
* **Sicherheitsabfragen (If-Statements):**
  * Prüft, ob das Feld leer ist. Wenn ja, erscheint eine Info-Meldung und der Prozess stoppt.
  * Prüft, ob ein aktives Arbeits-Bauteil (`workPart`) existiert. Ohne Bauteil kann kein Attribut gesetzt werden.
* **Schreibvorgang:** Mit dem Befehl `workPart.SetAttribute("PART_ID", eingegebeneID);` wird das eigentliche Attribut in das NX-Bauteil geschrieben.
* **Session Undo:** Setzt einen sichtbaren Rückgängig-Schritt ("Part ID gesetzt"), um die NX-Sitzung sauber zu halten.

### `ok_cb()`
*(OK Callback)*
Wird ausgeführt, wenn der Nutzer auf den "OK"-Button klickt. Diese Funktion ruft intern lediglich die `apply_cb()` auf, führt also das Speichern des Attributes aus und schließt danach das Dialogfenster.

### `GetUnloadOption()`
Definiert, wie das Programm nach der Ausführung im Speicher von NX behandelt wird. Hier ist `Session.LibraryUnloadOption.Immediately` gesetzt. Das bedeutet, dass der Arbeitsspeicher sofort nach Ausführung des Skripts wieder freigegeben wird. Das verhindert Speicherlecks während einer NX-Sitzung.

---

## Die Benutzeroberfläche (`add_PartID.dlx`)

Die mitgelieferte XML-Datei (`.dlx`) definiert das visuelle Erscheinungsbild des NX-Dialogs. Sie beinhaltet:
* Den Titel des Fensters: **"Hinzufügen einer PartID"**
* Eine Gruppe (`group0`) zur visuellen Strukturierung.
* Das essenzielle Texteingabefeld (`string0`) mit dem Label **"PartID eingeben"**.

---

## Installation & Ausführung in NX

1. Lade die Dateien `add_PartID.cs` und `add_PartID.dlx` herunter.
2. Stelle sicher, dass beide Dateien idealerweise im selben Verzeichnis liegen oder entsprechend der NX-Umgebungsvariablen platziert sind (z.B. im Ordner `application` unter `UGII_USER_DIR`).
3. Öffne ein Bauteil in Siemens NX.
4. Führe die C#-Datei über `Datei -> Ausführen -> NX Open` (File -> Execute -> NX Open) aus oder binde sie als Button in deine NX-Benutzeroberfläche (Ribbon) ein.

---

## Troubleshooting (Fehlerbehebung)

* **Fehler beim Starten (Dialog wird nicht gefunden):** Standardmäßig sucht das C#-Skript nach der Datei `C:\Users\XXXX\XXXXX\add_PartID.dlx` (wie im Code definiert). Wenn die Datei verschoben wurde, muss der Pfad in der Variable `theDlxFileName` im C#-Code angepasst werden, oder die `.dlx`-Datei muss in einen standardisierten NX-Ordner (`$UGII_USER_DIR/application/`) gelegt werden, sodass NX sie automatisch findet.
* **Meldung "Kein aktives Bauteil vorhanden":**
  Das Skript wurde ausgeführt, ohne dass ein Bauteil geöffnet ist, oder das angezeigte Bauteil ist nicht das "Work Part" (Arbeitsteil). Mache das Bauteil per Rechtsklick im Baugruppen-Navigator zum Work Part und versuche es erneut.
  und so weiter