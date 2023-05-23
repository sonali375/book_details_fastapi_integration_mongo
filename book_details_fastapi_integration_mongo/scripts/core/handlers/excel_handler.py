import pandas as pd

# Generate bill data
bill_data = [
    {'id': 44, 'name': "oil", 'quantity': 10, 'cost': 200},
    {'id': 3, 'name': "shampoo", 'quantity': 3, 'cost': 20}
]

# Create a DataFrame from the bill data
df = pd.DataFrame(bill_data)

# Calculate total price
df['total_amount'] = df['quantity'] * df['cost']

# Calculate grand total
grand_total = df['total_amount'].sum()

# Save the bill as an Excel file
excel_file = 'bill.xlsx'
df.to_excel(excel_file, index=False)

# Upload the bill in bulk by inserting all records
# Insert your code here to upload the Excel file

# Print the grand total
print('Grand Total:', grand_total)
