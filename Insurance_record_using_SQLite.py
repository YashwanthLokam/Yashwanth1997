"""Insurance with SQLite"""
import sqlite3
file_not_found_message = "File does not exist or unable to open the file."

field_names = ['Policy_Number', 'Insured_Name', 'Mobile_Number', 'Age', 'Tenure', 'Premium_Amount', 'Registration_No']		

fields_data_types_file = "data_types_of_fields.cfg"
with open(fields_data_types_file) as fields_data_types_obj:
	try:
		data_types_of_fields = fields_data_types_obj.read()
	except FileNotFoundError:
		print(file_not_found_message)
	else:
		fields_data_types_obj.close()

connection = sqlite3.connect("test.db")
connection.execute('CREATE TABLE IF NOT EXISTS Insurance(' + data_types_of_fields + ')')

def create_record():
	field_values = []
	field_values.append('A')
	for field_name in field_names:
		print(field_name + ": ", end = "")
		field_value = input()
		field_values.append(field_value)
	field_values_tuple = tuple(field_values)
	connection.execute('INSERT INTO Insurance VALUES' + str(field_values_tuple))
	connection.commit()
	print("Record is inserted.")

def print_all_records():
	query = "SELECT * FROM Insurance WHERE Status = 'A'"
	records = connection.execute(query)
	for record in records:
		index = 1
		for field_name in field_names:
			print(field_name + ": " + str(record[index]))
			index += 1

create_record()
print_all_records()

connection.close()