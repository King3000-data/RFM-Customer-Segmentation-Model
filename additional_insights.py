# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Load RFM data
rfm = pd.read_csv('rfm_data.csv', index_col='CustomerID')

print(rfm.columns)

# Select the necessary features
rfm_features = rfm[['Recency', 'Frequency', 'MonetaryValue']]

# Display the mean recency, frequency and monetary value for each cluster
for i in range(3):  # Replace 3 with the actual number of clusters
    print(f'Cluster {i}:')
    print('Mean Recency:')
    print(rfm[rfm['Cluster'] == i]['Recency'].mean())
    print('Mean Frequency:')
    print(rfm[rfm['Cluster'] == i]['Frequency'].mean())
    print('Mean Monetary Value:')
    print(rfm[rfm['Cluster'] == i]['MonetaryValue'].mean())
    print('\n')

# Visualize the mean recency, frequency and monetary value for each cluster
for i in range(3):  # Replace 3 with the actual number of clusters
    plt.figure(figsize=(12, 6))
    rfm[rfm['Cluster'] == i][['Recency', 'Frequency', 'MonetaryValue']].mean().plot(kind='bar', color='skyblue')
    plt.title(f'Mean Recency, Frequency and Monetary Value for Cluster {i}')
    plt.ylabel('Mean Value')
    plt.show()
