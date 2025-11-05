E-Commerce Analytics & BI Project (Brazil Olist Dataset)

A complete end-to-end E-Commerce data analytics and BI project built to simulate a real-world retail analytics system.

This project uses:

✅ Python — Data Cleaning & ETL

✅ MySQL — Database & Analytical SQL

✅ Power BI — Interactive Dashboard & DAX

✅ Git & GitHub — Version Control + Documentation

The goal is to analyze customer behavior, order trends, delivery performance, and payment insights using real marketplace data from the Brazil Olist dataset (Kaggle).

📊 Dashboard Preview

Power BI Dashboard analyzing Orders, Customers, Payments & Delivery performance.


✨ Key Insights
Insight Area	Key Findings
📈 Sales Growth	Monthly increasing order volume
👥 Top Customer Cities	São Paulo, Rio de Janeiro dominate demand
💳 Payment Behavior	Majority payments via credit card
🚚 Delivery Performance	Avg delivery ~12 days with state variation
📦 Category Demand	Top-selling categories include bed_bath_table, health_beauty, sports_leisure
📂 Project Structure
📦 e-commerce-analytics
├── data_raw/                      # Raw Olist CSVs (not uploaded)
├── data_clean/                    # Cleaned dataset (Python output)
├── powerbi/
│   ├── ecommerce_dashboard.pbix   # Power BI dashboard
│   └── ecommerce_dashboard.pdf
├── scripts/
│   └── etl_olist.py               # Python cleaning script
├── sql/
│   ├── table_query.sql            # Create tables
│   └── analysis_query.sql         # Analysis queries
├── docs/
│   └── dashboard_preview.png
└── README.md

🧠 Tech Stack
Tool	Purpose
🐍 Python (Pandas)	ETL & preprocessing
🗄️ MySQL	Database, SQL queries
📊 Power BI / DAX	Business dashboard
📁 GitHub	Version control & portfolio
⚙️ ETL Workflow (Python)

Tasks performed:

Handle missing values

Convert date columns to proper format

Merge Olist tables into olist_cleaned_merged

Export clean file for SQL & Power BI

Script: scripts/etl_olist.py

🧾 SQL Layers
✅ Schema Creation — table_query.sql

Orders Table

Order Items

Customers

Sellers

Products

Order Reviews

Order Payments

✅ Analytical Queries — analysis_query.sql

Total Orders

Total Customers

Total Revenue

Avg Order Value

Monthly Order Trend

Delivery Time KPI

📊 Power BI Metrics (DAX)
Metric	Formula
Total Orders	DISTINCTCOUNT(order_id)
Total Revenue	SUM(payment_value)
Avg Order Value	SUM(payment_value) / DISTINCTCOUNT(order_id)
Avg Delivery Days	DATEDIFF(order_purchase_timestamp, order_delivered_customer_date, DAY)
🚀 How to Run
1️⃣ Setup Database
CREATE DATABASE olist_db;
USE olist_db;


Run table_query.sql
Import cleaned CSV
Run analysis_query.sql

2️⃣ Run Python ETL
python scripts/etl_olist.py

3️⃣ Open Power BI File

Load → powerbi/ecommerce_dashboard.pbix

🏁 Conclusion

This project demonstrates:

✅ End-to-end data pipeline execution

✅ Business reporting using BI tools

✅ SQL analytical skills

✅ Dashboard storytelling with real insights

📎 Attribution

Dataset Source:
Kaggle — Brazilian E-Commerce Olist Dataset

⭐ Future Enhancements

Power BI refresh with MySQL connector

Streamlit dashboard version

ML model: delivery time prediction
