# PERSONAL EXPENSE TRACKER

## PROJECT TECHNICAL DOCUMENTATION

---

# 1. INTRODUCTION

## 1.1 Project Overview

Personal Expense Tracker is a command-line-based Python application
developed to help users record, manage, analyze, and visualize their
personal expenses.

The application allows users to add, view, edit, delete, categorize,
search, and filter expenses. It also provides reports and graphical
visualizations to help users understand their spending patterns.

Expense records are stored in a CSV file so that the data remains
available when the application is restarted.

---

# 2. PROBLEM STATEMENT

Managing daily expenses manually can make it difficult to maintain an
organized record of spending and understand spending patterns.

Users may need to track different types of expenses such as food,
transport, shopping, entertainment, bills, and travel.

The Personal Expense Tracker provides a simple command-line solution
for recording expenses, organizing them into categories, generating
useful reports, and visualizing spending data.

---

# 3. OBJECTIVES

The main objectives of the project are:

- To develop a simple personal expense management application.
- To record daily expenses systematically.
- To categorize expenses for easier analysis.
- To store expense records using CSV file handling.
- To generate useful spending reports.
- To calculate total, average, highest, and lowest expenses.
- To provide category-wise and monthly spending analysis.
- To visualize expense data using charts.
- To validate user input.
- To handle runtime and file-related errors.
- To demonstrate modular Python programming.

---

# 4. SCOPE OF THE PROJECT

The system focuses on personal expense management through a
command-line interface.

The application provides:

- Expense recording.
- Expense viewing.
- Expense editing.
- Expense deletion.
- Expense categorization.
- Expense searching and filtering.
- CSV-based persistent storage.
- Expense reports.
- Data visualization.
- Input validation.
- Exception handling.

The project is designed as a standalone Python application.

---

# 5. FUNCTIONAL REQUIREMENTS

## 5.1 Add Expense

The user can enter:

- Expense amount.
- Expense category.
- Expense description.
- Expense date.

Each expense is assigned a unique ID.

---

## 5.2 View Expenses

The application displays all recorded expenses in a structured
table containing:

- ID
- Date
- Category
- Description
- Amount

The total spending is also displayed.

---

## 5.3 Edit Expense

The user can select an expense using its ID and modify:

- Amount.
- Category.
- Description.
- Date.

Existing values can be retained when no new value is entered.

---

## 5.4 Delete Expense

The user can delete an expense by providing its ID.

A confirmation step is provided before deletion.

---

## 5.5 Categorize Expenses

Expenses can be organized into categories such as:

- Food
- Transport
- Entertainment
- Shopping
- Education
- Healthcare
- Bills
- Travel
- Other

The application can display expenses grouped by category.

---

## 5.6 Search and Filtering

The application provides filtering options based on:

- Category.
- Exact date.
- Month.
- Amount range.

This allows users to locate specific expense records efficiently.

---

## 5.7 Generate Reports

The application generates reports containing:

- Number of expenses.
- Total spending.
- Average expense.
- Highest expense.
- Lowest expense.
- Category-wise spending.
- Monthly spending.

---

## 5.8 Data Visualization

The application provides graphical representations using Matplotlib.

The supported visualizations are:

- Category-wise bar chart.
- Category-wise pie chart.
- Monthly spending chart.

---

# 6. NON-FUNCTIONAL REQUIREMENTS

## 6.1 Usability

The application should provide a simple menu-driven interface that is
easy for users to understand.

## 6.2 Reliability

The application should handle invalid inputs and file-related errors
without unexpectedly terminating.

## 6.3 Maintainability

The application is divided into separate modules so that individual
components can be modified and maintained independently.

## 6.4 Data Persistence

Expense records should remain available after the application is closed
and restarted.

## 6.5 Portability

The application can run on systems that support Python 3.

---

# 7. TECHNOLOGIES USED

## Programming Language

Python 3

## Standard Libraries

- csv
- datetime
- os
- collections
- unittest

## External Library

- Matplotlib

## Data Storage

CSV file

---

# 8. SYSTEM ARCHITECTURE

The application follows a modular architecture.

```text
                    PERSONAL EXPENSE TRACKER
                              |
                              v
                           main.py
                              |
          +-------------------+-------------------+
          |                   |                   |
          v                   v                   v
   Expense Manager       File Handler          Reports
          |                   |                   |
          |                   v                   |
          |             expenses.csv             |
          |                                       |
          +-------------------+-------------------+
                              |
                              v
                       Visualization
                              |
                              v
                         Matplotlib
```
