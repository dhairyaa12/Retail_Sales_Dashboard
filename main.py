
import pandas as pd
import matplotlib.pyplot as plt

# Reading CSV file
data = pd.read_csv("sales_data.csv")

# Calculating total sales
data["Total_Sales"] = data["Quantity"] * data["Price"]

# Converting date into date format
data["Date"] = pd.to_datetime(data["Date"])

# Displaying dashboard
print("\n====================================")
print("       RETAIL SALES DASHBOARD")
print("====================================")

total_sales = data["Total_Sales"].sum()
total_profit = data["Profit"].sum()
total_orders = len(data)
total_quantity = data["Quantity"].sum()

print("\nTOTAL SALES       :", total_sales)
print("TOTAL PROFIT      :", total_profit)
print("TOTAL ORDERS      :", total_orders)
print("PRODUCTS SOLD     :", total_quantity)

# Product-wise sales
product_sales = data.groupby("Product")["Total_Sales"].sum()

print("\nPRODUCT-WISE SALES")
print(product_sales)

# Finding best-selling product by quantity
best_product = data.groupby("Product")["Quantity"].sum().idxmax()

print("\nBEST SELLING PRODUCT:", best_product)

# Category-wise sales
category_sales = data.groupby("Category")["Total_Sales"].sum()

# Monthly sales
monthly_sales = data.groupby(
    data["Date"].dt.to_period("M")
)["Total_Sales"].sum()

print("\nMONTHLY SALES")
print(monthly_sales)

# Creating dashboard charts
plt.figure(figsize=(14, 9))

# Chart 1: Product-wise sales
plt.subplot(2, 2, 1)
product_sales.plot(kind="bar", color="skyblue")
plt.title("Product-wise Sales")
plt.xlabel("Product")
plt.ylabel("Sales Amount")
plt.xticks(rotation=45)

# Chart 2: Category-wise sales
plt.subplot(2, 2, 2)
category_sales.plot(
    kind="pie",
    autopct="%1.1f%%",
    startangle=90
)
plt.title("Category-wise Sales")
plt.ylabel("")

# Chart 3: Monthly sales
plt.subplot(2, 2, 3)
monthly_sales.plot(
    kind="line",
    marker="o",
    color="green"
)
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales Amount")
plt.xticks(rotation=45)
plt.grid(True)

# Chart 4: Quantity sold by product
plt.subplot(2, 2, 4)

quantity_sales = data.groupby("Product")["Quantity"].sum()

quantity_sales.plot(
    kind="bar",
    color="orange"
)

plt.title("Products Sold")
plt.xlabel("Product")
plt.ylabel("Quantity")
plt.xticks(rotation=45)

# Displaying all charts
plt.tight_layout()
plt.show()

print("\nDashboard Generated Successfully!")
