---
name: requirements-engineering
description: Leite aus Stakeholderinterviews und einem Produktkonzept nachvollziehbare Stakeholderbedarfe und prüfbare Systemanforderungen ab. Nutze den Skill für frühes Requirements Engineering, die schrittweise Abstimmung mit Entwicklern und die Übergabe freigegebener Prüfkriterien an die Testfallentwicklung.
---

# Requirements Engineering

Erarbeite mit dem Nutzer einen prüfbaren Anforderungsstand. Analysiere die Quellen und bereite Vorschläge sowie ihre Verknüpfungen vor. Der Nutzer entscheidet über den Bedarf, den Anforderungswortlaut und die Freigabe einzelner Prüfkriterien. Übernimm bestätigte Produktentscheidungen, vorhandene IDs und ausdrücklich bestätigte Formulierungen.

## Zusammenarbeit

- Lies das Briefing, die Interviews, das freigegebene Produktkonzept und den vorhandenen Anforderungsstand. Im Schulungsprojekt liegen die Interviews unter `Stakeholder Interviews/` und das Konzept unter `Ergebnisse/<produkt-slug>/produktkonzept.md`. Frage vorab nur bei unklarem Produktgegenstand oder fehlender Grundlage für einen sinnvollen Einstieg.
- Arbeite nach dem Dialogmuster von Product Ideation. Pro Karte steht genau ein Bedarf, eine Systemanforderung oder ein Prüfkriterium mit genau einer Entscheidungsfrage im Fokus. Bereite weitere Befunde im Hintergrund vor. Beginne mit dem wichtigsten offenen Punkt.
- Zeige vor jeder Frage und Zwischenzusammenfassung die Phasen **Stakeholderbedarfe › Systemanforderungen › Prüfkriterien und Freigabe**. Hebe die aktive Phase sichtbar hervor und kennzeichne sie in HTML mit `aria-current="step"`. Verwende in der Textfassung eckige Klammern um die aktive Phase.
- Nutze bei verfügbarem interaktivem Chat den Skill `visualize`. Zeige Kontext und Entscheidungsfrage mit passenden Auswahlmöglichkeiten und dem Feld „Meine Aussage“. Erlaube eine reine Freitextantwort. Übergib die ID, die gewählte oder bearbeitete Fassung und den Freitext gemeinsam über die Chat-Folgenachricht. Fehlt die Übergabe, zeige dieselbe Antwort zum Kopieren. Ohne Inline-Widget nutze das native Frageformular oder nummerierte Optionen mit Freitext im Chat.
- Biete „Später entscheiden“ und sinngleiche Aufschuboptionen niemals an. Dokumentiere vom Nutzer offen gelassene Fragen sowie unbelegte Werte oder Auslöser mit betroffener ID. Wenn der Nutzer eine Phase abschließt oder aus Zeitgründen Punkte überspringt, setze an der gewünschten Stelle fort. Übersprungene Punkte behalten ihren Entwurfsstatus.
- Arbeite nach jeder Antwort die bestätigte Fassung und die offenen Punkte in den Arbeitsstand ein. Bei einem Änderungswunsch lege die überarbeitete Fassung erneut vor. Hole die Zustimmung zum Phasenwechsel ein, sofern der Nutzer ihn noch nicht selbst angeordnet hat. Bei ausdrücklich delegierter Bearbeitung liefere begründete Vorschläge ohne Bestätigungsschleife und dokumentiere offene Entscheidungen als solche.

## 1 Stakeholderbedarfe

Erfasse die relevanten Bedarfe aus den verfügbaren Quellen. Bündele verwandte Aussagen, sofern die Unterschiede zwischen Rollen sichtbar bleiben. Der freigegebene Funktionsumfang bestimmt, welche Bedarfe unmittelbar in Systemanforderungen einfließen. Halte weitere Bedarfe und Umfangskonflikte nachvollziehbar fest.

Zeige pro Bedarf diese vier Punkte in der angegebenen Reihenfolge.

1. **Quelldatei** mit Rolle und konkreter Fundstelle, etwa Abschnitt oder Anfang des Interviewabsatzes.
2. **Zitat** mit dem wörtlichen Ausschnitt, auf den sich die Ableitung stützt.
3. **Übertragung auf das Produkt** als konkreter Bedarf in Alltagssprache aus Sicht der Rolle. Kennzeichne die Übertragung aus einem anderen Produktkontext als Transferannahme. Im Schulungsfall NapoliOne stammen die Interviews aus dem Grillkontext.
4. **Deine Entscheidung** mit einer konkreten Frage zur Aufnahme oder Formulierung des Bedarfs und „Meine Aussage“.

Zeige die Systemanforderung und das Prüfkriterium erst in ihrer jeweiligen Phase.

## 2 Systemanforderungen

