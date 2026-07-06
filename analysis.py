import pandas as pd

# ==========================
# Load Datasets
# ==========================

orders = pd.read_csv("data/olist_orders_dataset.csv")
payments = pd.read_csv("data/olist_order_payments_dataset.csv")
items = pd.read_csv("data/olist_order_items_dataset.csv")
products = pd.read_csv("data/olist_products_dataset.csv")
category_translation = pd.read_csv(
    "data/product_category_name_translation.csv"
)

# ==========================
# Data Cleaning
# ==========================

orders["order_purchase_timestamp"] = pd.to_datetime(
    orders["order_purchase_timestamp"]
)

orders.drop_duplicates(inplace=True)

# ==========================
# Merge Product Data
# ==========================

product_categories = items.merge(
    products,
    on="product_id"
)

product_categories = product_categories.merge(
    category_translation,
    on="product_category_name",
    how="left"
)

product_categories["product_category_name_english"] = (
    product_categories["product_category_name_english"]
    .fillna("Unknown")
)

# ==========================
# Summary
# ==========================

def total_orders():
    return len(orders)


def cancelled_orders():
    return len(orders[orders["order_status"] == "canceled"])


def cancellation_rate():
    return round(cancelled_orders() / total_orders() * 100, 2)


# ==========================
# Order Status
# ==========================

def status_distribution():
    return orders["order_status"].value_counts().to_dict()


# ==========================
# Monthly Orders
# ==========================

def monthly_orders():
    monthly = (
        orders.groupby(
            orders["order_purchase_timestamp"].dt.to_period("M")
        )
        .size()
    )

    monthly.index = monthly.index.astype(str)

    return monthly.to_dict()


# ==========================
# Monthly Cancellations
# ==========================

def monthly_cancellations():

    cancelled = orders[
        orders["order_status"] == "canceled"
    ]

    trend = (
        cancelled.groupby(
            cancelled["order_purchase_timestamp"].dt.to_period("M")
        )
        .size()
    )

    trend.index = trend.index.astype(str)

    return trend.to_dict()


# ==========================
# Payment Methods
# ==========================

def payment_methods():
    return payments["payment_type"].value_counts().to_dict()


# ==========================
# Top Categories
# ==========================

def top_categories():

    top = (
        product_categories["product_category_name_english"]
        .value_counts()
        .head(10)
    )

    return top.to_dict()
def monthly_revenue():

    revenue = items.merge(
        orders[["order_id", "order_purchase_timestamp"]],
        on="order_id"
    )

    revenue["order_purchase_timestamp"] = pd.to_datetime(
        revenue["order_purchase_timestamp"]
    )

    revenue["month"] = revenue[
        "order_purchase_timestamp"
    ].dt.to_period("M").astype(str)

    monthly = (
        revenue.groupby("month")["price"]
        .sum()
        .round(2)
    )

    return monthly.to_dict()
def business_insights():

    # Most used payment method
    top_payment = payments["payment_type"].value_counts().idxmax()

    # Top category
    top_category = (
        product_categories["product_category_name_english"]
        .value_counts()
        .idxmax()
    )

    # Highest revenue month
    revenue = items.merge(
        orders[["order_id", "order_purchase_timestamp"]],
        on="order_id"
    )

    revenue["order_purchase_timestamp"] = pd.to_datetime(
        revenue["order_purchase_timestamp"]
    )

    revenue["month"] = revenue[
        "order_purchase_timestamp"
    ].dt.to_period("M").astype(str)

    revenue_month = (
        revenue.groupby("month")["price"]
        .sum()
        .idxmax()
    )

    return {
        "Total Orders": total_orders(),
        "Cancellation Rate": f"{cancellation_rate()}%",
        "Top Payment Method": top_payment.title(),
        "Top Category": top_category.replace("_", " ").title(),
        "Highest Revenue Month": revenue_month
    }