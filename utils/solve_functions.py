def normal_equation(base: int, rate: float, days_gap=365) -> float:
    return base * (rate / 100) * (days_gap / 365)
