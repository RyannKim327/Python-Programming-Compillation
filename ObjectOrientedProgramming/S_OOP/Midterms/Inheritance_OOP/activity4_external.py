class Animal:
	def __init__(self, name, specie):
		self.type = name
		self.sound = specie
	
	def speak(self):
		print(f"{self.name} is an {self.specie} and makes a sound.")
	
class Dog(Animal):
	def __init__(self, name, breed):
		super().__init__(name, "Dog")
		self.name = name
		self.breed = breed

	def speak(self):
		print(f"{self.name}, is a type of {self.breed} and makes a sound.")