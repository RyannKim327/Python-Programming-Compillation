class IT2A:
	def __init__(self, name, section, subject):
		self.attendance = 0
		self.name = name
		self.section = section
		self.subject = subject
		msg = f"Student name: {self.name}\nSection: {self.section}\nSubject: {self.subject}"
		print(msg)
	
	def present(self):
		self.attendance += 1

	def absent(self):
		self.attendance -= 1
	
	def totalGrade(self):
		self.total_grade = self.attendance + 80
		msg = f"Student {self.name} "

kim = IT2A("Kim", "IT2A", "PF101")
gem = IT2A("Gem", "IT2A", "PF101")
jiro = IT2A("Jiro", "IT2A", "PF101")