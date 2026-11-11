class Expense:

    def __init__(self, name, price):

        # Validate expense name
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Expense name cannot be empty.")

        # Validate expense price
        if isinstance(price, bool) or not isinstance(price, (int, float)):
            raise TypeError("Expense price must be numeric.")

        if price <= 0:
            raise ValueError("Price cannot be negative or zero.")

        # Initialise attributes
        self.name = name.strip()
        self.price = round(price, 2)