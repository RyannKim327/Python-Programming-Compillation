class Payment:
	def __init__(self, price):
		self.final_price = price + (price * 0.05)
		self.__final_price = price + (price * 0.05)

pay = Payment(100)
print(pay.__final_price)
print(pay.__final_price)
