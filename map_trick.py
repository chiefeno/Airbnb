# Code to map zip codes and missing city names in the company csv


import csv

# Read the CSV file
with open('companies.csv', 'r') as file:
    reader = csv.DictReader(file)
    rows = list(reader)

    # Create a dictionary to store zip-city mappings
    zip_city_map = {}

    # Iterate over the rows and populate the zip-city map
    for row in rows:
        zip_code = row['zip']
        city = row['city']
        if zip_code and city:
            zip_city_map[zip_code] = city

    # Update the rows with missing city values
    for row in rows:
        if not row['city']:
            zip_code = row['zip']
            if zip_code in zip_city_map:
                row['city'] = zip_city_map[zip_code].title()

# Write the updated rows back to the CSV file
with open('companies_city.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=reader.fieldnames)
    writer.writeheader()
    writer.writerows(rows)