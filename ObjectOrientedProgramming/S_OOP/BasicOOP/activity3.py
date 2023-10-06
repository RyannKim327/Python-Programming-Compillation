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
	_ = ["1", "2", "3", "4"]
	a = input("""
Select your activity:
[1] Check Balance
[2] Widraw
[3] Deposit
[4] Exit
""")
	while not a in _:
		a = input("Enter your choice: ")
	
	while a != "4":
		match(a):
			case "1":
				print(f"Your current balance is: {user.checkBalance()}")
			case "2":
				b = input("Enter your widrawal: ")
				while not b.isdigit():
					b = input("Enter your widrawal: ")
				
				user.setWidraw(int(b))
			case "3":
				b = input("Enter your deposit: ")
				user.setDeposit(b)
		
		a = input("""
 your activity:
1] Check Balance
2] Widraw
3] Deposit
4] Exit
""")
		while not a in _:
			a = input("Enter your choice: ")

	users.append(user)
	if "n" in input("Do you want to continue? ").lower():
		break

print(users[0].checkBalance())
