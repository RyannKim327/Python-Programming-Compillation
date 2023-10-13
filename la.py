import time

a = [
	[8, 4, 2, 1],
	[8, 4, 2, 1],
	[8, 4, 2, 1],
	[8, 4, 2, 1]
]


def getTime():
	timer = time.ctime()
	time1 = timer.split(" ")[3]
	return time1.split(":")

def convert(a):
	if a.isdigit():
		return int(a) % 12
	else:
		return 0

def start():
	timer = getTime()
	hr = convert(timer[0])
	min = convert(timer[1])
	sec = convert(timer[2])
	for i in range(len(a)):
		for j in range(len(a[i])):
			pass
	pass

if __name__ == "__main__":
	start()