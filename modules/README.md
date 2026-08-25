# 📦 Application Modules

This directory contains the core Python modules used to implement the
Personal Expense Tracker.

The application follows a modular programming approach where different
functional responsibilities are separated into individual modules.

---

## 📂 Modules

| Module | Responsibility |
|---|---|
| `expense_manager.py` | Manages expense records and operations |
| `file_handler.py` | Handles CSV data storage and retrieval |
| `validator.py` | Validates user inputs |
| `reports.py` | Generates expense reports and calculations |
| `visualization.py` | Generates graphical expense visualizations |

---

## 🔹 expense_manager.py

Handles the main expense management operations:

- Add expenses
- View expenses
- Edit expenses
- Delete expenses
- Search expenses
- Filter expenses
- Categorize expenses

---

## 🔹 file_handler.py

Responsible for persistent data storage.

It provides functionality for:

- Loading expenses from CSV
- Saving expenses to CSV
- Maintaining expense records between application sessions

---

## 🔹 validator.py

Provides input validation for:

- Expense amounts
- Dates
- Categories
- Descriptions
- Menu selections

The validation layer prevents invalid data from entering the system.

---

## 🔹 reports.py

Performs expense calculations and generates analytical information
including:

- Total spending
- Average expense
- Highest expense
- Lowest expense
- Category-wise spending
- Monthly spending

---

## 🔹 visualization.py

Uses Matplotlib to generate graphical representations of expense data.

Supported visualizations include:

- Category-wise bar chart
- Category-wise pie chart
- Monthly spending chart

---

## 🔄 Module Flow

```text
main.py
   │
   ├── expense_manager.py
   │
   ├── validator.py
   │
   ├── file_handler.py
   │
   ├── reports.py
   │
   └── visualization.py
