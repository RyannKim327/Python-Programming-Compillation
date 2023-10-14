# Mean, Median, Mode
# Variable initiation

list = []
a = input("Please enter a valid number: ")


while a != "" or len(list) < 2:
	# Use try catch to avoid error or program crash
	# This is also very helpful for you to create an alternative way if every that there's a problem.
	
	try:
		list.append(int(a))
	except:
		print("This is not an integer.")
	
	a = input("Please enter another number or leave a blank to terminate: ")

# Mean:
# This is also called as the average

mean = sum(list) / len(list)


# Median:
# The middle value in a list ordered from smallest to largest

# Sort (Bubble sort)
for i in range(len(list)):
	for j in range(i):
		if list[i] < list[j]:
			list[i], list[j] = list[j], list[i]

median = list[len(list) // 2]

# Mode:
# Most frequent or called number in a list

# I use None as default, instead of 0
mode = None
current = -1
total = 0
high = -1
for i in range(1, len(list)):
	if mode == None:
		mode = list[i]
	if list[i] == list[i - 1]:
		total += 1
		current = list[i]
	else:
		if total > high:
			high = total
			mode = list[i - 1]
		total = 1

print(f"Mean: {mean}\nMedian: {median}\nMode: {mode}")