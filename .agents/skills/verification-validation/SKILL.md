---
name: verification-validation
description: Wähle geeignete Systemanforderungen aus, entwirf ein realistisches Testszenario und leite rückverfolgbare Testfälle aus Prüfkriterien ab. Nutze den Skill für die Verifikationsplanung nach Requirements Engineering und bei einem Validierungsauftrag für die Prüfung des beabsichtigten Gebrauchs.
---

# Verification & Validation

Erarbeite einen Testentwurf aus einem vorhandenen Anforderungsstand. Verifikation weist nach, ob das System festgelegte Anforderungen erfüllt. Validierung prüft anhand von Stakeholderbedarf, Zielgruppe und Einsatzkontext, ob das System für den beabsichtigten Gebrauch geeignet ist.

## Zusammenarbeit

- Lies das Briefing, das freigegebene Produktkonzept und die aktuelle Anforderungsdatei. Im Schulungsprojekt liegen Konzept und Anforderungen unter `Ergebnisse/<produkt-slug>/`. Lies einen vorhandenen Testentwurf, bevor du ihn änderst. Übernimm IDs, bestätigte Wortlaute und Freigabestatus. Ein Produktbeispiel aus Schulungsunterlagen dient zur Orientierung. Verwende den aktuellen Prüfgegenstand und seine Quellen für alle Testfälle.
- Zeige bei jeder Frage und Zwischenzusammenfassung **Anforderungsauswahl › Testszenario › Testfälle**. Markiere die aktuelle Phase im Chat mit eckigen Klammern und in HTML mit `aria-current="step"`. Besprich pro Karte genau eine Entscheidung. Eine Karte kann mehrere Anforderungen für dieselbe Auswahlentscheidung anbieten.
- Nutze bei verfügbarer Inline-Interaktion den Skill `visualize`. Biete zur Auswahl passende Optionen, zum Szenario und Testfall editierbare Felder und jeweils „Meine Aussage“ an. Erlaube reinen Freitext. Übergib Phase, betroffene IDs, Auswahl oder bearbeitete Fassung und Freitext gemeinsam als Chat-Folgenachricht. Zeige die Antwort zum Kopieren, wenn die Übergabe fehlt. Verwende ohne Widget nummerierte Optionen oder editierbare Textvorlagen im Chat.
- Arbeite bestätigte Entscheidungen und offene Punkte nach jeder Antwort in den Arbeitsstand ein. Lege eine geänderte Fassung erneut vor und wechsle die Phase bei Zustimmung oder auf Anweisung des Nutzers. Wenn der Nutzer Codex die Auswahl und Ableitung delegiert, bearbeite alle drei Phasen in einem Durchlauf und kennzeichne eigene Annahmen und offene Entscheidungen.

## 1 Anforderungsauswahl

- Wähle Anforderungen anhand des vereinbarten Umfangs, der Relevanz für das Nutzungsziel und der Prüfbarkeit mit verfügbaren oder konkret planbaren Mitteln. Begründe die Auswahl knapp pro SYS-ID. Ein bestätigt formulierter Sollsatz mit einzeln freigegebenem Prüfkriterium ist die bevorzugte Basis. Übernimm eine Einzelfreigabe auch bei noch ausstehender Gesamtfreigabe.
- Übernimm aus Requirements Engineering die drei Teile des Prüfkriteriums „Vorbereitung“, „Prüfhandlung“ und „Bestanden, wenn“. Halte unbestätigte Anforderungen, fehlende Kriterien und offene Auslöser oder Grenzwerte mit ihrer ID und der betroffenen Prüfung fest. Falls dafür Testfälle erwünscht oder für die Planung sinnvoll sind, kennzeichne sie als Entwürfe und benenne die Festlegung, die zur Durchführung oder Bewertung fehlt. Verwende Beispieldaten als solche. Leite Akzeptanzgrenzen aus belegten Festlegungen ab.

## 2 Testszenario

