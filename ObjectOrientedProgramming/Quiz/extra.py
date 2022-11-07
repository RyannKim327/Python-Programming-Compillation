def typing(txt, time):
	speed = 10000 * time
	length = len(txt)
	i = 0
	while i < speed * length:
		if i % speed == 0:
			print(txt[i // speed], end="", flush=True)
		i += 1
	print()

def enter(txt, time):
	txt += ": "
	speed = 10000 * time
	length = len(txt)
	i = 0
	while i < speed * length:
		if i % speed == 0:
			print(txt[i // speed], end="", flush=True)
		i += 1
	return input()

def addZero(num, max):
	a = ""
	for i in range(len(str(max)) - len(str(num))):
		a += str(0)
	a += str(num)
	return a