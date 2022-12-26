arr = []
total = 4

def createPrime():
	arr = []
	for i in range(100):
		if i % 2 == 0 and i != 2:
			print("", end="")
		elif i % 3 == 0 and i != 3:
			print("", end="")
		elif i % 4 == 0 and i != 4:
			print("", end="")
		elif i % 5 == 0 and i != 5:
			print("", end="")
		elif i % 6 == 0 and i != 6:
			print("", end="")
		elif i % 7 == 0 and i != 7:
			print("", end="")
		elif i % 8 == 0 and i != 8:
			print("", end="")
		elif i % 9 == 0 and i != 9:
			print("", end="")
		elif i % 10 == 0 and i != 10:
			print("", end="")
		else:
			arr.append(i)
	return arr
	
def counting(list):
	div = list[1] - list[0]
	isSeq = True
	
	for i in range(1, len(arr)):
		if(list[i] - list[i - 1]) != div:
			isSeq = False
			break
	
	if isSeq:
		print("This is a sequence")
		x = div
		type = "Increment"
		if list[1] < list[0]:
			type = "Decrement"
			x = div * -1
		print(f"Reason: {type} of {x}")
		if div == 2:
			if list[1] % 2 == 0:
				print("Even Sequence")
			else:
				print("Odd Sequence")
		print(f"Answer: {list[total - 1] + div}")
		return True
	return False

def prime(list):
	primes = createPrime()
	total = 0
	x = 0
	type = "Increment"
	if list[0] in primes:
		for i in range(len(primes)):
			if list[0] == primes[i]:
				x = i
				break
	
	if list[0] < list[1]:
		for i in range(len(list)):
			if list[i] == primes[x + i]:
				total += 1
	else:
		type = "Decrement"
		for i in range(len(list)):
			if list[i] == primes[x - i]:
				total += 1
	if total == len(list):
		print(f"This is a prime number sequence in {type}.")
		return True
	return False

for i in range(total):
	a = int(input(f"Enter number {i + 1}: "))
	arr.append(a)

if counting(arr):
	print("")
elif prime(arr):
	print("")
else:
	print("Nothing Match")