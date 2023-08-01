# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns
import plotly.express as px

# Load the data
rfm_data = pd.read_csv("rfm_data.csv")

# 3D scatter plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
scatter = ax.scatter(rfm_data['Recency'], rfm_data['Frequency'], rfm_data['MonetaryValue'], c=rfm_data['Cluster'], cmap='viridis')
ax.set_xlabel('Recency')
ax.set_ylabel('Frequency')
ax.set_zlabel('Monetary Value')
legend1 = ax.legend(*scatter.legend_elements(), title="Clusters")
ax.add_artist(legend1)
plt.show()

# Bar plot for average RFM values across clusters
plt.figure(figsize=(12, 10))
plt.subplot(3, 1, 1); sns.barplot(x=rfm_data['Cluster'], y=rfm_data['Recency'])
plt.title('Average Recency by Cluster')
plt.subplot(3, 1, 2); sns.barplot(x=rfm_data['Cluster'], y=rfm_data['Frequency'])
plt.title('Average Frequency by Cluster')
plt.subplot(3, 1, 3); sns.barplot(x=rfm_data['Cluster'], y=rfm_data['MonetaryValue'])
plt.title('Average Monetary Value by Cluster')
plt.tight_layout()
plt.show()

# Pie chart for the distribution of customers across clusters
cluster_counts = rfm_data['Cluster'].value_counts()
plt.figure(figsize=(6, 6))
plt.pie(cluster_counts, labels = cluster_counts.index, startangle=90, autopct='%1.1f%%')
plt.title('Customer Distribution Across Clusters')
plt.show()

# Interactive 3D scatter plot using plotly
fig = px.scatter_3d(rfm_data, x='Recency', y='Frequency', z='MonetaryValue', color='Cluster', hover_data=['Cluster'])
fig.update_layout(title='3D Scatterplot of RFM values')
fig.show()
