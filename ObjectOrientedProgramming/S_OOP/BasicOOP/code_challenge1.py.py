from code_challenge1_external import *

student = []
librarian = []

def start():
	choice = input("Login as:\n[1] Student\n[2] Librarian\n[3] Exit")
	_a_ = ["1", "2", "3"]

	while choice in _a_:
		choice = input("Login as:\n[1] Student\n[2] Librarian\n[3] Exit\n")
	
	match choice:
		case "1":
			id = len(student)
			name = input("Enter your name: ")
			student = Student({
				"ID": id,
				"studentName": name
			})

			print(student.getStudentID())


if __name__ == "__main__":
	start()