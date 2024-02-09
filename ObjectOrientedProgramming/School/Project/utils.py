import json
class JSON:
	def __init__(self):
		with open("students.json", "r") as file:	
			self._json = json.load(file)

class Student:
	def __init__(self):
		self.name = "Enter student name: "
		