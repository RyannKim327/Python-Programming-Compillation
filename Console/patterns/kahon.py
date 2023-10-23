n  = int(input("Enter numbers of squares: "))
r = ""

for i in range(n):
	for j in range(n):
		for k in range(n):
			if i == 0 or k == 0 or k == n-1 or i == n-1:
				r += "*"
			else:
				r += " "
	r += "\n"

print(r)