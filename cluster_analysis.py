# Import necessary libraries
import pandas as pd
from sklearn.cluster import KMeans, DBSCAN
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Define necessary functions
def calculate_silhouette_scores(rfm_scaled, algorithm='kmeans'):
    silhouette_scores = []
    K = range(2, 10)  # silhouette_score requires at least 2 clusters
    if algorithm == 'kmeans':
        for k in K:
            kmeans = KMeans(n_clusters=k, n_init=10)
            kmeans.fit(rfm_scaled)
            silhouette_scores.append(silhouette_score(rfm_scaled, kmeans.labels_))
    elif algorithm == 'dbscan':
        for k in K:
            dbscan = DBSCAN(eps=0.5, min_samples=k)  # You can adjust the hyperparameters accordingly
            dbscan_labels = dbscan.fit_predict(rfm_scaled)
            # The silhouette score requires at least 2 unique clusters to be meaningful
            if len(np.unique(dbscan_labels)) > 1:
                silhouette_scores.append(silhouette_score(rfm_scaled, dbscan_labels))
            else:
                silhouette_scores.append(-1.0)  # Placeholder for single-cluster cases
    return silhouette_scores

def calculate_distortions(rfm_scaled):
    distortions = []
    K = range(1, 10)
    for k in K:
        kmeanModel = KMeans(n_clusters=k, n_init=10)
        kmeanModel.fit(rfm_scaled)
        distortions.append(kmeanModel.inertia_)
    return distortions

def find_elbow(distortions):
    second_order_diffs = np.diff(distortions, 2)
    return np.argmax(second_order_diffs) + 3

def find_optimal_clusters(rfm_scaled, algorithm='kmeans'):
    silhouette_scores = calculate_silhouette_scores(rfm_scaled, algorithm=algorithm)
    optimal_clusters_silhouette = silhouette_scores.index(max(silhouette_scores)) + 2
    distortions = calculate_distortions(rfm_scaled)
    elbow_value = find_elbow(distortions)
    return max(optimal_clusters_silhouette, elbow_value)

# Load scaled data
rfm_scaled = pd.read_csv("scaled_rfm_data.csv")

# Elbow Method to find optimal number of clusters (using WCSS)
sns.set()
distortions = calculate_distortions(rfm_scaled)

plt.figure(figsize=(16, 8))
plt.plot(range(1, 10), distortions, 'bx-')
plt.xlabel('k')
plt.ylabel('WCSS (Within-Cluster Sum of Squares)')
plt.title('The Elbow Method showing the optimal k')
plt.axvline(x=find_elbow(distortions), linestyle='--', color='red')
plt.show()

# Silhouette Method to find optimal number of clusters (KMeans)
silhouette_scores_kmeans = calculate_silhouette_scores(rfm_scaled, algorithm='kmeans')

plt.figure(figsize=(16, 8))
plt.plot(range(2, 10), silhouette_scores_kmeans, 'bx-')
plt.xlabel('k')
plt.ylabel('Silhouette Score (KMeans)')
plt.title('Silhouette Method showing the optimal k for KMeans')
plt.axvline(x=silhouette_scores_kmeans.index(max(silhouette_scores_kmeans)) + 2, linestyle='--', color='red')
plt.show()

# Silhouette Method to find optimal number of clusters (DBSCAN)
silhouette_scores_dbscan = calculate_silhouette_scores(rfm_scaled, algorithm='dbscan')

plt.figure(figsize=(16, 8))
plt.plot(range(2, 10), silhouette_scores_dbscan, 'bx-')
plt.xlabel('min_samples (DBSCAN)')
plt.ylabel('Silhouette Score (DBSCAN)')
plt.title('Silhouette Method showing the optimal min_samples for DBSCAN')
plt.axvline(x=silhouette_scores_dbscan.index(max(silhouette_scores_dbscan)) + 2, linestyle='--', color='red')
plt.show()

# Find optimal number of clusters for KMeans
optimal_k_kmeans = find_optimal_clusters(rfm_scaled, algorithm='kmeans')
print(f'The optimal number of clusters for KMeans is {optimal_k_kmeans}')

# Find optimal number of clusters for DBSCAN
optimal_k_dbscan = find_optimal_clusters(rfm_scaled, algorithm='dbscan')
print(f'The optimal min_samples for DBSCAN is {optimal_k_dbscan}')
