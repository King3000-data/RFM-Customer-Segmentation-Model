# Import necessary libraries
import pandas as pd

# Load the data
df = pd.read_excel("Online Retail.xlsx")

# Parse 'InvoiceDate' column as a datetime object
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'], format="%m/%d/%Y %H:%M")

# Clean the data
df.dropna(subset=["CustomerID"], inplace=True)
df.drop_duplicates(inplace=True)

# Create 'TotalCost' column
df['TotalCost'] = df['Quantity'] * df['UnitPrice']

# Save cleaned data
df.to_csv("cleaned_data.csv", index=False)
