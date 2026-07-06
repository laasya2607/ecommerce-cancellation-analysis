# 🛒 E-Commerce Order Cancellation Analytics Dashboard

A web-based analytics dashboard built using **FastAPI**, **Pandas**, and **Chart.js** to analyze over **99,000+ e-commerce orders** and visualize cancellation trends, revenue, payment methods, and business insights.

---

## 🚀 Features

- 📊 Interactive analytics dashboard
- 📦 Order status distribution
- 📈 Monthly orders visualization
- 💰 Monthly revenue analysis
- 💳 Payment methods analysis
- 🏷️ Top product categories
- 💡 Business insights generation
- 🗄️ SQLite database integration
- ⚡ REST API using FastAPI

---

## 🛠 Tech Stack

- Python
- FastAPI
- Pandas
- NumPy
- SQLite
- HTML
- CSS
- JavaScript
- Chart.js

---

## 📁 Project Structure

```text
ecommerce-dashboard/
│
├── data/
├── static/
├── templates/
├── analysis.py
├── app.py
├── database.py
├── ecommerce.db
├── requirements.txt
└── README.md
```

---

## 📸 Dashboard Preview

### Dashboard

![Dashboard](screenshots/dashboard.png)

### Analytics Charts

![Charts](screenshots/charts.png)

### Business Insights

![Insights](screenshots/insights.png)

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/ecommerce-dashboard.git
```

Go into the project:

```bash
cd ecommerce-dashboard
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it:

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
uvicorn app:app --reload
```

Open:

```
http://127.0.0.1:8000
```

---

## 📈 Dataset

This project uses the **Brazilian E-Commerce Public Dataset by Olist** available on Kaggle.

---

## 👨‍💻 Author

**Laasya Sri**

Engineering Student | Python | Data Analytics | FastAPI