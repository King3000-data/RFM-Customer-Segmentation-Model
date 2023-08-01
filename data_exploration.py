import pandas as pd

# Load the data
df = pd.read_csv('rfm_data.csv')

# Display the first few rows of the dataset
print("First few rows of the dataset:")
print(df.head())

# Print the size of the dataset
print("\nSize of the dataset:")
print(f"{df.shape[0]} rows, {df.shape[1]} columns")

# Descriptive statistics
print("\nDescriptive statistics:")
print(df.describe(include='all'))

# Check for missing values and if they have been corrected
print("\nMissing values:")
print(df.isnull().sum())
