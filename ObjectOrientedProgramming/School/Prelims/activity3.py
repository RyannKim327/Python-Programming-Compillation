from activity3_external import BankAccount

users = []

def checkBalance(new_user):
	print(f"Your current balance is ${new_user.checkBalance()}")

def deposit(new_user):
	balance = input("Enter amount you want to deposit: ")
	while not balance.isdigit():
		balance = input("Enter amount you want to deposit: ")
	new_user.setDeposit(balance)
	checkBalance(new_user)

def widraw(new_user):
	balance = input("Enter amount you want to deposit: ")
	while not balance.isdigit():
		balance = input("Enter amount you want to deposit: ")
	new_user.setWidraw(balance)
	checkBalance(new_user)

def pick(new_user):
	while True:
		a = ["1", "2", "3", "4"]
		choice = input("Menu:\n[1]Check Balance\n[2]Deposit\n[3]Widraw\n[4]Exit\nEnter your choice:")
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

	users.append(new_user)
		

def createAccount():
	name = input("Enter holder name: ")
	balance = input("Enter your balance (500 Minimum): ")
	while not balance.isdigit():
		balance = input("Enter your balance (500 Minimum): ")
	while int(balance) < 500:
		balance = input("Enter your balance (500 Minimum): ")

	new_user = BankAccount(name, int(balance))
	pick(new_user)

def start():
	while True:
		a = ["1", "2"]
		choice = input("Menu\n[1] Create account\n[2] Exit\nEnter your choice: ")
		while not choice in a:
			choice = input("Menu\n[1] Create account\n[2] Exit\nEnter your choice: ")
		if choice == "1":
			createAccount()
			cont = input("Would you like to continue? ").lower()
			if cont.startswith("n"):
				break
		else:
			print("Thank you")
			break

if __name__ == "__main__":
	start()