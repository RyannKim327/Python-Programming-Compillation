class Student:
	def __init__(self, name):
		self.name = name
	
	def getName(self):
		return self.name
	
	def setName(self, name):
		self.name = name



student1 = Student("Kim")
print(student1.getName())
student1.setName("Kimmy")
print(student1.getName())