import json

class MayErrorPre(Exception):
	def __init__(self):
		self.__errorprii__ = "Ginagawa mueh"
	
	def __str__(self):
		return self.__errorprii__

class StudentData:
	def __init__(self):
		self.file = "sample.json"
		try:
			with open(self.file, "r") as file:
				self.data = json.loads(file.read())
		except:
			self.data = {}
			with open(self.file, "w") as file:
				file.write(json.dumps(self.data, indent=4))

	def addStudent(self):
		name = input("Enter student name: ")
		if name == "":
			raise MayErrorPre()
		grade = input("Enter student grade: ")
		while not grade.isdigit():
			grade = input("Enter student grade: ")
		grade = int(grade)
		
		if self.data.get(name) == None:
			self.data[name] = []
		self.data[name].append(grade)
	
	def saveToJSON(self):
		with open(self.file, "w") as file:
			file.write(json.dumps(self.data, indent=4))
			print("Data modified successfully")

	def viewGrades(self):
		print("Student liists")
		for i in self.data.keys():
			print(i)
		name = input("Please enter the student name: ")
		try:
			with open(self.file, "r") as file:
				data = json.loads(file.read())
			grade = ""
			for i in data:
				grade += f"{i}\n"
			print(f"Grades: {grade}\nAverage: {sum(data) / len(data)}")
		except:
			print("Student not found")
		

if __name__ == "__main__":
	try:
		student = StudentData()
		student.addStudent()
		student.viewGrades()
		student.saveToJSON()
	except Exception as e:
		print(e)