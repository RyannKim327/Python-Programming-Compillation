from tkinter import X, Tk, Entry, Button, Frame, mainloop

def add(x):
	s = str(x)
	e.insert(len(e.get()) + 1, s)
	print(s)

def total():
	s = eval(e.get())
	e.delete(0, len(e.get()))
	e.insert(len(e.get()), s)

def backspace():
	e.delete(len(e.get()) - 1)

def main():
	
	global e
	
	b = Tk()
	b.geometry("300x300")
	b.minsize(height=150, width=150)
	
	f = Frame(b)
	f1 = Frame(f)
	f2 = Frame(f)
	f3 = Frame(f)
	f4 = Frame(f)
	
	e = Entry(f, font=("Times New Roman", 50))
	e.pack(fill=X, padx=5, pady=5)
	
	_1 = Button(f1, text = "1")
	_1.config(width = "5")
	_1.config(command = lambda: add(1))
	_1.pack(side='left')
	
	_2 = Button(f1, text = "2")
	_2.config(width = "2")
	_2.config(command = lambda: add(2))
	_2.pack(side='left')
	
	_3 = Button(f1, text = "3")
	_3.config(width = "2")
	_3.config(command = lambda: add(3))
	_3.pack(side='left')
	
	_p = Button(f1, text = "+")
	_p.config(width = "2")
	_p.config(command = lambda: add("+"))
	_p.pack(side='left')
	
	f1.pack()
	
	_4 = Button(f2, text = "4")
	_4.config(width = "2")
	_4.config(command = lambda: add(4))
	_4.pack(side = 'left')
	
	_5 = Button(f2, text = "5")
	_5.config(width = "2")
	_5.config(command = lambda: add(5))
	_5.pack(side = 'left')
	
	_6 = Button(f2, text = "6")
	_6.config(width = "2")
	_6.config(command = lambda: add(6))
	_6.pack(side = 'left')
	
	_d = Button(f2, text = "-")
	_d.config(width = "2")
	_d.config(command = lambda: add("-"))
	_d.pack(side = 'left')
	
	f2.pack()
	
	_7 = Button(f3, text = "7")
	_7.config(width = "2")
	_7.config(command = lambda: add(7))
	_7.pack(side = 'left')
	
	_8 = Button(f3, text = "8")
	_8.config(width = "2")
	_8.config(command = lambda: add(8))
	_8.pack(side = 'left')
	
	_9 = Button(f3, text = "9")
	_9.config(width = "2")
	_9.config(command = lambda: add(9))
	_9.pack(side = 'left')
	
	_m = Button(f3, text = "*")
	_m.config(width = "2")
	_m.config(command = lambda: add("*"))
	_m.pack(side = 'left')
	
	f3.pack()
	
	_0 = Button(f4, text = "0")
	_0.config(width = "2")
	_0.config(command = lambda: add(0))
	_0.pack(side = 'left')
	
	_q = Button(f4, text = "/")
	_q.config(width = "2")
	_q.config(command = lambda: add("/"))
	_q.pack(side = 'left')
	
	_d = Button(f4, text = "=")
	_d.config(width = "2")
	_d.config(command = total)
	_d.pack(side = 'left')
	
	_b = Button(f4, text = "<")
	_b.config(width = "2")
	_b.config(command = backspace)
	_b.pack(side = 'left')
	
	f4.pack()
	
	f.pack(side="bottom")
	
	b.mainloop()
main()