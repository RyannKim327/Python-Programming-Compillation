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
	time2 = time1.split(":")

print(time.ctime())