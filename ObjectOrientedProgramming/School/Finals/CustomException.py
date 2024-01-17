# Just ignore this

class BebeNotFoundException(Exception):
	def __init__(self, value):
		super().__init__("")
		value = value.lower()
		if value != "wala":
			self.error = "Wala ka nun pre."
	
	def __str__(self) -> str:
		return self.error

class Sample:
	def __init__(self):
		self.answer = input("May bebe ka? ")
	
	def getAnswer(self):
		if self.answer.lower() == "wala":
			return("Buti alam mo")
		else:
			raise BebeNotFoundException(self.answer)

# try:
# 	a = input("May bebe ka? ")
# 	raise BebeNotFoundException(a)
# except BebeNotFoundException as e:
# 	print(e.error)

sample = Sample()
try:
	print(sample.getAnswer())
except BebeNotFoundException as e:
	print(e)