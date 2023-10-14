from measure import check

def do():
	var = "Hello World"
	print(var)

def do2():
	print("Hello World")

def loop():
	lists = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
	print(lists)
	for i in range(len(lists)):
		for j in range(i):
			if lists[i] < lists[j]:
				lists[i], lists[j] = lists[j], lists[i]
	print(lists)

check(loop)