class Pizza:
	def __init__(self, size: str, toppings=[]):
		self.size = size.lower()
		self.toppings = toppings
		self.price = 0
	
	def get_description(self):
		toppings = ""
		if len(self.toppings) > 0:
			toppings = f"that has {', '.join(self.toppings)}"
		return f"A {self.size} pizza {toppings}"
	
	def get_price(self):
		sizes = {
			"s": 10,
			"m": 12,
			"l": 15 
		}
		self.price = sizes[self.size[0]] + (len(self.toppings) * 2)

		return self.price

class Order:
	def __init__(self):
		self.pizzas = []
	
	def add_pizza(self, pizza: Pizza):
		self.pizzas.append(pizza)
	
	def calculate_total(self):
		total = 0
		for i in self.pizzas:
			total += i.get_price()
		return total
	
	def get_order_summary(self):
		desciptions = [i.get_description() for i in self.pizzas]
		return f"You ordered {', '.join(desciptions)}"
	
def addPizza():
	toppings = []
	sizes = [
		"small",
		"medium",
		"large"
	]
	a = ["1", "2", "3"]
	for i in range(len(sizes)):
		print(f"[{i + 1}]: {sizes[i]}")
	size = input("Enter pizza size: ")
	while not size in a:
		size = input("Enter pizza size: ")
	size = sizes[int(size) - 1]

	top = input("Enter toppings: ")
	while top != "":
		toppings.append(top)
		top = input("Enter toppings: ")
	
	return Pizza(size, toppings)

def getOrder():
	order = Order()
	for piz in pizzas:
		order.add_pizza(piz)
	print(f"{}")
	

if __name__ == "__main__":
	pizzas = []
	menu = [
		"Add Pizza",
		"Exit"
	]
	menun = ["1", "2"]
	cont = True
	while cont:
		print("Welcome to PizzaPY")
		for i in range(len(menu)):
			print(f"[{i + 1}]: {menu[i]}")
		choice = input("Please enter your choice: ")
		while not choice in menun:
			choice = input("You've entered invalid choice: ")
		choice = menu[int(choice) - 1]

		match choice:
			case "Add Pizza":
				pizzas.append(addPizza())
				menu = [
					"Add Pizza",
					"Get Order",
					"Exit"
				]
				menun = ["1", "2", "3"]
			case "Get Order":
				getOrder()
			case "Exit":
				print("Thank you for choosing us.")
				cont = False