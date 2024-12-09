import csv
from helpers import get_date, get_amount, get_category, get_description


class CSV:
    CSV_FILE = "finance_data.csv"
    COLUMNS = ["date", "amount", "category", "description"]

    @classmethod
    def initialize_csv(cls):
        """
        Initializes the CSV file by checking if it exists and has the correct header.
        If the file does not exist or the header is incorrect, it creates a new CSV file with the correct header.

        Raises:
            ValueError: If the existing CSV file has an incorrect header.
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


def add():
    """
    Adds a new entry to the CSV file.

    This function initializes the CSV file if it is not already initialized,
    then prompts the user to input the date, amount, category, and description
    of the entry. Finally, it adds the entry to the CSV file and prints a
    success message.
    """
    CSV.initialize_csv()
    date = get_date()
    amount = get_amount()
    category = get_category()
    description = get_description()
    CSV.add_entry(date, amount, category, description)
    print("Entry added successfully!")
    print()


if __name__ == "__main__":
    add()
