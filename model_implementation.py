# Import necessary libraries
import pandas as pd
from sklearn.cluster import KMeans

# Function to get optimal number of clusters
def get_optimal_k():
    while True:
        try:
            optimal_k = int(input("Enter the optimal number of clusters from the plot: "))
            if optimal_k < 1:
                raise ValueError
            return optimal_k
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

# Load scaled data
rfm_scaled = pd.read_csv("scaled_rfm_data.csv")

# Load original RFM data
rfm_data = pd.read_csv("rfm_data.csv")

# Implement the K-Means Algorithm
optimal_k = get_optimal_k()
kmeans = KMeans(n_clusters=optimal_k, random_state=0)
clusters = kmeans.fit_predict(rfm_scaled)
rfm_data["Cluster"] = clusters

# Save updated RFM data
rfm_data.to_csv("rfm_data.csv", index=False)

# Analyze the Segments
print(rfm_data.groupby('Cluster').agg({
    'Recency': 'mean',
    'Frequency': 'mean',
    'MonetaryValue': ['mean', 'count']
}).round(0))

