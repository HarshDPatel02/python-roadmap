import sys

expenses = []

def main():
    while True:
        print("\nPersonal Finance Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Summary Report")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            summary_report()
        elif choice == "4":
            sys.exit("Goodbye!")
        else:
            print("Invalid option")


def add_expense():
    try:
        amount = float(input("Amount: "))
    except ValueError:
        print("Invalid amount")
        return

    category = input("Category (food, travel, bills, other): ").lower()

    expense = {"amount": amount, "category": category}
    expenses.append(expense)

    print("Expense added!")


def view_expenses():
    if not expenses:
        print("No expenses recorded.")
        return

    for i, exp in enumerate(expenses, start=1):
        print(f"{i}. ${exp['amount']} - {exp['category']}")


def summary_report():
    if not expenses:
        print("No expenses to summarize.")
        return

    summary = calculate_summary(expenses)

    print("\nSummary Report")
    for category in summary:
        print(f"{category}: ${summary[category]}")


def calculate_summary(data):
    result = {}

    for exp in data:
        cat = exp["category"]
        amount = exp["amount"]

        if cat not in result:
            result[cat] = 0

        result[cat] += amount

    return result


if __name__ == "__main__":
    main()
