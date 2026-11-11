from expense import Expense

class ExpenseManager:

    def __init__(self):
        self.expenses = []

    def add_expense(self, expense):
        self.expenses.append(expense)

    def get_expenses_count(self):
        return len(self.expenses)

    def view_expenses(self):
        position = 1

        for expense in self.expenses:
            print(f"{position}. {expense.name}: €{expense.price:.2f}")
            position += 1

    def get_expense(self, index):
        if index < 0 or index >= len(self.expenses):
            raise IndexError("Invalid expense position.")

        expense = self.expenses[index]
        return f"{expense.name}: €{expense.price:.2f}"

    def edit_expense(self, index, name, price):
        if index < 0 or index >= len(self.expenses):
            raise IndexError("Invalid expense position.")

        self.expenses[index] = Expense(name, price)

    def delete_expense(self, index):
        if index < 0 or index >= len(self.expenses):
            raise IndexError("Invalid expense position.")

        self.expenses.pop(index)