n  = int(input("Enter numbers of squares: "))
r = ""

for i in range(n):
	for j in range(n):
		for k in range(n):
			r += "* "
	r += "\n"

print(r)