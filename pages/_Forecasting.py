import streamlit as st
import pandas as pd
import plotly.express as px

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

st.set_page_config(
    page_title="Forecasting",
    layout="wide"
)

# Theme Styling
st.markdown("""
<style>

.main {
    padding-top: 1rem;
}

h1 {
    color: #0F172A;
    font-weight: 700;
}

.block-container {
    padding-top: 2rem;
}

div[data-testid="metric-container"] {
    background-color: #ffffff;
    border: 1px solid #e2e8f0;
    padding: 15px;
    border-radius: 12px;
}

</style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("## SmartDemand AI")
    st.caption("Business Intelligence Platform")

    st.divider()

    st.markdown("""
**Core Modules**

• Dashboard

• Analytics

• AI Insights

• Forecasting

• Reports
""")

    st.divider()

    st.caption("Version 2.0")

# Header
st.title("AI Sales Forecasting")

st.caption(
    "Demand forecasting powered by Machine Learning and historical sales trends."
)

# Load Dataset
df = pd.read_csv("sales.csv", encoding="latin1")

df["Order Date"] = pd.to_datetime(
    df["Order Date"],
    format="mixed",
    errors="coerce"
)

df = df.dropna(subset=["Order Date"])

# Monthly Sales
monthly_sales = (
    df.groupby(pd.Grouper(key="Order Date", freq="ME"))["Sales"]
    .sum()
    .reset_index()
)

# Feature Engineering
monthly_sales["Month_Number"] = range(len(monthly_sales))

X = monthly_sales[["Month_Number"]]
y = monthly_sales["Sales"]

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Model
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Error Metric
mae = mean_absolute_error(y_test, y_pred)

# Future Forecast
future_months = pd.DataFrame({
    "Month_Number": [
        len(monthly_sales),
        len(monthly_sales) + 1,
        len(monthly_sales) + 2
    ]
})

future_predictions = model.predict(future_months)

future_dates = pd.date_range(
    monthly_sales["Order Date"].max(),
    periods=4,
    freq="ME"
)[1:]

forecast_df = pd.DataFrame({
    "Order Date": future_dates,
    "Forecast Sales": future_predictions
})

# Growth Rate
last_sales = monthly_sales["Sales"].iloc[-1]

growth_rate = (
    (future_predictions[-1] - last_sales)
    / last_sales
) * 100

# Demand Trend
if growth_rate > 5:
    trend = "Increasing"
elif growth_rate < -5:
    trend = "Declining"
else:
    trend = "Stable"

# KPI Cards
c1, c2, c3, c4 = st.columns(4)

c1.metric(
    "Records Analyzed",
    f"{len(df):,}"
)

c2.metric(
    "Forecast Horizon",
    "3 Months"
)

c3.metric(
    "Demand Trend",
    trend
)

c4.metric(
    "Growth Forecast",
    f"{growth_rate:.1f}%"
)

st.divider()

# Forecast Chart
st.subheader("Historical vs Forecast Sales")

fig = px.line(
    monthly_sales,
    x="Order Date",
    y="Sales",
    markers=True
)

fig.update_traces(
    line_width=4,
    marker_size=8
)

fig.add_scatter(
    x=forecast_df["Order Date"],
    y=forecast_df["Forecast Sales"],
    mode="lines+markers",
    name="Forecast"
)

fig.update_layout(
    template="plotly_white",
    height=600,
    margin=dict(l=20, r=20, t=20, b=20)
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.caption(
    "Forecast values are generated using historical sales performance patterns."
)

st.divider()

# Forecast Table
st.subheader("Future Sales Forecast")

st.dataframe(
    forecast_df,
    use_container_width=True
)

st.divider()

# Forecast Summary
st.subheader("Forecast Summary")

col1, col2 = st.columns(2)

with col1:
    st.success(f"Demand Trend\n\n{trend}")

with col2:
    st.success(f"Projected Growth\n\n{growth_rate:.2f}%")

st.divider()

# Recommendation
st.subheader("Business Recommendation")

st.info(f"""
Focus on high-performing products and regions.

Align inventory planning with the projected demand trend.

Monitor future sales performance regularly to support business growth.

Current demand trend indicates: {trend}.
""")

st.divider()

st.caption(
    "Forecasts are generated automatically using the latest available sales data."
)