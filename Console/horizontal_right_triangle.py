# h = height, w = width, d = repeatition or duplication

h = 5
w = 5
d = int(input("Enter number of repeatition: ")) + 1

# Result (Use of contatination)
r = ""

# Generate the right triangle's height as last loop
for i in range(1, h + 1):

	# Generate the repeatition
	for j in range(1, d):

		# I Use while to work it with another loop
		# While loop to generate *
		k = 1
		while k < i:
			r += "* "
			k += 1
		
		# This loop generate spaces
		for l in range(k, w + 1):
			r += "  "
	
	# To break the line
	r += "\n"

# Print
print(r)