from tkinter import Label, Entry, Button, mainloop, Tk

def toBin(s):
	o = ""
	for i in range(len(s)):
		c = ord(s[i])
		x = 1
		while x < c or x < 65:
			x += x
		while x > 0:
			o += str(c // x)
			c %= x
			x //= 2
		o += " "
		if(((i + 1) % 3) == 0):
			o += "\n"
	return o

def conv():
	txt = e.get()
	l.config(text=toBin(txt))

def start():
	t = Tk()
	t.geometry("300x300")
	
	global l
	global e
	
	l = Label(text="Output")
	l.pack()
	
	e = Entry()
	e.pack()
	
	b = Button(text="Convert")
	b.config(command=conv)
	b.pack()
	
	mainloop()
start()