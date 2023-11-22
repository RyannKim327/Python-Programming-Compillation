class Payment:
	def __init__(self, price):
		self.final_price = price + (price * 0.05)
		self.__final_price = price + (price * 0.05)
	
	def getFinalPrice(self):
		return self.__final_price

pay = Payment(100)
print(pay.final_price)
print(pay.getFinalPrice())