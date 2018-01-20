# SELECT

import sqlite3

with sqlite3.connect("new.db") as connection:
	cursor = connection.cursor()

	# print the results
	for row in cursor.execute("SELECT firstname, lastname FROM employees"):
		print(row)