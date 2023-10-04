class IT2A:
	def __init__(self, name, section, subject):
		self.attendance = 0
		self.name = name
		self.section = section
		self.subject = subject
		msg = f"Student name: {self.name}\nSection: {self.section}\nSubject: {self.subject}"
		print(msg)

kim = IT2A("Kim")