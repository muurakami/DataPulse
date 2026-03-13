import argparse
from pathlib import Path

from csv_stats.parser import iter_csv
from csv_stats.stats import column_stats


def main() -> None:
    parser = argparse.ArgumentParser(description="CSV column statistics")
    parser.add_argument("file", type=Path, help="Path to the CSV file")
    args = parser.parse_args()

    rows = list(iter_csv(args.file))
    if not rows:
        print("Empty file")
        return

    columns = rows[0].keys()
    for column in columns:
        values = [row[column] for row in rows]
        stats = column_stats(values)
        if stats.avg is not None:
            print(f"{column}: min={stats.min}, max={stats.max}, avg={stats.avg:.2f}")
        else:
            print(f"{column}: no numeric data")


if __name__ == "__main__":
    main()
