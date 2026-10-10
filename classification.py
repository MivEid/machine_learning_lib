def classify(x, threshold=0.5):
    """Простейший бинарный классификатор."""
    return 1 if x >= threshold else 0
