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

class DrinkItem(MenuItem):
	def __init__(self, item_name, price):
		super().__init__(item_name, price, "This is Drink Item")

class Order:
	def __init__(self):
		self.__orders = []
	
	def addOrder(self, order):
		self.__