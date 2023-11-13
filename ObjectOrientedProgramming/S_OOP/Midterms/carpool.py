class Vehicle:
	def __init__(self, name: str, capacity: int, fare: float):
		self.name = name
		self.capacity = capacity
		self.driver = None
		self.fare = fare
		self.customers = []

	def getCapacity(self):
		return self.capacity
	

class Driver:
	def __init__(self, name, license):
		pass
