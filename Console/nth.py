num = int(input("Enter a number: "))
last = num % 10
s_last = num % 100
result = ""

if s_last >= 10 and s_last < 20:
	result = "th"
else:
	if last == 1:
		result = "st"
	elif last == 2:
		result = "nd"
	elif last == 3:
		result = "rd"
	else:
		result = "th"

print(f"{num}{result}")