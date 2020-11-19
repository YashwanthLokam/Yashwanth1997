"""Framework program using SQLite"""
import sqlite3
file_not_found_message = "File does not exist or unable to open the file."

menu_file_name = "menu.cfg"
with open(menu_file_name) as menu_file_obj:
	try:
		menu = menu_file_obj.read()
		menu_file_obj.close()
	except FileNotFoundError:
		print(file_not_found_message)

updatable_fields_position_file = "updatable_fields_position.cfg"
with open(updatable_fields_position_file) as updatable_fields_position_obj:
	try:
		updatable_fields_position = updatable_fields_position_obj.readlines()
		updatable_fields_position_obj.close()
	except FileNotFoundError:
		print(file_not_found_message)

messages_file = "messages.cfg"
with open(messages_file) as messages_obj:
	try:
		messages = messages_obj.read()
		messages = eval(messages)
		messages_obj.close()
	except FileNotFoundError:
		print(file_not_found_message)

connection = sqlite3.connect("framework.db")
cursor = connection.execute("pragma table_info('my_table')")
field_names = []
for field_name in cursor:
	if field_name[1] != 'Status':
		field_names.append(field_name[1])

def check_record_present(id):
	is_record_found = False
	records = connection.execute('SELECT ' + field_names[0] + ' FROM my_table WHERE Status = "A"')
	for record in records:
		if record[0] == id:
			is_record_found = True
	return is_record_found

def print_record(record):
	index = 0
	for field_name in field_names:
		print(field_name + ": " + str(record[index]))
		index += 1
	print('-' * 20)

def print_record_not_found():
	print(messages[2])

def get_id():
	return input("Enter " + field_names[0] + ": ")

def create_record():
	field_values = []
	for field_name in field_names:
		print(field_name + ": ", end = "")
		field_value = input()
		field_values.append(field_value)
	field_values.append('A')
	record = tuple(field_values)
	connection.execute('INSERT INTO my_table VALUES' + str(record))
	connection.commit()
	print(messages[0])

def search_record():
	id_to_search_record = get_id()
	is_record_found = check_record_present(id_to_search_record)
	if is_record_found == True:
		record_obj = connection.execute('SELECT * FROM my_table WHERE ' + field_names[0] + ' = ' + id_to_search_record)
		record = record_obj.fetchone()
		print_record(record)
	else:
		print_record_not_found()

def print_all_records():
	query = "SELECT * FROM my_table WHERE Status = 'A'"
	records = connection.execute(query)
	for record in records:
		print_record(record)

def delete_record():
	id_to_delete_record = get_id()
	is_record_found = check_record_present(id_to_delete_record)
	if is_record_found == True: 
		connection.execute('UPDATE my_table SET Status = "D" WHERE ' + field_names[0] + ' = ' + id_to_delete_record)
		connection.commit()
		print(messages[1])
	else:
		print_record_not_found()
		
def update_record():
	id_to_update_record = get_id()
	is_record_found = check_record_present(id_to_update_record)
	if is_record_found == True:
		counter = 1
		for field_position in updatable_fields_position:
			print(str(counter) + ". Update " + field_names[int(field_position.rstrip()) - 1])
			counter += 1
		choice = int(input("Enter a number: "))
		if choice > 0 and choice < counter:
			print("Enter " + field_names[int(updatable_fields_position[choice - 1].rstrip()) - 1] +": ", end = "")
			field_value_to_update_record = input()
			connection.execute('UPDATE my_table SET ' + field_names[int(updatable_fields_position[choice - 1].rstrip()) - 1] + ' = ' + "\"" + field_value_to_update_record + "\""+ ' WHERE ' + field_names[0] + ' = ' + id_to_update_record)
			connection.commit()
			print(field_names[int(updatable_fields_position[choice - 1].rstrip()) - 1] + " is updated.")
		else:
			print("ENTER A VALID NUMBER.")
	else:
		print_record_not_found()

def confirm_to_exit():
	print("Are you sure? ")
	print("Press Y or N" + ": ", end = "")
	choice = input()
	if choice.upper() == 'Y':
		connection.close()
		exit()

functions_list = [create_record, search_record, print_all_records, update_record, delete_record, confirm_to_exit]

while True:
	print(menu)
	user_choice = input("Enter a number: ")
	user_choice = int(user_choice)
	if user_choice > 0 and user_choice <= 6:
		functions_list[user_choice - 1]()
	else:
		print("ENTER A VALID NUMBER.")
