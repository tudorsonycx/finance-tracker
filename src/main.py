import csv
from helpers import get_date, get_amount, get_category, get_description
from datetime import datetime as dt
import pandas as pd
from matplotlib import pyplot as plt
from config import CSV_FILE, COLUMNS, FORMAT


class CSV:
    CSV_FILE = CSV_FILE
    COLUMNS = COLUMNS
    FORMAT = FORMAT

    @classmethod
    def initialize_csv(cls):
        """
        Initializes the CSV file by checking if it exists and has the correct header.
        If the file does not exist or the header is incorrect, it creates a new CSV file with the correct header.

        Returns:
            None
        """
        try:
            with open(cls.CSV_FILE, "r", newline="") as csvfile:
                reader = csv.reader(csvfile)
                header = next(reader)
                if header != cls.COLUMNS:
                    raise ValueError
        except:
            with open(cls.CSV_FILE, "w", newline="") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(cls.COLUMNS)

    @classmethod
    def add_entry(cls, date, amount, category, description):
        """
        Adds a new entry to the CSV file.

        Args:
            date (str): The date of the entry in DD-MM-YY format.
            amount (float): The amount of the entry.
            category (str): The category of the entry.
            description (str): A brief description of the entry.

        Returns:
            None
        """
        with open(cls.CSV_FILE, "a", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([date, amount, category, description])

    @classmethod
    def get_transactions(cls, start_date, end_date):
        """
        Retrieves and prints transactions within a specified date range from a CSV file.

        Args:
            start_date (str): The start date in the format specified by cls.FORMAT.
            end_date (str): The end date in the format specified by cls.FORMAT.

        Returns:
            pd.DataFrame: A DataFrame containing the filtered transactions within the specified date range.

        Prints:
            - Transactions within the specified date range.
            - Summary of total income, total expense, and net amount.
        """
        df = pd.read_csv(cls.CSV_FILE)
        df["date"] = pd.to_datetime(df["date"], format=cls.FORMAT)
        start_date_dt = dt.strptime(start_date, cls.FORMAT)
        end_date_dt = dt.strptime(end_date, cls.FORMAT)
        mask = (df["date"] >= start_date_dt) & (df["date"] <= end_date_dt)
        df_filtered = df[mask]
        print(f"Transactions from {start_date} to {end_date}")
        print(
            df_filtered.to_string(
                index=False, formatters={"date": lambda x: x.strftime(cls.FORMAT)}
            )
        )
        total_income = df_filtered[df_filtered["category"] == "Income"]["amount"].sum()
        total_expense = df_filtered[df_filtered["category"] == "Expense"][
            "amount"
        ].sum()
        print("\nSummary:")
        print(f"Total income: {total_income:.2f}")
        print(f"Total expense: {total_expense:.2f}")
        print(f"Net: {(total_income - total_expense):.2f}")
        return df_filtered

    @classmethod
    def plot_transactions(cls, df):
        """
        Plots the income and expense transactions over time.

        Args:
            df (pd.DataFrame): A DataFrame containing the transactions.
        Returns:
            None
        """
        df.set_index("date", inplace=True)
        income_df = df[df["category"] == "Income"].resample("D").sum()
        expense_df = df[df["category"] == "Expense"].resample("D").sum()
        plt.figure(figsize=(12, 6))
        plt.plot(income_df.index, income_df["amount"], label="Income", color="g")
        plt.plot(expense_df.index, expense_df["amount"], label="Expense", color="r")
        plt.xlabel("Date")
        plt.ylabel("Amount")
        plt.title("Income and Expense Over Time")
        plt.show()


def add():
    CSV.initialize_csv()
    date = get_date()
    amount = get_amount()
    category = get_category()
    description = get_description()
    CSV.add_entry(date, amount, category, description)
    print("Entry added successfully!")
    print()


def main():
    while True:
        print("A. Add a new transaction")
        print("V. View transactions and summary within a date range")
        print("Q. Exit\n")
        choice = input("Enter your choice: ")
        if choice.lower() == "a":
            add()
        elif choice.lower() == "v":
            start_date = get_date()
            today = False
            if input("Do you want the end date to be today? (y/n): ").lower() == "y":
                today = True
            end_date = get_date(today=today)
            df = CSV.get_transactions(start_date, end_date)

            if input("Do you want to plot the transactions? (y/n): ").lower() == "y":
                CSV.plot_transactions(df)
            print()
        elif choice.lower() == "q":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.\n")


if __name__ == "__main__":
    main()
