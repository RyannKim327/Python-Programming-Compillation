table = []

for i in range(1, 7):
	for j in range(1, 7):
		table.append((i * j) - i)

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

n = input("Enter string: ")
print(encrypt(n))
n = input("Enter string: ")
print(decrypt(n))