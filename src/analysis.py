def category_analysis(df):

    category_data = df.groupby("Category")["Amount"].sum()

    print("\nCategory-wise Analysis:")
    print(category_data)

    return category_data


def monthly_analysis(df):

    monthly_data = df.groupby("Month")["Amount"].sum()

    print("\nMonthly Analysis:")
    print(monthly_data)

    return monthly_data


def payment_method_analysis(df):

    payment_data = df.groupby("Payment_Method")["Amount"].sum()

    print("\nPayment Method Analysis:")
    print(payment_data)

    return payment_data


def daily_spending_analysis(df):

    daily_data = df.groupby("Date")["Amount"].sum()

    print("\nDaily Spending:")
    print(daily_data)

    return daily_data


def highest_spending_category(category_data):

    highest = category_data.idxmax()

    print("\nHighest Spending Category:", highest)

    return highest


def average_daily_spending(daily_data):

    average = daily_data.mean()

    print("\nAverage Daily Spending:", average)

    return average