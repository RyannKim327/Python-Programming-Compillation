class Animal:
	def __init__(self, _type, sound):
		self.type = _type
		self.sound = sound
	
	def speak(self):
		print(f"{self.sound} is an {self.type}")