import csv
import os


# ==========================================
# FILE HANDLER MODULE
# Personal Expense Tracker
# ==========================================

CSV_FILE = "data/expenses.csv"

FIELDNAMES = [
    "id",
    "date",
    "category",
    "description",
    "amount"
]


def initialize_csv():
    """
    Create the CSV file and data directory
    if they do not already exist.
    """

    try:
        os.makedirs("data", exist_ok=True)

        if not os.path.exists(CSV_FILE):
            with open(
                CSV_FILE,
                "w",
                newline="",
                encoding="utf-8"
            ) as file:

                writer = csv.DictWriter(
                    file,
                    fieldnames=FIELDNAMES
                )

                writer.writeheader()

            return True, "CSV file created successfully."

        return True, "CSV file already exists."

    except OSError as error:
        return False, f"Unable to initialize CSV file: {error}"


def save_expenses(expenses):
    """
    Save all expense records to the CSV file.
    """

    try:
        initialize_csv()

        with open(
            CSV_FILE,
            "w",
            newline="",
            encoding="utf-8"
        ) as file:

            writer = csv.DictWriter(
                file,
                fieldnames=FIELDNAMES
            )

            writer.writeheader()

            for expense in expenses:
                writer.writerow(expense)

        return True, "Expenses saved successfully."

    except PermissionError:
        return False, "Permission denied while saving expenses."

    except OSError as error:
        return False, f"Error saving expenses: {error}"


def load_expenses():
    """
    Load expense records from the CSV file.
    """

    expenses = []

    try:
        initialize_csv()

        with open(
            CSV_FILE,
            "r",
            newline="",
            encoding="utf-8"
        ) as file:

            reader = csv.DictReader(file)

            if reader.fieldnames is None:
                return [], "CSV file has no header."

            missing_fields = [
                field
                for field in FIELDNAMES
                if field not in reader.fieldnames
            ]

            if missing_fields:
                return [], (
                    "CSV file is missing required fields: "
                    + ", ".join(missing_fields)
                )

            for row_number, row in enumerate(
                reader,
                start=2
            ):

                try:
                    expense = {
                        "id": int(row["id"]),
                        "date": row["date"],
                        "category": row["category"],
                        "description": row["description"],
                        "amount": float(row["amount"])
                    }

                    expenses.append(expense)

                except (ValueError, TypeError, KeyError) as error:
                    print(
                        f"Warning: Skipping invalid CSV "
                        f"row {row_number}: {error}"
                    )

        return expenses, (
            f"{len(expenses)} expense(s) loaded successfully."
        )

    except FileNotFoundError:
        return [], "Expense file not found."

    except PermissionError:
        return [], "Permission denied while reading expenses."

    except OSError as error:
        return [], f"Error loading expenses: {error}"