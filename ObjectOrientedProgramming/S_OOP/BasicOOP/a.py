class class_s:
	def __init__(self):
		print("Initated")

	def a(self):
		return 123

	def __str__(self):
		return "This class is for something"

class class_a:
	def __init__(self):
		print("This is class a")

s = class_s()
print(s)
print(s.a())