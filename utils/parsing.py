from datetime import datetime


def parse_float(value: str) -> float:
    return float(value.replace(',', '.'))

def parse_int(value: str) -> int:
    return int(value)

def parse_date(value: str) -> datetime:
    day, date, year =  value.split('/')
    return datetime(int(year), int(date), int(day))

def get_gap(date1: datetime, date2: datetime) -> int:
    return (date1 - date2).days