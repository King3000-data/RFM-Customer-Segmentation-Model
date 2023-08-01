import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the cleaned data
df = pd.read_csv("cleaned_data.csv")

# Assume 'Quantity', 'UnitPrice', 'TotalCost' are the numerical columns of your DataFrame
columns = ['Quantity', 'UnitPrice', 'TotalCost']

for column in columns:
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1

    # Define bounds for outliers
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    # Identify outliers
    outliers = df[(df[column] < lower_bound) | (df[column] > upper_bound)]

    # Print the number of outliers in each column
    print(f'Number of outliers in {column}: {len(outliers)}')

    # Create boxplots for columns with outliers
    if not outliers.empty:
        plt.figure(figsize=(5,5))
        df[[column]].boxplot()
        plt.title(f'Outliers of {column}')
        plt.show()
