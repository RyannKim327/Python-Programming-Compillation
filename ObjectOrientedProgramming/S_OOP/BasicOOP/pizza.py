

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
	
pizzas = []
toppings = []

while True:
	top = input("Enter topping: ")
	if top == "":
		break
	toppings.append(top)

pizza1 = Pizza("large", toppings)
pizzas.append(pizza1)
order = Order()

for piz in pizzas:
	order.add_pizza(piz)

print(order.calculate_total())
print(order.get_order_summary())