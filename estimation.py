def mse(y_true, y_pred):
    """Среднеквадратичная ошибка."""
    return sum((a - b) ** 2 for a, b in zip(y_true, y_pred)) / len(y_true)
