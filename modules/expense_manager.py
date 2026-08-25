from modules.validator import (
    validate_amount,
    validate_date,
    validate_category,
    validate_description,
    CATEGORIES
)


# ==========================================
# EXPENSE MANAGER MODULE
# Personal Expense Tracker
# ==========================================


def get_next_expense_id(expenses):
    """
    Generate the next unique expense ID.
    """

    if not expenses:
        return 1

    return max(expense["id"] for expense in expenses) + 1


def add_expense(expenses):
    """
    Add a new expense to the expense list.
    """

    print("\n" + "=" * 45)
    print("              ADD EXPENSE")
    print("=" * 45)

    # Amount
    while True:
        amount_input = input("Enter amount: ").strip()

        valid, result = validate_amount(amount_input)

        if valid:
            amount = result
            break

        print(f"Error: {result}")

    # Category
    print("\nAvailable Categories:")

    for index, category in enumerate(CATEGORIES, start=1):
        print(f"{index}. {category}")

    while True:
        category_input = input(
            "\nEnter category: "
        ).strip()

        valid, result = validate_category(category_input)

        if valid:
            category = result
            break

        print(f"Error: {result}")

    # Description
    while True:
        description_input = input(
            "Enter description: "
        ).strip()

        valid, result = validate_description(
            description_input
        )

        if valid:
            description = result
            break

        print(f"Error: {result}")

    # Date
    while True:
        date_input = input(
            "Enter date (YYYY-MM-DD): "
        ).strip()

        valid, result = validate_date(date_input)

        if valid:
            expense_date = result
            break

        print(f"Error: {result}")

    # Create expense dictionary
    expense = {
        "id": get_next_expense_id(expenses),
        "date": expense_date,
        "category": category,
        "description": description,
        "amount": amount
    }

    expenses.append(expense)

    print("\nExpense added successfully!")
    print(f"Expense ID: {expense['id']}")

    return expense


def view_expenses(expenses):
    """
    Display all expenses in a formatted table.
    """

    print("\n" + "=" * 80)
    print("                         ALL EXPENSES")
    print("=" * 80)

    if not expenses:
        print("No expenses found.")
        return

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

    total = sum(
        expense["amount"]
        for expense in expenses
    )

    print(f"{'Total:':>63} ₹{total:>10.2f}")


def find_expense_by_id(expenses, expense_id):
    """
    Find an expense using its ID.
    """

    for expense in expenses:
        if expense["id"] == expense_id:
            return expense

    return None


def edit_expense(expenses):
    """
    Edit an existing expense.
    """

    if not expenses:
        print("\nNo expenses available to edit.")
        return False

    view_expenses(expenses)

    try:
        expense_id = int(
            input("\nEnter Expense ID to edit: ").strip()
        )
    except ValueError:
        print("Error: Expense ID must be a number.")
        return False

    expense = find_expense_by_id(
        expenses,
        expense_id
    )

    if expense is None:
        print("Error: Expense not found.")
        return False

    print("\nPress Enter to keep the existing value.")

    # Amount
    while True:
        amount_input = input(
            f"Amount [{expense['amount']}]: "
        ).strip()

        if not amount_input:
            break

        valid, result = validate_amount(amount_input)

        if valid:
            expense["amount"] = result
            break

        print(f"Error: {result}")

    # Category
    print("\nAvailable Categories:")

    for index, category in enumerate(CATEGORIES, start=1):
        print(f"{index}. {category}")

    while True:
        category_input = input(
            f"Category [{expense['category']}]: "
        ).strip()

        if not category_input:
            break

        valid, result = validate_category(category_input)

        if valid:
            expense["category"] = result
            break

        print(f"Error: {result}")

    # Description
    while True:
        description_input = input(
            f"Description [{expense['description']}]: "
        ).strip()

        if not description_input:
            break

        valid, result = validate_description(
            description_input
        )

        if valid:
            expense["description"] = result
            break

        print(f"Error: {result}")

    # Date
    while True:
        date_input = input(
            f"Date [{expense['date']}]: "
        ).strip()

        if not date_input:
            break

        valid, result = validate_date(date_input)

        if valid:
            expense["date"] = result
            break

        print(f"Error: {result}")

    print("\nExpense updated successfully!")

    return True


def delete_expense(expenses):
    """
    Delete an expense using its ID.
    """

    if not expenses:
        print("\nNo expenses available to delete.")
        return False

    view_expenses(expenses)

    try:
        expense_id = int(
            input("\nEnter Expense ID to delete: ").strip()
        )
    except ValueError:
        print("Error: Expense ID must be a number.")
        return False

    expense = find_expense_by_id(
        expenses,
        expense_id
    )

    if expense is None:
        print("Error: Expense not found.")
        return False

    print("\nSelected Expense:")
    print(f"Date       : {expense['date']}")
    print(f"Category   : {expense['category']}")
    print(f"Description: {expense['description']}")
    print(f"Amount     : ₹{expense['amount']:.2f}")

    confirmation = input(
        "\nAre you sure you want to delete this expense? (y/n): "
    ).strip().lower()

    if confirmation == "y":
        expenses.remove(expense)
        print("Expense deleted successfully!")
        return True

    print("Delete operation cancelled.")
    return False


def categorize_expenses(expenses):
    """
    Display expenses grouped by category.
    """

    if not expenses:
        print("\nNo expenses available.")
        return

    print("\n" + "=" * 60)
    print("                 EXPENSES BY CATEGORY")
    print("=" * 60)

    categories = {}

    for expense in expenses:
        category = expense["category"]

        if category not in categories:
            categories[category] = []

        categories[category].append(expense)

    for category, category_expenses in categories.items():

        print(f"\n--- {category} ---")

        category_total = 0

        for expense in category_expenses:
            print(
                f"{expense['date']} | "
                f"{expense['description']} | "
                f"₹{expense['amount']:.2f}"
            )

            category_total += expense["amount"]

        print(
            f"Category Total: ₹{category_total:.2f}"
        )