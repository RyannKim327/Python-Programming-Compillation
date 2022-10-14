name = input("Enter a name: ")
a = []

while name != "":
	a.append(name)
	name = input("Enter another name: ")

for i in range(len(a)):
	for j in range(i):
		x = 0
		b = ord(a[i][x])
		c = ord(a[j][x])
		if b < c:
			d = a[i]
			a[i] = a[j]
			a[j] = d
		while b == c:
			x += 1
			b = ord(a[i][x])
			c = ord(a[j][x])
			if b < c:
				d = a[i]
				a[i] = a[j]
				a[j] = d

print(a)