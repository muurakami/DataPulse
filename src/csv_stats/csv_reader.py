import csv
import io
from collections.abc import Iterator
from pathlib import Path
from types import TracebackType


class CSVReader:
    def __init__(self, path: str | Path) -> None:
        self.path = path
        self.file: io.TextIOWrapper | None = None
        self.reader: csv.DictReader[str] | None = None

    def __enter__(self) -> "CSVReader":
        self.file = open(self.path, newline="", encoding="utf-8")
        self.reader = csv.DictReader(self.file)
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        if self.file is not None:
            self.file.close()

    def __iter__(self) -> Iterator[dict[str, str]]:
        if self.reader is None:
            raise RuntimeError("CSVReader not initialized")
        yield from self.reader


path = Path("data/sample.csv")

with CSVReader(path) as reader:
    for row in reader:
        print(row)
