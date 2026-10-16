import streamlit as st

from src.read_database import (
    read_financial_data,
    read_financial_ratios
)


# --------------------------------------------------
# Page configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Financial Health Analysis",
    page_icon="📊",
    layout="wide"
)


# --------------------------------------------------
# Load data from Supabase PostgreSQL
# --------------------------------------------------

financial_data_df = read_financial_data()
financial_ratios_df = read_financial_ratios()


# --------------------------------------------------
# Dashboard title
# --------------------------------------------------

st.title("📊 Financial Health Analysis")

st.write(
    "Interactive analysis of financial liquidity "
    "and working capital."
)


# --------------------------------------------------
# Year selector
# --------------------------------------------------

selected_year = st.selectbox(
    "Select Year",
    financial_data_df["year"].sort_values(
        ascending=False
    )
)


# Get data for selected year
selected_financial_data = financial_data_df[
    financial_data_df["year"] == selected_year
].iloc[0]

selected_ratio_data = financial_ratios_df[
    financial_ratios_df["year"] == selected_year
].iloc[0]


# --------------------------------------------------
# KPI cards
# --------------------------------------------------

st.subheader(f"Financial Overview — {selected_year}")

col1, col2, col3, col4 = st.columns(4)


col1.metric(
    label="Current Ratio",
    value=f"{selected_ratio_data['current_ratio']:.2f}"
)


col2.metric(
    label="Quick Ratio",
    value=f"{selected_ratio_data['quick_ratio']:.2f}"
)


col3.metric(
    label="Cash Ratio",
    value=f"{selected_ratio_data['cash_ratio']:.2f}"
)


col4.metric(
    label="Working Capital",
    value=f"{selected_ratio_data['working_capital']:,.0f}"
)


st.divider()


# --------------------------------------------------
# Liquidity ratio trends
# --------------------------------------------------

st.subheader("📈 Liquidity Ratio Trends")


ratio_chart_data = (
    financial_ratios_df[
        [
            "year",
            "current_ratio",
            "quick_ratio",
            "cash_ratio"
        ]
    ]
    .set_index("year")
)


st.line_chart(
    ratio_chart_data
)


st.divider()


# --------------------------------------------------
# Assets vs liabilities
# --------------------------------------------------

left_column, right_column = st.columns(2)


with left_column:

    st.subheader("Assets vs Liabilities")

    asset_liability_data = (
        financial_data_df[
            [
                "year",
                "current_asset",
                "current_liabilities"
            ]
        ]
        .set_index("year")
    )

    st.bar_chart(
        asset_liability_data
    )


# --------------------------------------------------
# Working capital trend
# --------------------------------------------------

with right_column:

    st.subheader("Working Capital Trend")

    working_capital_data = (
        financial_ratios_df[
            [
                "year",
                "working_capital"
            ]
        ]
        .set_index("year")
    )

    st.line_chart(
        working_capital_data
    )


st.divider()


# --------------------------------------------------
# Selected year's financial details
# --------------------------------------------------

st.subheader(f"Financial Details — {selected_year}")


detail_col1, detail_col2, detail_col3 = st.columns(3)


detail_col1.metric(
    "Current Assets",
    f"{selected_financial_data['current_asset']:,.0f}"
)


detail_col2.metric(
    "Current Liabilities",
    f"{selected_financial_data['current_liabilities']:,.0f}"
)


detail_col3.metric(
    "Cash",
    f"{selected_financial_data['cash']:,.0f}"
)


# --------------------------------------------------
# Raw data
# --------------------------------------------------

with st.expander("View Raw Financial Data"):

    st.dataframe(
        financial_data_df,
        use_container_width=True
    )


with st.expander("View Financial Ratio Data"):

    st.dataframe(
        financial_ratios_df,
        use_container_width=True
    )