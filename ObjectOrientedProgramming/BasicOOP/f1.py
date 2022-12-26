# Object Oriented Programming
class room:
	def __init__(self):
		self.data = "Sample"
	
	def set(self, text):
		self.data = text
	
	def get(self):
		return self.data