import json
class StudentData:
	def __init__(self):
		self.file = "sample.json"
	
	def addStudent(self):
		name = input("Enter student name: ")
		while name == "":
			name = input("Enter student name: ")
		grade = input("Enter student grade: ")
		while not grade.digit():
			grade = input("Enter student grade: ")
		grade = int(grade)
		with open(self.file) as file:
			data = file.read()
		try:
			data = json.loads(data)
			if data.get(name) == None:
				data[name] = []
			
		except:
			pass
		

if __name__ == "__main__":
	student = StudentData()
