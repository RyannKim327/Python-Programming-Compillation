import os
import random
import time

def mixWord(word):
	m = ""
	w = []
	i = 0
	while i < len(word):
		x = random.randint(0, len(word) - 1)
		if x in w:
			i -= 1
		else:
			w.append(x)
		i += 1
	for i in w:
		m += word[i].upper()
	return m

def shuffles(list):
	lists = []
	i = 0
	while i < len(list):
		x = random.randint(0, len(list) - 1)
		if x in lists:
			i -= 1
		else:
			lists.append(x)
		i += 1
	return lists

def typing(txt, time = 3):
	speed = 10000 * time
	length = len(txt)
	i = 0
	while i < speed * length:
		if i % speed == 0:
			print(txt[i // speed], end="", flush=True)
		i += 1
	print()

words = [
	"virtue",
	"happiness",
	"voluntary", 
	"character",
	"Aristotle",
	"Knowledge",
	"Judgement",
	"Wisdom",
	"Partnership",
	"Friendship",
	"Ethical",
	"Nicomachean",
	"Modernization"
]

cooldown = 5
shuffle = 5

lists = shuffles(words)

os.system("title Shuffled Letters")
os.system("cls")
input("")
os.system("cls")
typing("Welcome to our simple shuffled letter game. In this game, you'll need to guess the word which all related to this topic. The letter were shuffled everyn wrong answers or atleast 5 seconds delay. And each word can reshuffled 5 times. Now let's start the game", 1)
input("")
os.system("cls")

for i in range(len(lists)):
	while shuffle >= 0:
		rand = lists[i]
		word = mixWord(words[rand])
		os.system("cls")
		if shuffle > 0:
			print("Here's the shuffled letters: ")
			typing(word)
		else:
			typing(f"The word is\n{words[rand].upper()}")
		if len(input()) > 0:
			shuffle = 0
		else:
			shuffle -= 1
	shuffle = 5

os.system("cls")

typing(f"Thank you for your cooperation, and now, we will going to proceed to our discussion...", 5)
input("")