from datetime import datetime


# ==========================================
# VALIDATOR MODULE
# Personal Expense Tracker
# ==========================================


CATEGORIES = [
    "Food",
    "Transport",
    "Entertainment",
    "Shopping",
    "Education",
    "Healthcare",
    "Bills",
    "Travel",
    "Other"
]


def validate_amount(amount):
    """
    Validate and return a positive expense amount.
    """

    try:
        amount = float(amount)

        if amount <= 0:
            return False, "Amount must be greater than zero."

        return True, round(amount, 2)

    except (ValueError, TypeError):
        return False, "Amount must be a valid number."


def validate_date(date):
    """
    Validate date in YYYY-MM-DD format.
    """

    try:
        expense_date = datetime.strptime(
            date,
            "%Y-%m-%d"
        )

        if expense_date > datetime.now():
            return False, "Future dates are not allowed."

        return True, date

    except (ValueError, TypeError):
        return False, "Date must be in YYYY-MM-DD format."


def validate_category(category):
    """
    Validate expense category.
    """

    if not isinstance(category, str):
        return False, "Category must be text."

    category = category.strip()

    for valid_category in CATEGORIES:
        if category.lower() == valid_category.lower():
            return True, valid_category

    return False, "Invalid expense category."


def validate_description(description):
    """
    Validate expense description.
    """

    if not isinstance(description, str):
        return False, "Description must be text."

    description = description.strip()

    if not description:
        return False, "Description cannot be empty."

    return True, description


def validate_menu_choice(choice, minimum, maximum):
    """
    Validate a menu choice within a given range.
    """

    try:
        choice = int(choice)

        if minimum <= choice <= maximum:
            return True, choice

        return False, (
            f"Please enter a number between "
            f"{minimum} and {maximum}."
        )

    except (ValueError, TypeError):
        return False, "Menu choice must be a number."