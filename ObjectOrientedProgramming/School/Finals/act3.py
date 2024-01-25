class StudentGradesManager:
	def __init__(self):
		self.file = ""
		self.name = ""

		with open("grades.txt", "r") as file:
			self.file = file.read()
	
	def addStudentGrade(self):
		if self.name == "":
			self.name = input("Enter student name: ")
		try:
			grade = int(input("Enter student grade: "))
			with open("grades.txt", "w") as file:
				file.write(f"The grade of {self.name}, is {grade}")
		except ValueError as valur:
			print("Please enter a valid grade")
			self.addStudentGrade()
		except Exception as e:
			print("Something went wrong")
	
	def viewStudentGrade(self):
		try:
			for i in self.file:
				print(f"{i.strip()}")
		except FileNotFoundError as e:
			print(f"File not found")
		except Exception as e:
			print("Something went wrong")

	def menu(self):
		return ["Add student grade", "View Student Grade"]

def main():
	student = StudentGradesManager()
	student.addStudentGrade()
	student.viewStudentGrade()

if __name__ == "__main__":
	main()