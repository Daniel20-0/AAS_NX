## Prerequisites
Für die erfolgreiche Einrichtung und Ausführung der Integration zwischen Siemens NX und der AAS müssen folgende Systemvoraussetzungen erfüllt sein:

### Software & Lizenzen
- [ ] **Siemens NX:** Lokale Installation (z. B. Version 2021).
- [ ] **NX-Lizenz:** Enterprise- bzw. NX Open-Lizenz zur Ausführung und Kompilierung von Skripten und externen Programmen.
- [ ] **AASX Package Explorer:** Tool zur Betrachtung und Validierung der Verwaltungsschalen.

### Entwicklungsumgebung & Sprachen
- [ ] **Python:** Eigenständige Installation (ab Version 3.11) für Adapter weil in der NX 2021 die Python Version nur die (Version 3.8 ist und in dieser die lxml-Bibliothek nicht enthalten ist).
- [ ] **IDE:** Visual Studio (für z.B. C#) oder Visual Studio Code (für Python) zum anpassen der Sktipte.

### Systemrechte & Konfiguration
- [ ] **Administratorrechte:** Lokale Windows-Adminrechte (für Installationen via `pip` und das Setzen von Umgebungsvariablen).
- [ ] **NX-Rolle:** Eine fortgeschrittene Benutzerrolle (z. B. "Advanced"), um den Entwickler-Tab in der NX-Oberfläche freizuschalten.