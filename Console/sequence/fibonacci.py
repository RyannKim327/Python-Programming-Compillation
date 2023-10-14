print("Fibonacci sequence")

a = [0, 1]

for i in range(len(a) -1, 10):
	b = a[i - 1]
	c = a[i]
	d = c + b
	a.append(d)

print(a)