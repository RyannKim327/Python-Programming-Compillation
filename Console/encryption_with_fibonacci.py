def fibonacci(txt):
	array = [0, 1]
	for i in range(2, len(txt)):
		n1 = array[i - 2]
		n2 = array[i - 1]
		array.append(n1 + n2)
	return array

def encrypt(word):
	data = fibonacci(word)
	result = ""
	for i in range(len(word)):
		result += chr(ord(word[i]) + data[i])
	return result

def decrypt(word):
	data = fibonacci(word)
	result = ""
	for i in range(len(word)):
		result += chr(ord(word[i]) - data[i])
	return result

print(encrypt("Kimmy"))
print(decrypt("Kjno|"))