from .expense import Expense
from .category import Category

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
            print(f"{position}. ({expense.category.value}) {expense.name}: €{expense.price:.2f}")
            position += 1

    def get_expense(self, index):
        if index < 0 or index >= len(self.expenses):
            raise IndexError("Invalid expense position.")

        expense = self.expenses[index]
        return f"({expense.category.value}) {expense.name}: €{expense.price:.2f}"

    def get_expense_by_category(self, category):
        category_expenses = []

        for expense in self.expenses:
            if expense.category == category:
                category_expenses.append(expense)

        return category_expenses

    def edit_expense(self, index, name, price, category):
        if index < 0 or index >= len(self.expenses):
            raise IndexError("Invalid expense position.")

        self.expenses[index] = Expense(name, price, category)

    def delete_expense(self, index):
        if index < 0 or index >= len(self.expenses):
            raise IndexError("Invalid expense position.")

        self.expenses.pop(index)

    def get_total(self):
        return sum(expense.price for expense in self.expenses)

    def get_total_by_category(self):
        category_total = {category: 0 for category in Category}

        for expense in self.expenses:
            category_total[expense.category] += expense.price

        return category_total