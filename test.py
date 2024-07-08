import sqlite3
connection= sqlite3.connect('example.db')
cursor = connection.cursor()
cursor.execute('''SELECT * FROM books''')
data = cursor.fetchall()
print(data)