from activity3_external import BankAccount

users = []

def createAccount():
	name = 
	a = ["1", "2", "3", "4"]
	choice = input("Menu:\n[1]Check Balance\n[2]Deposit\n[3]Widraw\nEnter your choice:")

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