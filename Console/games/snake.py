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

players = []
playerscore = []
player = input("Enter player: ")
while player != "" or len(players) < 2:
	if(player != ""):
		players.append(player)
		playerscore.append(0)
	player = input("Enter player: ")

good = [1, 4 ,8, 21, 28, 50, 71, 80]
landgood = [38, 14, 30, 42, 76, 67, 92, 99]
bad = [32, 36, 48, 62, 88, 95, 97]
landbad = [10, 6, 26, 18, 24, 56, 78]
winner = ""
gaming = True
while gaming:
	for p in range(len(players)):
		player = players[p]
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
				for p2 in range(len(players)):
					if board[i][j] == playerscore[p2]:
						textboard +=  players[p2][0]
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

		playerscore[p] += dice
		
		if playerscore[p] > 100:
			p3 = playerscore[p] - 100
			playerscore[p] = 100 - p3
		cond1 = condition(playerscore[p])
		playerscore[p] = cond1[0]
		os.system("cls")
		if cond1[1] != "":
			print(f"Player {player} {cond1[1]}")
		print("Scoreboard: ")
		for p4 in range(len(players)):
			print(f"{players[p4]}: {playerscore[p4]}")
		print(f"\nPlayer {player} moved [{dice}] squares")
		
		if playerscore[p] == 100:
			winner = player
			gaming = False
			break

print(f"The winner is {winner}")