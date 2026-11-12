import json
import os

class ExpenseStorage:

    def __init__(self):
        self.path = os.path.join('..', 'data', 'expenses.json')
        os.makedirs(os.path.dirname(self.path), exist_ok=True)

    def save_expenses(self, expenses):

        expenses_dict_list = []

        for expense in expenses:
            expenses_dict_list.append({
                "name": expense.name,
                "price": expense.price,
                "category": expense.category.value
            })

        with open(self.path, "w", encoding="utf-8") as file:
            json.dump(expenses_dict_list, file, indent=4)