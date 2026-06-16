import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Analytics",
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
st.title("Business Analytics")

st.caption(
    "Explore category, regional and product-level sales performance."
)

# Load Data
df = pd.read_csv("sales.csv", encoding="latin1")

# Summary Highlights
top_region = (
    df.groupby("Region")["Sales"]
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

col1.success(f"Top Region\n\n{top_region}")
col2.success(f"Top Category\n\n{top_category}")
col3.success(f"Best Product\n\n{top_product}")

st.divider()

# Category Analysis
st.subheader("Sales by Category")

category_sales = (
    df.groupby("Category")["Sales"]
    .sum()
    .reset_index()
)

fig1 = px.bar(
    category_sales,
    x="Category",
    y="Sales",
    text_auto=True
)

fig1.update_layout(
    template="plotly_white",
    height=550,
    showlegend=False
)

st.plotly_chart(
    fig1,
    use_container_width=True
)

st.caption(
    "Category analysis identifies the strongest revenue contributors."
)

st.divider()

# Regional Analysis
st.subheader("Regional Sales Distribution")

region_sales = (
    df.groupby("Region")["Sales"]
    .sum()
    .reset_index()
)

fig2 = px.pie(
    region_sales,
    names="Region",
    values="Sales",
    hole=0.45
)

fig2.update_layout(
    template="plotly_white",
    height=550
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

st.caption(
    "Regional distribution highlights geographic revenue concentration."
)

st.divider()

# Top Products
st.subheader("Top 10 Products")

top_products = (
    df.groupby("Product Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

fig3 = px.bar(
    top_products,
    x="Sales",
    y="Product Name",
    orientation="h",
    text_auto=True
)

fig3.update_layout(
    template="plotly_white",
    height=650,
    showlegend=False
)

st.plotly_chart(
    fig3,
    use_container_width=True
)

st.caption(
    "Top-performing products generate the largest share of overall revenue."
)

st.divider()

st.caption(
    "Analytics are generated dynamically from the latest sales dataset."
)