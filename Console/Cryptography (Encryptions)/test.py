table = []

for i in range(1, 7):
	for j in range(1, 7):
		table.append(i * j)

n = input("Enter string: ")

for i in range(n):
	m = ord(n[i]) + table[i % 26]