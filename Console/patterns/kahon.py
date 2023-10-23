n  = int(input("Enter numbers of squares: "))
r = ""

for i in range(n):
	for j in range(n):
		if i == 0 or i == n-1 or j == 0 or j == n-1:
			r += "* "
		else:
		for k in range(n):
			r += "* "
		for k in range(n-2):
			r += "  "
	r += "\n"

print(r)