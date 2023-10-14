import numpy
import matplotlib.pyplot as plot
import time

lists = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
a = []
m = []
start = time.time()
time.sleep(0.01)

for i in range(len(lists)):
	for j in range(i):
		if lists[i] < lists[j]:
			lists[i], lists[j] = lists[j], lists[i]
	print(end=" ")

last = time.time()
a.append(last - start)
m.append("Bubble sort")
time.sleep(1)
lists = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
start = time.time()
time.sleep(0.01)

for i in range(len(lists)):
	small = i
	for j in range(i + 1, len(lists)):
		if lists[small] > lists[j]:
			small = j
	lists[small], lists[i] = lists[i], lists[small]
	print(end=" ")

last = time.time()
a.append(last - start)
m.append("Selection Method")

time.sleep(1)
lists = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
start = time.time()
time.sleep(0.01)

for i in range(1, len(lists)):
	k = lists[i]
	j = i - 1
	while j >= 0 and k < lists[j]:
		lists[j + 1] = lists[j]
		j = j - 1
	lists[j + 1] = k
	print(end=" ")

last = time.time()
a.append(last - start)
m.append("Insertion Method")

time.sleep(1)
lists = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
start = time.time()
time.sleep(0.01)

interval = len(lists) // 2
while interval > 0:
	for i in range(interval, len(lists)):
		temp = lists[i]
		j = i
		while j >= interval and lists[j - interval] > temp:
			lists[j] = lists[j - interval]
			j -= interval
		lists[j] = temp
	interval //= 2
	print(end=" ")


last = time.time()
a.append(last - start)
m.append("Shell Method")


data = numpy.array(a)


plot.plot(data)
plot.grid()
plot.ylabel("Time")
plot.xlabel(m)
plot.show()

print()
print(a)