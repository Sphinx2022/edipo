def normal_equation(base: int, rate: float, year_gap= 0) -> float:
    return base * (rate / 100) * (year_gap / 365)