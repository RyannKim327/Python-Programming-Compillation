# Ask some input from user
n = int(input("Enter column: "))

# This is for output
o = ""

# Lets do looping vertically
for i in range(1, n + 1):
	# Make this x in side, to call it outside of while
	x = i
	while x <= n:
		# This will generare inverted right triangle of numbers
		'''
		1 2 3 4 5
		2 3 4 5
		3 4 5
		4 5
		5
		'''
		o += str(x) + "\t"
		
		# Increment
		x += 1
	
	# Let's have some formula, the equation is below
	e = n - (x - i)
	
	# Formulas: (Sample)
	# 5 - 5 = 0
	# 5 - 4 = 1
	# 5 - 3 = 2
	# 5 - 2 = 3
	# 5 - 1 = 4
	
	# Then let's filled up the blanks
	for j in range(1, e + 1):
		# j can only call inside of for loop
		# always add 1 (+1) to make the condition <= and not <
		o += str(j) + "\t"
	
	# To break the line
	o += "\n"

# Output or print output
print(o)

'''
Enter column: 5
1       2       3       4       5
2       3       4       5       1
3       4       5       1       2
4       5       1       2       3
5       1       2       3       4
'''