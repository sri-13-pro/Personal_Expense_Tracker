from collections import defaultdict
from datetime import datetime


# ==========================================
# REPORTS MODULE
# Personal Expense Tracker
# ==========================================


def calculate_total(expenses):
    """
    Calculate total spending.
    """

    return sum(
        expense["amount"]
        for expense in expenses
    )


def calculate_average(expenses):
    """
    Calculate average expense.
    """

    if not expenses:
        return 0.0

    return calculate_total(expenses) / len(expenses)


def highest_expense(expenses):
    """
    Find the highest expense.
    """

    if not expenses:
        return None

    return max(
        expenses,
        key=lambda expense: expense["amount"]
    )


def lowest_expense(expenses):
    """
    Find the lowest expense.
    """

    if not expenses:
        return None

    return min(
        expenses,
        key=lambda expense: expense["amount"]
    )


def category_summary(expenses):
    """
    Calculate total spending for each category.
    """

    category_totals = defaultdict(float)

    for expense in expenses:
        category = expense["category"]
        category_totals[category] += expense["amount"]

    return dict(category_totals)


def monthly_summary(expenses):
    """
    Calculate total spending for each month.
    """

    monthly_totals = defaultdict(float)

    for expense in expenses:
        try:
            date = datetime.strptime(
                expense["date"],
                "%Y-%m-%d"
            )

            month_name = date.strftime("%B %Y")
            monthly_totals[month_name] += expense["amount"]

        except (ValueError, TypeError):
            continue

    return dict(monthly_totals)


def generate_report(expenses):
    """
    Generate and display a complete expense report.
    """

    print("\n" + "=" * 65)
    print("                     EXPENSE REPORT")
    print("=" * 65)

    if not expenses:
        print("No expenses available for generating a report.")
        return

    # Overall calculations
    total = calculate_total(expenses)
    average = calculate_average(expenses)
    highest = highest_expense(expenses)
    lowest = lowest_expense(expenses)

    print("\nOVERALL SUMMARY")
    print("-" * 65)

    print(f"Number of Expenses : {len(expenses)}")
    print(f"Total Spending     : ₹{total:.2f}")
    print(f"Average Expense    : ₹{average:.2f}")

    if highest:
        print(
            f"Highest Expense    : ₹{highest['amount']:.2f}"
        )
        print(
            f"Highest Category   : {highest['category']}"
        )
        print(
            f"Highest Date       : {highest['date']}"
        )

    if lowest:
        print(
            f"Lowest Expense     : ₹{lowest['amount']:.2f}"
        )
        print(
            f"Lowest Category    : {lowest['category']}"
        )
        print(
            f"Lowest Date        : {lowest['date']}"
        )

    # Category summary
    print("\nCATEGORY-WISE SPENDING")
    print("-" * 65)

    categories = category_summary(expenses)

    for category, amount in sorted(
        categories.items(),
        key=lambda item: item[1],
        reverse=True
    ):
        percentage = (amount / total) * 100

        print(
            f"{category:<20}"
            f"₹{amount:>12.2f}  "
            f"({percentage:>6.2f}%)"
        )

    # Monthly summary
    print("\nMONTHLY SPENDING")
    print("-" * 65)

    months = monthly_summary(expenses)

    for month, amount in months.items():
        print(
            f"{month:<20}"
            f"₹{amount:>12.2f}"
        )

    print("-" * 65)