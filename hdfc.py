import pandas as pd
import matplotlib.pyplot as plt
import re

# Load the data
data = pd.read_csv('/mnt/data/hdfcjuly.csv')

# Convert 'Date' to datetime format
data['Date'] = pd.to_datetime(data['Date'], format='%d/%m/%y')

# Replace missing values in 'Withdrawal Amt.' and 'Deposit Amt.' with 0
data['Withdrawal Amt.'] = data['Withdrawal Amt.'].fillna(0)
data['Deposit Amt.'] = data['Deposit Amt.'].fillna(0)

# Calculate total income, total spending and net amount
total_income = data['Deposit Amt.'].sum()
total_spending = data['Withdrawal Amt.'].sum()
net_amount = total_income - total_spending

# Group the data by date and calculate the sum of the 'Deposit Amt.' and 'Withdrawal Amt.' for each date
daily_data = data.groupby('Date').agg({'Deposit Amt.': 'sum', 'Withdrawal Amt.': 'sum'}).reset_index()

# Create a line graph for daily income and spending
plt.figure(figsize=(12,6))
plt.plot(daily_data['Date'], daily_data['Deposit Amt.'], label='Income')
plt.plot(daily_data['Date'], daily_data['Withdrawal Amt.'], label='Spending')
plt.xlabel('Date')
plt.ylabel('Amount (INR)')
plt.title('Daily Income and Spending')
plt.legend()
plt.grid(True)
plt.show()

# Define a function to categorize transactions based on keywords in the 'Narration' field
def categorize(narration):
    # Define categories and associated keywords
    categories = {
        'Food': ['restaurant', 'cafe', 'dining'],
        'Utilities': ['electricity', 'utility', 'bill'],
        'Shopping': ['shopping', 'mall', 'store'],
        'Travel': ['flight', 'hotel', 'travel'],
        'Healthcare': ['hospital', 'pharmacy', 'health'],
        'Entertainment': ['movie', 'music', 'game']
    }
    
    # Convert the narration to lowercase
    narration = narration.lower()
    
    # Check each category
    for category, keywords in categories.items():
        # Check each keyword
        for keyword in keywords:
            # If the keyword is found in the narration, return the category
            if keyword in narration:
                return category
    
    # If no keyword is found, return 'Other'
    return 'Other'

# Apply the categorize function to the 'Narration' field
data['Category'] = data['Narration'].apply(categorize)

# Group the data by category and calculate the sum of the 'Withdrawal Amt.' for each category
category_data = data.groupby('Category').agg({'Withdrawal Amt.': 'sum'}).reset_index()

# Create a DataFrame for the insights
insights = pd.DataFrame({
    'Total Income': [total_income],
    'Total Spending': [total_spending],
    'Net Amount': [net_amount]
})

# Write the insights, the cleaned data, and the category data to CSV files
insights.to_csv('/mnt/data/insights.csv', index=False)
data.to_csv('/mnt/data/cleaned_data.csv', index=False)
daily_data.to_csv('/mnt/data/daily_income_spending.csv', index=False)
category_data.to_csv('/mnt/data/category_data.csv', index=False)
