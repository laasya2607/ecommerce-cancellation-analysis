import sqlite3
import pandas as pd

# Connect to SQLite database
conn = sqlite3.connect("ecommerce.db")

# Load CSV files
orders = pd.read_csv("data/olist_orders_dataset.csv")
payments = pd.read_csv("data/olist_order_payments_dataset.csv")
products = pd.read_csv("data/olist_products_dataset.csv")
items = pd.read_csv("data/olist_order_items_dataset.csv")
category = pd.read_csv("data/product_category_name_translation.csv")

# Store them as SQLite tables
orders.to_sql("orders", conn, if_exists="replace", index=False)
payments.to_sql("payments", conn, if_exists="replace", index=False)
products.to_sql("products", conn, if_exists="replace", index=False)
items.to_sql("items", conn, if_exists="replace", index=False)
category.to_sql("category_translation", conn, if_exists="replace", index=False)

conn.close()

print("Database created successfully!")