h, w = 10, 5
r = ""

for i in range(1, h + 1):
	if i < (h // 2):
		for j in range(h - i):
			r += " "
		for j in range(1, i + 1):
			r += " " + str(i)
	else:
		for j in range(i):
			r += " "
		for j in range(i - w, w):
			r += " " + str(i)
	r += "\n"

print(r)