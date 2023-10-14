import time, os
from tkinter import *

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

def algo(a, w):
	b = [
		[32, 16, 8, 4, 2, 1],
		[32, 16, 8, 4, 2, 1],
		[32, 16, 8, 4, 2, 1]
	]
	c = []
	d = ""
	a1 = "[1]"
	b1 = "[0]"
	for e in b[0]:
		c.append(a // e)
		a %= e
	for e in range(len(c)):
		# d += f"[{e}]"
		if c[e] == 1:
			w[e].config(bg="green")

	
	return d

def run():
	timer = getTime()
	hr =  convert(timer[0])
	min = convert(timer[1])
	sec = convert(timer[2])
	print(algo(hr))
	print(algo(min))
	print(algo(sec))
	time.sleep(.1)
	os.system("cls")

def start():
	global hs
	global ms
	global ss
	
	base = Tk()
	base.geometry("500x500")

	h = Label(base, text="32", font=("", 20), width=5)
	h.grid(row=0, column=0)

	h1 = Label(base, text="16", font=("", 20), width=5)
	h1.grid(row=0, column=1)
	
	h2 = Label(base, text="8", font=("", 20), width=5)
	h2.grid(row=0, column=2)

	h3 = Label(base, text="4", font=("", 20), width=5)
	h3.grid(row=0, column=3)

	h4 = Label(base, text="2", font=("", 20), width=5)
	h4.grid(row=0, column=4)

	h5 = Label(base, text="1", font=("", 20), width=5)
	h5.grid(row=0, column=5)

	m = Label(base, text="32", font=("", 20), width=5)
	m.grid(row=1, column=0)

	m1 = Label(base, text="16", font=("", 20), width=5)
	m1.grid(row=1, column=1)
	
	m2 = Label(base, text="8", font=("", 20), width=5)
	m2.grid(row=1, column=2)

	m3 = Label(base, text="4", font=("", 20), width=5)
	m3.grid(row=1, column=3)

	m4 = Label(base, text="2", font=("", 20), width=5)
	m4.grid(row=1, column=4)

	m5 = Label(base, text="1", font=("", 20), width=5)
	m5.grid(row=1, column=5)

	s = Label(base, text="32", font=("", 20), width=5)
	s.grid(row=2, column=0)

	s1 = Label(base, text="16", font=("", 20), width=5)
	s1.grid(row=2, column=1)
	
	s2 = Label(base, text="8", font=("", 20), width=5)
	s2.grid(row=2, column=2)

	s3 = Label(base, text="4", font=("", 20), width=5)
	s3.grid(row=2, column=3)

	s4 = Label(base, text="2", font=("", 20), width=5)
	s4.grid(row=2, column=4)

	s5 = Label(base, text="1", font=("", 20), width=5)
	s5.grid(row=2, column=5)

	hs = [h, h1, h2, h3, h4, h5]
	ms = [m, m1, m2, m3, m4, m5]
	ss = [s, s1, s2, s3, s4, s5]

	base.mainloop()

	
if __name__ == "__main__":
	start()