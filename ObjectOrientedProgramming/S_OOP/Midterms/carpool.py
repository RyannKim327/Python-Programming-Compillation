class Vehicle:
	def __init__(self, name: str, capacity: int, fare: float):
		self.name = name
		self.capacity = capacity
		self.driver = None
		self.fare = fare
		self.customers = []

	def getCapacity(self):
		return self.capacity

	def assignDriver(self, driver):
		self.driver = driver
	
	def getCustomers(self):
		return len(self.customers)

	def addCustomer(self, customer):
		if len(self.customers) < self.capacity:
			self.customers.append(customer)
		else:
			print("You exceed the limit, tama na kuya.")

	def getDescrition(self):
		return f"A {self.name} that has {len(self.customers)} customers inside, with a driver named {driver.getName()} with license number {driver.getLicense()} and with {self.fare} fare per kilometers."
	
class Driver:
	def __init__(self, name, license):
		self.name = name
		self.license = license
	
	def getName(self):
		return self.name

	def getLicense(self):
		return self.license
	
class Customer:
	def __init__(self, name, phone_number):
		self.name = name
		self.num = phone_number

vehicles = []

while True:
	vehicleName = input("Enter vehicle name: ")
	if vehicleName == "":
		break
	vehicleCapacity = int(input("Enter vehicle capacity: "))
	vehicleFare = float(input("Enter fair per kilometer: "))

	vehicle = Vehicle(vehicleName, vehicleCapacity, vehicleFare)

	driverName = input("Enter driver's name: ")
	driverLicense = input("Enter driver's license number: ")
	driver = Driver(driverName, driverLicense)

	vehicle.assignDriver(driver)

	onRide = True
	while onRide and vehicle.getCapacity() > vehicle.getCustomers():
		customerName = input("Enter customer name: ")
		if customerName == "":
			onRide = False
			break
		customerNumber = input("Enter phone number: ")
		customer = Customer(customerName, customerNumber)
		vehicle.addCustomer(customer)

	if onRide:
		print("You've exceed to the capacity of the vehicle")

	print(f"{vehicle.getDescrition()}")
	vehicles.append(vehicle)