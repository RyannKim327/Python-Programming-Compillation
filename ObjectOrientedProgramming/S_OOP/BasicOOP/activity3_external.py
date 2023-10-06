class BankAccount:
	def __init__(self, account_holder, initial_deposit=500):
		self.account_holder = account_holder
		self.initial_deposit = initial_deposit

		while self.initial_deposit < 500:
			value = input("Enter an initial deposit: ")
			if value.isdigit():
				self.setDeposit(value)

	def setDeposit(self, value=0):
		if value.isdigit():
			return int(value)
		else:
			return 0

	def setWidraw(self, amt=0):
		while 0 >= amt > 500:
			val = input("Enter atleast 500 pesos of widrawal")
			if val.isdigit():
				amt = int(val)
			else:
				amt = 0

	def checkBalance(self):
		return self.initial_deposit
