# Python program to run SQLite commands with out using SQLite command prompt
import sqlite3
from printy import printy
import subprocess
import sys

def establish_connection(name_of_database):
	return sqlite3.connect(name_of_database)
	
print("SQLite version 3.33.0 2020-08-14 13:23:32")
print("Enter \".help\" for usage hints.")
if len(sys.argv) == 2:
	name_of_database = sys.argv[1]
else:
	print("Connected to a ", end = "")
	printy("transient in-memory database", "r", end = "")
	print(".")
	print("Use \".open FILENAME\" to reopen on a persistent database.")
	name_of_database = 'temp.db'
connection = establish_connection(name_of_database)
while True:
	print("sqlite> ", end = "")
	query = input()
	if query[0] != '.':
		try:
			response = connection.execute(query.replace(";", ""))
			records = response.fetchall()
			connection.commit()
		except:
			print("INVALID QUERY")
			continue
		if records != []:
			for record in records:
				count = len(record)
				for index in range(count):
					print(record[index], end = "")
					if index != count - 1:
						print("|", end = "")
				print()
	else:
		if query == '.quit':
			connection.close()
			exit()
		elif query[:5] == '.open':
			connection.close()
			name_of_database = query[6:]
			connection = establish_connection(name_of_database)
		else:
			subprocess.run(['sqlite3', name_of_database, query])

