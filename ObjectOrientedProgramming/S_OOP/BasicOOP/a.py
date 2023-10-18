class class_s:
	def __init__(self):
		self.a_class = []
		print("Initated")

	def a(self):
		return 123
	
	def addclass(self, class_a):
		self.a_class.append(class_a)

	def __str__(self):
		return "This class is for something"

class class_a:
	def __init__(self):
		print("This is class a")

s = class_s()
print(s)
print(s.a())

a = class_a()
s.addclass(a)
