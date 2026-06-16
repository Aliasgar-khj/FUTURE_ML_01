import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="AI Insights",
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
st.title("AI Business Insights")

st.caption(
    "Automated business recommendations generated from sales performance data."
)

# Load Data
df = pd.read_csv("sales.csv", encoding="latin1")

# Metrics
total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()

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

avg_order = df["Sales"].mean()

# KPI Cards
col1, col2, col3 = st.columns(3)

col1.metric(
    "Top Region",
    top_region
)

col2.metric(
    "Top Category",
    top_category
)

col3.metric(
    "Avg Order Value",
    f"${avg_order:,.2f}"
)

st.divider()

# Executive Summary
st.subheader("Executive Summary")

st.markdown(f"""
The business generated **${total_sales:,.0f}** in revenue and
**${total_profit:,.0f}** in profit.

The **{top_region}** region continues to be the strongest contributor
to total sales performance.

The **{top_category}** category remains the leading revenue generator
and represents a significant growth opportunity.
""")

st.divider()

# Key Business Highlights
st.subheader("Key Business Highlights")

c1, c2, c3 = st.columns(3)

with c1:
    st.success(f"""
Revenue Leader

{top_region}
""")

with c2:
    st.success(f"""
Best Category

{top_category}
""")

with c3:
    st.success(f"""
Average Order Value

${avg_order:,.2f}
""")

st.divider()

# Strategic Recommendations
st.subheader("Strategic Recommendations")

st.info(f"""
Increase inventory allocation for **{top_category}** products.

Expand marketing initiatives within the **{top_region}** region.

Monitor underperforming categories to identify optimization opportunities.

Use forecasting outputs to improve inventory planning and resource allocation.
""")

st.divider()

# Growth Opportunities
st.subheader("Growth Opportunities")

st.markdown(f"""
• Strengthen market presence in high-performing regions.

• Increase cross-selling opportunities within **{top_category}**.

• Improve customer retention through targeted campaigns.

• Leverage predictive forecasting for demand planning.

• Optimize inventory levels using historical sales trends.
""")

st.divider()

# Footer
st.caption(
    "Insights are automatically generated from the latest sales dataset."
)