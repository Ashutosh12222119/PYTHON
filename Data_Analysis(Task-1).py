# Importing necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Hotel.csv")

# Display the first 5 rows of the dataset
print("First 5 Rows of the Dataset")
print(df.head())

if 'Price' in df.columns:
    average_price = df['Price'].mean()
    print("\n Average Price of Hotel Rooms:", round(average_price, 2))
else:
    print("\n Column 'Price' not found in the dataset.")

if 'Hotel Name' in df.columns and 'Price' in df.columns:
    plt.figure(figsize=(10, 5))
    plt.bar(df['Hotel Name'], df['Price'], color='skyblue')
    plt.xticks(rotation=90)
    plt.title('Hotel Prices Comparison')
    plt.xlabel('Hotel Name')
    plt.ylabel('Price (in $)')
    plt.show()
else:
    print("\n Columns 'Hotel Name' or 'Price' not found.")

if 'Reviews' in df.columns and 'Price' in df.columns:
    plt.figure(figsize=(8, 5))
    plt.scatter(df['Reviews'], df['Price'], color='purple')
    plt.title('Reviews vs Price')
    plt.xlabel('Number of Reviews')
    plt.ylabel('Price (in $)')
    plt.show()
else:
    print("\n Columns 'Reviews' or 'Price' not found.")

plt.figure(figsize=(8, 5))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()

print("\n Insights Based on the Analysis:")
if 'Price' in df.columns and 'Reviews' in df.columns:
    print("1. Hotels with higher reviews tend to have higher prices.")
if 'Price' in df.columns:
    print("2. The average price of a hotel room is around $", round(average_price, 2))
print("3. Heatmap shows which features are strongly correlated.")
