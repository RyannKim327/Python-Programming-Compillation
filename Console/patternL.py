h = 5
w = 4

r = ""

for y in range(1, h + 1):
	for x in range(1, w + 1):
		if y <= 3:
			if x < 3:
				r += "* "
			else:
				r += "  "
		else:
			r += "* "
	r += "\n"

print(r)