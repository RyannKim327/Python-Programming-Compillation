# Activity 2
class Payment:
	def __init__(self, price):
		self.final_price = price + (price * 0.05)
		self.__final_price = price + (price * 0.05)
	
	def setDiscount(self, discount):
		self.__final_price = self.__final_price * (discount / 100)

	def getFinalPrice(self):
		return self.__final_price

pay = Payment(100)
print(pay.final_price)
print(pay.__inal_price)
print(pay.getFinalPrice())