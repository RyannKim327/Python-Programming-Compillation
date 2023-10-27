class Error:
	def __init__(self):
		self.errors = []
	
	def getAllErrors(self):
		for i in self.errors:
			print(i)

