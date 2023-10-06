from activity3_external import BankAccount

users = []

while True:
	name = input("Enter account holder: ")
	val = input("Enter initial deposit: ")
	if val.isdigit():
		val = int(val)
	else:
		val = 0
	user = BankAccount(name, val)
	_ = ["1", "2", "3"]
	a = input("""
		Select your activity:
	   [1] Check Balance
	   [2] Widraw
	   [3] Deposit
		   [4]
	""")
	while 
	users.append(user)
	if "n" in input("Do you want to continue? ").lower():
		break

print(users[0].checkBalance())
