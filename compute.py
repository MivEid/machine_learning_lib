def mean(values):
    """Среднее значение."""
    return sum(values) / len(values)

def median(values):
    s = sorted(values)
    return s[len(s) // 2]

def variance(values):
    m = mean(values)
    return sum((v - m) ** 2 for v in values) / len(values)
