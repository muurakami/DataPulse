import csv


class CSVReader:
    def __init__(self, path):
        self.path = path
        self.file = None
        self.reader = None

    def __enter__(self):
        self.file = open(self.path, newline="", encoding="utf-8")
        self.reader = csv.DictReader(self.file)
        return self.reader

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()


path = "csv-stats/data/sample.csv"

with CSVReader(path) as reader:
    for row in reader:
        print(row)
