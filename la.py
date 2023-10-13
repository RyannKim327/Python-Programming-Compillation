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
	return tuple(time1.split(":"))

def convert(a):
	if a.isdigit():
		return int(a) % 12
	else:
		return 0

def start():
	timer = getTime()
	hr = convert(timer[0])
	min = convert(timer[0])
	sec = convert(timer[0])

if __name__ == "__main__":
	start()