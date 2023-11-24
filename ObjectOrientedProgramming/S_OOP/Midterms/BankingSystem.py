class BackAccount:
	def __init__(self, accountHolder: str, balance: int):
		self.__accountHolder = accountHolder
		self.__balance = balance
	
	def getBalance(self):
		return self.__balance
	
	def deposit(self, amount: int):
		self.__balance += amount

