import time

a = [
	[16, 8, 4, 2, 1],
	[16, 8, 4, 2, 1],
	[16, 8, 4, 2, 1]
]


def getTime():
	timer = time.ctime()
	time1 = timer.split(" ")[3]
	return time1.split(":")

def convert(a):
	if a.isdigit():
		b = int(a) % 12
		
		return b
	else:
		return 0

def start():
	timer = getTime()
	hr = convert(timer[0])
	min = convert(timer[1])
	sec = convert(timer[2])
	for i in range(len(a)):
			
	# pass

if __name__ == "__main__":
	# a = getTime()
	# b = convert(a[0])
	print(13 % 12)