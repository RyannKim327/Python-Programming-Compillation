class Vehicle:
	def __init__(self, name: str, capacity: int, fare: float):
		self.name = name
		self.capacity = capacity
		self.driver = None
		self.fare = fare
		self.customers = []

	def getCapacity(self):
		return self.capacity

	def getDescrition(self):
		return f"A {self.name} that has {}"
	

class Driver:
	def __init__(self, name, license):
		self.name = name
		self.license = license
	
class Customer:
	def __init__(self, name, phone_number):
		self.name = name
		self.num = phone_number


