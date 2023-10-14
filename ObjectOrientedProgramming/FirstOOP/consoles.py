from extra import enter as input, typing as print

def welcome():
	com = [
		"About",
		"Contact",
		"Help"
	]
	commands = {
		"help": "Here are the lists of commands that you may use..."
	}
	x = input("Enter your command").toLower()
	
	commands[x]

print("Welcome to MPOP Reverse II, kindly typr help for thos list of commandments...")