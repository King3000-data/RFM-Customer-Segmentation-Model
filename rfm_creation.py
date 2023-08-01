# Import necessary libraries
import pandas as pd
import datetime as dt

# Load cleaned data
df = pd.read_csv("data_after_outlier_removal.csv", parse_dates=['InvoiceDate'])

# Create RFM Metrics
snapshot_date = df['InvoiceDate'].max() + dt.timedelta(days=1)
rfm_data = df.groupby('CustomerID').agg({
    'InvoiceDate': lambda x: (snapshot_date - x.max()).days,
    'InvoiceNo': 'count',
    'TotalCost': 'sum'
})

rfm_data.rename(columns={'InvoiceDate': 'Recency',
                         'InvoiceNo': 'Frequency',
                         'TotalCost': 'MonetaryValue'}, inplace=True)

# Save RFM data
rfm_data.to_csv("rfm_data.csv")

print("RFM data has been saved successfully.")
