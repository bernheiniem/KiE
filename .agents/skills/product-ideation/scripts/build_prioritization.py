import argparse
import hashlib
import html
import json
from pathlib import Path
import re


CRITERIA = ("benefit", "fit", "effort")
DEFAULT_WEIGHTS = {"benefit": 50, "fit": 25, "effort": 25}
ASSETS = Path(__file__).resolve().parent.parent / "assets"
DATA_MARKER = "__IDEATION_DATA__"


def validate(data):
    if not isinstance(data, dict):
        raise ValueError("Die Eingabe muss ein JSON-Objekt sein.")

    context = data.get("context", "")
    if not isinstance(context, str) or len(context) > 180:
        raise ValueError("Der Kontext muss aus höchstens 180 Zeichen bestehen.")

    weights = data.get("weights", DEFAULT_WEIGHTS)
    if (
        not isinstance(weights, dict)
        or set(weights) != set(CRITERIA)
        or any(type(value) is not int or not 0 <= value <= 100 for value in weights.values())
        or sum(weights.values()) != 100
    ):
        raise ValueError("Die drei Gewichte müssen ganze Zahlen sein und zusammen 100 ergeben.")

    features = data.get("features")
    if not isinstance(features, list) or not 1 <= len(features) <= 50:
        raise ValueError("Es werden 1 bis 50 Funktionen benötigt.")

    validated_features = []
    seen_ids = set()
    for position, feature in enumerate(features, 1):
        if not isinstance(feature, dict):
            raise ValueError(f"Funktion {position}: JSON-Objekt erwartet.")
        feature_id = feature.get("id")
        if not isinstance(feature_id, str) or not re.fullmatch(r"F-[A-Za-z0-9-]{1,28}", feature_id):
            raise ValueError(f"Funktion {position}: ungültige Funktions-ID.")
        if feature_id in seen_ids:
            raise ValueError(f"Funktions-ID {feature_id} ist doppelt vergeben.")
        seen_ids.add(feature_id)

        name = feature.get("name")
        blocker = feature.get("blocker", "")
        if not isinstance(name, str) or not name.strip() or len(name) > 180:
            raise ValueError(f"{feature_id}: Name mit 1 bis 180 Zeichen erwartet.")
        if not isinstance(blocker, str) or len(blocker) > 300:
            raise ValueError(f"{feature_id}: Sperrgrund mit maximal 300 Zeichen erwartet.")

        ratings = {criterion: feature.get(criterion) for criterion in CRITERIA}
        for criterion, value in ratings.items():
            if value is not None and (type(value) is not int or not 1 <= value <= 5):
                raise ValueError(f"{feature_id}: {criterion} muss leer oder eine ganze Zahl von 1 bis 5 sein.")
        validated_features.append({
            "id": feature_id,
            "name": name.strip(),
            "blocker": blocker.strip(),
            "ratings": ratings,
        })

    return {"context": context.strip(), "weights": weights, "features": validated_features}


def build(data, standalone):
    canonical_data = json.dumps(data, ensure_ascii=True, sort_keys=True, separators=(",", ":"))
    session = hashlib.sha256(canonical_data.encode("ascii")).hexdigest()[:16]
    payload = json.dumps({"session": session, **data}, ensure_ascii=True, separators=(",", ":"))
    payload = payload.replace("<", r"\u003c").replace(">", r"\u003e").replace("&", r"\u0026")
    fragment = (ASSETS / "prioritization.fragment.html").read_text(encoding="utf-8")
    output = fragment.replace(DATA_MARKER, payload, 1)
    if standalone:
        wrapper = (ASSETS / "prioritization.standalone.html").read_text(encoding="utf-8")
        output = wrapper.replace("__IDEATION_FRAGMENT__", output, 1)
    return session, output


def main():
    parser = argparse.ArgumentParser(description="Erzeugt eine interaktive Funktionspriorisierung.")
    parser.add_argument("input", type=Path, help="JSON mit Funktionskandidaten")
    parser.add_argument("output", type=Path, help="Zielpfad für das HTML")
    parser.add_argument("--standalone", action="store_true", help="Vollständiges Browser-Dokument erzeugen")
    args = parser.parse_args()
    if args.input.resolve() == args.output.resolve():
        parser.error("Eingabe und Ausgabe müssen verschiedene Dateien sein.")
    try:
        data = validate(json.loads(args.input.read_text(encoding="utf-8-sig")))
        session, output = build(data, args.standalone)
        args.output.write_text(output, encoding="utf-8")
    except (OSError, ValueError) as error:
        parser.error(str(error))
    print(f"Bewertungssitzung: {session}")


if __name__ == "__main__":
    main()
