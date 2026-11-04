import matplotlib.pyplot as plt


def mostra_dataset(dataset):
    """
    Visualizza il dataset originale.
    """

    plt.figure(figsize=(10, 3))

    plt.scatter(
        dataset,
        [0] * len(dataset),
        color="blue"
    )

    plt.title("Dataset Originale")
    plt.xlabel("Valori")
    plt.yticks([])

    plt.grid(True)

    plt.show()


def mostra_cluster(clusters, centroidi):
    """
    Visualizza i cluster finali e i centroidi.
    """

    colori = [
        "red",
        "blue",
        "green",
        "orange"
    ]

    plt.figure(figsize=(12, 4))

    for indice, cluster in enumerate(clusters):

        plt.scatter(
            cluster,
            [indice] * len(cluster),
            color=colori[indice],
            label=f"Cluster {indice + 1}"
        )

    plt.scatter(
        centroidi,
        range(len(centroidi)),
        color="black",
        marker="X",
        s=200,
        label="Centroidi"
    )

    plt.title("Risultato K-Means")
    plt.xlabel("Valori")
    plt.ylabel("Cluster")

    plt.legend()
    plt.grid(True)

    # Salvataggio immagine
    plt.savefig(
        "clustering_finale.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.show()
