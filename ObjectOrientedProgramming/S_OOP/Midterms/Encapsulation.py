class Payment:
	def __init__(self, price):
		self.final_price = price + (price * 0.05)
		self._final_price = price + (price * 0.05)

pay = Payment(100)
print(pay.final_price)