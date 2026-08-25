# 💰 Personal Expense Tracker

<p align="center">
  <b>A Python-based command-line application for managing, analyzing, storing, and visualizing personal expenses.</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Matplotlib-Visualization-11557C?style=for-the-badge&logo=matplotlib&logoColor=white" alt="Matplotlib">
  <img src="https://img.shields.io/badge/CSV-Data%20Storage-217346?style=for-the-badge&logo=files&logoColor=white" alt="CSV">
  <img src="https://img.shields.io/badge/Unittest-21%2F21%20Passed-2EA44F?style=for-the-badge&logo=python&logoColor=white" alt="Tests">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Status-Completed-success?style=flat-square" alt="Project Status">
  <img src="https://img.shields.io/badge/Project-Major%20Project-blue?style=flat-square" alt="Major Project">
  <img src="https://img.shields.io/badge/Interface-CLI-orange?style=flat-square" alt="CLI">
</p>

---

## 📌 Overview

**Personal Expense Tracker** is a command-line-based Python application
designed to help users record, manage, categorize, analyze, and
visualize their daily expenses.

The application provides a structured approach to expense management
using Python data structures, modular programming, CSV-based persistent
storage, input validation, analytical reports, and Matplotlib-based
visualization.

The project demonstrates practical implementation of core Python
programming concepts in a real-world application.

---

## ✨ Features

### 💳 Expense Management

- Add new expenses
- View all expenses
- Edit existing expenses
- Delete expenses
- Categorize expenses

### 🔎 Search & Filtering

- Search by category
- Filter by date
- Filter by month
- Filter by amount range

### 📊 Reports & Analysis

- Total spending
- Average expense
- Highest expense
- Lowest expense
- Category-wise spending
- Monthly spending

### 📈 Data Visualization

- Category-wise bar chart
- Category-wise pie chart
- Monthly spending chart

### 💾 Data Persistence

- CSV-based storage
- Load existing expenses when the application starts
- Save expense records for future use

### 🛡️ Validation & Error Handling

- Amount validation
- Negative amount validation
- Date validation
- Category validation
- Description validation
- Menu validation
- Exception handling

### 🧪 Testing

- Python `unittest` framework
- 21 automated test cases
- **21/21 tests passed successfully**

---

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| 🐍 Python | Core application development |
| 📄 CSV | Persistent expense storage |
| 📊 Matplotlib | Data visualization |
| 🧪 unittest | Automated testing |
| 📦 Lists | Expense collection |
| 🗂️ Dictionaries | Individual expense records |

---

## 📂 Project Structure

```text
Personal_Expense_Tracker/
│
├── main.py
│
├── modules/
│   ├── __init__.py
│   ├── expense_manager.py
│   ├── file_handler.py
│   ├── validator.py
│   ├── reports.py
│   └── visualization.py
│
├── data/
│   └── expenses.csv
│
├── tests/
│   ├── __init__.py
│   └── test_expense_tracker.py
│
├── docs/
│   └── project_documentation.md
│
├── requirements.txt
├── README.md
└── .gitignore



## 🏗️ Project Architecture

```text
                         ┌─────────────────┐
                         │      User       │
                         └────────┬────────┘
                                  │
                                  ▼
                         ┌─────────────────┐
                         │     main.py     │
                         │  CLI Interface  │
                         └────────┬────────┘
                                  │
              ┌───────────────────┼───────────────────┐
              │                   │                   │
              ▼                   ▼                   ▼
       ┌─────────────┐     ┌─────────────┐     ┌─────────────┐
       │   Expense   │     │  Validator  │     │   Reports   │
       │   Manager   │     │             │     │             │
       └──────┬──────┘     └─────────────┘     └──────┬──────┘
              │                                       │
              ▼                                       ▼
       ┌─────────────┐                         ┌─────────────┐
       │    File     │                         │Visualization│
       │   Handler   │                         │ Matplotlib  │
       └──────┬──────┘                         └─────────────┘
              │
              ▼
       ┌─────────────┐
       │ expenses.csv│
       └─────────────┘




