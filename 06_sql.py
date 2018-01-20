# SELECT, remove unicode characters

import sqlite3

with sqlite3.connect("new.db") as connection:
	cursor = connection.cursor()

	cursor.execute("SELECT firstname, lastname FROM employees")

	# retrieve all records from the query
	rows = cursor.fetchall()

	# output the rows
	for r in rows:
		print(r[0], r[1])