- Entwirf ein realistisches Szenario als gemeinsamen Rahmen für mehrere Fälle. Beschreibe Prüfling und Systemgrenze, Situation oder Ereignis, Ausgangszustand, beteiligte Akteure oder Schnittstellen sowie relevante System-, Eingabe- und Umgebungsparameter. Verknüpfe das Szenario mit den ausgewählten SYS-IDs und, soweit vorhanden, mit dem Nutzungsszenario. Kennzeichne Annahmen zur Verfügbarkeit von Prototyp, Prüfstand oder Simulation.
- Lege hier fest, unter welchen Bedingungen was geprüft werden soll. Konkrete Methoden, Schritte und Soll-Ergebnisse folgen pro Testfall. Gib dem Testszenario eine stabile ID `TS-…`.

## 3 Testfälle

- Lies die [Vorlage für den Testentwurf](references/testentwurf.md). Leite mehrere fachlich unterschiedliche Fälle aus dem Szenario ab, etwa für eine Ausgangslage und einen Zustandswechsel. Verwende Grenz- und Fehlerfälle, wenn vorgesehene Betriebsgrenzen oder bestätigte Anforderungen sie tragen. Mehrere Fälle dürfen dieselbe SYS-ID abdecken. Halte bei geteiltem Prüfkriterium fest, welchen Teil jeder Fall abdeckt und welche Fälle gemeinsam für den Nachweis erforderlich sind. Wenn die Quellen für weitere sinnvolle Fälle fehlen, dokumentiere die fehlende Grundlage.
- Dokumentiere pro `TF-…` die Anforderung mit ID und Wortlaut, das Testziel, die Testmethode, die konkrete Testumgebung, die Vorbedingungen und Testdaten, nummerierte Testschritte und das erwartete Ergebnis. Beschreibe die Methode durch passende Angaben zu Art, Technik und Ebene. Benenne in der Testumgebung den Aufbau, relevante Mess- oder Referenzmittel und ob ein physisches System, ein Prüfstand oder eine Simulation verwendet werden soll.
- Prüfe für jeden Fall die Kette SYS-ID → Prüfkriterium → Testszenario → Testfall → erwartetes Ergebnis. Das erwartete Ergebnis muss aus den Schritten beobachtbar oder messbar sein und die belegte Bestehensregel erhalten. Gib an, welche Beobachtung oder welcher Messwert später als Nachweis zu erfassen ist. Erfasse Ist-Ergebnis und Bewertung nach einer tatsächlichen Durchführung. Ein Auftrag zum Testentwurf umfasst die Planung. Führe Tests aus, wenn dies ebenfalls beauftragt ist und die Voraussetzungen vorliegen.

## Validierung bei entsprechendem Auftrag

Leite die Validierungsfrage aus Stakeholderbedarf und beabsichtigtem Gebrauch ab. Beschreibe Zielgruppe, repräsentative Nutzungssituation, Aufgabe, Beobachtung und belegtes Erfolgskriterium. Verknüpfe den Plan mit STK- und SZ-IDs sowie gegebenenfalls der Zielgruppe. Verwende `VAL-…` für Validierungsfälle und dokumentiere offene Erfolgskriterien. Eine Verifikationsprüfung kann Daten für die Validierung liefern, wenn ihr Aufbau die Validierungsfrage abdeckt.

## Übergabe

Speichere den Arbeitsstand neben dem Anforderungsstand als `Ergebnisse/<produkt-slug>/testfaelle.md` oder am vorgegebenen Zielort. Verwende im reinen Chat dieselbe Struktur. Dokumentiere Auswahl, Szenario, Fälle, Abdeckung und offene Punkte. Kennzeichne den Stand als Testentwurf und vermerke, für welche Fälle Voraussetzungen offen sind. Prüfe vor der Übergabe, ob jede ausgewählte Anforderung durch Fälle abgedeckt oder als Lücke ausgewiesen ist.
