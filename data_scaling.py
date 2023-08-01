# Import necessary libraries
import pandas as pd
from sklearn.preprocessing import StandardScaler
import numpy as np
import os

# Change working directory
os.chdir("C:/Users/Jared King/OneDrive/Desktop/NEW PROJECTS 2023/Customer Segmentation Model/")

# Print the current working directory
print("Current working directory:", os.getcwd())

# Load RFM data and set 'CustomerID' as the index
rfm_data = pd.read_csv("rfm_data.csv", index_col=0)

# Find the minimum value in each column
min_values = rfm_data.min()

# If the minimum is less than 0, shift all values in that column up by the absolute value of the minimum plus 1
for column in rfm_data.columns:
    if min_values[column] < 0:
        rfm_data[column] = rfm_data[column] + abs(min_values[column]) + 1

# Adding 1 to each value to handle zeros and negatives
rfm_data_log = np.log(rfm_data[['Recency', 'Frequency', 'MonetaryValue']] + 1)

# Check skewness again
print("After Log Transformation Skewness:")
print(rfm_data_log.skew())

# Scale the Data
scaler = StandardScaler()
rfm_scaled = pd.DataFrame(scaler.fit_transform(rfm_data_log), columns=rfm_data_log.columns, index=rfm_data_log.index)

# Save scaled data
rfm_scaled.to_csv("scaled_rfm_data.csv")
