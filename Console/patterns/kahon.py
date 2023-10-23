n  = int(input("Enter numbers of squares: "))
r = ""

for i in range(n):
	for j in range(n):
		# if i % 2 == 0:
		# 	r += "  "
		# else:
			r += "* "
	r += "\n"

print(r)