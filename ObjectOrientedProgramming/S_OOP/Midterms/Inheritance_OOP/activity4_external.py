class Animal:
	def __init__(self, name, specie):
		self.type = name
		self.sound = specie
	
	def speak(self):
		print(f"{self.name} is an {self.specie} and makes a sound.")
	
class Dog(Animal):
	def __init__(self, name, specie):
		super.__init__(name, specie)
		