Verknüpfe jede Systemanforderung mit bestätigten Stakeholder-IDs oder einer direkten, belegten Konzeptvorgabe. Ergänze einschlägige Szenario- und Funktions-IDs. Formuliere pro Anforderung eine beobachtbare Aussage über das System als Black Box. Übernimm technische Lösungen, wenn sie vorgegeben oder bestätigt sind. Formuliere nicht-funktionale Anforderungen anhand der relevanten Qualitätsmerkmale, Betriebsbedingungen, Messgrößen, Einheiten oder Grenzwerte.

Zeige pro Anforderung Quelldatei und Fundstelle, den einschlägigen Beleg, die Übertragung als Anforderungsvorschlag und eine Entscheidung zu genau dieser Fassung. Verwende für funktionale Anforderungen die [editierbare Satzschablone](assets/satzschablone.fragment.html). Kopiere sie an den Ort für Inline-Visualisierungen und ersetze die Beispieldaten im JSON-Block durch die Daten der aktuellen SYS-ID. Serialisiere Quelltext als JSON und kodiere `<` im JSON-Block als `\u003c`. Nutze für nicht-funktionale Anforderungen passende editierbare Felder für Qualitätsmerkmal, Betriebsbedingung und belegten Messwert oder Grenzwert.

- Die funktionale Satzschablone enthält Bedingung, Verbindlichkeit, System oder Element, Art der Funktionalität, Objekt mit Ergänzung und Prozesswort. Stelle die Live-Vorschau des ganzen Satzes über die Eingabefelder. Unterstütze die direkte Systemfunktion sowie bei fachlichem Bedarf „fähig sein“ und „einem Akteur die Möglichkeit bieten“.
- Biete die Verbindlichkeit als Dropdown an. Geschlossen zeigt es nur das ausgewählte Wort. In der geöffneten Liste stehen die Erläuterungen, etwa „muss · verbindlich“ und „soll · vorgegeben“. Die Live-Vorschau und die übergebene Fassung enthalten nur das Wort.
- Frage, ob der Nutzer die angezeigte, gegebenenfalls bearbeitete Fassung übernimmt. Der Nutzer kann zusätzlich einen Änderungswunsch formulieren. Ohne Widget zeige die Satzbausteine getrennt und bitte um den vollständigen Satz oder die zu ändernden Bausteine.

## 3 Prüfkriterien und Freigabe

Leite ein Prüfkriterium aus genau einer Systemanforderung ab. Zeige ihre ID und ihren bestätigten Wortlaut über drei editierbaren Feldern.

| Feld | Inhalt |
| --- | --- |
| Vorbereitung | Ausgangszustand, benötigte Daten und gegebenenfalls Betriebsbedingungen |
| Prüfhandlung | Eingabe, Ereignis oder Handlung, die das geforderte Verhalten auslöst |
| Bestanden, wenn | Beobachtbares Ergebnis oder Messgröße mit belegter Einheit, Grenze oder Toleranz |

Wenn ein Auslöser oder Grenzwert offen ist, nenne den fehlenden Parameter und die abhängige Prüfung. Eine Freigabe der Formulierung ersetzt diese Festlegung nicht. Prüfe die Rückverfolgbarkeit vom Quellbeleg über die Systemanforderung bis zum erwarteten Ergebnis.

Frage nach der Freigabe der angezeigten Fassung für genau diese SYS-ID. Biete „Prüfkriterium freigeben“ sowie „Änderungswunsch senden“ mit dem Feld „Meine Aussage“ an. Übergib alle drei Felder zusammen mit Entscheidung und Freitext. Dokumentiere eine ausdrückliche Einzelfreigabe beim betreffenden Prüfkriterium. Halte die Freigabe des gesamten Anforderungsstands als eigene Entscheidung fest. Prüfergebnisse gehören in die spätere Testdurchführung.

## Ergebnis

Speichere den Arbeitsstand neben dem Produktkonzept unter `Ergebnisse/<produkt-slug>/anforderungen.md` oder am vorgegebenen Zielort. Gib im reinen Chat dieselbe Struktur aus.

| Stakeholder-ID | Rolle | Stakeholderanforderung | Quelle und Einordnung |
| --- | --- | --- | --- |
| STK-01 | Rolle aus dem Interview | Bedarf aus Stakeholder-Sicht | Fundstelle, gegebenenfalls Transferannahme und Bestätigung |

| System-ID | Typ | Systemanforderung | Herkunft | Prüfkriterium |
| --- | --- | --- | --- | --- |
| SYS-01 | Funktional oder nicht-funktional | Beobachtbare oder messbare Aussage | STK-ID oder Konzeptfundstelle, gegebenenfalls bestätigter Wortlaut | Vorbereitung, Prüfhandlung, erwartetes Ergebnis und Freigabestatus |

Vergib stabile IDs. Führe unter **Offene Punkte** die betroffenen IDs, die fehlenden Festlegungen und relevante Bedarfe außerhalb des Umfangs auf. Unterscheide bestätigte Wortlaute, freigegebene Einzelkriterien und den Status des Gesamtstands.
