from dataset import DATASET, INITIAL_CENTROIDS

from kmeans import (
    assegna_clusters,
    aggiornamento,
    convergenza
)

from plot import (
    mostra_dataset,
    mostra_cluster
)

# Visualizzazione dataset iniziale
mostra_dataset(DATASET)

centroids = INITIAL_CENTROIDS

iterazione = 1

while True:

    print(f"\n===== ITERAZIONE {iterazione} =====")

    clusters = assegna_clusters(
        DATASET,
        centroids
    )

    new_centroids = aggiornamento(
        clusters
    )

    print("\nCluster:")
    print(clusters)

    print("\nCentroidi:")
    print(new_centroids)

    if convergenza(
        centroids,
        new_centroids
    ):
        print("\nAlgoritmo convergente.")

        mostra_cluster(
            clusters,
            new_centroids
        )

        break

    centroids = new_centroids

    iterazione += 1
