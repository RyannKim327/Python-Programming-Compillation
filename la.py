import time

def getTime():
	timer = time.ctime()
	time1 = timer.split(" ")[3]
	return time1.split(":")

def convert(a):
	if a.isdigit():
		b = int(a)
		return b
	else:
		return 0

def algo(a):
	b = [
		[16, 8, 4, 2, 1],
		[16, 8, 4, 2, 1],
		[16, 8, 4, 2, 1]
	]
	c = []
	d = ""
	for e in b[0]:
		c.append(a // e)
		a %= e
	for i in c:
		if i == 1:
			d += a
		else:
			d += b
	


def start():
	timer = getTime()
	a = "[1]"
	b = "[0]"
	hr =  5 #convert(timer[0])
	min = convert(timer[1])
	sec = convert(timer[2])
	_hr = ""
	_min = ""
	_sec = ""
	
	
	print(_hr)
	
if __name__ == "__main__":
	start()

	# a = 501
	# b = [1000, 500, 200, 100, 50, 20, 5, 1, .25]
	# for i in b:
	# 	print(a // i)
	# 	a %= i