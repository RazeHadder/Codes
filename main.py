from bdb import Breakpoint


class Expense:
    def __init__(self, date, amount, category, description=""):
        self.date = date
        self.amount = amount
        self.category = category
        self.description = description

    def __str__(self):
        return f"{self.date}, {self.amount}, {self.category}, {self.description}"

def add_expense(expenses_list):
    date = input("Enter the date (YYYY-MM-DD): ")
    amount = float(input("Enter the amount: "))
    category = input("Enter the category (e.g, food, transport, etc.): ")
    description = input("Enter the description (optional): ")
    expense = Expense(date, amount, category, description)
    expenses_list.append(expense)
    save_expenses(expenses_list)
    print("Expense added succesfully")

def view_expenses(expenses_list, filter_by=None, filter_value=None):
    for expense in expenses_list:
        if not filter_by or getattr(expense, filter_by) == filter_value:
            print(f"Date: {expense.date}, Amount: {expense.amount}, Category: {expense.category}, Description: {expense.description}")

def delete_expense(expenses_list):
    index = int(input("Enter the index of the expense to delete: "))
    if 0 <= index < len(expenses_list):
        del expenses_list[index]
        save_expenses(expenses_list)
        print("Expenses deleted succesfully")
    else:
        print("Invalid index!")

def show_summary(expenses_list):
    total_expense = sum(expense.amount for expense in expenses_list)
    print(f"Total expense: {total_expense}")
    category_totals = {}
    for expense in expenses_list:
        category_totals[expense.category] = category_totals.get(expense.category, 0) + expense.amount
    for category, total in category_totals.items():
        print(f"Category: {category}, Total: {total}")

def save_expenses(expenses_list, filename="expense.txt"):
    with open(filename, "w") as file:
        for expense in expenses_list:
            file.write(str(expense) + "\n")

def load_expenses(filename="expense.txt"):
    expense_list = []
    try:
        with open(filename, "r") as file:
            for line in file:
                date, amount, category, description = line.strip().split(',')
                expense_list.append(Expense(date, float(amount), category, description))
    except FileNotFoundError:
        print(f"No data found. Starting with an empty expense list.")
    return expense_list

def main():
    expenses_list = load_expenses()

    while True:
        print("\n--- Expense Tracker Menu ---")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Show Summary")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_expense(expenses_list)
        elif choice == '2':
            view_expenses(expenses_list)
        elif choice == '3':
            delete_expense(expenses_list)
        elif choice == '4':
            show_summary(expenses_list)
        elif choice == '5':
            break
        else:
            print("invalid choice! Please choose again.")

if __name__ == "__main__":
    main()