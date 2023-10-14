money = [
	1000, 500, 200,
	100, 50, 20, 10,
	5, 1, .25, .05
]
coins = [
	0, 0, 0,
	0, 22, 20, 70,
	19, 15, 0, 0
]
x = []
total = 0
sure = False

bill = 1234

print(f"Your current bill is: {bill}")

while not sure:
	for i in range(len(money)):
		n = int(input(f"Enter the amt of {money[i]} peso:\t"))
		x.append(n)
		coins[i] += n
		total += money[i] * n
	
	while total < bill:
		for i in range(len(money)):
			n = int(input(f"Enter the amt of {money[i]} peso {x[i]}:\t"))
			x[i] += n
			coins[i] += n
			total += money[i] * n
	
	if "y" in input("Are you sure? "):
		sure = True

print(f"The total amount you've entered is {total} pesos composed of: ")
for i in range(len(money)):
	if x[i] != 0:
		print(f"{money[i]}\t-\t{x[i]}")

print("")

if bill < total:
	# sukli
	total -= bill
	_total = total
	if total < 0:
		total *= -1
	x = []
	for i in range(len(money)):
		y = 0
		if coins[i] != 0:
			y = int(total / money[i])
			total %= money[i]
		x.append(y)
	
	print(f"Your return {_total} is composed of: ")
	for i in range(len(money)):
		if x[i] != 0:
			print(f"{money[i]}\t-\t{x[i]}")
	print("")