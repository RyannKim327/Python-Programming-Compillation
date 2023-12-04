class MenuItem:
	def __init__(self, item_name, price, description):
		self.item_name = item_name
		self.price = price
		self.description = description
		
	def getDescription(self):
		return self.description

class FoodItem(MenuItem):
	def __init__(self, item_name, price):
		super().__init__(item_name, price, "This is Food Item")

class DrinkItem(MenuItem):
	def __init__(self, item_name, price):
		super().__init__(item_name, price, "This is Drink Item")

a = FoodItem("Kasuy", 100)
print(a.getDescription())
