from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi import FastAPI
import analysis

app = FastAPI(title="E-Commerce Analytics Dashboard")
templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )


@app.get("/summary")
def summary():

    return {
        "total_orders": analysis.total_orders(),
        "cancelled_orders": analysis.cancelled_orders(),
        "cancellation_rate": analysis.cancellation_rate()
    }


@app.get("/status")
def status():

    return analysis.status_distribution()

@app.get("/payment-analysis")
def payment_analysis():
    return analysis.payment_methods()

@app.get("/monthly-cancellations")
def monthly():

    return analysis.monthly_cancellations()

@app.get("/monthly-orders")
def monthly_orders():
    return analysis.monthly_orders()
@app.get("/top-categories")
def top_categories():
    return analysis.top_categories()
@app.get("/monthly-revenue")
def monthly_revenue():
    return analysis.monthly_revenue()
@app.get("/business-insights")
def insights():
    return analysis.business_insights()