def classify(x, threshold=0.5):
    """Простой бинарный классификатор по порогу"""
    return 1 if x >= threshold else 0
