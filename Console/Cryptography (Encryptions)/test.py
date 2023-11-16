table = []

for i in range():
	for j in range(1, 7):
		table.append((i * j))

def encrypt(n):
	o = ""
	for i in range(len(n)):
		m = chr(ord(n[i]) + table[i % 26])
		o += m
	return o

def decrypt(n):
	o =  ""
	for i in range(len(n)):
		m = chr(ord(n[i]) - table[i % 26])
		o += m
	return o

print(table)

n = input("Enter string: ")
print(encrypt(n))
n = input("Enter string: ")
print(decrypt(n))