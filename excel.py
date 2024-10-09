import pandas as pd

# Load the Excel file
file_path = 'D:\Loan Eligible.xlsx'
df = pd.read_excel(file_path)

# Define the criteria for loan eligibility
def check_eligibility(income, criteria):
    return income >= criteria

# Function to determine eligibility for each person
def determine_eligibility(income):
    results = []
    for index, row in df.iterrows():
        person = row['Person']
        person_income = row['Income']
        criteria = row['Criteria']

        if check_eligibility(income, criteria):
            results.append(f"{person} is eligible for the loan.")
        else:
            results.append(f"{person} is not eligible for the loan.")
    return results

# Input income value
income_input = float(input("Enter the income: "))

# Determine eligibility
eligibility_results = determine_eligibility(income_input)

# Print the results
for result in eligibility_results:
    print(result)
