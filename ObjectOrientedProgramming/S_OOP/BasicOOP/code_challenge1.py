from code_challenge1_external import *
import getpass

students= []
librarians = []
books = []

def enterBook(librarian):
	global books
	id = len(books) + 1
	name = input("Enter the book name: ")
	author = input("Enter the book author: ")
	publisher = input("Enter the publisher name: ")
	date = input("Enter the publishing date: ")
	book = Books()
	pass

def start():
	global books, librarians, students
	choice = input("Login as:\n[1] Student\n[2] Librarian\n[3] Exit\nEnter your choice: ")
	_a_ = ["1", "2", "3"]

	while not choice in _a_:
		choice = input("Login as:\n[1] Student\n[2] Librarian\n[3] Exit\nEnter your choice: ")
	
	match choice:
		case "1":
			id = len(students) + 1
			name = input("Enter your name: ")
			for i in students:
				if name == i.getStudentName():
					
			student = Student({
				"ID": id,
				"studentName": name
			})

			print(f"Welcome to Library Mr/Ms. {student.getStudentName()}")
			if len(books) <= 0:
				print("There's no books yet.")
			else:
				another_choice = input("Enter a book you want to borrow: ")

			students.append(student)

		case "2":
			id = len(librarians) + 1
			name = input("Enter your name: ")
			password = getpass.getpass("Enter your password: ")
			for lib in librarians:
				lib.getName()
			password1 = getpass.getpass("Verify your password: ")
			while password == password1:
				password = getpass.getpass("Enter your password: ")
				password1 = getpass.getpass("Verify your password: ")

			librarian = Librarian({
				"ID": id,
				"name": name,
				"password": password
			})

			enterBook(librarian)

			librarians.append(librarian)

		case _:
			print("Thank you...")

if __name__ == "__main__":
	start()