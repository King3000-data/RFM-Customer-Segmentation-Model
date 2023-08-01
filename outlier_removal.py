import pandas as pd
import matplotlib.pyplot as plt

def remove_outliers(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1

    # Define bounds for outliers
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    # Remove outliers
    df = df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]
    return df

# Load the cleaned data
df = pd.read_csv("cleaned_data.csv")

# Assume 'Quantity', 'UnitPrice', 'TotalCost' are the numerical columns of your DataFrame
columns = ['Quantity', 'UnitPrice', 'TotalCost']

for column in columns:
    df = remove_outliers(df, column)

    # Create boxplots for the column after outlier removal
    plt.figure(figsize=(5,5))
    df[[column]].boxplot()
    plt.title(f'Boxplot of {column} after Outlier Removal')
    plt.show()

# Create new CSV file
df.to_csv('data_after_outlier_removal.csv', index=False)

