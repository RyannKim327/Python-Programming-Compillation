class Animals:
	def __init__(self):
		print("I am an animal")
	def say(self, a):
		print(f"Hello {a}")
	
class Dog(Animals):
	def __init__(self):
		print("I am a Dog")

a = Animals()
b = Dog()
a.say("kim")
b.say("nix")