# Funktionen bewerten und priorisieren

Bewerte die abgestimmte Auswahlliste. Halte verbindliche Einschränkungen und ungeklärte Voraussetzungen gesondert fest. Eine Idee mit bestätigtem Ausschluss oder einer blockierenden Voraussetzung bleibt bis zur Klärung außerhalb der Rangfolge. Zwingend notwendige Komponenten werden mit Begründung im Umfang geführt, auch wenn ihr eigener Punktwert niedrig ist.

## Kriterien und Bewertungsmatrix

| Kriterium | 1 | 3 | 5 | Standardgewicht |
|---|---|---|---|---:|
| Nutzwert | Kaum Verbesserung im Szenario | Spürbare Verbesserung | Löst eine entscheidende Hürde | 50 % |
| Zielpassung | Geringer Beitrag zum abgestimmten Produktziel | Trägt zu einem Teilziel bei | Stützt Produktversprechen und Fokus direkt | 25 % |
| Aufwand | Geringer Aufwand und bekannte Umsetzung | Mittlerer Aufwand oder einzelne offene Fragen | Hoher Aufwand oder grundlegende Umsetzungshürden | 25 % |

Verwende ganze Werte von 1 bis 5. Für andere Gewichte vereinbare ganze Prozentwerte, die zusammen 100 ergeben. Der Punktwert auf der Skala 0–100 ist `(w_N × (N−1) + w_Z × (Z−1) + w_A × (5−A)) / 4`. Fehlende Kriterien mit positivem Gewicht bleiben offen. Kriterien mit Gewicht 0 sind optional. Gleiche Ergebnisse teilen sich einen Rang. Dokumentiere die Evidenz für die Bewertungen getrennt von der Zahl.

| Funktions-ID | Nutzwert (1–5) | Zielpassung (1–5) | Aufwand (1–5) | Punkte | Begründung oder Sperrgrund | Entscheidung |
|---|---:|---:|---:|---:|---|---|
| F-… | […] | […] | […] | […] | [Grundlage, Annahme oder Sperre] | [Erster Umfang, später, verworfen oder Klärung nötig] |

## Interaktive Bewertung im Chat oder Browser

Erstelle aus der aktuellen Auswahlliste eine temporäre JSON-Eingabe. Verwende die echten Funktions-IDs. Lass unbewertete Felder weg oder setze sie auf `null`. Verwende Zahlen als Ausgangswerte, wenn sie bereits besprochen wurden oder der Nutzer ausdrücklich einen Bewertungsvorschlag möchte. Weise im Chat auf Schätzungen hin. `blocker` ist optional und enthält einen vereinbarten Sperrgrund. Übernimm in den Bewertungsdialog nur Informationen, die der Nutzer dort sehen soll.

```json
{
  "context": "Werkstattreservierung – Konzept A",
  "weights": { "benefit": 50, "fit": 25, "effort": 25 },
  "features": [
    { "id": "F-01", "name": "Gruppenreservierung", "benefit": null, "fit": null, "effort": null },
    { "id": "F-02", "name": "Automatischer Gerätewechsel", "blocker": "Kompatibilität ungeklärt" }
  ]
}
```

Setze `context` auf eine eindeutige Produkt- oder Variantenbezeichnung, damit Rückgaben zugeordnet werden können. Führe aus dem Skill-Ordner mit einem verfügbaren Python 3 aus:

```text
python scripts/build_prioritization.py <eingabe.json> <ausgabe.html>
```

Für die Inline-Ansicht im Codex-Chat schreibe das Fragment in ein beschreibbares Visualisierungsverzeichnis. Wähle pro Bewertung einen eindeutigen Dateinamen. Zeige es im aktuellen Antwortturn auf einer eigenen Zeile an: `visualize{"path":"<absoluter Pfad zur erzeugten .html>"}`. Falls der Client diese Darstellung nicht unterstützt, erzeuge mit `--standalone` eine lokal im Browser öffnbare HTML-Datei und verlinke sie. Wenn keine interaktive Ausgabe möglich ist, verwende die Markdown-Matrix. Bei mehr als 50 Kandidaten stimme eine kleinere Auswahlliste ab oder verwende die Matrix.

Bei mehreren Kandidaten wählt die Person die zu bearbeitende Funktion durch Klick auf ihre Zeile in der Rangliste. Die Liste zeigt Gesamtpunkte und die drei Einzelwerte je Kandidat und aktualisiert sich direkt. Ein einzelner Kandidat wird direkt mit seinen Bewertungskriterien und dem Gesamtwert angezeigt. Die Schaltfläche zur Übergabe sendet den Zwischenstand mit `session`, `weights` und `ratings` als Chat-Folgenachricht, wenn der Client den Kanal unterstützt. Ansonsten kann die Person den angezeigten JSON-Stand kopieren und im Chat senden. Das Widget selbst speichert keine Projektdateien.

Gleiche bei der Rückgabe die Sitzungs-ID mit der aus der Generierung und die IDs und Gewichte mit der aktuellen Auswahlliste ab. Verwende nur gültige Bewertungen dieser Auswahl. Berechne Rangfolge und Punkte erneut und frage nach Ausschlägen, Abhängigkeiten oder Zielkonflikten, die die Auswahl tatsächlich verändern. Übernimm die Entscheidung zum ersten Umfang in den Konzeptentwurf. Eine Zwischenbewertung kann bewusst unvollständig bleiben.
