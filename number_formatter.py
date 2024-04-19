import csv

# Function to format phone numbers
def format_phone_numbers(numbers):
    """
    Formats a list of phone numbers by removing leading zeros, adding "+91" in place of the removed zeros,
    removing spaces, and joining the formatted numbers with commas.

    Args:
        numbers (list): List of phone numbers as strings.

    Returns:
        str: Formatted phone numbers joined by commas.
    """
    formatted_numbers = []
    for number in numbers:
        formatted_number = "+91" + number.lstrip('0').replace(" ", "")
        formatted_numbers.append(formatted_number)
    return ','.join(formatted_numbers)

# Read numbers from CSV file
numbers = []
with open("coaching_india.csv", newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        numbers.extend(row)

# Format the phone numbers
formatted_result = format_phone_numbers(numbers)

# Save the formatted result in a text file
with open("formatted_numbers.txt", "w") as file:
    file.write(formatted_result)

print("Formatted numbers saved in formatted_numbers.txt")
