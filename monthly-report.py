# monthly_report.py
# -----------------------------------------------------------
# Module to calculate total income, expenses, and show summary
# -----------------------------------------------------------

def calculate_summary(income_list, expense_list):
    """Calculate total income, total expenses, and net balance."""
    total_income = sum(income_list)
    total_expenses = sum(expense_list)
    net_balance = total_income - total_expenses
    return total_income, total_expenses, net_balance


def display_summary(income_list, expense_list):
    """Display the monthly income and expense summary."""
    income, expenses, balance = calculate_summary(income_list, expense_list)
    print("----- Monthly Summary -----")
    print(f"Total Income  : ₹{income}")
    print(f"Total Expenses: ₹{expenses}")
    print(f"Net Balance   : ₹{balance}")


# Example usage
if __name__ == "__main__":
    # Sample income and expense lists
    incomes = [5000, 2000, 1500]
    expenses = [1200, 800, 600]

    # Display the summary
    display_summary(incomes, expenses)
