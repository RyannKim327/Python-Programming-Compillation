table = []

for i in range(1, 7):
	for j in range(1, 7):
		table.append(i * j)

n = input("Enter string: ")
o = ""
for i in range(n):
	m = chr(ord(n[i]) + table[i % 26])
	o += m

print(o)