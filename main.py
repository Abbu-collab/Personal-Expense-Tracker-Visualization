from src.data_loader import load_data
from src.data_cleaning import clean_data

from src.analysis import (
    category_analysis,
    monthly_analysis,
    payment_method_analysis,
    daily_spending_analysis,
    highest_spending_category,
    average_daily_spending
)

from src.visualization import (
    category_bar_chart,
    monthly_line_chart,
    payment_pie_chart,
    daily_spending_chart
)

from src.report_generator import generate_report

# -----------------------------
# STEP 1: LOAD DATA
# -----------------------------

file_path = "data/expense_data.csv"

df = load_data(file_path)

print(df.head())

# -----------------------------
# STEP 2: CLEAN DATA
# -----------------------------

df = clean_data(df)

# -----------------------------
# STEP 3: ANALYSIS
# -----------------------------

category_data = category_analysis(df)

monthly_data = monthly_analysis(df)

payment_data = payment_method_analysis(df)

daily_data = daily_spending_analysis(df)

highest_category = highest_spending_category(category_data)

average_spending = average_daily_spending(daily_data)

# Total Spending
total_spending = df["Amount"].sum()

print("\nTotal Spending:", total_spending)

# -----------------------------
# STEP 4: VISUALIZATION
# -----------------------------

category_bar_chart(category_data)

monthly_line_chart(monthly_data)

payment_pie_chart(payment_data)

daily_spending_chart(daily_data)

# -----------------------------
# STEP 5: REPORT GENERATION
# -----------------------------

generate_report(
    total_spending,
    average_spending,
    highest_category
)

print("\nProject Executed Successfully!")