def sort(text):
	a = []
	for i in range(len(text)):
		a.append(ord(text[i]))
	
	for i in range(len(a)):
		for j in range(i):
			if a[i] < a[j]:
				a[i], a[j] = a[j], a[i]
	
	return a

def isAnagram(text1, text2):
	return sort(text1) == sort(text2)

text1 = input("Enter text 1: ")
text2 = input("Enter text 1: ")

print(isAnagram(text1, text2))