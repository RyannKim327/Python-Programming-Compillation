from extra import enter, typing, addZero

# A simple Object Oriented Programming Program
# Check out the extra.py for the code of enter and typing

a = enter("Please enter number", 1)
b = enter("Please enter another number", 1)
c = ""
for d in range(1, int(a) + 1):
	for e in range(1, int(b) + 1):
		c += addZero(str(d * e), int(a) * int(b))+ "  "
	c += "\n"
typing(c, 3)