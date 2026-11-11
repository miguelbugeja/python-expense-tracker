class SummaryGenerator:

    def generate_summary(self, manager):
        total_expenses = manager.get_expenses_count()
        total_amount = manager.get_total()

        # Avoid division by zero
        average_amount = (
            total_amount / total_expenses
            if total_expenses > 0
            else 0
        )

        summary = {
            "total_expenses": total_expenses,
            "total_amount": f"€{total_amount:.2f}",
            "average_amount": f"€{average_amount:.2f}",
            "categories": {}
        }

        categories_totals = manager.get_total_by_category()

        for category, total in categories_totals.items():

            # Get individual expenses belonging to this category
            expenses = manager.get_expense_by_category(category)

            category_data = {
                "total": total,
                "expenses": []
            }

            for expense in expenses:
                category_data["expenses"].append({
                    "name": expense.name,
                    "price": expense.price
                })

            summary["categories"][category.value] = category_data

        return summary

    def view_summary(self, manager):
        if manager.get_expenses_count() <= 0:
            return "No expenses found."
        else:
            result = ""
            summary = self.generate_summary(manager)

            result += "Summary: \n\n"

            for k, v in summary.items():
                if k == "categories":
                    result += "Categories: \n"
                    for categoryName, data in v.items():
                        if data["total"] > 0:
                            result += f"\n{categoryName}: €{data["total"]:.2f}\n"
                            for expense in data["expenses"]:
                                result += f"- {expense["name"]}: €{expense["price"]:.2f}\n"
                else:
                    result += f"{k}: {v}\n\n"

            return result

    def export_summary_txt(self, manager):
        with open("summary.txt", "w") as f:
            f.write(self.view_summary(manager))