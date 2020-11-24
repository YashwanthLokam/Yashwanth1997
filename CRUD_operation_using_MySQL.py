# Framework program using MySQL databese
import mysql.connector
import table_format1
file_not_found_error = "File does not exist or unable to open the file."

menu_file = "menu.cfg"
updatable_fields_index_file = "updatable_field_positions1.cfg"
messages_file = "messages.cfg"

connection = mysql.connector.connect(host = "165.22.14.77", user = "Yashwanth", password = "Yashwanth", database = "dbYashwanth")
cursor = connection.cursor()

cursor.execute("select * from information_schema.columns where table_schema = 'dbYashwanth' and table_name = 'my_table1'")
field_names = []
for field_name in cursor:
	if field_name[3] != 'Status':
		field_names.append(field_name[3])

def read_data_from_file(file_name):
	try:
		with open(file_name) as data_file_obj:
			data = data_file_obj.read()
			data_file_obj.close()
			return data
	except:
		print(file_not_found_error)

def get_id():
	return input("Enter " + field_names[0] + ": ")

def check_record_present_or_not(id):
	is_record_found = False
	cursor.execute("SELECT " + field_names[0] + " FROM my_table1 WHERE Status = 'A'")
	for record in cursor:
		if record[0] == id:
			is_record_found = True
	return is_record_found

def print_record_not_found():
	print(messages[1])

def create_record():
	field_values = []
	for field_name in field_names:
		print("Enter " + field_name + ": ", end = "")
		field_value = input()
		field_values.append(field_value)
	field_values.append('A')
	record = tuple(field_values)
	cursor.execute('INSERT INTO my_table1 VALUES' + str(record))
	connection.commit()
	print(messages[0])

def search_record():
	id_to_search_record = get_id()
	is_record_found = check_record_present_or_not(id_to_search_record)
	field_values = []
	if is_record_found == True:
		cursor.execute('SELECT * FROM my_table1 WHERE ' + field_names[0] + ' = ' + id_to_search_record)
		record = cursor.fetchone()
		field_values.append(record)
		table_format1.display_table_format(field_values, field_names)
	else:
		print_record_not_found()

def print_all_records():
	cursor.execute("SELECT * FROM my_table1 WHERE Status = 'A'")
	records = []
	for record in cursor:
		records.append(record)
	table_format1.display_table_format(records, field_names)

def delete_record():
	id_to_delete_record = get_id()
	is_record_found = check_record_present_or_not(id_to_delete_record)
	if is_record_found == True:
		cursor.execute('UPDATE my_table1 SET Status = "D" WHERE ' + field_names[0] + ' = ' + id_to_delete_record)
		connection.commit()
		print(messages[2])
	else:
		print_record_not_found()

def update_record():
	id_to_update_record = get_id()
	is_record_found = check_record_present_or_not(id_to_update_record)
	if is_record_found == True:
		counter = 1
		for field_position in updatable_fields_index:
			print(str(counter) + ". Update " + field_names[int(field_position) - 1])
			counter += 1
		choice = int(input("Enter a number" + ": "))
		if choice > 0 and choice < counter:
			print("Enter " + field_names[int(updatable_fields_index[choice - 1]) - 1] + ": ", end = "")
			field_value_to_update_record = input()
			cursor.execute('UPDATE my_table1 SET ' + field_names[int(updatable_fields_index[choice - 1]) - 1] + ' = ' + "\"" + field_value_to_update_record + "\"" + ' WHERE ' + field_names[0] + ' = ' + id_to_update_record)
			connection.commit()
			print(field_names[int(updatable_fields_index[choice - 1]) - 1] + " is updated.")
		else:
			print("ENTER A VALID NUMBER.")
	else:
		print_record_not_found()

def confirm_to_exit():
	print("Are you sure? ")
	choice = input("Press Y or N: ")
	if choice.upper() == 'Y':
		connection.close()
		exit()

menu = read_data_from_file(menu_file)
updatable_fields_index = eval(read_data_from_file(updatable_fields_index_file))
messages = eval(read_data_from_file(messages_file))

functions_list = [create_record, search_record, print_all_records, update_record, delete_record, confirm_to_exit]

while True:
	print(menu)
	choice = int(input("Enter a number" + ": "))
	if choice > 0 and choice < 7:
		functions_list[choice - 1]()
	else:
		print("ENTER A VALID NUMBER.")
