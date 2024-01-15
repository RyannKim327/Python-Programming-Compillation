import random, os
def createBoard():
	board = []
	a = []
	for i in range(1, 101):
		if (i - 1) % 10 == 0 and (i - 1) != 0:
			board.append(a)
			a = []
		a.append(i)
	board.append(a)
	board.reverse()
	for i in range(len(board)):
		if i % 2 == 0:
			board[i].reverse()
	return board

def condition(score):
	penalty = ""
	match(score):
		case 1:
			score = 38
			penalty = "go up the ladder"
		case 4:
			score = 14
			penalty = "go up the ladder"
		case 8:
			score = 30
			penalty = "go up the ladder"
		case 21:
			score = 42
			penalty = "go up the ladder"
		case 28:
			score = 76
			penalty = "go up the ladder"
		case 32:
			score = 10
			penalty = "bitten by the snake"
		case 36:
			score = 6
			penalty = "bitten by the snake"
		case 48:
			score = 26
			penalty = "bitten by the snake"
		case 50:
			score = 67
			penalty = "go up the ladder"
		case 62:
			score = 18
			penalty = "bitten by the snake"
		case 71:
			score = 92
			penalty = "go up the ladder"
		case 80:
			score = 99
			penalty = "go up the ladder"
		case 88:
			score = 24
			penalty = "bitten by the snake"
		case 95:
			score = 56
			penalty = "bitten by the snake"
		case 97:
			score = 78
			penalty = "bitten by the snake"
	return [score, penalty]

player1 = 0
player2 = 0
x = 0
good = [1, 4 ,8, 21, 28, 50, 71, 80]
landgood = [38, 14, 30, 42, 76, 67, 92, 99]
bad = [32, 36, 48, 62, 88, 95, 97]
landbad = [10, 6, 26, 18, 24, 56, 78]
winner = ""
while True:
	board = createBoard()
	textboard = ""
	for i in range(len(board)):
		for j in range(len(board[i])):
			if board[i][j] in good:
				textboard += "("
			elif board[i][j] in bad:
				textboard += "{"
			elif board[i][j] in landgood or board[i][j] in landbad:
				textboard += "["
			else:
				textboard += "|"
			if board[i][j] == player1:
				textboard +=  "*"
			elif board[i][j] == player2:
				textboard +=  "-"
			else:
				textboard +=  " "
			if board[i][j] in good:
				textboard += ") "
			elif board[i][j] in bad:
				textboard += "} "
			elif board[i][j] in landgood or board[i][j] in landbad:
				textboard += "] "
			else:
				textboard += "| "
		textboard += "\n"
	print(textboard, end="\r")
	input("Enter to continue: ")
	dice = random.randint(1, 6)
	if x % 2 == 0:
		player1 += dice
	else:
		player2 += dice
	if player1 > 100:
		p = player1 - 100
		player1 = 100 - p
	if player2 > 100:
		p = player2 - 100
		player2 = 100 - p
	cond1 = condition(player1)
	cond2 = condition(player2)
	player1 = cond1[0]
	player2 = cond2[0]
	os.system("cls")
	if cond1[1] != "" or cond2[1] != "":
		print(f"Player {(x % 2) + 1} {cond1[1]}{cond2[1]}")
	print(f"Scoreboard:\nPlayer 1: {player1}\nPlayer 2: {player2}\n\nPlayer {(x % 2) + 1} moved [{dice}] squares")
	x += 1
	if player1 == 100:
		winner = "Player 1"
		break
	if player2 == 100:
		winner = "Player 2"
		break

print(f"The winner is {winner}")