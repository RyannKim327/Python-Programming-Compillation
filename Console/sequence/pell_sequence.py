# 0, 1, 2, 5, 12, 29, 70, 169, 408, 985, 2378, 5741, 13860
print("Pell Sequence")

lists = [0, 1]

for i in range(2, 10):
	x = lists[i - 2]
	y = lists[i - 1]
	y += y
	lists.append(x + y)

print(lists)