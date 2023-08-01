import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('data_after_outlier_removal.csv')

# Convert InvoiceDate to datetime format and extract the month
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
df['Month'] = df['InvoiceDate'].dt.month

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

# Print number of unique customers, products, and invoices
print("\nNumber of unique customers: ", df['CustomerID'].nunique())
print("Number of unique products: ", df['StockCode'].nunique()) 
print("Number of unique invoices: ", df['InvoiceNo'].nunique()) 

# Countries with 2nd to 4th Highest Number of Orders
top_countries_orders = df['Country'].value_counts().iloc[1:4].index.tolist()
df_top_countries_orders = df[df['Country'].isin(top_countries_orders)]
df_top_countries_orders['Country'].value_counts().plot(kind='bar', figsize=(12,6))
plt.title('Countries with 2nd to 4th Highest Number of Orders')
plt.xlabel('Country')
plt.ylabel('Number of Orders')
plt.show()

# Countries with 2nd to 4th Highest Total Revenue
top_countries_revenue = df.groupby('Country')['TotalCost'].sum().sort_values(ascending=False).iloc[1:4].index.tolist()
df_top_countries_revenue = df[df['Country'].isin(top_countries_revenue)]
df_top_countries_revenue.groupby('Country')['TotalCost'].sum().plot(kind='bar', figsize=(12,6))
plt.title('Countries with 2nd to 4th Highest Total Revenue')
plt.xlabel('Country')
plt.ylabel('Total Revenue')
plt.show()

# Top 2nd to 4th Countries with Highest Revenue by Month
top_countries_monthly = df.groupby('Country')['TotalCost'].sum().sort_values(ascending=False).iloc[1:4].index.tolist()
df_top_countries_monthly = df[df['Country'].isin(top_countries_monthly)]
monthly_revenue = df_top_countries_monthly.groupby(['Country', 'Month'])['TotalCost'].sum().reset_index()

fig, ax = plt.subplots(figsize=(12,6))

color_map = {'Germany': 'orange', 'France': 'green', 'EIRE': 'red'}  # Define color map

for country in top_countries_monthly:
    data = monthly_revenue[monthly_revenue['Country'] == country]
    ax.plot(data['Month'], data['TotalCost'], marker='o', label=country, color=color_map[country])  # Specify color

ax.set_xlabel('Month')
ax.set_ylabel('Total Revenue')
plt.title('Top 2nd to 4th Countries with Highest Revenue by Month')
plt.legend()
plt.grid(True)
plt.show()
