from activity3_external import BankAccount

users = []

def checkBalance(new_user):
	print(f"Your current balance is {new_user.checkBalance}")

def deposit(new_user):
	new_user.setDeposit()
	pass

def widraw(new_user):
	pass

def pick(new_user):
	while True:
		a = ["1", "2", "3", "4"]
		choice = input("Menu:\n[1]Check Balance\n[2]Deposit\n[3]Widraw\nEnter your choice:")
		while not choice in a:
			choice = input("Enter your choice: ")
		
		match(choice):
			case "1":
				checkBalance(new_user)
			case "2":
				deposit(new_user)
			case "3":
				widraw(new_user)
			case _:
				break
		

def createAccount():
	global users
	name = input("Enter holder name: ")
	balance = input("Enter your balance (500 Minimum): ")
	while not balance.isdigit():
		balance = input("Enter your balance (500 Minimum): ")
	while int(balance) < 500:
		balance = input("Enter your balance (500 Minimum): ")

	new_user = BankAccount(name, int(balance))
	users.append(new_user)
	pick(new_user)

def start():
	while True:
		a = ["1", "2"]
		choice = input("Menu\n[1] Create account\n[2] Exit")
		while not choice in a:
			choice = input("Menu\n[1] Create account\n[2] Exit")
		if a == "1":
			createAccount()
			cont = input("Would you like to continue? ").lower()
			if cont.startswith("y"):
				break
		else:
			print("Thank you")

if __name__ == "__main__":
	start()