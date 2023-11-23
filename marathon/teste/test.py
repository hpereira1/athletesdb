import csv
import os

directory = '/home/hpereira1/Documents/Projetopet/athletesdb/teste/tokyo/data-mar/fim/'
# Replace these values with your own.
#csv_file_path = 'athletesdb/shotput/data_shotput/OGmen22.csv'
table_name = 'marathon'
field_names = ['competition', 'country', 'gender', 'link', 'mark', 'name', 'position', 'sport']
sql_script = ''
# Open the CSV file and read its contents.
for filename in os.listdir(directory):
    if filename.endswith('.csv'):
        file_path = os.path.join(directory, filename)
        with open(file_path, 'r') as csv_file:
            reader = csv.reader(csv_file)
            # Skip the header row.
            next(reader)
            for row in reader:
                sql_script += f"INSERT INTO {table_name} (competition, country,gender, link, mark, name, position, sport)  VALUES ('{row[0]}', '{row[1]}', '{row[2]}','{row[3]}',CONCAT('0', '{row[4]}'),'{row[5]}','{row[6]}', '{row[7]}');\n"
                # Write the SQL statement to the SQL file.
with open('insert_major_fim.sql', 'w') as sql_file:
    sql_file.write(sql_script)
print(sql_script)
print("script gerado")
