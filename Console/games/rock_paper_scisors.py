import random
import os

x = [
	"rock",
	"scisor",
	"paper"
]

c = {
	"r": 0,
	"s": 1,
	"p": 2
}

while True:
	if os.system("cls"):
		os.system("clear")
	_usr = input("[R]ock\n[P]aper\n[S]cisors\nEnter the letter of your choice: ")
	if c.get(_usr) == None:
		print("Invalid Choice:")
	else:
		usr = c.get(_usr)
		bot = random.randint(0, 2)
		print(f"You: {x[usr]}\nBot: {x[bot]}")
		if usr == 0:
			if bot == 0:
				print("It's a tie")
			elif bot == 1:
				print("You win againts the bot")
			else:
				print("Bot wins")
		
		elif usr == 1:
			if bot == 0:
				print("Bot wins")
			elif bot == 1:
				print("It's a tie")
			else:
				print("You win againts the bot")
		
		elif usr == 2:
			if bot == 0:
				print("You win againts the bot")
			elif bot == 1:
				print("Bot wins")
			else:
				print("It's a tie")

	if input("Enter close to terminate: ") == "close":
		break