class RySes:
	def __init__(self):
		self.characters = "fghiedcba"
		self.bin = [128, 64, 32, 16, 8, 4, 2, 1]

	def encrypt(self, pos):
		res = ""
		for i in range(len(pos)):
			if pos[i] == "1":
				res += str(self.characters[i])
		return res

	def binary(self, char):
		res = ""
		n = ord(char)
		m = 1
		while m < n or m < 65:
			m += m
		while n > 0:
			res += str(n // m)
			n %= m
			m //=2
		while len(res) < 8:
			res += "0"
		return res
	
	def decrypt(self, txt):
		res = ""

		for i in range(len(self.characters)):
			if self.characters[i] in txt:
				res += "1"
			else:
				res += "0"

		return res
	
	def fromBinary(self, bins):
		res = 0
		for i in range(len(bins)):
			if bins[i] == "1":
				res += self.bin[i]
		
		return chr(res)

if __name__ == "__main__":

	text = input("Enter a word: ")
	result = ""

	ryses = RySes()

	for i in range(len(text)):
		txt = ryses.binary(text[i])
		r = ryses.encrypt(txt)
		result += r + " "

	print("Encrypted text:", result)

	text = input("Enter the encrypted data: ").split(" ")
	result = ""

	for i in range(len(text)):
		txt = ryses.fromBinary(ryses.decrypt(text[i]))
		result += txt
	
	print("Decrypted text:", result)