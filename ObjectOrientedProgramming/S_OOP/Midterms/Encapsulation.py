class Payment:
	def __init__(self, price):
		self.final_price = price + (price * 0.05)
		self.__final_price = price + (price * 0.05)
	
	def setDiscount(self, discount):
		self.__

	def getFinalPrice(self):
		return self.__final_price

pay = Payment(100)
print(pay.final_price)
print(pay.__inal_price)
print(pay.getFinalPrice())