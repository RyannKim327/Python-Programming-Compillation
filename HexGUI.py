from tkinter import Tk, Label, Entry, Button, mainloop

def toHex(s):
	h = "0123456789ABCDEF"
	o = ""
	for i in range(len(s)):
		c = ord(s[i])
		o += h[c // 16]
		o += h[c % 16]
		o += " "
		if ((i + 1) % 10) == 0:
			o += "\n"
	return o

def conv():
	l.config(text = toHex(e.get()))

def main():
	global l
	global e
	
	b = Tk()
	b.geometry("300x300")
	
	l = Label(text="Output")
	l.pack()
	
	e = Entry()
	e.pack()
	
	b = Button()
	b.config(text = "Convert")
	b.config(command = conv)
	b.pack()
	
	mainloop()
main()