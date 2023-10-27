class Pizza:
	def __init__(self, size: str, toppings=[]):
		self.size = size
		self.toppings = toppings
		self.price = 0
	
	def get_description(self):
		toppings = ""
		if len(self.toppings) > 0:
			toppings = "that has{}"
		return f"A {size} pizza"