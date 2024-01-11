import os
import json
from datetime import datetime

class BudgetTracker:
    def __init__(self):
        self.transactions = []
        self.load_transactions()

    def load_transactions(self):
        try:
            with open("transactions.json", "r") as file:
                self.transactions = json.load(file)
        except FileNotFoundError:
            pass  # File does not exist yet

    def save_transactions(self):
        with open("transactions.json", "w") as file:
            json.dump(self.transactions, file, indent=2)

    def show_menu(self):
        print("\n===== Budget Tracker Menu =====")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Transactions")
        print("4. View Budget")
        print("5. View Expense Analysis")
        print("6. Exit")

    def add_transaction(self, transaction_type):
        amount = float(input(f"Enter {transaction_type} amount: "))
        category = input("Enter category: ")

        new_transaction = {
            "type": transaction_type,
            "amount": amount,
            "category": category,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }

        self.transactions.append(new_transaction)
        self.save_transactions()
        print(f"{transaction_type.capitalize()} added successfully.")

    def view_transactions(self):
        if not self.transactions:
            print("No transactions found.")
        else:
            print("\n===== Your Transactions =====")
            for i, transaction in enumerate(self.transactions, start=1):
                print(f"{i}. {transaction['type']} - {transaction['amount']} - {transaction['category']} - {transaction['date']}")

    def view_budget(self):
        total_income = sum(transaction['amount'] for transaction in self.transactions if transaction['type'] == 'income')
        total_expense = sum(transaction['amount'] for transaction in self.transactions if transaction['type'] == 'expense')
        remaining_budget = total_income - total_expense

        print("\n===== Your Budget =====")
        print(f"Total Income: {total_income}")
        print(f"Total Expense: {total_expense}")
        print(f"Remaining Budget: {remaining_budget}")

    def view_expense_analysis(self):
        expense_categories = {}
        for transaction in self.transactions:
            if transaction['type'] == 'expense':
                category = transaction['category']
                amount = transaction['amount']
                if category in expense_categories:
                    expense_categories[category] += amount
                else:
                    expense_categories[category] = amount

        if not expense_categories:
            print("No expense data available.")
        else:
            print("\n===== Expense Analysis =====")
            for category, amount in expense_categories.items():
                print(f"{category}: {amount}")

    def run(self):
        while True:
            self.show_menu()
            choice = input("Enter your choice (1-6): ")

            if choice == "1":
                self.add_transaction("income")
            elif choice == "2":
                self.add_transaction("expense")
            elif choice == "3":
                self.view_transactions()
            elif choice == "4":
                self.view_budget()
            elif choice == "5":
                self.view_expense_analysis()
            elif choice == "6":
                print("Exiting the application. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    budget_tracker = BudgetTracker()
    budget_tracker.run()
