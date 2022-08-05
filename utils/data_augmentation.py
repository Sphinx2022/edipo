import random
from datetime import date

def generate_random_base(von = 0, bis = 10_000) -> int:
    return random.randint(von, bis)

def generate_random_rate(von = 0, bis = 300) -> float:
    return random.randint(von, bis) / 100

def generate_random_dates(year: int):
    day = random.randint(1, 28)
    date = random.randint(1, 12)
    return sorted(date(year, date, day), date(year, date, day))