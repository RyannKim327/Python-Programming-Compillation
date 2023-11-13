class Vehicle:
	def __init__(self, name: str, capacity: int, fare: float):
		self.name = name
		self.capacity = capacity
		self.driver = None
		self.fare = fare
		self.customers = []

	def getCapacity(self):
		return self.capacity

	def assignDriver(self, driver: Driver):
		self.driver = driver

	def getDescrition(self):
		return f"A {self.name} that has {len(self.customers)} customers inside, with a driver named {driver.getName()} with {self.fare}"
	

class Driver:
	def __init__(self, name, license):
		self.name = name
		self.license = license
	
	def getName(self):
		return self.name
	
class Customer:
	def __init__(self, name, phone_number):
		self.name = name
		self.num = phone_number


