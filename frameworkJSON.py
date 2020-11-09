"""Framework using JSON"""

def print_record_not_found():
	print("Record is not found.")

def save_all_records():
	with open(data_file_name, 'w') as data_file_obj:
		data_file_obj.write(str(data))
	data_file_obj.close()

def print_record(record):
	for field_name in field_names:
		print(field_name + ": " + record[field_name])

def get_id():
	id = input("Enter " + field_names[0] + ": ")
	return id

def create_record():
	record = {}
	record['Status'] = 'A'
	for field_name in field_names:
		record[field_name] = input("Enter " + field_name + ": ")
	data[records].append(record)
	save_all_records()

def search_record():
	id = get_id()
	is_record_found = False
	for record in data[records]:
		if record['Status'] == 'A' and record[field_names[0]] == id:
			print_record(record)
			is_record_found = True
			break
	if is_record_found == False:
		print_record_not_found()

def print_all_records():
	for record in data[records]:
		if record['Status'] == 'A':
			print_record(record)

def update_record():
	id = get_id()
	is_record_found = False
	for record in data[records]:
		if record['Status'] == 'A' and record[field_names[0]] == id:
			is_record_found = True
			counter = 1
			for field_position in updatable_fields_position:
				print(str(counter) + ". Update " + field_names[int(field_position.rstrip()) - 1])
				counter += 1
			choice = int(input("Enter a number: "))
			print("Enter " + field_names[int(updatable_fields_position[choice - 1].rstrip()) - 1] +": ", end = "")
			record[field_names[int(updatable_fields_position[choice - 1].rstrip()) - 1]] = input()
			print(field_names[int(updatable_fields_position[choice - 1].rstrip()) - 1] + " is updated.")
			break
	if is_record_found == False:
		print_record_not_found()
	else:
		save_all_records()

def delete_record():
	id = get_id()
	is_record_found = False
	for record in data[records]:
		if record['Status'] == 'A' and record[field_names[0]] == id:
			is_record_found = True
			record['Status'] = 'D'
			print("Record is deleted")
			break
	if is_record_found == False:
		print_record_not_found()
	else:
		save_all_records()

def confirm_to_exit():
	print("Are you sure? ")
	print("Press Y or N" + ": ", end = "")
	choice = input()
	if choice == 'Y':
		exit()

data = {}
records = 'Records'

file_not_found_message = "File does not exist or unable to open the file."
menu_file_name = "menu.cfg"
with open(menu_file_name) as menu_file_obj:
	try:
		menu = menu_file_obj.read()
	except FileNotFoundError:
		print(file_not_found_message)
	else:
		menu_file_obj.close()
		
updatable_fields_position_file = "updatable_fields_position.cfg"
with open(updatable_fields_position_file) as updatable_fields_position_obj:
	try:
		updatable_fields_position = updatable_fields_position_obj.readlines()
	except FileNotFoundError:
		print(file_not_found_message)
	else:
		updatable_fields_position_obj.close()

field_names_file = "fields.cfg"
with open(field_names_file) as field_names_obj:
	try:
		field_names = field_names_obj.read()
		field_names = eval(field_names)

	except FileNotFoundError:
		print(file_not_found_message)
	else:
		field_names_obj.close()

data_file_name = "data.json"
with open(data_file_name) as data_file_obj:
	try:
		data[records] = data_file_obj.read()
		data = eval(data[records])
	except FileNotFoundError:
		print(file_not_found_message)
	else:
		data_file_obj.close()

functions_list = [create_record, search_record, print_all_records, update_record, delete_record, confirm_to_exit]

while True:
	print(menu)
	user_choice = input("Enter a number: ")
	user_choice = int(user_choice)
	if user_choice > 0 and user_choice <= 6:
		functions_list[user_choice - 1]()
	else:
		print("ENTER A VALID NUMBER.")