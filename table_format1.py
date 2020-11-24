def print_border_line(max_length_of_field_values_in_each_column, field_names):
	counter = 0
	for field_name in field_names:
		print('+', end = "")
		for index in range(0,max((len(field_name)), max_length_of_field_values_in_each_column[counter]) + 2):
			print('-', end = "")
		counter += 1
	print('+')

def display_table_format(records, field_names):
	max_length_of_field_values_in_each_column = []
	index = 1
	for field_name in field_names:
		lengths_of_field_value = []
		for record in records:
			length = len(str(record[index - 1]))
			lengths_of_field_value.append(length)
		max_length_of_field_values_in_each_column.append(max(lengths_of_field_value))
		index += 1
	print_border_line(max_length_of_field_values_in_each_column, field_names)
	print('| ', end = "")
	counter = 0
	for field_name in field_names:
		print(field_name, end ="")
		if len(field_name) < max_length_of_field_values_in_each_column[counter]:
			for index_for_space in range(0, max_length_of_field_values_in_each_column[counter] - len(field_name)):
				print(' ', end = "")
		print(' | ', end = "")
		counter += 1
	print()
	print_border_line(max_length_of_field_values_in_each_column, field_names)
	print_all_records(records, field_names, max_length_of_field_values_in_each_column)

def print_all_records(records, field_names, max_length_of_field_values_in_each_column):
	for record in records:
		index = 1
		counter = 0
		print('| ', end = "")
		for field_name in field_names:
			print(record[index - 1], end = "")
			max_length = max(len(field_name), max_length_of_field_values_in_each_column[counter])
			if len(str(record[index - 1])) < max_length:
				for index_for_space in range(0, max_length - len(str(record[index - 1]))):
					print(' ', end = "")
			print(' | ', end = "")
			index += 1
			counter += 1
		print()
	print_border_line(max_length_of_field_values_in_each_column, field_names)