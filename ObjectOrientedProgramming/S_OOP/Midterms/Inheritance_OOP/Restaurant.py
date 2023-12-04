class MenuItem:
	def __init__(self, item_name, price, description):
		self.item_name = item_name
		self.__price = price
		self.description = description
		
	def getDetails(self):
		return self.description

	def setPrice(self, price):
		self.__price = price
	
	def getPrice(self):
		return self.__price

class FoodItem(MenuItem):
	def __init__(self, item_name, price):
		super().__init__(item_name, price, "This is Food Item")
	
	def cook(self):
		print("Cooking in process")

class DrinkItem(MenuItem):
	def __init__(self, item_name, price):
		super().__init__(item_name, price, "This is Drink Item")

	def pour(self):
		print("Pouring...")

class PremiumFoodItem(FoodItem):
	def __init__(self, item_name, price):
		super().__init__(item_name, price)
	
	def makeItToast(self, isToasted=False):
		if isToasted:
			price = self.getPrice() + 5
			self.setPrice(price)
	
	def isPr

class Order:
	def __init__(self):
		self.__orders = []
	
	def addOrder(self, order):
		self.__orders.append(order)
	
	def getOrders(self):
		return self.__orders
	
	def calculateTotalPrice(self):
		total = 0
		for i in self.__orders:
			total += i.getPrice()
		
		return total


a = PremiumFoodItem("Pork", 100)
print(a.getPrice())
a.makeItToast(True)
print(a.getPrice())
