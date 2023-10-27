class Pizza:
	def __init__(self, size: str, toppings=[]):
		self.size = size
		self.toppings = toppings
		self.price = 0
	
	def get_description(self):
		return f"A {size} pizza that"