import csv

# Define the CSV dialect with '|' as the delimiter and skip initial spaces
csv.register_dialect('csv_dialect', delimiter='|', skipinitialspace=True, quoting=csv.QUOTE_ALL)

# Read the CSV file and remove line spaces
with open('filtered_data.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, dialect='csv_dialect')
    cleaned_lines = [row for row in reader if row != []]

# Write the cleaned data to a new CSV file
with open('cleaned_output.csv', 'w', newline='') as cleaned_csv:
    writer = csv.writer(cleaned_csv)
    writer.writerows(cleaned_lines)

print("Line spaces removed successfully!")