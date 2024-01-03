class Student:
	def __init__(self, name):
		self.name = name
		print("Initiated student")
	
	def getName(self):
		return self.name
	
	def setName(self, name):
		self.name = name

class Teacher:
	def __init__(self, name):
		self.name = name
	
	def getName(self):
		return self.getName()
	
	def setName(self, name):
		self.name = name

students = []

while True:
	name  = input("Enter student name: ")
	student = Student(name)
	students.append(student)

	if input("Would you like to continue? ") == "n":
		break

student_names = [f"The name is {student.getName()}" for student in students]
print(student_names)