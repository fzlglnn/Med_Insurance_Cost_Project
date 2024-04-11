import csv
#import pandas as pd

# Define the column headers
headers = ['age', 'sex', 'bmi', 'children', 'smoker', 'region', 'charges']
path_to_csv = '/home/faizal/Desktop/DATA ANALIST ASSIGNMENTS/Mediacal_insurance_cost_group_project/python-portfolio-project-starter-files/insurance.csv'

# Initialize an empty list to store dictionaries for each row
data = []
# Open the CSV file
with open(path_to_csv, newline='') as csvfile:
    # Create a CSV reader object
    reader = csv.reader(csvfile)
    # Skip the header row
    next(reader)
    # Iterate over each row in the CSV file
    for row in reader:
        # Create a dictionary for the current row
        row_dict = {}
        # Iterate over each value in the row and assign it to the corresponding header
        for i, header in enumerate(headers):
            row_dict[header] = row[i]
        # Append the dictionary for the current row to the list
        data.append(row_dict)

# Print the first few rows to verify
for i in range(13):
    print(data[i])

