import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Dashboard",
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
st.title("Business Dashboard")

st.caption(
    "Monitor sales performance, profitability and key business metrics."
)

# Load Data
df = pd.read_csv("sales.csv", encoding="latin1")

df["Order Date"] = pd.to_datetime(
    df["Order Date"],
    format="mixed",
    errors="coerce"
)

df = df.dropna(subset=["Order Date"])

df["Year"] = df["Order Date"].dt.year

with st.sidebar:
    st.divider()

    region_filter = st.selectbox(
        "Region",
        ["All"] + sorted(df["Region"].unique().tolist())
    )

    category_filter = st.selectbox(
        "Category",
        ["All"] + sorted(df["Category"].unique().tolist())
    )

    year_filter = st.selectbox(
        "Year",
        ["All"] + sorted(df["Year"].unique().tolist())
    )

filtered_df = df.copy()

if region_filter != "All":
    filtered_df = filtered_df[
        filtered_df["Region"] == region_filter
    ]

if category_filter != "All":
    filtered_df = filtered_df[
        filtered_df["Category"] == category_filter
    ]

if year_filter != "All":
    filtered_df = filtered_df[
        filtered_df["Year"] == year_filter
    ]

if filtered_df.empty:
    st.warning("No data available for selected filters.")
    st.stop()

# KPI Metrics
total_sales = filtered_df["Sales"].sum()
total_profit = filtered_df["Profit"].sum()
total_orders = len(filtered_df)
avg_order_value = total_sales / total_orders

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Sales",
    f"${total_sales:,.0f}"
)

col2.metric(
    "Total Profit",
    f"${total_profit:,.0f}"
)

col3.metric(
    "Total Orders",
    f"{total_orders:,}"
)

col4.metric(
    "Avg Order Value",
    f"${avg_order_value:,.2f}"
)

st.divider()

# Monthly Sales Trend
st.subheader("Monthly Sales Trend")

monthly_sales = (
    filtered_df.groupby(
        pd.Grouper(key="Order Date", freq="ME")
    )["Sales"]
    .sum()
    .reset_index()
)

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

fig.update_layout(
    template="plotly_white",
    height=550,
    showlegend=False,
    margin=dict(l=20, r=20, t=20, b=20)
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.caption(
    "Sales performance reflects overall business growth across reporting periods."
)

st.divider()

# Category Analysis
st.subheader("Sales by Category")

category_sales = (
    filtered_df.groupby("Category")["Sales"]
    .sum()
    .reset_index()
)

fig2 = px.bar(
    category_sales,
    x="Category",
    y="Sales",
    text_auto=True
)

fig2.update_layout(
    template="plotly_white",
    height=550,
    showlegend=False,
    margin=dict(l=20, r=20, t=20, b=20)
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

st.caption(
    "Category performance highlights the strongest contributors to total revenue."
)

st.divider()

# Business Highlights
st.subheader("Business Highlights")

top_region = (
    filtered_df.groupby("Region")["Sales"]
    .sum()
    .idxmax()
)

top_category = (
    df.groupby("Category")["Sales"]
    .sum()
    .idxmax()
)

top_product = (
    df.groupby("Product Name")["Sales"]
    .sum()
    .idxmax()
)

col1, col2, col3 = st.columns(3)

col1.success(
    f"Top Region\n\n{top_region}"
)

col2.success(
    f"Top Category\n\n{top_category}"
)

col3.success(
    f"Best Product\n\n{top_product}"
)

st.caption(
    "Business highlights are automatically generated from the latest sales dataset."
)