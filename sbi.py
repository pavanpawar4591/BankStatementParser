import pandas as pd

def extract_category(description):
    # Add more rules here if needed to extract categories based on different patterns
    if 'HOTEL' in description:
        return 'Hotel'
    elif 'RESTAURANT' in description:
        return 'Restaurant'
    elif 'SHOPPING' in description:
        return 'Shopping'
    else:
        return 'Other'

def main():
    # Replace 'your_file.csv' with the actual file path of your CSV bank statement
    file_path = 'your_file.csv'

    try:
        # Read the CSV file into a pandas DataFrame with a custom delimiter "|"
        df = pd.read_csv(file_path, delimiter='|')

        # Initialize a dictionary to store the spending by category
        spending_by_category = {}

        # Loop through each row in the DataFrame
        for index, row in df.iterrows():
            # Extract the category from the description
            category = extract_category(row['Description'])

            # Convert Debit, Credit, and Balance fields to numeric values
            debit = float(row['Debit'].replace(',', '')) if not pd.isnull(row['Debit']) else 0
            credit = float(row['Credit'].replace(',', '')) if not pd.isnull(row['Credit']) else 0
            spending = debit - credit

            # Update the total spending by category
            spending_by_category[category] = spending_by_category.get(category, 0) + spending

        # Calculate the total spending
        total_spending = sum(spending_by_category.values())

        # Write insights to a file named "spending_insights.txt"
        with open("spending_insights.txt", "w") as file:
            file.write("Total Spending by Category:\n")
            for category, spending in spending_by_category.items():
                file.write(f"{category}: {spending:.2f}\n")

            file.write("\nTotal Spending: {:.2f}".format(total_spending))

        print("Insights saved to 'spending_insights.txt'.")

    except FileNotFoundError:
        print("File not found. Please check the file path.")
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()
