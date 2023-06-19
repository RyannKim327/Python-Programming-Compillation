from tkinter import *
from tkinter import messagebox
import random as r

def n(num):
	global a, b
	if a[b] == num:
		messagebox.showinfo("Congrats", "You've got it")
	else:
		messagebox.showerror("Error", "Hehe")

	c.config(text=a[b])
	a = []
	for i in range(3):
		a.append(r.randint(0, 100))
	b = r.randint(0, len(a) - 1)
	e.config(text=a[0], command=lambda: n(a[0]))
	f.config(text=a[1], command=lambda: n(a[1]))
	g.config(text=a[2], command=lambda: n(a[2]))

global a, b

root = Tk()
root.geometry("300x300")
root.title("Sample app")

a = []
for i in range(3):
	a.append(r.randint(0, 100))

b = r.randint(0, len(a) - 1)

c = Label(root, text="?", font=("", 50), justify='center')
c.pack(side="top", fill='both', expand=True)

d = Frame(root)

e = Button(d, text=a[0], font=("", 25), justify='center', command=lambda: n(a[0]))
e.pack(side="left", fill='both', expand=True)

f = Button(d, text=a[1], font=("", 25), justify='center', command=lambda: n(a[1]))
f.pack(side="left", fill='both', expand=True)

g = Button(d, text=a[2], font=("", 25), justify='center', command=lambda: n(a[2]))
g.pack(side="left", fill='both', expand=True)

d.pack(side='left', fill='both', expand=True)

root.mainloop()