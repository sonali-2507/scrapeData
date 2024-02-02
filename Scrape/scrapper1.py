import csv

# Assume you have a list of dictionaries containing your scraped data
data = [
    {'Name': 'John', 'Age': 25, 'Location': 'New York'},
    {'Name': 'Alice', 'Age': 30, 'Location': 'San Francisco'},
    # Add more entries as needed
]

# Specify the CSV file name
csv_filename = 'scraped_data.csv'

# Write the data to the CSV file
with open(csv_filename, 'w', newline='') as csvfile:
    fieldnames = data[0].keys()  # Assuming all dictionaries have the same keys
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # Write the header
    writer.writeheader()

    # Write the data
    writer.writerows(data)
