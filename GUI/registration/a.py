from tkinter import *
import random as r

def click(a):
	x = r.randint(0, root.winfo_width())
	y = r.randint(0, root.winfo_height())
	a.place(x=x, y=y)

root = Tk()
root.geometry("600x600")
root.title("Login Panel")

x = r.randint(0, root.winfo_width())
y = r.randint(0, root.winfo_height())

a = Button(root, text="Click me")
a.config(command=lambda:click(a))
a.place(x=x, y=y)

root.mainloop()