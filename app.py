import streamlit as st

st.set_page_config(
    page_title="SmartDemand AI",
    page_icon="📊",
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

h2, h3 {
    color: #1E293B;
}

div[data-testid="stInfo"] {
    border-radius: 12px;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
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

# Hero Section
st.title("SmartDemand AI")

st.caption(
    "Sales Forecasting & Business Intelligence Platform"
)

st.markdown("""
Transform raw sales data into actionable insights, business analytics,
AI-powered recommendations, and future demand forecasts.
""")

st.divider()

# Capabilities
st.subheader("Platform Capabilities")

col1, col2, col3 = st.columns(3)

with col1:
    st.info("""
**Dashboard**

Monitor KPIs, revenue,
profitability and business performance.
""")

with col2:
    st.info("""
**Analytics**

Explore trends across
categories, products and regions.
""")

with col3:
    st.info("""
**AI Insights**

Generate intelligent business
recommendations from sales data.
""")

col4, col5 = st.columns(2)

with col4:
    st.info("""
**Forecasting**

Predict future sales demand
using Machine Learning.
""")

with col5:
    st.info("""
**Reports**

Export reports and analyze
business performance.
""")

st.divider()

# Business Value
st.subheader("Business Value")

c1, c2, c3 = st.columns(3)

with c1:
    st.success("Real-Time Analytics")

with c2:
    st.success("Machine Learning Forecasting")

with c3:
    st.success("Data-Driven Decisions")

st.markdown("""
Organizations can use SmartDemand AI to monitor performance,
identify growth opportunities and improve operational planning.
""")

st.divider()

# Business Profile
st.subheader("Business Profile")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
**Industry**

Retail & E-Commerce

**Business Type**

Multi-Region Superstore

**Regions Covered**

West, East, Central, South
""")

with col2:
    st.markdown("""
**Product Lines**

• Furniture

• Office Supplies

• Technology

**Objective**

Analyze sales performance and forecast future demand.
""")

st.divider()

# Footer
st.caption(
    "SmartDemand AI v2 • Built with Python, Streamlit, Pandas, Plotly and Scikit-Learn"
)