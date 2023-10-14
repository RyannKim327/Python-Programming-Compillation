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
	_hr_ = []
	for i in t[0]:
		_hr_.append(hr // i)
		hr %= i


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
	
	for i in _hr_:
		if i == 1:
			_hr += a
		else:
			_hr += b

	print(_hr)
	
if __name__ == "__main__":
	start()

	# a = 501
	# b = [1000, 500, 200, 100, 50, 20, 5, 1, .25]
	# for i in b:
	# 	print(a // i)
	# 	a %= i