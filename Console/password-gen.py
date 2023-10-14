import random

a = input("Enter your easy to remember password: ")
alpha = "abcdefghijklmnopqrstuvwxyz"
alter = [
	"@", "13", "c", "d", "3",
	"f", "9", "h", "!", "j",
	"k", "1", "m", "n", "0",
	"p", "q", "12", "$", "+",
	"u", "v", "w", "x", "y", "z"
]

b = ""

for i in range(len(a)):
	c = True
	for j in range(len(alpha)):
		if (random.randint(0, 1) % 2) == 0 and a[i] == alpha[j]:
			b += alter[j]
			c = False
			break
	if c:
		b += a[i]

print(b.replace(" ", "_"))