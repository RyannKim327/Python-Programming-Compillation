class BankAccount:
	def __init__(self, account_holder, initial_deposit=500):
		self.account_holder = account_holder
		self.initial_deposit = initial_deposit

		while self.initial_deposit < 500:
			value = input("Enter an initial deposit: ")
			self.setDeposit(value)

	def setDeposit(self, value="0"):
		if value.isdigit():
			self.initial_deposit += int(value)

	def setWidraw(self, val="0"):
		if val.isdigit():
			while 0 >= val > 500:
				val = input("Enter atleast 500 pesos of widrawal")
				self.initial_deposit -= int(val)
		else:
			val = 0

	def checkBalance(self):
		return self.initial_deposit
