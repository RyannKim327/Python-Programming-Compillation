class Animal:
	def __init__(self, type, sound):
		self.type = type
		self.sound = sound

	def sound(self):
		print(f"The {self.type}")