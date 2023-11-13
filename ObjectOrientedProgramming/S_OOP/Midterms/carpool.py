class Vehicle:
	def __init__(self, name: str, capacity = 3, fare: float):
		self.name = name
		self.capacity = capacity
		self.driver = None
		self.fare = fare
		self.customers = []

class Driver:
	def __init__(self):
		pass
