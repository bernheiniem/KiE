# Vorlage für den Testentwurf

## Anforderungsauswahl

| System-ID und bestätigter Wortlaut | Prüfkriterium und Freigabestand | Auswahlgrund oder offene Festlegung |
| --- | --- | --- |
| SYS-… | Fundstelle, relevante Bestehensregel, Freigabestatus | Nutzungsrelevanz und Prüfbarkeit oder Grund für die vorläufige Auslassung |

## Testszenario TS-…

- **Bezug** Systemanforderungen und gegebenenfalls Nutzungsszenario.
- **Prüfgegenstand** System, Subsystem oder Prototyp mit relevantem Versions- und Konfigurationsstand.
- **Situation** Ausgangszustand, auslösendes Ereignis und Beteiligte beziehungsweise Schnittstellen.
- **Parameter** Relevante Systemzustände, Eingaben, Umgebungsbedingungen und Annahmen für die Fallvarianten.

## Testfall TF-…

| Feld | Inhalt |
| --- | --- |
| Anforderung | SYS-ID, Wortlaut, Bezug zum freigegebenen Prüfkriterium und TS-ID. |
| Testziel | Nachweis, den dieser Fall erbringt. Bei Teilabdeckung den geprüften Aspekt benennen. |
| Testmethode | Art, Technik und Ebene, soweit relevant. |
| Testumgebung | Geplanter Versuchsaufbau, Prüfling, Konfiguration, Einsatzbedingungen und benötigte Mess- oder Referenzmittel. |
| Vorbedingungen und Testdaten | Startzustand, fallbezogene Parameter und Eingabedaten. Belegte Festlegungen sowie beispielhafte Werte und offene Voraussetzungen kenntlich machen. |
| Testschritte | Nummerierte Handlungen vom Herstellen des Startzustands bis zur Beobachtung und Erfassung. |
| Erwartetes Ergebnis | Beobachtete Größe oder Verhalten mit eindeutiger Bestehensregel. Belegte Einheit, Grenze oder Toleranz übernehmen. |
| Nachweis und Status | Später zu erfassende Beobachtungen, Messdaten oder Protokolle. Im Entwurf Durchführung und Bewertung als ausstehend führen. |

## Abdeckung und offene Punkte

| System-ID | Testfälle und Teilabdeckung | Offene Festlegungen oder fehlende Abdeckung |
| --- | --- | --- |
| SYS-… | TF-… | Benötigter Parameter, betroffener Testfall und Auswirkung auf Durchführung oder Bewertung. |

Wenn eine Validierung beauftragt ist, ergänze je VAL-ID Zielgruppe, STK- und SZ-Bezug, Nutzungsaufgabe, repräsentative Bedingungen, zu erfassende Beobachtung und belegtes Erfolgskriterium.
