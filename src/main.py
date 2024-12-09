import csv


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
