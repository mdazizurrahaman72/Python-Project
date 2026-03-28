import datetime
import os

os.makedirs("DATA", exist_ok=True)
os.makedirs("REPORTS", exist_ok=True)

# ======= SET UP FILE PATHS =======
TRANSACTION_FILE = "DATA/transactions.txt"
CATEGORY_FILE = "DATA/categories.txt"
REPORT_FILE = "REPORTS/monthly_report.txt"

SEPARATOR = "|"

def setup_files():
    try:
        file = open(CATEGORY_FILE,"r")
        file.close()
    except:

        with open(CATEGORY_FILE,"w") as file:
            file.write("Food\nRent\nTransport\nShopping\nSalary\nUtilities\nEntertainment\nOther\n")
        
        print("✅ Categories File Created")

    try:
        file = open(TRANSACTION_FILE, "r")
        file.close()
    except:

        with open(TRANSACTION_FILE, "w") as file:
            file.write("Date|Type|Category|Amount|Description\n")
        
        print("✅ Transaction file Created")

def display_menu():
    print("\n" + "-" * 50)
    print(" "*9 + "💰 PERSONAL FINANCE MANAGER 💰")
    print("-" * 50)
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View All Transactions")
    print("4. Calculate Current Balance")
    print("5. Category-wise Spending")
    print("6. Generate Monthly Report")
    print("7. Search Transactions")
    print("8. Exit")
    print("=" * 50)

def load_categories():
    categories = []

    try:
        with open(CATEGORY_FILE,"r") as file:
            lines = file.readlines()

            for line in lines:
                line = line.strip()
                categories.append(line)

            return categories
    except:
        print("⚠️ Category file not found")
        return []

def get_valid_date():

    while True:
        date_time = input("Enter date (YYYY-MM-DD) or press enter for today: ")
        
        if date_time == "":
            return datetime.datetime.now().strftime("%Y-%m-%d")
        else:
            
            try:
                valid_date = datetime.datetime.strptime(date_time,"%Y-%m-%d")
                return valid_date.strftime("%Y-%m-%d")
            except ValueError:
                print("⚠ Invalid date formate! Use YYY-MM-DD (example: 2025-11-08)")

def get_valid_category(categories):
    print("Available Categories: ")
    print("-"*30)

    for i, Categorie in enumerate(categories,1):
        print(f"{i}. {Categorie}")

    while True:
        try:
            choice = int(input(f"Select Category (1 - {len(categories)}): "))
            
            if 1<= choice and choice <= len(categories):
                return categories[choice-1]
            else:
                print(f"⚠ Please enter a number between 1 and {len(categories)}")
        
        except ValueError:
            print("⚠ Please enter a valid number")

def get_valid_amount():

    while True:
        try:
            amount = float(input("Enter Amount: "))

            if amount > 0:
                return amount
            else:
                print("⚠ Amount must be greater than 0!")

        except ValueError:
            print("⚠ Please enter a valid number")

def save_transaction(date, transaction_type, category, amount, description):
    
    with open(TRANSACTION_FILE,"a") as file:
        line = SEPARATOR.join([date,transaction_type,category,str(amount),description])
        file.write(line + "\n")

    print("✅ Transaction saved successfully!")
    return True

def add_income():
    categories = load_categories()
    date = get_valid_date()
    category = get_valid_category(categories)
    amount = get_valid_amount()
    description = input("Enter Description: ")
    save_transaction(date, "Income", category, amount, description)
    
def add_expense():
    categories = load_categories()
    date = get_valid_date()
    category = get_valid_category(categories)
    amount = get_valid_amount()
    description = input("Enter Description: ")
    save_transaction(date, "Expense", category, amount, description)

def load_all_transactions():
    transactions = []
    try:
        with open(TRANSACTION_FILE,"r") as file:
            lines = file.readlines()

            for line in lines[1:]:
                line = line.strip()
                if line == "":
                    continue
                parts = line.split(SEPARATOR)
                if len(parts) == 5:
                    transactions.append(parts)
            
        return transactions
    except:
        return []
    
def view_all_transactions():
    print("\n===== VIEW ALL TRANSACTIONS =====")
    transactions = load_all_transactions()

    if len(transactions) == 0:
        print("No Transaction Found")
        return
    
    transactions.sort(key=lambda x:x[0],reverse=True)
    
    for transaction in transactions:
        print("Date: ", transaction[0])
        print("Type: ", transaction[1])
        print("Category: ", transaction[2])
        print("Amount: ", transaction[3])
        print("Description: ", transaction[4])
        print("------------------------")
    
    print("Total Transactions: ", len(transactions))
    
