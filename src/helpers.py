from datetime import datetime as dt

FORMAT = "%d-%m-%y"
CATEGORIES = {"I": "Income", "E": "Expense"}


def get_date(today=False):
    if today:
        return dt.today().strftime(FORMAT)
    while not today and True:
        try:
            date_prompt = input("Enter date in the format 'DD-MM-YY': ")
            return dt.strptime(date_prompt, FORMAT).strftime(FORMAT)
        except ValueError:
            print("Wrong format! Try again.")


def get_amount():
    while True:
        try:
            return float(input("Enter the amount: "))
        except ValueError:
            print("Invalid input! Please enter a non-negative, non-zero number.")


def get_category():
    while True:
        print("Enter a category: ")
        for key, value in CATEGORIES.items():
            print(f"- {key} for {value}")
        category = input("Category: ").upper()
        try:
            return CATEGORIES[category]
        except KeyError:
            print("Invalid category! Try again.")
