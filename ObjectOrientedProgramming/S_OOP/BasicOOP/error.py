class Error:
	def __init__(self):
		self.errors = []
	
	def getAllErrors(self):
		for i in self.errors:
			print(i)

	def addError(self, error: str):
		self.errors.append(error)

error = input("Enter a sample error: ")
while not error == "":
	