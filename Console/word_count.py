import re

text = input("Enter your phrase here: ")
split = re.split("\s", text)
total = 0
for i in split:
	if i != "":
		total += 1
print(f"{text}: has {total} words")