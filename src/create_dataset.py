import pandas as pd
import os

# Create data folder if not exists
os.makedirs("data", exist_ok=True)

expense_data = {
    "Date": [
        "2026-01-01", "2026-01-02", "2026-01-03",
        "2026-01-04", "2026-01-05", "2026-01-06",
        "2026-02-01", "2026-02-03", "2026-02-05",
        "2026-03-01", "2026-03-02", "2026-03-03"
    ],

    "Category": [
        "Food", "Travel", "Shopping",
        "Bills", "Entertainment", "Food",
        "Travel", "Food", "Bills",
        "Shopping", "Food", "Travel"
    ],

    "Amount": [
        250, 500, 1200,
        1500, 700, 300,
        600, 450, 1800,
        2000, 350, 750
    ],

    "Payment_Method": [
        "UPI", "Cash", "Card",
        "UPI", "Card", "Cash",
        "UPI", "Card", "Cash",
        "UPI", "Card", "Cash"
    ],

    "Note": [
        "Lunch", "Bus", "Clothes",
        "Electricity Bill", "Movie", "Dinner",
        "Train", "Snacks", "Internet Bill",
        "Mobile", "Breakfast", "Cab"
    ]
}

# Convert to DataFrame
df = pd.DataFrame(expense_data)

# Save CSV
df.to_csv("data/expense_data.csv", index=False)

print("Expense dataset created successfully!")