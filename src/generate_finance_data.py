import csv
import random
from datetime import datetime as dt, timedelta
from config import CSV_FILE, COLUMNS, CATEGORIES


def generate_finance_data():
    # Define the descriptions
    categories = list(CATEGORIES.values())
    descriptions = [
        "Salary",
        "Groceries",
        "Rent",
        "Utilities",
        "Entertainment",
        "Miscellaneous",
    ]
    # Generate 100 random data entries within the past 30 days
    data = []
    start_date = dt.today()
    for _ in range(100):
        date = (start_date - timedelta(days=random.randint(0, 30))).strftime("%d-%m-%y")
        amount = round(random.uniform(10.0, 5000.0), 2)
        category = random.choice(categories)
        description = random.choice(descriptions)
        data.append([date, amount, category, description])
    # Write data to CSV file
    with open(CSV_FILE, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(COLUMNS)
        writer.writerows(data)
    print(f"CSV file '{CSV_FILE}' with 100 rows has been generated.")


if __name__ == "__main__":
    generate_finance_data()
