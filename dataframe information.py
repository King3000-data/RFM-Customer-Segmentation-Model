import pandas as pd
import numpy as np

# Load the data
df = pd.read_excel("Online Retail.xlsx")

# Check for missing values
print("\nMissing values:")
print(df.isnull().sum())

# Check for duplicate rows
print("\nNumber of duplicate rows:")
print(df.duplicated().sum())

# Show statistical descriptions
print("\nStatistical descriptions:")
print(df.describe())

# Show data types
print("\nData types:")
print(df.dtypes)

# Show unique values in each column
print("\nUnique values in each column:")
for col in df.columns:
    print(f"\n{col}:")
    print(df[col].value_counts())

# Show correlation for numerical data
print("\nCorrelation:")
print(df.select_dtypes(include=[np.number]).corr())
