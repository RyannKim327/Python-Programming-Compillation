# Activity 5
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
	
	def getItem(self):
		return self.item_name

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
		self.item_name = item_name
		self.adds = addons
	
	def getItem(self):
		a =  f"{self.item_name}"
		if len(self.adds) > 0:
			a += f" with some {tuple(self.adds)}"
		return a

class Order:
	def __init__(self):
		self.__orders = []
	
	def addOrder(self, order):
		self.__orders.append(order)
	
	def getOrders(self):
		return self.__orders
	
	def calculateTotalPrice(self):
		return sum([i.getPrice() for i in self.__orders])

if __name__ == "__main__":
	order = Order()
	while True:
		a = input("Menu: \n[1] Food\n[2] Drinks\n[3] Food Premium\n[4] Close\nEnter your choice: ")
		b = True
		match(a):
			case "1":
				print("You've chosen a food item, we have here: ")
				a = [
					["Pansit", 50], ["Spaghetti", 50], ["Rice", 10], ["Chicken", 25], ["Burger", 35], ["Eggs", 10]
				]
				for i, j in enumerate(a):
					print(f"[{i + 1}]: {j[0]} - {j[1]}")
				c = input("Enter your choice: ")
				while not c.isdigit():
					c = input("Enter your choice: ")
				d = a[(int(c) - 1) % len(a)]
				_order = FoodItem(d[0], d[1])
			case "2":
				print("You've chosen a drink item, we have here: ")
				a = [
					["Coke", 13], ["Pepsi", 15], ["Royal", 15], ["Mt. Dew", 20], ["Gatorade", 35], ["Water", 10]
				]
				for i, j in enumerate(a):
					print(f"[{i + 1}]: {j[0]} - {j[1]}")
				c = input("Enter your choice: ")
				while not c.isdigit():
					c = input("Enter your choice: ")
				d = a[(int(c) - 1) % len(a)]
				_order = DrinkItem(d[0], d[1])
			case "3":
				print("You've chosen a food item 16 ultra mega pro max, we have here: ")
				a = [
					["Pansit Palabok", 150], ["Pansit Lucban", 150], ["Imported Rice made in China", 1000], ["Spicy Chicken with Rootbeer", 75], ["Burger with Fries", 50], ["Burger with Ham and Eggs", 45]
				]
				for i, j in enumerate(a):
					print(f"[{i + 1}]: {j[0]} - {j[1]}")
				c = input("Enter your choice: ")
				while not c.isdigit():
					c = input("Enter your choice: ")
				d = a[(int(c) - 1) % len(a)]
				addons = []
				addon = input("Enter additional toppings you want: ")
				while not addon == "": 
					addons.append(addon)
					addon = input("Enter additional toppings you want: ")
				_order = PremiumFoodItem(d[0], d[1], addons)
			case "4":
				break
			case _:
				b = False
				print("Invalid choice")

		if b:
			order.addOrder(_order)

for i in order.getOrders():
	print(f"You've purchase {i.getItem()} for ${i.getPrice()}")

print(f"With the total of ${order.calculateTotalPrice()}")