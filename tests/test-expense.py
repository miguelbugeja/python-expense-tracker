import unittest
from src.expense import Expense
from src.category import Category

class TestExpense(unittest.TestCase):

    def test_valid_expense(self):
        expense = Expense("Petrol", 40, Category.TRANSPORT)

        self.assertEqual(expense.name, "Petrol")
        self.assertEqual(expense.price, 40)
        self.assertEqual(expense.category, Category.TRANSPORT)

    def test_invalid_expense_name(self):
        with self.assertRaises(ValueError):
            Expense(123, 40, Category.TRANSPORT)

    def test_empty_expense_name(self):
        with self.assertRaises(ValueError):
            Expense(" ", 40, Category.TRANSPORT)

    def test_float_expense_price(self):
        expense = Expense("Petrol", 40.50, Category.TRANSPORT)
        self.assertEqual(expense.price, 40.50)

    def test_bool_expense_price(self):
        with self.assertRaises(TypeError):
            Expense("Petrol", True, Category.TRANSPORT)

    def test_non_numeric_expense_price(self):
        with self.assertRaises(TypeError):
            Expense("Petrol", "40", Category.TRANSPORT)

    def test_zero_expense_price(self):
        with self.assertRaises(ValueError):
            Expense("Petrol", 0, Category.TRANSPORT)

    def test_negative_expense_price(self):
        with self.assertRaises(ValueError):
            Expense("Petrol", -40, Category.TRANSPORT)

    def test_invalid_expense_category(self):
        with self.assertRaises(ValueError):
            Expense("Petrol", 40, "Transport")

if __name__ == '__main__':
    unittest.main()