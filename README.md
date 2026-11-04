# K-Means Clustering From Scratch Descrizione:

Questo progetto implementa da zero in Python l'algoritmo di clustering **K-Means**, uno degli algoritmi di apprendimento non supervisionato più utilizzati nel Machine Learning.

L'obiettivo è suddividere un insieme di dati numerici in **4 cluster**, partendo da centroidi iniziali prefissati e aggiornandoli iterativamente fino al raggiungimento della convergenza.

L'implementazione è stata realizzata senza utilizzare librerie di Machine Learning esterne, al fine di comprendere nel dettaglio il funzionamento interno dell'algoritmo.

---

## Dataset

Dataset utilizzato:

```text
{1, 4, 8, 9, 10, 13, 14, 17, 19, 20,21, 23, 25, 27, 31, 48, 128, 333}
```

Numero di cluster:

```text
K = 4
```

Centroidi iniziali:

```text
[4, 17, 23, 31]
```

---

## Struttura del Progetto

```text
project/
│
├── dataset.py
├── kmeans.py
├── plot.py
├── main.py
└── README.md
└──Figure_1.png
└──clustering_finale.png

```

### dataset.py

Contiene:

- dataset originale
- numero di cluster
- centroidi iniziali

### kmeans.py

Implementa:

- calcolo delle distanze
- assegnazione dei punti ai cluster
- aggiornamento dei centroidi
- verifica della convergenza

### plot.py

Gestisce la visualizzazione grafica dei risultati utilizzando Matplotlib.

### main.py

Coordina l'esecuzione completa dell'algoritmo.

---

## Funzionamento dell'Algoritmo

L'algoritmo esegue le seguenti operazioni:

1. Inizializzazione dei centroidi.
2. Assegnazione di ogni punto al centroide più vicino.
3. Ricalcolo dei centroidi mediante media aritmetica.
4. Ripetizione del processo fino alla convergenza.

Formula utilizzata per il calcolo del centroide:

```text
Centroide = Somma degli elementi del cluster / Numero degli elementi del cluster
```

Esempio:

```text
Cluster = {1, 4, 8, 9, 10}

Centroide = (1 + 4 + 8 + 9 + 10) / 5 = 6.4
```

---

## Visualizzazione dei Risultati

### Cluster Finali
Nel grafico:

- ogni colore rappresenta un cluster differente;
- le **X nere** rappresentano i centroidi finali;
- l'asse X contiene i valori del dataset;
- l'asse Y identifica il cluster di appartenenza.

---

## Analisi del Grafico

Osservando il risultato ottenuto è possibile notare come il dataset venga suddiviso in gruppi distinti sulla base della vicinanza ai centroidi.

Le X nere evidenziano la posizione finale dei centroidi calcolati dall'algoritmo.

La distribuzione mostra chiaramente la presenza di alcuni valori molto più grandi rispetto alla maggior parte dei dati.

---

## Analisi degli Outlier

Durante l'esecuzione emergono due valori particolarmente distanti dal resto del dataset:

```text
128
333
```

Questi punti possono essere considerati **outlier**, poiché si trovano molto lontani dalla distribuzione principale dei dati.

La loro presenza influenza significativamente il calcolo dei centroidi e può portare alla formazione di cluster composti da pochissimi elementi.

Questo comportamento evidenzia uno dei principali limiti del K-Means: la sensibilità agli outlier.

---

## Risultati

L'algoritmo raggiunge la convergenza dopo alcune iterazioni successive di:

- assegnazione dei punti ai cluster;
- aggiornamento dei centroidi;
- verifica del criterio di arresto.

I centroidi finali rappresentano il centro dei cluster individuati e descrivono la struttura del dataset secondo la logica del K-Means.

---

## Vantaggi del K-Means

- Semplice da implementare.
- Facile da interpretare.
- Computazionalmente efficiente.
- Adatto a dataset di grandi dimensioni.
- Ampiamente utilizzato in Machine Learning e Data Mining.

---

## Limiti del K-Means

- Richiede la scelta preventiva del numero di cluster K.
- Sensibile ai centroidi iniziali.
- Sensibile agli outlier.
- Non garantisce sempre la soluzione ottimale globale.

---

## Tecnologie Utilizzate

- Python 3
- Matplotlib

---

## Obiettivi Formativi

Questo progetto è stato sviluppato per approfondire:

- Machine Learning Foundations
- Unsupervised Learning
- K-Means Clustering
- Data Analysis
- Data Visualization
- Outlier Detection
- Python Programming

---

## Possibili Miglioramenti Futuri

- Rimozione automatica degli outlier.
- Salvataggio automatico dei grafici.
- Supporto a dataset multidimensionali.
- Implementazione del metodo Elbow per la scelta di K.
- Confronto con algoritmi di clustering gerarchico.