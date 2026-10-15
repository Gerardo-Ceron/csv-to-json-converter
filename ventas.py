# Import native data handling modules
import csv
import json

# Mock sales data simulating an external CSV source
mock_csv_data = """Product,Quantity
Laptop,800
Mouse,25
Keyboard,45
Monitor,150
HDMI Cable,15"""

# Save the mock dataset into a local CSV file
with open("sales.csv", "w", newline="") as file:
    file.write(mock_csv_data)

# AUTOMATION SCRIPT: Parse and transform data
sales_list = []

with open("sales.csv", "r") as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        sales_list.append(row)

# Export the structured dataset into a JSON file
with open("sales.json", "w") as json_file:
    json.dump(sales_list, json_file, indent=4)
    print("Data successfully exported to sales.json.")
