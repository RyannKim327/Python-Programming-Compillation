class Animal:
	def __init__(self, type, sound):
		self.type = type
		self.sound = sound

	def sound(self):
		print(f"The {self.type} sounds like {self.sound}")

class Dog(Animal):
	def __init__(self, type, sound):
		self.type = "DOG"
		self.sound = "Awrf"

dog = Dog("Dog", "Awrf")
