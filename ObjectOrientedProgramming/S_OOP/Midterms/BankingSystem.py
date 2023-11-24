class BackAccount:
	def __init__(self, accountHolder: str, balance: int = 0):
		self._accountHolder = accountHolder
		self._balance = balance
	
	def getBalance(self):
		return self._balance
	
	def deposit(self, amount: int):
		if 0 < amount:
			self._balance += amount
			return f"{self._accountHolder} deposited ${amount}"
		else:
			print("Invalid input")

	def widraw(self, amount: int = 0):
		if 0 < amount <= self._balance:
			self._balance -= amount
			return f"{self._accountHolder} widrew ${amount}"
		else:
			print("Inssuficient balance")

class TranscationHistory:
	def __init__(self):
		self._transactions = []
	
	def addTransaction(self, transtaction):
		if transtaction:
			self._transactions.append(transtaction)
	
	def getAllTransactions(self):
		return self._transactions

# Start
if __name__ == "__main__":

	# Create 2 bank accounts
	acct1 = BackAccount("John Doe", 1000)
	acct2 = BackAccount("John Smith")

	print(f"The {acct1._accountHolder}'s balance is {acct1.getBalance()}")
	print(f"The {acct2._accountHolder}'s balance is {acct2.getBalance()}")

	tra(acct1.deposit(500))
	tra(acct2.deposit(200))
	
	print(f"The {acct1._accountHolder}'s balance is {acct1.getBalance()}")
	print(f"The {acct2._accountHolder}'s balance is {acct2.getBalance()}")