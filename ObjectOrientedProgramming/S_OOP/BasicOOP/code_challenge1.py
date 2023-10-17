from code_challenge1_external import *

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
	stocks = insert("Enter the number of stocks: ")
	while not stocks.isdigit():
		stocks = input("Enter the number of stocks: ")

	book = Books({
		"ID": id,
		"title": name,
		"author": author,
		"publisher": publisher,
		"date": date,
		"stocks": int(stocks)
	})

	books.append(book)

def start():
	global books, librarians, students
	menu = [
		"Student",
		"Librarian"
	]
	# choice = insert("Login as:\n[1] Student\n[2] Librarian\n[3] Exit\nEnter your choice: ")
	typing("Welcome to my Library Management System. Would you like to LOGIN as: ")
	_a_ = ["1", "2"]
	choice = insertlists(menu, "Enter your choice:")
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
						books_ = [i.getBookName() for i in books]
						another_choice = insertlists(books_, "Enter a book you want to borrow: ")

			if it:
				student = Student({
					"ID": id,
					"studentName": name
				})

				typing(f"Welcome to Library Mr/Ms. {student.getStudentName()}")
				if len(books) <= 0:
					print("There's no books yet.")
				else:
					books_ = [i.getBookName() for i in books]
					another_choice = insertlists(books_, "Enter a book you want to borrow: ")
					while not another_choice.isdigit():
						another_choice = input("Enter a book you want to borrow: ")

					books[int(another_choice) - 1].doBorrow()

				students.append(student)
				if not "Exit" in menu:
					menu.append("Exit")
					_a_.append("3")

		case "2":
			id = len(librarians) + 1
			name = input("Enter your name: ")
			it = True
			for lib in librarians:
				if name == lib.getName():
					attempt = 5
					password = insert("Enter your password: ", True)
					while password != lib.getPassword():
						if attempt == 0:
							input("Ano kaya pa? ")
						password = insert("Enter your password: ", True)
						attempt -= 1
					it = False
					librarian = lib
			if it:
				password = insert("Enter your password: ", True)
				password1 = insert("Verify your password: ", True)
				while password != password1:
					password = insert("Enter your password: ", True)
					password1 = insert("Verify your password: ", True)

				librarian = Librarian({
					"ID": id,
					"name": name,
					"password": password
				})
				librarians.append(librarian)

			_b_ = ["Enter a book", "Modify a book", "Exit"]
			_c_ = ["1"]
			insert("What do you want to do? ")

			enterBook(librarian)
			if not "Exit" in menu:
				menu.append("Exit")
				_a_.append("3")
			
		case _:
			typing("Thank you for using this project\nCode challege accepted by Ryann Kim Sesgundo of BS Information Technology 2A...")
			cont = False

	if cont:
		start()

if __name__ == "__main__":
	start()