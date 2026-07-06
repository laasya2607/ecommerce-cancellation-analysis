async function loadSummary() {

    const response = await fetch("/summary");
    const data = await response.json();

    document.getElementById("totalOrders").innerHTML = data.total_orders.toLocaleString();
    document.getElementById("cancelledOrders").innerHTML = data.cancelled_orders.toLocaleString();
    document.getElementById("cancelRate").innerHTML = data.cancellation_rate + " %";
}

async function loadStatusChart() {

    const response = await fetch("/status");
    const data = await response.json();

    new Chart(document.getElementById("statusChart"), {
        type: "pie",
        data: {
            labels: Object.keys(data),
            datasets: [{
                data: Object.values(data),
                backgroundColor: [
                    "#2563eb",
                    "#22c55e",
                    "#f59e0b",
                    "#ef4444",
                    "#8b5cf6",
                    "#06b6d4",
                    "#64748b",
                    "#ec4899"
                ]
            }]
        }
    });
}

async function loadPaymentChart() {

    const response = await fetch("/payment-analysis");
    const data = await response.json();

    new Chart(document.getElementById("paymentChart"), {
        type: "bar",
        data: {
            labels: Object.keys(data),
            datasets: [{
                label: "Payments",
                data: Object.values(data),
                backgroundColor: "#2563eb"
            }]
        }
    });
}

async function loadMonthlyChart() {

    const response = await fetch("/monthly-orders");
    const data = await response.json();

    new Chart(document.getElementById("monthlyChart"), {
        type: "line",
        data: {
            labels: Object.keys(data),
            datasets: [{
                label: "Orders",
                data: Object.values(data),
                borderColor: "#22c55e",
                tension: 0.3
            }]
        }
    });
}

async function loadCategoryChart() {

    const response = await fetch("/top-categories");
    const data = await response.json();

    new Chart(document.getElementById("categoryChart"), {
        type: "bar",
        data: {
            labels: Object.keys(data),
            datasets: [{
                label: "Orders",
                data: Object.values(data),
                backgroundColor: "#f59e0b"
            }]
        },
        options: {
            indexAxis: "y"
        }
    });
}

async function loadRevenueChart() {

    const response = await fetch("/monthly-revenue");
    const data = await response.json();

    new Chart(document.getElementById("revenueChart"), {
        type: "line",
        data: {
            labels: Object.keys(data),
            datasets: [{
                label: "Revenue",
                data: Object.values(data),
                borderColor: "#ef4444",
                tension: 0.3
            }]
        }
    });
}

async function loadInsights() {

    const response = await fetch("/business-insights");
    const data = await response.json();

    const list = document.getElementById("insightsList");
    list.innerHTML = "";

    for (const key in data) {
        list.innerHTML += `<li><strong>${key}:</strong> ${data[key]}</li>`;
    }
}

loadSummary();
loadStatusChart();
loadPaymentChart();
loadMonthlyChart();
loadCategoryChart();
loadRevenueChart();
loadInsights();
