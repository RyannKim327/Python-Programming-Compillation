n  = int(input("Enter numbers of squares: "))
r = ""

for i in range(n):
	for j in range(n):
		for k in range(n):
			r += "* "
		for k in range(n-2):
			if i == 0 or i == n-1 or k == 0 or k == n-1:
				r += "* "
			else:
				r += "  "
	r += "\n"

print(r)