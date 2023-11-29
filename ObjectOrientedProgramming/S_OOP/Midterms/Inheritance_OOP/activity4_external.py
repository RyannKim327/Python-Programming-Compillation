class Animal:
	def __init__(self, name, sound):
		self.type = name
		self.sound = sound
	
	def speak(self):
		print(f"{self.name} is an {self.type} and makes a sound.")
	
class Dog(Animal):
	