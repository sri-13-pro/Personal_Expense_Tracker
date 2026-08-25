# 🧪 Tests

This directory contains the automated tests for the Personal Expense
Tracker.

The project uses Python's built-in `unittest` framework.

---

## 📄 Test File

### `test_expense_tracker.py`

The test suite verifies important application functionality including:

- Expense management
- Expense ID generation
- Expense searching
- Report calculations
- Category summaries
- Monthly summaries
- Input validation
- Date validation
- Amount validation
- Category validation
- Description validation
- Menu validation

---

## ▶️ Running Tests

Run the following command from the project root:

```bash
python -m unittest discover -s tests -p "test_*.py" -v
