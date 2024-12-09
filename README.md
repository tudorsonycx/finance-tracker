# Personal Finance Tracker

## Table of Contents
- [Description](#description)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Description
This is a simple Finance Tracker built in Python. It allows you to track various transactions in a CSV file, view transactions within a specified date range, and visualize the transactions on a graph.

## Technologies Used
- Python
- Pandas
- Matplotlib

## Features
- Track transactions in a CSV file
- Show transactions in a given date range along with a summary of expenses, income, and net savings
- Ability to visualize the transactions on a graph

## Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/tudorsonycx/finance-tracker.git
    ```
2. Navigate to the project directory:
    ```sh
    cd my-python-app
    ```
3. Create a virtual environment:
    ```sh
    python3 -m venv venv
    ```
4. Activate the virtual environment:
    - On **Windows**:
        ```sh
        venv\Scripts\activate
        ```
    - On **macOS/Linux**:
        ```sh
        source venv/bin/activate
        ```
5. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage
Optionally, run
```sh
python src/generate_finance_data.py
```
to generate 100 random data entries within the last 30 days.
Be warned that this will overwrite the `finance_data.csv` file.

Run the main script to start the application:
```sh
python src/main.py
```

1. **Add a new transaction**:
    - Follow the prompts to enter the date, amount, category, and description of the transaction.
    - The transaction will be added to the CSV file.

2. **View transactions and summary within a date range**:
    - Enter the start and end dates to view transactions within that range.
    - The application will display the transactions and provide a summary of total income, total expense, and net amount.
    - You will also have the option to plot the transactions on a graph.

## License
This project is licensed under the MIT [License](LICENSE).