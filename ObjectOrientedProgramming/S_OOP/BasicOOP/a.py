class Student:
	def __init__(self, name):
		self.name = name
	
	def getName(self):
		return self.name



student1 = Student("Kim")
print(student1.getName())