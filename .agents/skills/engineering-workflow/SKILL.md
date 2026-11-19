---
name: engineering-workflow
description: Führe den delegierten Engineering-Workflow für NapoliOne aus. Verknüpfe Produktideation, Requirements Engineering und Verifikations- und Validierungsplanung und dokumentiere Übergaben, Annahmen, offene Entscheidungen und menschliche Kontrollpunkte.
---

# Engineering Workflow

Nutze diesen Skill für den zusammenhängenden NapoliOne-Durchlauf. Wende die drei Fachskills in der angegebenen Reihenfolge im selben Auftrag an und lies ihre Anleitungen und jeweils einschlägigen Vorlagen. Ein Aufruf des Gesamtworkflows delegiert die fachliche Entwurfsarbeit an Codex. Verwende den delegierten Modus der Fachskills und führe Routineentscheidungen und Phasenwechsel ohne Einzelabfragen aus. Beachte ausdrücklich gesetzte Prüfumfänge, Freigabepunkte und Abbruchbedingungen des Nutzers.

## Einstieg

Lies im Projektordner `Briefing.pdf`, die vorhandenen Interviews unter `Stakeholder Interviews/` und vorhandene Ergebnisdateien unter `Ergebnisse/napolione/`. Die Interviews beziehen sich auf Grillprodukte. Markiere Schlussfolgerungen für den Pizzaofen als Transferannahmen und nenne die Fundstellen.

Arbeite auf dem vorhandenen Stand weiter. Übernimm gültige IDs, bestätigte Wortlaute, Umfangsentscheidungen und Freigaben. Weise Widersprüche mit Fundstelle und betroffenen IDs aus. Falls eine bestätigte Fassung geändert werden müsste, halte den Änderungsvorschlag und seine Auswirkungen gesondert zur Entscheidung fest. Neue Ableitungen und vorläufige Entscheidungen von Codex bleiben Entwürfe.

## Reihenfolge und Übergaben

1. **Ideation.** Lies und nutze [Product Ideation](../product-ideation/SKILL.md). Verwende Briefing, Interviews und bestehende Entscheidungen. Arbeite Zielgruppen, Nutzungsszenarien, Funktionsideen, Priorisierung und ersten Funktionsumfang aus oder prüfe den einschlägigen vorhandenen Stand. Speichere in `Ergebnisse/napolione/produktkonzept.md`. Übergib Zielgruppen-, Szenario- und Funktions-IDs, Quellen, Umfang, Status und offene Konzeptannahmen an Schritt 2.
2. **Anforderungsmanagement.** Lies und nutze [Requirements Engineering](../requirements-engineering/SKILL.md). Verwende den eben gespeicherten Konzeptstand, die Interviewbelege und den vorhandenen Anforderungsstand. Leite Stakeholderbedarfe, Systemanforderungen und die jeweils belegbaren Prüfkriterien mit Vorbereitung, Prüfhandlung und Bestehensregel ab. Ein Konzeptentwurf kann vorläufig als Grundlage dienen. Vermerke diesen Status an den davon abhängigen Ableitungen. Speichere in `Ergebnisse/napolione/anforderungen.md`. Übergib STK- und SYS-IDs, Anforderungswortlaute, Prüfkriterien und ihren jeweiligen Freigabestatus sowie fehlende Auslöser oder Grenzwerte an Schritt 3.
3. **Verifikation & Validierung.** Lies und nutze [Verification & Validation](../verification-validation/SKILL.md). Verwende das aktuelle Konzept, den eben gespeicherten Anforderungsstand und den vorhandenen Testentwurf. Wähle geeignete SYS-IDs aus, beschreibe Testszenarien und leite rückverfolgbare Testfälle mit beobachtbaren Soll-Ergebnissen ab. Einzeln freigegebene Prüfkriterien gelten auch bei ausstehender Gesamtfreigabe. Fälle auf vorläufiger Grundlage bleiben Testentwürfe. Fehlt eine Grundlage für die Bewertung, benenne die Lücke und die betroffene Prüfung. Der vollständige Durchlauf umfasst auch die Planung der Validierung des beabsichtigten Gebrauchs, soweit der Nutzer den Umfang nicht einschränkt. Leite dazu mindestens eine Validierungsfrage aus Zielgruppe, Nutzungsszenario und zugehörigem Stakeholderbedarf ab und dokumentiere offene Erfolgskriterien. Speichere in `Ergebnisse/napolione/testfaelle.md`. Eine tatsächliche Testdurchführung erfordert einen entsprechenden Auftrag und die nötigen Voraussetzungen.

Verwende bei abweichenden Zielorten die Vorgaben des Nutzers und dieselben Übergabedaten. Arbeite mit dokumentierten Annahmen weiter, wenn sie einen sinnvollen Entwurf ermöglichen. Wenn ein fehlender Input einen Teil fachlich blockiert, dokumentiere die abhängigen IDs und bearbeite die übrigen Teile. Frage gezielt nach, wenn die Antwort für weiteren sinnvollen Fortschritt nötig ist oder ein ausdrücklich gesetzter Kontrollpunkt erreicht ist.

## Kontrollpunkte und Abschluss

Dokumentiere Annahmen und offene Entscheidungen in der jeweils betroffenen Ergebnisdatei mit Quelle oder Begründung, betroffenen IDs und Auswirkung auf die Folgephase. Fasse im Abschnitt **Workflow-Übergabe** in `testfaelle.md` zusammen, was Codex selbstständig entschieden hat, welche Informationen fehlen und welche Widersprüche oder Abdeckungslücken aufgefallen sind. Liste die menschlichen Kontrollpunkte mit betroffenen IDs, anstehender Entscheidung und Zeitpunkt, etwa:

- **Vor Freigabe des Produktumfangs:** Übertragung zentraler Interviewbefunde auf die Zielgruppe und Priorisierung prüfen.
- **Vor Anforderungsfreigabe:** offene Anforderungen, Auslöser, Grenzwerte und Prüfkriterien fachlich entscheiden. Einzelfreigaben und Gesamtfreigabe eigens ausweisen.
- **Vor Verifikation oder Validierung am realen Produkt:** Prüfling, Messaufbau oder repräsentative Nutzungsaufgabe und anwendbare Bestehensregeln bestätigen.

Führe diese Punkte als dokumentierte Entscheidungen beziehungsweise als ausstehende Prüfungen. Während eines delegierten Entwurfs wartet Codex nur an ausdrücklich gesetzten Kontrollpunkten oder bei einer blockierenden Unklarheit.

Prüfe vor der Übergabe die Kette von Quelle, Zielgruppe, Szenario und Funktion über Bedarf oder belegte Konzeptvorgabe und Systemanforderung bis zu Prüfkriterium, Testszenario und Testfall. Prüfe, ob Verweise aufgelöst werden, Freigaben korrekt fortgeführt sind und jede ausgewählte Anforderung durch Fälle abgedeckt oder als Lücke ausgewiesen ist. Nenne im Chat die Ergebnisdateien, ihren Stand und die wichtigsten verbleibenden Entscheidungen.
