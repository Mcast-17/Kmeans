def calcolo_distanza(point, centroid):
    """
    Calcola la distanza tra un punto e un centroide.
    Nel caso monodimensionale basta il valore assoluto.
    """

    return abs(point - centroid)


def assegna_clusters(data, centroids):
    """
    Assegna ogni punto al centroide più vicino.
    """

    clusters = [[] for _ in centroids]

    for point in data:

        distances = [
            calcolo_distanza(point, centroid)
            for centroid in centroids
        ]

        nearest_index = distances.index(min(distances))

        clusters[nearest_index].append(point)

    return clusters


def calcolo_centroide(cluster):
    """
    Calcola il nuovo centroide come media aritmetica.
    """

    if len(cluster) == 0:
        return 0

    return sum(cluster) / len(cluster)


def aggiornamento(clusters):
    """
    Aggiorna tutti i centroidi.
    """

    return [
        calcolo_centroide(cluster)
        for cluster in clusters
    ]


def convergenza(old_centroids, new_centroids):
    """
    Verifica se i centroidi sono cambiati.
    """

    return old_centroids == new_centroids
