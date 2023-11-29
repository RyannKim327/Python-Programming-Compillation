class BackAccount:
	def __init__(self, accountHolder: str, balance: int = 0):
		self._accountHolder = accountHolder
		self._balance = balance
		self._initial_deposit = balance
	
	def getBalance(self):
		return self._balance
	
	def deposit(self, amount: int):
		if 0 < amount:
			self._balance += amount
			return f"{self._accountHolder} deposited ${amount}"
		else:
			return f"The amount must be a positive value and not equal to zero [{self._accountHolder}]"

	def widraw(self, amount: int = 0):
		if 0 < amount <= self._balance:
			self._balance -= amount
			return f"{self._accountHolder} widrew ${amount}"
		else:
			return f"{self._accountHolder} can't widraw due to its insufficient balance"
	
	def __str__(self):
		a = f"New account created for {self._accountHolder}"
		if self._initial_deposit > 0:
			a += f" with initial deposite of {self._initial_deposit}"
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
	transactions.addTransaction(acct2.deposit(0))

	transactions.addTransaction(acct1.widraw(500))
	transactions.addTransaction(acct2.widraw(500))

	for i in transactions.getAllTransactions():
		print(i)