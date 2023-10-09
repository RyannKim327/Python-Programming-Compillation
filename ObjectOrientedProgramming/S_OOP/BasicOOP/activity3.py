from activity3_external import BankAccount

users = []

def pick(new_user):
	a = ["1", "2", "3", "4"]
	choice = input("Menu:\n[1]Check Balance\n[2]Deposit\n[3]Widraw\nEnter your choice:")
	while not choice in a:
		choice = input("Enter your choice: ")
	
	match(choice):
		case "1":
			

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
	pass

def start():
	while True:
		a = ["1", "2"]
		choice = input("Menu\n[1] Create account\n[2] Exit")
		while not choice in a:
			choice = input("Menu\n[1] Create account\n[2] Exit")
		if a == "1":
			createAccount()
		else:
			print("Thank you")

if __name__ == "__main__":
	start()