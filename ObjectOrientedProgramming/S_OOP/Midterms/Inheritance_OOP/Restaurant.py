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
		super().__init__(item_name, price, "Food")
	
	def cook(self):
		print(f"Please wait for your {self.item_name}, we still cooking it.")

class DrinkItem(MenuItem):
	def __init__(self, item_name, price):
		super().__init__(item_name, price, "Drink")

	def pour(self):
		print(f"Your {self.item_name} is on the way, please wait.")

class PremiumFoodItem(FoodItem):
	def __init__(self, item_name, price, addons):
		super().__init__(item_name, price)
		price = self.getPrice() + (len(addons) * 2)
		self.setPrice(price)

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
