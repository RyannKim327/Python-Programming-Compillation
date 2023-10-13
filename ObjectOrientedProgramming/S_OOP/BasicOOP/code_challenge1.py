from code_challenge1_external import *
import getpass

students= []
librarians = []
books = []

def enterBook(librarian):
	global books
	id = len(books) + 1
	name = insert("Enter the book name: ")
	author = insert("Enter the book author: ")
	publisher = insert("Enter the publisher name: ")
	date = insert("Enter the publishing date: ")
	book = Books({
		"ID": id,
		"title": name,
		"author": author,
		"publisher": publisher,
		"date": date,
		"isBorrowed": False
	})
	pass

def start():
	global books, librarians, students
	menu = [
		"Student",
		"Librarian",
		"Exit"
	]
	# choice = insert("Login as:\n[1] Student\n[2] Librarian\n[3] Exit\nEnter your choice: ")
	typing("Welcome to my Library Management System:")
	_a_ = ["1", "2", "3"]
	byonearray(menu, "Enter your choice:")
	cont = True

	while not choice in _a_:
		choice = input("Login as:\n[1] Student\n[2] Librarian\n[3] Exit\nEnter your choice: ")
	
	match choice:
		case "1":
			id = len(students) + 1
			name = insert("Enter your name: ")
			it = True
			for i in students:
				if name == i.getStudentName():
					typing(f"Welcome back to Library Mr/Ms. {i.getStudentName()}")
					it = True
					if len(books) <= 0:
						print("There's no books yet.")
					else:

						another_choice = input("Enter a book you want to borrow: ")

			if it:
				student = Student({
					"ID": id,
					"studentName": name
				})

				typing(f"Welcome to Library Mr/Ms. {student.getStudentName()}")
				if len(books) <= 0:
					print("There's no books yet.")
				else:
					another_choice = input("Enter a book you want to borrow: ")

				students.append(student)

		case "2":
			id = len(librarians) + 1
			name = input("Enter your name: ")
			it = True
			for lib in librarians:
				if name == lib.getName():
					attempt = 5
					password = getpass.getpass("Enter your password: ")
					while password != lib.getPassword():
						if attempt == 0:
							input("Ano kaya pa? ")
						password = getpass.getpass("Enter your password: ")
						attempt -= 1
					it = False
					librarian = lib
			if it:
				password = getpass.getpass("Enter your password: ")
				password1 = getpass.getpass("Verify your password: ")
				while password != password1:
					password = getpass.getpass("Enter your password: ")
					password1 = getpass.getpass("Verify your password: ")

				librarian = Librarian({
					"ID": id,
					"name": name,
					"password": password
				})
				librarians.append(librarian)

			enterBook(librarian)
			
		case _:
			print("Thank you...")
			cont = False

	if cont:
		start()

if __name__ == "__main__":
	start()