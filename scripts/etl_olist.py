import pandas as pd
import os

# Set paths
base_path = r"D:\e-commerce analytics"
raw_path = os.path.join(base_path, "data_raw")
clean_path = os.path.join(base_path, "data_clean")

# Load datasets
customers = pd.read_csv(os.path.join(raw_path, "olist_customers_dataset.csv"))
orders = pd.read_csv(os.path.join(raw_path, "olist_orders_dataset.csv"))
order_items = pd.read_csv(os.path.join(raw_path, "olist_order_items_dataset.csv"))
payments = pd.read_csv(os.path.join(raw_path, "olist_order_payments_dataset.csv"))
reviews = pd.read_csv(os.path.join(raw_path, "olist_order_reviews_dataset.csv"))
products = pd.read_csv(os.path.join(raw_path, "olist_products_dataset.csv"))
sellers = pd.read_csv(os.path.join(raw_path, "olist_sellers_dataset.csv"))
geo = pd.read_csv(os.path.join(raw_path, "olist_geolocation_dataset.csv"))
category = pd.read_csv(os.path.join(raw_path, "product_category_name_translation.csv"))

# Merge tables step-by-step
df = orders.merge(customers, on="customer_id", how="left") \
           .merge(order_items, on="order_id", how="left") \
           .merge(payments, on="order_id", how="left") \
           .merge(reviews, on="order_id", how="left") \
           .merge(products, on="product_id", how="left") \
           .merge(sellers, on="seller_id", how="left") \
           .merge(category, on="product_category_name", how="left")

# Convert date columns
date_cols = ["order_purchase_timestamp", "order_approved_at", "order_delivered_carrier_date",
             "order_delivered_customer_date", "order_estimated_delivery_date"]
for col in date_cols:
    df[col] = pd.to_datetime(df[col], errors='coerce')

# Clean: remove duplicates
df.drop_duplicates(inplace=True)

# Save cleaned data
output_file = os.path.join(clean_path, "olist_cleaned_merged.csv")
df.to_csv(output_file, index=False)

print("✅ ETL Completed — File saved at:", output_file)
