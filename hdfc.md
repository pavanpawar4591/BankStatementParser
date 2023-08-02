# Deployment Guide for Bank Statement Analysis

This guide provides instructions on how to set up and run the Bank Statement Analysis script. This script reads a CSV file of a bank statement, processes the data to compute insights such as total income, total spending, and net amount, and writes these insights to CSV files.

## Prerequisites

- Python 3.6 or higher
- Pip (Python package installer)

## Setup Instructions

1. **Clone the repository and navigate to the directory containing the script.**

    Replace `<repository_url>` and `<repository_directory>` with the actual URL of your repository and the directory containing the script.

    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2. **Create a Python virtual environment and activate it.**

    This step is optional, but it's a good practice to use a virtual environment to avoid interfering with your system Python and other projects.

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

    If you're using Windows, use the following commands instead:

    ```bash
    py -m venv venv
    .\venv\Scripts\activate
    ```

3. **Install the required Python packages.**

    This script requires the `pandas` and `matplotlib` packages. You can install them using pip:

    ```bash
    pip install pandas matplotlib
    ```

## Running the Script

1. **Prepare the input data.**

    The script requires a CSV file of a bank statement as input. Make sure the file is in the correct format and replace `/path/to/bank_statement.csv` with the path to your file.

2. **Run the script.**

    ```bash
    python script.py /path/to/bank_statement.csv
    ```

    The script will process the data and create several CSV files in the current directory:
    - `insights.csv`: Contains the total income, total spending, and net amount.
    - `cleaned_data.csv`: Contains the cleaned data with 'Date', 'Deposit Amt.', and 'Withdrawal Amt.'.
    - `daily_income_spending.csv`: Contains the daily income and spending.
    - `category_data.csv`: Contains the total spending for each category.

    The script will also display a line graph for daily income and spending.
