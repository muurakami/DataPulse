import csv
from collections.abc import Iterator
from pathlib import Path


def iter_csv(path: Path) -> Iterator[dict[str, str]]:
    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")
    if not path.is_file():
        raise ValueError(f"Not a file: {path}")
    if path.suffix.lower() != ".csv":
        raise ValueError(f"Not a CSV file: {path}")
    if path.stat().st_size == 0:
        raise ValueError(f"Empty file: {path}")
    with open(path, newline="", encoding="utf-8") as file:
        yield from csv.DictReader(file)
