import json
import os
from category import Category

from src.expense import Expense


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

    def load_expenses(self):

        try:
            with open(self.path, encoding="utf-8") as file:
                expenses_dict = json.load(file)
                expenses = []

                for expense_dict in expenses_dict:
                    expense = Expense(
                        expense_dict["name"],
                        expense_dict["price"],
                        Category(expense_dict["category"])
                    )
                    expenses.append(expense)

                return expenses

        except FileNotFoundError:
            return []

        except (json.decoder.JSONDecodeError, ValueError):
            print("Data stored cannot be loaded.")
            return []