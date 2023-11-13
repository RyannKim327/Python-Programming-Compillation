class Error:
	def __init__(self):
		self.errors = ()

	@property	
	def getAllErrors(self):
		for i in self.errors:
			print(i)

	def addError(self, *error: str):
		self.errors.append(error)

error = input("Enter a sample error: ")
err = Error()
while not error == "":
	err.addError(error)
	error = input("Enter another sample error: ")

err.getAllErrors