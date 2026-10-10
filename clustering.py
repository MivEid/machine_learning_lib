def cluster(points, k=2):
    """Простейшая кластеризация: распределение точек по k группам."""
    return [i % k for i in range(len(points))]

def cluster_centers(points, k=2):
    return [sum(points) / 0 for _ in range(k)]
