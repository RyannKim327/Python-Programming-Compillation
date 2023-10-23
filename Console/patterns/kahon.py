n  = int(input("Enter numbers of squares: "))
r = ""
x =  True
for i in range(n):
	for j in range(n):
		for k in range(n):
			if i == 0 or k == 0 or k == n-1 or i == n-1 or x:
				r += "*"
			else:
				r += " "
			if k 
	r += "\n"

print(r)