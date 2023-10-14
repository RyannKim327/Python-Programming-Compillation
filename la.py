import time

def getTime():
	timer = time.ctime()
	time1 = timer.split(" ")[3]
	return time1.split(":")

def convert(a):
	if a.isdigit():
		b = int(a) % 12
		if b == 0:
			return 12
		return b
	else:
		return 0

def start():
	t = [
		[16, 8, 4, 2, 1],
		[16, 8, 4, 2, 1],
		[16, 8, 4, 2, 1]
	]
	timer = getTime()
	a = "*"
	b = "."
	hr = convert(timer[0])
	min = convert(timer[1])
	sec = convert(timer[2])
	_hr = ""
	_min = ""
	_sec = ""
	_hr_ = [16]
	print(t[0])
	for i in t[0]:
		print(i)
		# if i in _hr_:
		# 	_hr += a
		# else:
		# 	_hr += b

	print(_hr)
	
if __name__ == "__main__":
	start()