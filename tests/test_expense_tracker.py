import unittest

from modules.validator import (
    validate_amount,
    validate_date,
    validate_category,
    validate_description,
    validate_menu_choice
)

from modules.expense_manager import (
    get_next_expense_id,
    find_expense_by_id
)

from modules.reports import (
    calculate_total,
    calculate_average,
    highest_expense,
    lowest_expense,
    category_summary,
    monthly_summary
)


class TestValidator(unittest.TestCase):

    def test_valid_amount(self):
        valid, result = validate_amount("250")
        self.assertTrue(valid)
        self.assertEqual(result, 250.0)

    def test_invalid_amount(self):
        valid, result = validate_amount("abc")
        self.assertFalse(valid)

    def test_negative_amount(self):
        valid, result = validate_amount("-100")
        self.assertFalse(valid)

    def test_valid_date(self):
        valid, result = validate_date("2026-08-20")
        self.assertTrue(valid)

    def test_invalid_date(self):
        valid, result = validate_date("20-08-2026")
        self.assertFalse(valid)

    def test_valid_category(self):
        valid, result = validate_category("Food")
        self.assertTrue(valid)
        self.assertEqual(result, "Food")

    def test_invalid_category(self):
        valid, result = validate_category("InvalidCategory")
        self.assertFalse(valid)

    def test_valid_description(self):
        valid, result = validate_description("Lunch")
        self.assertTrue(valid)

    def test_empty_description(self):
        valid, result = validate_description("")
        self.assertFalse(valid)

    def test_valid_menu_choice(self):
        valid, result = validate_menu_choice("3", 1, 5)
        self.assertTrue(valid)
        self.assertEqual(result, 3)

    def test_invalid_menu_choice(self):
        valid, result = validate_menu_choice("8", 1, 5)
        self.assertFalse(valid)


class TestExpenseManager(unittest.TestCase):

    def setUp(self):
        self.expenses = [
            {
                "id": 1,
                "date": "2026-08-23",
                "category": "Food",
                "description": "Lunch",
                "amount": 250.00
            },
            {
                "id": 2,
                "date": "2026-08-22",
                "category": "Transport",
                "description": "Bus",
                "amount": 100.00
            }
        ]

    def test_next_expense_id(self):
        next_id = get_next_expense_id(self.expenses)
        self.assertEqual(next_id, 3)

    def test_next_id_empty_list(self):
        next_id = get_next_expense_id([])
        self.assertEqual(next_id, 1)

    def test_find_expense(self):
        expense = find_expense_by_id(
            self.expenses,
            1
        )

        self.assertIsNotNone(expense)
        self.assertEqual(expense["category"], "Food")

    def test_find_nonexistent_expense(self):
        expense = find_expense_by_id(
            self.expenses,
            99
        )

        self.assertIsNone(expense)


class TestReports(unittest.TestCase):

    def setUp(self):
        self.expenses = [
            {
                "id": 1,
                "date": "2026-08-23",
                "category": "Food",
                "description": "Lunch",
                "amount": 250.00
            },
            {
                "id": 2,
                "date": "2026-08-22",
                "category": "Transport",
                "description": "Bus",
                "amount": 100.00
            },
            {
                "id": 3,
                "date": "2026-08-20",
                "category": "Food",
                "description": "Dinner",
                "amount": 300.00
            }
        ]

    def test_total(self):
        total = calculate_total(self.expenses)
        self.assertEqual(total, 650.00)

    def test_average(self):
        average = calculate_average(self.expenses)
        self.assertAlmostEqual(
            average,
            216.666666,
            places=2
        )

    def test_highest_expense(self):
        highest = highest_expense(self.expenses)

        self.assertEqual(
            highest["amount"],
            300.00
        )

    def test_lowest_expense(self):
        lowest = lowest_expense(self.expenses)

        self.assertEqual(
            lowest["amount"],
            100.00
        )

    def test_category_summary(self):
        summary = category_summary(self.expenses)

        self.assertEqual(
            summary["Food"],
            550.00
        )

        self.assertEqual(
            summary["Transport"],
            100.00
        )

    def test_monthly_summary(self):
        summary = monthly_summary(self.expenses)

        self.assertEqual(
            summary["August 2026"],
            650.00
        )


if __name__ == "__main__":
    unittest.main()