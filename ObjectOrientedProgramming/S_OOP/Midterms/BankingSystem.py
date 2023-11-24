class BackAccount:
	def __init__(self, accountHolder: str, balance: int = 0):
		self._accountHolder = accountHolder
		self._balance = balance
	
	def getBalance(self):
		return self._balance
	
	def deposit(self, amount: int):
		if 0 < amount:
			self._balance += amount

	def widraw(self, amount: int = 0):
		if 0 < amount <= self._balance:
			self._balance -= amount:

# Start
if __name__ == "__main__":

	# Create 2 bank accounts
	acct1 = BackAccount("John Doe", 1000)
	acct2 = BackAccount("John Smith")

	print(f"The {acct1._accountHolder}'s balance is {acct1.getBalance()}")
	print(f"The {acct2._accountHolder}'s balance is {acct2.getBalance()}")

	acct1.deposit(500)
	acct2.deposit(200)
	
	print(f"The {acct1._accountHolder}'s balance is {acct1.getBalance()}")
	print(f"The {acct2._accountHolder}'s balance is {acct2.getBalance()}")