def cluster(points, k=2):
    """Простейшая кластеризация: распределение точек по k группам."""
    return [i % k for i in range(len(points))]
