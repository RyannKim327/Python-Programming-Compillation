import random
import os

if os.system("cls"):
	os.system("clear")

x = [
	' ', ' ', ' ',
	' ', ' ', ' ',
	' ', ' ', ' '
]

process = True

while ' ' in x and process:
	print(f"{x[0]} {x[1]} {x[2]}\n{x[3]} {x[4]} {x[5]}\n{x[6]} {x[7]} {x[8]}")

	user = int(input("Enter a position: "))
	com = random.randint(0, 8)
	while x[user] != " ":
		user = int(input("Enter a position: "))
	x[user] = "o"
	while x[com] != " ":
		com = random.randint(0, 8)
	x[com] = "x"

	win = [
		[0, 1, 2],
		[3, 4, 5],
		[6, 7, 8],
		[0, 5, 8],
		[6, 5, 2],
		[0, 3, 6],
		[1, 4, 7],
		[2, 5, 8]
	]

	for w in range(len(win)):
		_u = 0
		_e = 0
		for u in range(len(win[w])):
			if x[win[w][u]] == 'o':
				_u += 1
			elif x[win[w][u]] == 'x':
				_e += 1
	
		if _u == 3:
			print("User wins")
			process = False
			break
		elif _e == 3:
			print("Enemy wins")
			process = False
			break
		_u = 0
		_e = 0
	if os.system("cls"):
		os.system("clear")
	if not ' ' in x:
		process = False


print(f"{x[0]} {x[1]} {x[2]}\n{x[3]} {x[4]} {x[5]}\n{x[6]} {x[7]} {x[8]}")