text = input("Enter a string: ").upper()
pal = ""
for i in range(len(text) - 1, -1, -1):
	pal += text[i]
palindrome = "not palindrome"
if text == pal:
	palindrome = "palindrome"
print(f"{text} is a {palindrome}")