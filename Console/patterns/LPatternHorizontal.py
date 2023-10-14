height = 5
width = 4
dumplication = int(input("Enter number of duplication: "))

result = ""

for h in range(1, height + 1):
	for d in range(1, dumplication + 1):
		for w in range(1, width + 1):
			if h <= 3:
				if w < 3:
					result += "* "
				else:
					result += "  "
			else:
				result += "* "
		result += "  "
	result += "\n"

print(result)