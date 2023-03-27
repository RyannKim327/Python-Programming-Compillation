def enc(pos):
	characters = ['i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']
	res = ""
	for i in range(len(pos)):
		if pos[i] == "1":
			res += str(characters[i])
	return res

def binary(char):
	res = ""
	n = ord(char)
	m = 1
	while m < n or m < 129:
		m += m
	while n > 0:
		res += str(n // m)
		n %= m
		m //=2
	return res


text = input("Enter a word: ")
result = ""

for i in range(len(text)):
	txt = binary(text[i])
	r = enc(txt)
	result += r + " "

print(result)