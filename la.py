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

def algo(a):
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
	for e in c:
		d += f"[{e}]"
	
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
	base = Tk()
	base.geometry("500x500")

	h1 = Label(base, text="16", font=("", 25), width=)
	h1.grid(row=0, column=0)
	
	h2 = Label(base, text="8", font=("", 25), width=)
	h2.grid(row=0, column=1)

	h3 = Label(base, text="4", font=("", 25), width=)
	h3.grid(row=0, column=2)

	h4 = Label(base, text="2", font=("", 25), width=)
	h4.grid(row=0, column=3)

	h5 = Label(base, text="1", font=("", 25), width=)
	h5.grid(row=0, column=4)

	m1 = Label(base, text="16", font=("", 25), width=)
	m1.grid(row=1, column=0)
	
	m2 = Label(base, text="8", font=("", 25), width=)
	m2.grid(row=1, column=1)

	m3 = Label(base, text="4", font=("", 25), width=)
	m3.grid(row=1, column=2)

	m4 = Label(base, text="2", font=("", 25), width=)
	m4.grid(row=1, column=3)

	m5 = Label(base, text="1", font=("", 25), width=)
	m5.grid(row=1, column=4)


	base.mainloop()

	
if __name__ == "__main__":
	start()