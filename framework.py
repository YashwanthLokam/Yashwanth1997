"""Framework program"""

def print_record_not_found():
	print("Record is not found.")

def print_record(field_values):			
	index = 1
	for field_name in field_names:
		print(field_name.rstrip(), ": ", field_values[index])
		index += 1

def save_all_records():
	with open(data_file_name, 'w') as data_obj:
		data_obj.write(str(records))
	data_obj.close()

def create_record():
	field_values = []
	status = 'A'
	field_values.append(status)
	index = 1
	for field_name in field_names:
		print("Enter ", field_name.rstrip(), ": ", end = "")
		field_value = input()
		field_values.append(field_value)
	records.append(field_values)
	save_all_records()
	print("Record is inserted.")

def print_all_records():
	for record in records:
		if record[0] == 'A':
			print_record(record)

def search_record():
	print("Enter ", field_names[0].rstrip(), ": ", end = "")
	id = input()
	for record in records:
		if record[0] == 'A' and record[1] == str(id):
			print("Record details\n")
			print_record(record)
			break

def update_record():
	print("Enter ", field_names[0].rstrip(), ": ", end = "")
	id = input()
	is_record_found = False
	counter = 1
	for record in records:
		if record[0] == 'A' and record[1] == str(id):
			is_record_found = True
			for field_position in updatable_fields_position:
				print(counter,". Update", field_names[int(field_position.rstrip())].rstrip())
				counter += 1
			choice = int(input("Enter a number: "))
			print("Enter ", field_names[int(updatable_fields_position[choice - 1].rstrip()) - 1].rstrip() ,": ", end = "")
			record[int(updatable_fields_position[choice - 1].rstrip())] = input()
			print(field_names[int(updatable_fields_position[choice - 1].rstrip()) - 1].rstrip(), "is updated.")
	save_all_records()
	if is_record_found == False:
		print_record_not_found()

def delete_record():
	print("Enter ", field_names[0].rstrip(), ": ", end = "")
	id = input()
	is_record_found = False
	for record in records:
		if record[0] == 'A' and record[1] == str(id):
			is_record_found = True
			record[0] ='D'
			print("Record is deleted.")
	save_all_records()
	if is_record_found == False:
		print_record_not_found()

def confirm_to_exit():
	print("Do you want to exit? ")
	print("Press Y or N", ": ", end = "")
	choice = input()
	if choice == 'Y':
		exit()

file_not_found_message = "File does not exist or unable to open the file."
menu_file_name = "menu.cfg"
with open(menu_file_name) as menu_file_obj:
	try:
		menu = menu_file_obj.read()
	except FileNotFoundError:
		print(file_not_found_message)
	else:
		menu_file_obj.close()
		
try:
	data_file_name = "data.dat"
	with open(data_file_name) as data_obj:
		records = data_obj.read()
		records = eval(records)
except FileNotFoundError:
	with open(data_file_name, 'w') as data_obj:
		records = []
		data_obj.write(str(records))
		data_obj.close()

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
		field_names = field_names_obj.readlines()
	except FileNotFoundError:
		print(file_not_found_message)
	else:
		field_names_obj.close()

functions_list = [create_record, search_record, print_all_records, update_record, delete_record, confirm_to_exit]

while True:
	print(menu)
	user_choice = input("Enter a number: ")
	user_choice = int(user_choice)
	if user_choice > 0 and user_choice <= 6:
		functions_list[user_choice - 1]()
	else:
		print("PLEASE ENTER A VALID NUMBER.")