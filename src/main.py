from expense import Expense
from expense_manager import ExpenseManager
from category import Category

def main():

    manager = ExpenseManager()

    while True:
        try:
            print("Expense Tracker - Main Menu:")
            print("1. View expenses")
            print("2. Add expense")
            print("3. Edit expense")
            print("4. Delete expense")
            print("5. Get Total Expenses")
            print("6. Exit")

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
                print(f"Total Amount: €{manager.get_total():.2f}\n")
                for k, v in manager.get_total_by_category().items():
                    if v > 0:
                        print(f"{k.value}: €{v:.2f}")
                print()

            elif choice == 6:
                break

            else:
                print("Invalid choice.\n")

        except (ValueError, TypeError, IndexError) as e:
            print(str(e) + "\n")
            
def view_categories():
    print("Categories:")
    for position, category in enumerate(Category, start=1):
        print(f"{position}. {category.value}")

def add_expense(manager):
    name = input("Enter expense name: ")
    price = float(input("Enter expense price: "))

    print()
    view_categories()

    choice = int(input("Enter category number: "))

    categories = list(Category)

    if choice < 1 or choice > len(categories):
        raise IndexError("Invalid category number.")

    category = categories[choice - 1]

    new_expense = Expense(name, price, category)

    manager.add_expense(new_expense)

    print(f"Expense ({manager.get_expense(manager.get_expenses_count()-1)}) added successfully.\n")

def edit_expense(manager):

    manager.view_expenses()

    try:
        position = int(input("Enter position: "))
        expense_index = position - 1
        print(f"Editing expense: ({manager.get_expense(expense_index)})\n")

        name = input("Enter expense name: ")
        price = float(input("Enter expense price: "))

        print()
        view_categories()

        choice = int(input("Enter category number: "))

        categories = list(Category)

        if choice < 1 or choice > len(categories):
            raise IndexError("Invalid category number.")

        category = categories[choice - 1]

        manager.edit_expense(expense_index, name, price, category)
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