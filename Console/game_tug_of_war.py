import random
import os
import time

min = 1
max = 10

l_min = 0
l_center = 50
l_max = 100

if os.system("cls"):
	os.system("clear")

while l_center > l_min and l_center < l_max:
	p = "You: "
	q = "     "
	for i in range(l_min, l_max):
		if i == l_center:
			q += "|>"
			p += "| "
		else:
			p += "-"
			q += " "
	p += " :Enemy"
	print(q)
	print(p)
	# input("")
	time.sleep(0.15)
	you = random.randint(min, max)
	enemy = random.randint(min, max)
	l_center -= you
	l_center += enemy
	# print(f"You: {you}\nEnemy: {enemy}")
	# input("")
	if os.system("cls"):
		os.system("clear")

if l_center >= l_max:
	print("Enemy wins the game")
else:
	print("You win")