class BankAccount:
	def __init__(self, account_holder, initial_deposit=500):
		self.account_holder = account_holder
		self.initial_deposit = initial_deposit

		while self.initial_deposit < 500:
			value = 
			self.setDeposit(value)

	def setDeposit(self, value=0):
		if value.isdigit():
			return value
		else:
			return 0
