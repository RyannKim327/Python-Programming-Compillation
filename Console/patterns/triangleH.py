duplication = int(input("Enter numbers of triangles: "))
height = 5
width = 5
result = ""

for h in range(1, height + 1):
	for d in range(1, duplication + 1):
		for s in range(height - h):
			result += " "
		for a in range(h):
			result += " *"
		for s in range(height - h):
			result += " "
		result += "  "
	result += "\n"

print(result)