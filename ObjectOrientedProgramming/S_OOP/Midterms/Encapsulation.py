class Payment:
	def __init__(self, price):
		self.final_price = price + (price * 0.05)

pay = Payment()
