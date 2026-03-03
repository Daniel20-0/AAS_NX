# 📚 Mein Markdown Cheat-Sheet

Dieses Dokument dient als Vorlage und Nachschlagewerk für alle wichtigen Markdown-Befehle.

---

## 1. Überschriften (Gliederung)
# Überschrift Ebene 1 (Haupttitel)
## Überschrift Ebene 2 (Kapitel)
### Überschrift Ebene 3 (Unterkapitel)
#### Überschrift Ebene 4
##### Überschrift Ebene 5
###### Überschrift Ebene 6

---

## 2. Textformatierung
So machst du Text **fett** (zwei Sternchen).
So machst du Text *kursiv* (ein Sternchen).
So machst du Text ***fett und kursiv*** (drei Sternchen).
So machst du Text ~~durchgestrichen~~ (zwei Tilden).

Ein Zeilenumbruch ohne neuen Absatz entsteht,  
wenn du zwei Leerzeichen ans Ende der Zeile setzt.

Ein neuer Absatz entsteht, wenn du eine komplette Zeile frei lässt.

---

## 3. Listen und Aufzählungen

**Unsortierte Liste (Punkte):**
- Erster Punkt
- Zweiter Punkt
  - Eingerückter Unterpunkt (mit Leerzeichen oder Tab davor)
  - Noch ein Unterpunkt
- Dritter Punkt

**Sortierte Liste (Zahlen):**
1. Erster Schritt
2. Zweiter Schritt
   1. Unter-Schritt (einrücken)
   2. Noch ein Unter-Schritt
3. Dritter Schritt

**Checkliste (Aufgaben):**
- [x] Diese Aufgabe ist erledigt.
- [ ] Diese Aufgabe ist noch offen.
- [ ] Noch eine offene Aufgabe.

---

## 4. Links und Bilder

**Links (Verweise):**
[Klicke hier, um zu Google zu gelangen](https://www.google.de)

**Bilder einfügen:**
![Beschreibung des Bildes](https://via.placeholder.com/150)
*Tipp: Statt des Links kannst du auch den lokalen Dateinamen (z.B. bild.png) eintragen, wenn das Bild im selben Ordner liegt.*

---

## 5. Zitate (Blockquotes)
Wenn du Text hervorheben oder zitieren möchtest:

> Das ist ein wichtiges Zitat.
> Es kann auch über mehrere Zeilen gehen.
>> Und man kann Zitate sogar verschachteln!

---

## 6. Code und technische Begriffe

**Code im Text (Inline):**
Um einen Befehl wie `Strg + C` oder `print("Hallo")` im Fließtext hervorzuheben, nutzt du einfache Backticks (Gravis-Zeichen).

**Code-Blöcke (Mehrzeilig):**
Für längere Code-Schnipsel nutzt du drei Backticks. Du kannst sogar die Programmiersprache dahinter schreiben, um den Code bunt zu machen (Syntax-Highlighting):

```python
def begruessung(name):
    print("Hallo, " + name + "!")