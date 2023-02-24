import random
import time
import os

amt = random.randint(5, 10)
while (amt % 2) != 0:
	amt = random.randint(5, 10)

lists = []
copy = []
reveal = []
pattern = ""

for i in range(amt):
	x = random.randint(0, amt // 2)
	while x in lists and x in copy:
		x = random.randint(0, amt // 2)
	while x in lists and i < amt:
		x = random.randint(0, amt // 2)
		copy.append(x)
	lists.append(x)
	print(lists)
	print(copy)

for i in range(amt):
	x = lists[i]
	# if (x + 1) > amt / 2:
	#	x //= 2
	
	pattern += str(x) + "\t"
	if i + 1 == amt // 2:
		pattern += "\n"

print(pattern)

time.sleep(5)

if os.system("cls"):
	os.system("clear")

while True:
	pattern = ""
	for i in range(amt):
		x = lists[i]
		# if (x + 1) > amt / 2:
		#	x //= 2
		
		pattern += (str(x) if not (i in reveal) else "_" + str(i) + "_") + "\t"
		if i + 1 == amt // 2:
			pattern += "\n"
	print(pattern)
	print(lists)

	try:
		y = input("Enter number position splited by [:] (e.g 1:2): ").split(":")
		num1 = int(y[0])
		num2 = int(y[1])
		print(lists[num1], lists[num2])
		if num1 == num2:
			continue
		elif (lists[num1] * 2) == lists[num2]:
			reveal.append(num1)
			reveal.append(num2)
		elif (lists[num2] * 2) == lists[num1]:
			reveal.append(num1)
			reveal.append(num2)
		else:
			continue
	except:
		continue
	if os.system("cls"):
		os.system("clear")