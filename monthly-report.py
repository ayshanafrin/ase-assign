def get_user_input():
    """Get incomes and expenses from user input."""
    income = list(map(int, input("Enter incomes separated by space: ").split()))
    expenses = list(map(int, input("Enter expenses separated by space: ").split()))
    return income, expenses


def calculate_summary(income, expenses):
    """Calculate and display the monthly summary."""
    total_income = sum(income)
    total_expenses = sum(expenses)
    balance = total_income - total_expenses

    print("\n----- Monthly Summary -----")
    print(f"Total Income  : ₹{total_income}")
    print(f"Total Expenses: ₹{total_expenses}")
    print(f"Net Balance   : ₹{balance}")

    if balance > 0:
        print("Status        : Savings this month ")
    elif balance < 0:
        print("Status        : Overspent ")
    else:
        print("Status        : Balanced ")


# --- main execution ---
if __name__ == "__main__":
    incomes, expenses = get_user_input()
    calculate_summary(incomes, expenses)
