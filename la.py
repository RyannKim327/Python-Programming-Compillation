import time

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
	t = [
		[16, 8, 4, 2, 1],
		[16, 8, 4, 2, 1],
		[16, 8, 4, 2, 1]
	]
	timer = getTime()
	a = "[1]"
	b = "[0]"
	hr = convert(timer[0])
	min = convert(timer[1])
	sec = convert(timer[2])
	_hr = ""
	_min = ""
	_sec = ""
	_hr_ = []
	_hr_.append((hr // 12))
	_hr_.append(hr % 12)
	for i in t[0]:
		if i in _hr_:
			_hr += a
		else:
			_hr += b

	print(_hr)
	
if __name__ == "__main__":
	start()