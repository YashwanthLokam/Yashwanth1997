"""Frame work using xml"""
import xml.etree.ElementTree as ET

tree = ET.parse("data.xml")
root = tree.getroot()

def print_record_not_found():
	print("Record is not found.")

def save_all_records():
	with open("data1.xml", "wb") as data_obj: 
	    tree.write(data_obj)
	data_obj.close()

def	print_record(record):
	for field_name in field_names:
		print(field_name + ": ", end = "")
		print(record.find(field_name).text)

def create_record():
	root_element = ET.Element('record')
	root_element.set('status', 'A')
	for field_name in field_names:
		root_sub_element = ET.SubElement(root_element, field_name)
		field_value = input("Enter " + field_name + ": ")
		root_sub_element.text = field_value
	root.append(root_element)
	save_all_records()
	print("Record is inserted.")

def	search_record():
	id = input("Enter " + field_names[0] + ": ")
	is_record_found = False
	for record in root.findall('record'):
		if record.attrib['status'] == 'A' and record.find(field_names[0]).text == id:
			is_record_found = True
			print_record(record)
			break
	if is_record_found == False:
		print_record_not_found()

def print_all_records():
	for record in root.findall('record'):
		if record.attrib['status'] == 'A':
			print_record(record)

def update_record():
	id = input("Enter " + field_names[0] + ": ")
	is_record_found = False
	counter = 1
	for record in root.findall('record'):
		if record.attrib['status'] == 'A' and record.find(field_names[0]).text == id:
			is_record_found = True
			for field_position in updatable_fields_position:
				print(str(counter) + ". Update " + field_names[int(field_position.rstrip()) - 1])
				counter += 1
			choice = int(input("Enter a number: "))
			print("Enter " + field_names[int(updatable_fields_position[choice - 1].rstrip()) - 1]  + ": ", end = "")
			record.find(field_names[int(updatable_fields_position[choice - 1].rstrip()) - 1]).text = input()
			print(field_names[int(updatable_fields_position[choice - 1]) - 1] + " is updated.")
			break
	if is_record_found == False:
		print_record_not_found()
	else:
		save_all_records()

def delete_record():
	id = input("Enter " + field_names[0] + ": ")
	is_record_found = False
	for record in root.findall('record'):
		if record.attrib['status'] == 'A' and record.find(field_names[0]).text == id:
			is_record_found = True
			record.set('status', 'D')
			print("Record is deleted.")
			break
	if is_record_found == False:
		print_record_not_found()
	else:
		save_all_records()

def confirm_to_exit():
	print("Do you want to exit? ")
	print("Press Y or N" + ": ", end = "")
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

functions_list = [create_record, search_record, print_all_records, update_record, delete_record, confirm_to_exit]

while True:
	print(menu)
	user_choice = input("Enter a number: ")
	user_choice = int(user_choice)
	if user_choice > 0 and user_choice <= 6:
		functions_list[user_choice - 1]()
	else:
		print("PLEASE ENTER A VALID NUMBER.")
