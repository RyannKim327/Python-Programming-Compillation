class BackAccount:
	def __init__(self, accountHolder: str, balance: int = 0):
		self.__accountHolder = accountHolder
		self.__balance = balance
	
	def getBalance(self):
		return self.__balance
	
	def deposit(self, amount: int):
		self.__balance += amount

# Start
if __name__ == "__main__":

	# Create 2 bank accounts
	acct1 = BackAccount("John Doe", 1000)
	acct2 = BackAccount("John Smith")