c = [
	["A", "B", "C", "D", "E", "F", "G", "H"],
	["I", "J", "K", "L", "M", "N", "O" "P"],
	["Q", "R", "S", "T", "U", "V", "W", "X"],
	["Y", "Z", "a", "b", "c", "d", "e", "f"],
	["g", "h", "i", "j", "k","l", "m", "n"],
	["o", "p","q", "r", "s", "t", "u", "v"],
	["w", "x", "y", "z", "0", "1", "2", "3"],
	["4", "5", "6", "7", "8", "9", "Ñ", "ñ"]
]

def encrypt(txt):
	b = ""
	for i in range(len(a)):
		for v in range(len(c)):
			for h in range(len(c[v])):
				if c[v][h] == a[i]:
					b += str(h + 1) + str(v + 1) + " "
					break
	return b

def decrypt(txt):
	b = txt.split(" ")
	d = ""
	for i in range(len(b)):
		e = int(b[i][0]) - 1
		f = int(b[i][1]) - 1
		d += c[f][e]
	return d

a = input("Enter text (Encrypt): ")
print(encrypt(a))
b = input("Enter text (Decrypt): ")
print(decrypt(b))

# 33 34 75 26 65 74
# 33 34 74 65 75 26
# 33 34 74 65 75 26