# Python program to run MySQL commands
import mysql.connector
import table_format1
import time

my_database = mysql.connector.connect(host = "165.22.14.77", user = "Yashwanth", password = "Yashwanth", database = "dbYashwanth")

print("Welcome to the MySQL monitor.  Commands end with ; or \\g.")
print("Your MySQL connection id is " + str(my_database.connection_id))
print("Server version: 5.7.32-0ubuntu0.18.04.1 (Ubuntu)")
print("\nCopyright (c) 2000, 2020, Oracle and/or its affiliates. All rights reserved.")
print("\nOracle is a registered trademark of Oracle Corporation and/or its")
print("affiliates. Other names may be trademarks of their respective")
print("owners.")
print("\nType 'help;' or '\\h' for help. Type '\\c' to clear the current input statement.")
while True:
	query = input("mysql> ")
	my_cursor = my_database.cursor()
	if query.lower() != "quit":
		start = time.time()
		try:
			my_cursor.execute(query)
		except:
			print("Invalid query")
			exit()
		if query[0:6].lower() != "select" and query[0:4].lower() != "show":
			my_database.commit()
		else:
			field_names = []
			list_of_field_values = []
			for description in my_cursor.description:
				field_names.append(description[0])
			for field_values in my_cursor:
				list_of_field_values.append(field_values)
			table_format1.display_table_format(list_of_field_values, field_names)
			end = time.time()
			print(str(len(list_of_field_values)) + "row(s) in set(" + str(round(end - start, 2)) + " secs)")
	else:
		my_database.close()
		print("Bye")
		exit()

