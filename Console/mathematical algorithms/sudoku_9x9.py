line_1 = []
line_2 = []
line_3 = []

result = ""

# 1 2 3 | 4 5 6 | 7 8 9 #
# 4 5 6 | 7 8 9 | 1 2 3 #
# 7 8 9 | 1 2 3 | 4 5 6 #
# --------------------- #
# 2 3 4 | 5 6 7 | 8 9 1 #
# 5 6 7 | 8 9 1 | 2 3 4 #
# 8 9 1 | 2 3 4 | 5 6 7 #
# --------------------- #
# 3 4 5 | 6 7 8 | 9 1 2 #
# 6 7 8 | 9 1 2 | 3 4 5 #
# 9 1 2 | 3 4 5 | 6 7 8 #


for i in range(3):
	line1 = []
	line2 = []
	line3 = []
	for j in range((i + 1), 10 + i):
		n = j % 10
		if j >= 10:
			n += 1
		line1.append(n)
	for j in range((i + 4), (10 + i) + 3):
		n = j % 10
		if j >= 10:
			n += 1
		line2.append(n)
	for j in range((i + 7), (10 + i) + 6):
		n = j % 10
		if j >= 10:
			n += 1
		line3.append(n)
	line_1.append(line1)
	line_2.append(line2)
	line_3.append(line3)


for i in range(len(line_1)):
	for j in range(len(line_1[i])):
		if(j % 3) == 0 and j != 0:
			result += "| "
		result += str(line_1[i][j]) + " "
	result += "\n"
	for j in range(len(line_2[i])):
		if(j % 3) == 0 and j != 0:
			result += "| "
		result += str(line_2[i][j]) + " "
	result += "\n"
	for j in range(len(line_3[i])):
		if(j % 3) == 0 and j != 0:
			result += "| "
		result += str(line_3[i][j]) + " "
	result += "\n---------------------- \n"

print(result)