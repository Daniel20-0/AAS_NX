# NX Part Loader  
### Automatisches Öffnen von NX-Part-Dateien über Block UI Styler

Dieses Projekt beinhaltet eine Siemens NX Open Anwendung (C#), die über den NX Block UI Styler erstellt wurde.

Das Tool ermöglicht es Konstrukteuren, über eine einfache grafische Benutzeroberfläche einen Dateinamen einzugeben.  
Die Anwendung sucht rekursiv in einem definierten Verzeichnis nach einer passenden `.prt`-Datei und öffnet diese automatisch in Siemens NX.

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

## Grundlegende Funktionsweise

Das Tool führt folgenden Ablauf aus:

1. **Work-Part-Sicherung**  
   Beim Start wird geprüft, ob ein aktives Work Part existiert.  
   Falls nicht, wird automatisch ein neues Part erzeugt.

2. **Benutzereingabe**  
   Ein Block UI Styler Dialog wird geöffnet.  
   Der Benutzer gibt den gewünschten Dateinamen ein.

3. **Validierung**
   - Prüft, ob eine Eingabe erfolgt ist
   - Ergänzt automatisch `.prt`, falls nötig
   - Prüft, ob das Suchverzeichnis existiert

4. **Dateisuche**  
   Das definierte Verzeichnis wird rekursiv durchsucht.

5. **Öffnen des Parts**  
   Die erste gefundene Datei wird mit der NX Open API geöffnet.

---

## Code-Struktur

Der Code basiert auf dem Standard-Template des NX Block UI Stylers.

### `Main()`

- Initialisiert NX Session und UI
- Prüft, ob ein Work Part existiert
- Erstellt ggf. automatisch ein neues Part
- Startet den Dialog

---

### `initialize_cb()`

- Verbindet UI-Elemente aus der `.dlx`-Datei mit dem C#-Code
- Sucht das Texteingabefeld (`string0`)
- Speichert die Referenz für spätere Nutzung

---

### `apply_cb()`

Kernlogik des Tools:

- Liest Benutzereingabe
- Validiert Eingabe
- Ergänzt `.prt` falls notwendig
- Prüft das Suchverzeichnis
- Führt rekursive Dateisuche durch
- Öffnet die Datei mit:

```csharp
theSession.Parts.OpenBaseDisplay(...)
```
geladen und als Display Part angezeigt.

- Fehlermeldung: Falls keine Datei gefunden wird, erscheint eine Warnmeldung.

---

### `ok_cb()`

Wird ausgeführt, wenn der Nutzer auf "OK" klickt.

Funktion:
- Ruft intern apply_cb() auf
- Führt also dieselbe Logik wie "Anwenden" aus
- Schließt danach das Dialogfenster

Damit wird doppelter Code vermieden.

---

### `update_cb()`
Wird bei Änderung an UI-Element ausgelöst.

Aktuell:
- Ohne implementierte Logik
- Dient als Erweiterungspunkt für zukünftige UI-Validierung

---

## Die Benutzeroberfläche (`open:Part.dlx`)
Die .dlx-Datei definiert das visuelle Erscheinungsbild des Dialogs

Sie beinhaltetL:

- Einen Fenstertitel
- Eine Gruppe (group0) zur Strukturierung
- Ein Texteingabefeld (string0) zur Eingabe des Dateinamens
- Apply- und OK-Button

Die grafische Oberfläche wird vollständig durch den NX Block UI Styler erzeugt.

---

### Installation & Asuführung in NX

1. Lade die Dateien `open_Part.cs` und `open_Part.dlx` herunter.
2. Stelle sicher, dass beide Dateien idealerweise im selben Verzeichnis liegen oder entsprechend der NX-Umgebungsvariablen platziert sind (z.B. im Ordner `application` unter `UGII_USER_DIR`).
4. Führe die C#-Datei über `Datei -> Ausführen -> NX Open` (File -> Execute -> NX Open) aus oder binde sie als Button in deine NX-Benutzeroberfläche (Ribbon) ein.

---

## Troubleshooting (Fehlerbehebung)

* **Fehler beim Starten (Dialog wird nicht gefunden):** Standardmäßig sucht das C#-Skript nach der Datei `C:\Users\XXXX\XXXXX\open_Part.dlx` (wie im Code definiert). Wenn die Datei verschoben wurde, muss der Pfad in der Variable `theDlxFileName` im C#-Code angepasst werden, oder die `.dlx`-Datei muss in einen standardisierten NX-Ordner (`$UGII_USER_DIR/application/`) gelegt werden, sodass NX sie automatisch findet.

