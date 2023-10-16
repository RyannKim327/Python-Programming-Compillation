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
		[16, 8, 4, 2, 1]
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
			w[e].config(bg="#aaaaaa", fg="#131320")
		else:
			w[e].config(bg="#131320", fg="#aaaaaa")

def run():
	global hs, ms, ss
	timer = getTime()
	hr =  convert(timer[0])
	min = convert(timer[1])
	sec = convert(timer[2])
	algo(hr, hs)
	algo(min, ms)
	algo(sec, ss)
	base.after(1, run)

def start():
	global hs
	global ms
	global ss
	global base

	base = Tk()
	base.geometry("200x100")
	base.title("Binary Clock")

	ft = Frame(base)

	h = Label(ft, text="32", bg="red")
	h.pack(padx=1, pady=1, side='left', fill='both', expand=True)

	h3 = Label(ft, text="04", bg="red")
	h3.pack(padx=1, pady=1, side='left', fill='both', expand=True)

	m = Label(ft, text="32", bg="red")
	m.pack(padx=1, pady=1, side='left', fill='both', expand=True)

	m3 = Label(ft, text="04", bg="red")
	m3.pack(padx=1, pady=1, side='left', fill='both', expand=True)

	s = Label(ft, text="32", bg="red")
	s.pack(padx=1, pady=1, side='left', fill='both', expand=True)

	s3 = Label(ft, text="04", bg="red")
	s3.pack(padx=1, pady=1, side='left', fill='both', expand=True)

	ft.pack(padx=1, pady=1, fill="both", expand=True)

	fm = Frame(base)

	h1 = Label(fm, text="16", bg="blue")
	h1.pack(padx=1, side='left', fill='both', expand=True)

	h4 = Label(fm, text="02", bg="red")
	h4.pack(padx=1, side='left', fill='both', expand=True)

	m1 = Label(fm, text="16", bg="blue")
	m1.pack(padx=1, side='left', fill='both', expand=True)

	m4 = Label(fm, text="02", bg="red")
	m4.pack(padx=1, side='left', fill='both', expand=True)

	s1 = Label(fm, text="16", bg="blue")
	s1.pack(padx=1, side='left', fill='both', expand=True)

	s4 = Label(fm, text="02", bg="red")
	s4.pack(padx=1, side='left', fill='both', expand=True)

	fm.pack(padx=1, fill="both", expand=True)

	fb = Frame(base)
	
	h2 = Label(fb, text="08", bg="red")
	h2.pack(padx=1, pady=1, side='left', fill='both', expand=True)

	h5 = Label(fb, text="01", bg="red")
	h5.pack(padx=1, pady=1, side='left', fill='both', expand=True)

	m2 = Label(fb, text="08", bg="red")
	m2.pack(padx=1, pady=1, side='left', fill='both', expand=True)

	m5 = Label(fb, text="01", bg="red")
	m5.pack(padx=1, pady=1, side='left', fill='both', expand=True)

	s2 = Label(fb, text="08", bg="red")
	s2.pack(padx=1, pady=1, side='left', fill='both', expand=True)

	s5 = Label(fb, text="01", bg="red")
	s5.pack(padx=1, pady=1, side='left', fill='both', expand=True)

	fb.pack(padx=1, pady=1, fill="both", expand=True)
	
	hs = [h, h1, h2, h3, h4, h5]
	ms = [m, m1, m2, m3, m4, m5]
	ss = [s, s1, s2, s3, s4, s5]

	run()

	base.mainloop()


def start2():
	base = Tk()
	base.geometry("200x100")
	base.title("Binary Clock")

	ft = Frame(base)

	h = Label(ft, text="32", bg="red")
	h.pack(padx=1, pady=1, side='left', fill='both', expand=True)

	h3 = Label(ft, text="04", bg="red")
	h3.pack(padx=1, pady=1, side='left', fill='both', expand=True)

	m = Label(ft, text="32", bg="red")
	m.pack(padx=1, pady=1, side='left', fill='both', expand=True)

	m3 = Label(ft, text="04", bg="red")
	m3.pack(padx=1, pady=1, side='left', fill='both', expand=True)

	s = Label(ft, text="32", bg="red")
	s.pack(padx=1, pady=1, side='left', fill='both', expand=True)

	s3 = Label(ft, text="04", bg="red")
	s3.pack(padx=1, pady=1, side='left', fill='both', expand=True)

	ft.pack(padx=1, pady=1, fill="both", expand=True)

	fm = Frame(base)

	h1 = Label(fm, text="16", bg="blue")
	h1.pack(padx=1, side='left', fill='both', expand=True)

	h4 = Label(fm, text="02", bg="red")
	h4.pack(padx=1, side='left', fill='both', expand=True)

	m1 = Label(fm, text="16", bg="blue")
	m1.pack(padx=1, side='left', fill='both', expand=True)

	m4 = Label(fm, text="02", bg="red")
	m4.pack(padx=1, side='left', fill='both', expand=True)

	s1 = Label(fm, text="16", bg="blue")
	s1.pack(padx=1, side='left', fill='both', expand=True)

	s4 = Label(fm, text="02", bg="red")
	s4.pack(padx=1, side='left', fill='both', expand=True)

	fm.pack(padx=1, fill="both", expand=True)

	fb = Frame(base)
	
	h2 = Label(fb, text="08", bg="red")
	h2.pack(padx=1, pady=1, side='left', fill='both', expand=True)

	h5 = Label(fb, text="01", bg="red")
	h5.pack(padx=1, pady=1, side='left', fill='both', expand=True)

	m2 = Label(fb, text="08", bg="red")
	m2.pack(padx=1, pady=1, side='left', fill='both', expand=True)

	m5 = Label(fb, text="01", bg="red")
	m5.pack(padx=1, pady=1, side='left', fill='both', expand=True)

	s2 = Label(fb, text="08", bg="red")
	s2.pack(padx=1, pady=1, side='left', fill='both', expand=True)

	s5 = Label(fb, text="01", bg="red")
	s5.pack(padx=1, pady=1, side='left', fill='both', expand=True)

	fb.pack(padx=1, pady=1, fill="both", expand=True)

	base.mainloop()

if __name__ == "__main__":
	start()