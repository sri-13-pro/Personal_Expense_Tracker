import matplotlib.pyplot as plt

from modules.reports import (
    category_summary,
    monthly_summary
)


# ==========================================
# VISUALIZATION MODULE
# Personal Expense Tracker
# ==========================================


def category_bar_chart(expenses):
    """
    Display a bar chart showing spending
    by category.
    """

    if not expenses:
        print("\nNo expenses available for visualization.")
        return

    categories = category_summary(expenses)

    if not categories:
        print("\nNo category data available.")
        return

    names = list(categories.keys())
    amounts = list(categories.values())

    plt.figure(figsize=(10, 6))

    plt.bar(names, amounts)

    plt.title("Category-wise Expense")
    plt.xlabel("Category")
    plt.ylabel("Amount (₹)")

    plt.xticks(rotation=30)
    plt.tight_layout()

    plt.show()


def category_pie_chart(expenses):
    """
    Display a pie chart showing the distribution
    of spending across categories.
    """

    if not expenses:
        print("\nNo expenses available for visualization.")
        return

    categories = category_summary(expenses)

    if not categories:
        print("\nNo category data available.")
        return

    names = list(categories.keys())
    amounts = list(categories.values())

    plt.figure(figsize=(8, 8))

    plt.pie(
        amounts,
        labels=names,
        autopct="%1.1f%%",
        startangle=90
    )

    plt.title("Expense Distribution by Category")

    plt.tight_layout()

    plt.show()


def monthly_spending_chart(expenses):
    """
    Display a bar chart showing monthly spending.
    """

    if not expenses:
        print("\nNo expenses available for visualization.")
        return

    months = monthly_summary(expenses)

    if not months:
        print("\nNo monthly data available.")
        return

    month_names = list(months.keys())
    amounts = list(months.values())

    plt.figure(figsize=(10, 6))

    plt.bar(month_names, amounts)

    plt.title("Monthly Spending")
    plt.xlabel("Month")
    plt.ylabel("Amount (₹)")

    plt.xticks(rotation=30)
    plt.tight_layout()

    plt.show()


def show_visualization_menu(expenses):
    """
    Display the visualization menu.
    """

    while True:

        print("\n" + "=" * 50)
        print("              EXPENSE VISUALIZATION")
        print("=" * 50)

        print("1. Category-wise Bar Chart")
        print("2. Category-wise Pie Chart")
        print("3. Monthly Spending Chart")
        print("4. Back to Main Menu")

        choice = input(
            "\nEnter your choice: "
        ).strip()

        if choice == "1":
            category_bar_chart(expenses)

        elif choice == "2":
            category_pie_chart(expenses)

        elif choice == "3":
            monthly_spending_chart(expenses)

        elif choice == "4":
            break

        else:
            print(
                "Invalid choice. "
                "Please enter a number from 1 to 4."
            )