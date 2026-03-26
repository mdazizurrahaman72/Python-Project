import os
import json
from datetime import datetime

# File to store expenses
EXPENSE_FILE = "expenses.json"

# Load expenses from file
def load_expenses():
    if os.path.exists(EXPENSE_FILE):
        with open(EXPENSE_FILE, "r") as f:
            return json.load(f)
    return []

# Save expenses to file
def save_expenses(expenses):
    with open(EXPENSE_FILE, "w") as f:
        json.dump(expenses, f, indent=4)

# Add a new expense
def add_expense(expenses):
    try:
        amount = float(input("Enter amount: "))
        category = input("Enter category (Food, Transport, etc.): ")
        note = input("Enter note (optional): ")
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        expense = {
            "amount": amount,
            "category": category,
            "note": note,
            "date": date
        }
        expenses.append(expense)
        save_expenses(expenses)
        print("Expense added successfully!\n")
    except ValueError:
        print("Invalid amount! Please enter a number.\n")

# View all expenses
def view_expenses(expenses):
    if not expenses:
        print("No expenses found.\n")
        return
    print("\n--- All Expenses ---")
    for i, exp in enumerate(expenses, start=1):
        print(f"{i}. {exp['date']} | {exp['category']} | ${exp['amount']} | {exp['note']}")
    print("-------------------\n")

# View total expenses
def total_expense(expenses):
    total = sum(exp["amount"] for exp in expenses)
    print(f"\nTotal Expenses: ${total}\n")

# Main program
def main():
    expenses = load_expenses()
    while True:
        print("Simple Expense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expense")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            total_expense(expenses)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.\n")

if __name__ == "__main__":
    main()