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
	
	def __str__(self):
		a = f"New account created for {self._accountHolder}"
		if self._
		return a
	
class TranscationHistory:
	def __init__(self):
		self.__transactions = []
	
	def addTransaction(self, transtaction):
		if transtaction:
			self.__transactions.append(transtaction)
	
	def getAllTransactions(self):
		return self.__transactions

# Start
if __name__ == "__main__":

	transactions = TranscationHistory()

	# Create 2 bank accounts
	acct1 = BackAccount("John Doe", 1000)
	acct2 = BackAccount("John Smith")

	transactions.addTransaction(acct1)
	transactions.addTransaction(acct2)

	transactions.addTransaction(acct1.deposit(500))
	transactions.addTransaction(acct2.deposit(200))

	for i in transactions.getAllTransactions():
		print(i)