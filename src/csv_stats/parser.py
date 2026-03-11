import csv 
from pathlib import Path


def load_csv(path: Path) -> list[dict[str, str]]:
    with open(path, newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))