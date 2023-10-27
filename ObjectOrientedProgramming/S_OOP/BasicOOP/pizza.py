class Pizza:
	def __init__(self, size: str, toppings=[]):
		self.size = size
		self.toppings = toppings
		self.price = 0
	
	def get_description(self):
		toppings = ""
		if len(self.toppings) > 0:
			toppings = f"that has{', '.join(self.toppings)}"
		return f"A {size} pizza"