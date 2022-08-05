import random
import csv
from datetime import date

from .solve_functions import normal_equation

def generate_random_base(von=0, bis=10_000) -> int:
    return random.randint(von, bis)

def generate_random_rate(von=0, bis=300) -> float:
    return random.randint(von, bis) / 100

def generate_random_dates(year: int):
    day = random.randint(1, 28)
    month = random.randint(1, 12)
    return sorted(date(year, month, day), date(year, month, day))

def generate_random_simple_tuple():
    base = generate_random_base()
    rate = generate_random_rate()
    fee = normal_equation(base, rate)
    return (base, rate, fee)

def generate_random_simple_tuples(size):
    result = [['base', 'rate', 'fee']]
    return result + [generate_random_simple_tuple() for _ in range(size)]

def generate_random_simple(outpath: str, size = int(1e5)):
    with open(outpath, 'w') as out_csv:
        csv_writer = csv.writer(out_csv, delimiter='\t')
        csv_writer.writerows(generate_random_simple_tuples(size))