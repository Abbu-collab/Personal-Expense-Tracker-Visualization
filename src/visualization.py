import matplotlib.pyplot as plt
import seaborn as sns
import os

# Create images folder
os.makedirs("images", exist_ok=True)

sns.set_style("whitegrid")

def category_bar_chart(category_data):

    plt.figure(figsize=(8, 5))

    category_data.plot(kind='bar')

    plt.title("Category Wise Spending")
    plt.xlabel("Category")
    plt.ylabel("Amount")

    plt.tight_layout()

    plt.savefig("images/category_wise_spending.png")

    plt.close()

    print("Category Bar Chart Saved!")


def monthly_line_chart(monthly_data):

    plt.figure(figsize=(8, 5))

    monthly_data.plot(kind='line', marker='o')

    plt.title("Monthly Spending Trend")
    plt.xlabel("Month")
    plt.ylabel("Amount")

    plt.tight_layout()

    plt.savefig("images/monthly_spending_trend.png")

    plt.close()

    print("Monthly Line Chart Saved!")


def payment_pie_chart(payment_data):

    plt.figure(figsize=(6, 6))

    payment_data.plot(kind='pie', autopct='%1.1f%%')

    plt.title("Payment Method Analysis")

    plt.ylabel("")

    plt.tight_layout()

    plt.savefig("images/payment_method_analysis.png")

    plt.close()

    print("Payment Pie Chart Saved!")


def daily_spending_chart(daily_data):

    plt.figure(figsize=(10, 5))

    daily_data.plot(kind='line', marker='o')

    plt.title("Daily Spending Trend")
    plt.xlabel("Date")
    plt.ylabel("Amount")

    plt.tight_layout()

    plt.savefig("images/daily_spending_trend.png")

    plt.close()

    print("Daily Spending Trend Chart Saved!")