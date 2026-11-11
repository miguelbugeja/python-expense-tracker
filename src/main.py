from operator import index

from expense import Expense
from expense_manager import ExpenseManager
from src import expense


def main():

    manager = ExpenseManager()

    try:

        while True:
            print("Expense Tracker - Main Menu:")
            print("1. View expenses")
            print("2. Add expense")
            print("3. Edit expense")
            print("4. Delete expense")
            print("5. Exit")

            choice = int(input("Enter your choice: "))

            if choice == 1:
                if manager.get_expenses_count() <= 0:
                    print("No expenses found.\n")
                else:
                    manager.view_expenses()
                    print()

            elif choice == 2:
                add_expense(manager)

            elif choice == 3:
                edit_expense(manager)

            elif choice == 4:
                delete_expense(manager)

            elif choice == 5:
                break

            else:
                print("Invalid choice.\n")

    except (ValueError, TypeError, IndexError) as e:
        print(e)

def add_expense(manager):
    name = input("Enter expense name: ")
    price = float(input("Enter expense price: "))

    new_expense = Expense(name, price)

    manager.add_expense(new_expense)

    print(f"Expense {name} added successfully.\n")

def edit_expense(manager):

    manager.view_expenses()

    try:
        position = int(input("Enter position: "))
        expense_index = position - 1
        print(f"Editing expense: ({manager.get_expense(expense_index)})\n")

        name = input("Enter expense name: ")
        price = float(input("Enter expense price: "))

        manager.edit_expense(expense_index, name, price)
        print("Expense edited successfully.\n")

    except (ValueError, TypeError, IndexError) as e:
        print(f"Failed to edit expense: {str(e)}\n")

def delete_expense(manager):

    manager.view_expenses()

    try:
        position = int(input("Enter position: "))
        expense_index = position - 1

        deleted_expense = manager.get_expense(expense_index)

        manager.delete_expense(expense_index)
        print(f"Expense: ({deleted_expense}) was deleted successfully!\n")

    except IndexError as e:
        print(f"Failed to delete expense: {str(e)}\n")

if __name__ == "__main__":
    main()