import random
import os

def cls():
	if os.system("cls"):
		os.system("clear")

human = [
	"  ___",
	" |   |",
	" |   |",
	" |   |",
	" |   o",
	" |  /|\\",
	" |  / \\",
	"_|______"
]

trial = 0
words = [
	"android", "modern", "technology", "ruin", "nation",
	"mobile", "computer", "limitation", "innovation", "indation",
	"player", "program", "robotics", "mechanism", "machines"
]

reveal = []
cls()
while True:
	w = random.randint(0, len(words) - 1)
	word = words[w]
	while trial < len(human):
		show = ""
		for i in range(trial):
			print(human[i])
		for i in range(len(word)):
			b = True
			for j in range(len(reveal)):
				if word[i] == reveal[j]:
					show += reveal[j]
					b = False
			if b:
				show += "_"
		print(show)
		if show == word:
			print("You've guessed it. Congrats")
			show = ""
			break
		try:
			guess = input("Enter a letter in lowercase: ").lower()[0]
			if guess in word:
				if guess in reveal:
					trial += 1
				else:
					reveal.append(guess)
			else:
				trial += 1
			if trial < len(human):
				cls()
		except:
			trial += 1
			cls()
	if input("Play again? [Type yes]: ") != "yes":
		cls()
		break
	else:
		cls()
		trial = 0
		reveal = []
		w = random.randint(0, len(words) - 1)
		word = words[w]
	cls()