def current_balance():
    print("\n===== CURRENT BALANCE =====")
    transactions = load_all_transactions()

    if len(transactions) == 0:
        print("No Transaction Found")
        return

    total_income = 0
    total_expense = 0

    for transaction in transactions:
        trans_type = transaction[1]
        trans_amount = float(transaction[3])

        if trans_type == "Income":
            total_income += trans_amount
        elif trans_type == "Expense":
            total_expense += trans_amount

    balance = total_income - total_expense
    print(f"\nTotal Income: {total_income:.2f} BDT")
    print(f"Total Expense: {total_expense:.2f} BDT")
    print("-"*40)
    print(f"Balance: {balance:.2f} BDT")

    if balance > 0:
        print("✅ You're saving money!")
    elif balance < 0:
        print("⚠ You're spending more than earning!")
    else:
        print("Your income equals your expenses.")

def category_wise_spending():
    print("\n===== CATEGORY-WISE SPENDING =====")
    transactions = load_all_transactions()
    if len(transactions) == 0:
        print("No Transactions Found")
        return
    
    category_totals = {}
    for transaction in transactions:
        trans_type = transaction[1]
        category = transaction[2]
        amount = float(transaction[3])

        if trans_type == "Expense":
            if category in category_totals:
                category_totals[category] += amount
            else:
                category_totals[category] = amount

    if len(category_totals) == 0:
        print("No expenses found!")
        return
    
    total_spent = 0
    print("\nSpending By Category:")
    for category in category_totals:
        print(category + ": " + str(category_totals[category]) + " BDT")
        total_spent += category_totals[category]

    print("\nTotal spent on all categories:", total_spent, "BDT")

def generate_monthly_report():
    print("\n===== GENERATE MONTHLY REPORT =====")
    transactions = load_all_transactions()
    if len(transactions) == 0:
        print("No Transactions Found")
        return
    
    month_input = input("Enter month (YYYY-MM), example 2025-11: ")

    monthly_transactions = []
    for transaction in transactions:
        date = transaction[0]

        if date.startswith(month_input):
            monthly_transactions.append(transaction)

    if len(monthly_transactions) == 0:
        print(f"No transactions found for {month_input}")
        return
    
    monthly_income = 0
    monthly_expense = 0

    for transaction in monthly_transactions:
        trans_type = transaction[1]
        amount = float(transaction[3])

        if trans_type == "Income":
            monthly_income = monthly_income + amount
        elif trans_type == "Expense":
            monthly_expense = monthly_expense + amount

    monthly_balance = monthly_income - monthly_expense

    report = ""
    report += "=" * 60 + "\n"
    report += f"     MONTHLY FINANCIAL REPORT - {month_input}\n"
    report += "=" * 60 + "\n\n"
    report += f"Total Income:  {monthly_income:.2f} BDT\n"
    report += f"Total Expense: {monthly_expense:.2f} BDT\n"
    report += f"Net Balance:   {monthly_balance:.2f} BDT\n"
    report += "\n" + "-" * 60 + "\n"
    report += "TRANSACTION DETAILS:\n"
    report += "-" * 60 + "\n\n"

    for transaction in monthly_transactions:
        report += f"Date: {transaction[0]}\n"
        report += f"Type: {transaction[1]}\n"
        report += f"Category: {transaction[2]}\n"
        report += f"Amount: {transaction[3]} BDT\n"
        report += f"Description: {transaction[4]}\n"
        report += "-" * 60 + "\n\n"

    try:
        file = open(REPORT_FILE, "w")
        file.write(report)
        file.close()
        print(f"\n✓ Report saved to: {REPORT_FILE}")
        print(f"✓ Total transactions: {len(monthly_transactions)}")
    except:
        print("⚠ Error saving report!")
    
def search_transactions():
    print("\n===== SEARCH TRANSACTIONS =====")
    transactions = load_all_transactions()
    if len(transactions) == 0:
        print("No Transactions Found")
        return
    
    word = input("Type a word to search (example: food, rent): ").strip().lower()
    matches = []

    for transaction in transactions:
        category = transaction[2].lower()
        description = transaction[4].lower()

        if word in category or word in description:
            matches.append(transaction)

    if len(matches) == 0:
        print("No results found for '" + word + "'")
        return   
        
    print("\nFound", len(matches), "matching transaction(s):\n")
    for transaction in matches:
        print("Date:", transaction[0])
        print("Type:", transaction[1])
        print("Category:", transaction[2])
        print("Amount:", transaction[3])
        print("Description:", transaction[4])
        print("---------")


def main():
    setup_files()
    print("\n🎉 Welcome to Personal Finance Manager!")

    while True:
        display_menu()

        choice = input("\nEnter your choice(1-8): ")

        if choice == "1":
            add_income()

        elif choice == "2":
            add_expense()

        elif choice == "3":
            view_all_transactions()

        elif choice == "4":
            current_balance()

        elif choice == "5":
            category_wise_spending()

        elif choice == "6":
            generate_monthly_report()

        elif choice == "7":
            search_transactions()

        elif choice == "8":
            print("\n👋 Thank you for using Personal Finance Manager!")
            print("💰 Keep tracking your money! Good bye!")
            break

        else:
            print("⚠ Invalid choice! Please enter a number between 1-8")

main()