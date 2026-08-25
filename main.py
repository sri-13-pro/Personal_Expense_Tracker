from modules.file_handler import (
    initialize_csv,
    load_expenses,
    save_expenses
)

from modules.expense_manager import (
    add_expense,
    view_expenses,
    edit_expense,
    delete_expense,
    categorize_expenses
)

from modules.reports import generate_report

from modules.visualization import show_visualization_menu


# ==========================================
# PERSONAL EXPENSE TRACKER
# MAIN APPLICATION
# ==========================================


def display_banner():
    """Display application title."""

    print("\n" + "=" * 60)
    print("             PERSONAL EXPENSE TRACKER")
    print("=" * 60)
    print("       Manage • Analyze • Visualize")
    print("=" * 60)


def display_main_menu():
    """Display the main application menu."""

    print("\n" + "-" * 60)
    print("                    MAIN MENU")
    print("-" * 60)

    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Search / Filter Expenses")
    print("4. Edit Expense")
    print("5. Delete Expense")
    print("6. Categorize Expenses")
    print("7. Generate Report")
    print("8. Visualize Expenses")
    print("9. Save Expenses")
    print("10. Exit")

    print("-" * 60)


def search_expenses(expenses):
    """
    Search and filter expenses.

    This provides the Phase 5 search/filtering functionality.
    """

    if not expenses:
        print("\nNo expenses available for searching.")
        return

    while True:

        print("\n" + "=" * 55)
        print("              SEARCH / FILTER EXPENSES")
        print("=" * 55)

        print("1. Filter by Category")
        print("2. Filter by Date")
        print("3. Filter by Month")
        print("4. Filter by Amount Range")
        print("5. Back")

        choice = input(
            "\nEnter your choice: "
        ).strip()

        if choice == "1":
            filter_by_category(expenses)

        elif choice == "2":
            filter_by_date(expenses)

        elif choice == "3":
            filter_by_month(expenses)

        elif choice == "4":
            filter_by_amount(expenses)

        elif choice == "5":
            break

        else:
            print("Invalid choice. Please try again.")


def display_filtered_expenses(expenses):
    """Display filtered expense records."""

    if not expenses:
        print("\nNo matching expenses found.")
        return

    print("\n" + "=" * 80)
    print("                   SEARCH RESULTS")
    print("=" * 80)

    print(
        f"{'ID':<5}"
        f"{'Date':<15}"
        f"{'Category':<18}"
        f"{'Description':<25}"
        f"{'Amount':>12}"
    )

    print("-" * 80)

    for expense in expenses:
        print(
            f"{expense['id']:<5}"
            f"{expense['date']:<15}"
            f"{expense['category']:<18}"
            f"{expense['description'][:23]:<25}"
            f"₹{expense['amount']:>10.2f}"
        )

    print("-" * 80)


def filter_by_category(expenses):
    """Filter expenses by category."""

    category = input(
        "\nEnter category: "
    ).strip().lower()

    results = [
        expense
        for expense in expenses
        if expense["category"].lower() == category
    ]

    display_filtered_expenses(results)


def filter_by_date(expenses):
    """Filter expenses by exact date."""

    date = input(
        "\nEnter date (YYYY-MM-DD): "
    ).strip()

    results = [
        expense
        for expense in expenses
        if expense["date"] == date
    ]

    display_filtered_expenses(results)


def filter_by_month(expenses):
    """Filter expenses by month."""

    month = input(
        "\nEnter month (YYYY-MM): "
    ).strip()

    results = [
        expense
        for expense in expenses
        if expense["date"].startswith(month)
    ]

    display_filtered_expenses(results)


def filter_by_amount(expenses):
    """Filter expenses within an amount range."""

    try:
        minimum = float(
            input("Enter minimum amount: ").strip()
        )

        maximum = float(
            input("Enter maximum amount: ").strip()
        )

        if minimum < 0 or maximum < 0:
            print("Amount cannot be negative.")
            return

        if minimum > maximum:
            print(
                "Minimum amount cannot be greater "
                "than maximum amount."
            )
            return

        results = [
            expense
            for expense in expenses
            if minimum <= expense["amount"] <= maximum
        ]

        display_filtered_expenses(results)

    except ValueError:
        print("Please enter valid numeric amounts.")


def main():
    """Run the Personal Expense Tracker."""

    display_banner()

    # Initialize CSV file
    success, message = initialize_csv()

    if not success:
        print(f"\nError: {message}")
        return

    # Load existing expenses
    expenses, message = load_expenses()

    print(f"\n{message}")

    while True:

        display_main_menu()

        choice = input(
            "Enter your choice: "
        ).strip()

        if choice == "1":

            add_expense(expenses)

        elif choice == "2":

            view_expenses(expenses)

        elif choice == "3":

            search_expenses(expenses)

        elif choice == "4":

            edit_expense(expenses)

        elif choice == "5":

            delete_expense(expenses)

        elif choice == "6":

            categorize_expenses(expenses)

        elif choice == "7":

            generate_report(expenses)

        elif choice == "8":

            show_visualization_menu(expenses)

        elif choice == "9":

            success, message = save_expenses(expenses)
            print(f"\n{message}")

        elif choice == "10":

            success, message = save_expenses(expenses)

            if success:
                print(f"\n{message}")

            print("\nThank you for using Personal Expense Tracker!")
            print("Goodbye!")
            break

        else:

            print(
                "\nInvalid choice. "
                "Please enter a number from 1 to 10."
            )


# ==========================================
# PROGRAM ENTRY POINT
# ==========================================

if __name__ == "__main__":
    main()