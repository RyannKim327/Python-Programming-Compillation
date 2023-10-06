from activity3_external import BankAccount

while True:
	name = input("Enter account holder: ")
	val = input("Enter initial deposit: ")
	if val.isdigit():
		val = int(val)
	else:
		val = 0
	user = BankAccount(name, val)

	
	if "y" in input("Do you want to continue? ").lower():
		break