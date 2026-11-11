from operator import index

from expense import Expense
from expense_manager import ExpenseManager

def main():

    try:
        manager = ExpenseManager()

        ex1 = Expense("Food", 10)
        ex2 = Expense("Food", 20)

        manager.add_expense(ex1)
        manager.add_expense(ex2)

        while manager.get_expenses_count() > 0:
            delete_expense(manager)

    except (ValueError, TypeError) as e:
        print(e)

def edit_expense(manager):

    manager.view_expenses()

    try:
        position = int(input("Enter position: "))
        expense_index = position - 1
        print("Editing expense: (" + manager.get_expense(expense_index) + ")\n")

        name = input("Enter expense name: ")
        price = float(input("Enter expense price: "))

        manager.edit_expense(expense_index, name, price)
        print("Expense edited successfully.\n")

    except (ValueError, TypeError, IndexError) as e:
        print("Failed to edit expense: " + str(e))

def delete_expense(manager):

    manager.view_expenses()

    try:
        position = int(input("Enter position: "))
        expense_index = position - 1

        expense = manager.get_expense(expense_index)

        manager.delete_expense(expense_index)
        print("Expense: (" + expense + ") was deleted successfully!\n")

    except IndexError as e:
        print("Failed to delete expense: " + str(e) + "\n")

if __name__ == "__main__":
    main()