import streamlit as st
import pandas as pd
import plotly.express as px
import os

# ---------------------------------
# PAGE CONFIGURATION
# ---------------------------------

st.set_page_config(
    page_title="Personal Expense Tracker",
    page_icon="💰",
    layout="wide"
)

# ---------------------------------
# TITLE
# ---------------------------------

st.title("💰 Personal Expense Tracker Dashboard")
st.markdown("### Analyze Your Expenses Professionally")

# ---------------------------------
# CREATE DATA FOLDER
# ---------------------------------

os.makedirs("data", exist_ok=True)

# ---------------------------------
# FILE UPLOAD
# ---------------------------------

uploaded_file = st.sidebar.file_uploader(
    "Upload Expense CSV",
    type=["csv"]
)

# ---------------------------------
# DEFAULT DATASET
# ---------------------------------

default_file = "data/expense_data.csv"

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
else:
    df = pd.read_csv(default_file)

# ---------------------------------
# DATA CLEANING
# ---------------------------------

df["Date"] = pd.to_datetime(df["Date"])

df.drop_duplicates(inplace=True)

df.dropna(inplace=True)

df["Month"] = df["Date"].dt.strftime("%B")

# ---------------------------------
# SIDEBAR FILTERS
# ---------------------------------

st.sidebar.header("Filter Expenses")

category_filter = st.sidebar.multiselect(
    "Select Category",
    options=df["Category"].unique(),
    default=df["Category"].unique()
)

payment_filter = st.sidebar.multiselect(
    "Select Payment Method",
    options=df["Payment_Method"].unique(),
    default=df["Payment_Method"].unique()
)

filtered_df = df[
    (df["Category"].isin(category_filter)) &
    (df["Payment_Method"].isin(payment_filter))
]

# ---------------------------------
# KPI CALCULATIONS
# ---------------------------------

total_spending = filtered_df["Amount"].sum()

average_spending = filtered_df["Amount"].mean()

highest_category = (
    filtered_df.groupby("Category")["Amount"]
    .sum()
    .idxmax()
)

transaction_count = filtered_df.shape[0]

# ---------------------------------
# KPI CARDS
# ---------------------------------

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("💸 Total Spending", f"₹ {total_spending}")

with col2:
    st.metric("📊 Average Expense", f"₹ {round(average_spending,2)}")

with col3:
    st.metric("🔥 Highest Category", highest_category)

with col4:
    st.metric("🧾 Transactions", transaction_count)

st.divider()

# ---------------------------------
# CATEGORY ANALYSIS
# ---------------------------------

category_data = (
    filtered_df.groupby("Category")["Amount"]
    .sum()
    .reset_index()
)

category_chart = px.bar(
    category_data,
    x="Category",
    y="Amount",
    title="Category Wise Spending",
    text_auto=True
)

st.plotly_chart(category_chart, use_container_width=True)

# ---------------------------------
# MONTHLY ANALYSIS
# ---------------------------------

monthly_data = (
    filtered_df.groupby("Month")["Amount"]
    .sum()
    .reset_index()
)

monthly_chart = px.line(
    monthly_data,
    x="Month",
    y="Amount",
    markers=True,
    title="Monthly Spending Trend"
)

st.plotly_chart(monthly_chart, use_container_width=True)

# ---------------------------------
# PAYMENT METHOD ANALYSIS
# ---------------------------------

payment_data = (
    filtered_df.groupby("Payment_Method")["Amount"]
    .sum()
    .reset_index()
)

payment_chart = px.pie(
    payment_data,
    names="Payment_Method",
    values="Amount",
    title="Payment Method Analysis"
)

st.plotly_chart(payment_chart, use_container_width=True)

# ---------------------------------
# DAILY SPENDING TREND
# ---------------------------------

daily_data = (
    filtered_df.groupby("Date")["Amount"]
    .sum()
    .reset_index()
)

daily_chart = px.line(
    daily_data,
    x="Date",
    y="Amount",
    markers=True,
    title="Daily Spending Trend"
)

st.plotly_chart(daily_chart, use_container_width=True)

# ---------------------------------
# DATA TABLE
# ---------------------------------

st.subheader("📁 Expense Dataset")

st.dataframe(filtered_df, use_container_width=True)

# ---------------------------------
# DOWNLOAD REPORT
# ---------------------------------

csv = filtered_df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="⬇ Download Expense Report",
    data=csv,
    file_name="expense_report.csv",
    mime="text/csv"
)

# ---------------------------------
# FOOTER
# ---------------------------------

st.markdown("---")

st.markdown(
    "Developed using Python, Pandas, Streamlit, and Plotly"
)