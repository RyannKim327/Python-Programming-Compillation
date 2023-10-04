class Animal:
	def __init__(self):
		self.type = "Animal"
		self.sound = "Wala"

	def itis(self):
		print(f"The {self.type} sounds like {self.sound}")

class Dog(Animal):
	def __init__(self):
		self.type = "DOG"
		self.sound = "Awrf"
	
dog = Dog()
dog.itis()