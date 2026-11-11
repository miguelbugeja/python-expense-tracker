class ExpenseManager:

    def __init__(self):
        self.expenses = []

    def add_expense(self, expense):
        self.expenses.append(expense)

    def get_expenses(self):
        for expense in self.expenses:
            print(f"{expense.name}: €{expense.price:.2f}")