import sqlite3

# connection of database
conn = sqlite3.connect("test.sqlite")

# Creating a table
conn.execute('''CREATE TABLE IF NOT EXISTS sample (
	ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	name VARCHAR(20),
	age INTEGER
)''')

def insert(conn):
	# Insertion of Data
	name = input("Please enter the name: ")
	age = input("Please enter the age: ")
	conn.execute(f"INSERT INTO sample (name, age) VALUES ('{name}', '{age}')")
	print("New data added")
	conn.commit()

def read(conn):
	# Reading a data
	rows = conn.execute("SELECT * FROM sample")
	for row in rows:
		print(f"ID: {row[0]}")
		print(f"name: {row[1]}")
		print(f"age: {row[2]}")

def update(conn):
	# Update a data
	id = input("Please enter the ID: ")
	name = input("Change the name to: ")
	age = input("Change the age to: ")
	conn.execute(f"UPDATE sample SET name = '{name}', age = {age} WHERE ID = {id}")
	print("Data updated successfully")
	conn.commit()

def delete(conn):
	# Delete a data
	id = input("Please enter the ID: ")
	conn.execute(f"DELETE FROM sample WHERE ID = {id}")
	print("Data deleted successfully")
	conn.commit()

if __name__ == "__main__":
	while True:
		print("Simple CRUD using Python and SQLite3")
		print("1. Create (insert)\n2. Read (select)\n3. Update\n4. Delete\n5. Terminate the program")
		n = int(input("Enter your choice: "))
		if n == 1:
			insert(conn)
		elif n == 2:
			read(conn)
		elif n == 3:
			update(conn)
		elif n == 4:
			delete(conn)
		elif n == 5:
			break

conn.close()