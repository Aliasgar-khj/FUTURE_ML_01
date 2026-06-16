import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Reports",
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
st.title("Reports Center")

st.caption(
    "Generate, review and export business reports from the latest dataset."
)

# Load Data
df = pd.read_csv("sales.csv", encoding="latin1")

# Summary Metrics
records = len(df)
regions = df["Region"].nunique()
categories = df["Category"].nunique()

col1, col2, col3 = st.columns(3)

col1.metric(
    "Records",
    f"{records:,}"
)

col2.metric(
    "Regions",
    regions
)

col3.metric(
    "Categories",
    categories
)

st.divider()

# Dataset Preview
st.subheader("Dataset Preview")

st.dataframe(
    df.head(20),
    use_container_width=True
)

st.caption(
    "Preview of the latest sales records available for analysis."
)

st.divider()

# Dataset Statistics
st.subheader("Dataset Statistics")

st.dataframe(
    df.describe(),
    use_container_width=True
)

st.caption(
    "Summary statistics generated automatically from the dataset."
)

st.divider()

# Export Section
st.subheader("Export Report")

st.markdown("""
Download the complete dataset for further analysis,
reporting or archival purposes.
""")

csv = df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="📥 Download Sales Report",
    data=csv,
    file_name="sales_report.csv",
    mime="text/csv"
)

st.divider()

# Footer
st.caption(
    "Reports are generated dynamically from the latest sales dataset."
)