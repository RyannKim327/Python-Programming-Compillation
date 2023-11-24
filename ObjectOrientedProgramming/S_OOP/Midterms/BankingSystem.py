class BackAccount:
	def __init__(self, accountHolder: str, balance: int):
		self.__accountHolder = accountHolder
		self.balance = balance
	
	def getBalance(self):
		return