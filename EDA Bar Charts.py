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

# Plot the distribution of orders per customer
df['CustomerID'].value_counts().head(10).plot(kind='bar', figsize=(12,6))
plt.title('Top 10 Customers with Most Orders')
plt.xlabel('Customer ID')
plt.ylabel('Number of Orders')
plt.show()

# Plot the distribution of orders per country
df['Country'].value_counts().head(10).plot(kind='bar', figsize=(12,6))
plt.title('Top 10 Countries with Most Orders')
plt.xlabel('Country')
plt.ylabel('Number of Orders')
plt.show()

# Top 10 countries with most orders
print("\nTop 10 countries with most orders:")
print(df['Country'].value_counts().head(10))

# Top 10 countries with the highest total revenue from 'TotalCost'
df.groupby('Country')['TotalCost'].sum().sort_values(ascending=False).head(10).plot(kind='bar', figsize=(12,6))
plt.title('Top 10 Countries with Highest Total Revenue')
plt.xlabel('Country')
plt.ylabel('Total Revenue')
plt.show()

# Calculate and print the total revenue for each country to check the values
country_revenue = df.groupby('Country')['TotalCost'].sum().sort_values(ascending=False)
print("\nTotal revenue for each country:")
print(country_revenue)

# Month with the highest revenue for the top 10 countries
top_countries = df['Country'].value_counts().head(10).index.tolist()
df_top_countries = df[df['Country'].isin(top_countries)]
monthly_revenue = df_top_countries.groupby(['Country', 'Month'])['TotalCost'].sum().reset_index()

fig, ax = plt.subplots(figsize=(12,6))

for country in top_countries:
    data = monthly_revenue[monthly_revenue['Country'] == country]
    ax.plot(data['Month'], data['TotalCost'], marker='o', label=country)

ax.set_xlabel('Month')
ax.set_ylabel('Total Revenue')
plt.title('Month with Highest Revenue in Top 10 Countries')
plt.legend()
plt.grid(True)
plt.show()

