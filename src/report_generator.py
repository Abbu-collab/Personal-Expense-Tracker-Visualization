import pandas as pd
import os

# Create reports folder
os.makedirs("reports", exist_ok=True)

def generate_report(total_spending,
                    average_spending,
                    highest_category):

    report = {
        "Total Spending": [total_spending],
        "Average Daily Spending": [average_spending],
        "Highest Spending Category": [highest_category]
    }

    report_df = pd.DataFrame(report)

    report_df.to_csv(
        "reports/expense_summary_report.csv",
        index=False
    )

    print("\nSummary Report Generated Successfully!")