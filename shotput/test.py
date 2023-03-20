import csv

# Replace these values with your own.
csv_file_path = 'athletesdb/shotput/data_shotput/OGmen22.csv'
sql_file_path = 'athletesdb/shotput/data_shotput/test.sql'
table_name = 'test'
field_names = ['competition', 'country', 'link', 'mark', 'name', 'position', 'sport']

# Open the CSV file and read its contents.
with open(csv_file_path, 'r') as csv_file:
    reader = csv.reader(csv_file)
    # Skip the header row.
    next(reader)
    # Open the SQL file for writing.
    with open(sql_file_path, 'w') as sql_file:
        # Loop through the rows in the CSV file.
        for row in reader:
            # Generate an SQL statement for the current row.
            values = ', '.join("'" + value.replace("'", "''") + "'" for value in row)
            sql_statement = "INSERT INTO {} ({}) VALUES ({});\n".format(table_name, ', '.join(field_names), values)
            # Write the SQL statement to the SQL file.
            sql_file.write(sql_statement)