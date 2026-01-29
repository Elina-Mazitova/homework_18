import json
from pathlib import Path


def load_schema(name: str):
    schema_path = Path(__file__).parent.parent / "schemas" / name
    with open(schema_path, encoding="utf-8") as file:
        return json.load(file)
