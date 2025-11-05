USE olist_db;

-- ✅ Total Orders
SELECT COUNT(DISTINCT order_id) AS total_orders
FROM olist_cleaned_merged;

-- ✅ Total Customers
SELECT COUNT(DISTINCT customer_id) AS total_customers
FROM olist_cleaned_merged;

-- ✅ Total Revenue
SELECT SUM(payment_value) AS total_revenue
FROM olist_cleaned_merged;

-- ✅ Average Order Value
SELECT SUM(payment_value) / COUNT(DISTINCT order_id) AS avg_order_value
FROM olist_cleaned_merged;

-- ✅ Monthly Orders Trend
SELECT 
    DATE_FORMAT(order_purchase_timestamp, '%Y-%m') AS month,
    COUNT(DISTINCT order_id) AS total_orders
FROM olist_cleaned_merged
GROUP BY month
ORDER BY month;

-- ✅ Top 10 customer cities by orders
SELECT customer_city, COUNT(DISTINCT order_id) AS total_orders
FROM olist_cleaned_merged
GROUP BY customer_city
ORDER BY total_orders DESC
LIMIT 10;

-- ✅ Orders by payment type
SELECT payment_type, COUNT(order_id) AS total_orders
FROM olist_cleaned_merged
GROUP BY payment_type
ORDER BY total_orders DESC;

-- ✅ Avg delivery days by customer state
SELECT 
    customer_state,
    AVG(DATEDIFF(order_delivered_customer_date, order_purchase_timestamp)) AS avg_delivery_days
FROM olist_cleaned_merged
WHERE order_delivered_customer_date IS NOT NULL
GROUP BY customer_state
ORDER BY avg_delivery_days DESC;
