import csv

def parseTsv(tsv_path: str) -> list(str):
    with open(tsv_path) as tsv_file:
        return csv.reader(tsv_file, delimiter='\t')