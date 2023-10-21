class Student:
	def __init__(self, name):
		self.name = name
		print("Initiated student")
	
	def getName(self):
		return self.name
	
	def setName(self, name):
		self.name = name


students = []

while True:
	