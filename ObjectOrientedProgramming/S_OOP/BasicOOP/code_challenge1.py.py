from code_challenge1_external import *

students= []
librarians = []
books = []

def start():
	choice = input("Login as:\n[1] Student\n[2] Librarian\n[3] Exit\nEnter your choice: ")
	_a_ = ["1", "2", "3"]

	while not choice in _a_:
		choice = input("Login as:\n[1] Student\n[2] Librarian\n[3] Exit\nEnter your choice: ")
	
	match choice:
		case "1":
			id = len(students) + 1
			name = input("Enter your name: ")
			student = Student({
				"ID": id,
				"studentName": name
			})

			print(f"Welcome to Library Mr/Ms. {student.getStudentName()}")
			another_choice = input("Enter a book you want to borrow")

			students.append(student)
		case "2":
			id = len(librarians)
			librarian = Librarian()
		case _:
			print("Thank you...")
			break

if __name__ == "__main__":
	start()