# Just ignore this

class BebeNotFoundException(Exception):
	def __init__(self, value):
		super().__init__("")
		value = value.lower()
		if value == "meron":
			self.error = "Wala ka nun priii"
		elif value == "wala":
			self.error = "Buti alam mo"
		else:
			self.error = "Invalid Input"

class Sample:
	def __init__(self):
		self.answer = input("May bebe ka? ")
	
	def getAnswer(self):
		raise BebeNotFoundException(self.answer)

# try:
# 	a = input("May bebe ka? ")
# 	raise BebeNotFoundException(a)
# except BebeNotFoundException as e:
# 	print(e.error)

try:
	sample = Sample()
	sample.getAnswer()
except BebeNotFoundException as e:
	print(e.error)