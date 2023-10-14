from tkinter import *
from tkinter import messagebox
import random

def itsyes():
	messagebox.showinfo("Nice one baby", "Dapat lang, kasi wala kang choice.")

def itsno():
	x = random.randint(0, 300)
	y = random.randint(0, 300)
	n.place(x=x, y=y)

global n

root = Tk()
root.geometry("500x500")

l = Label(root, text="Tanggap mo na ba na bagsak ka?", font=("", 25))
l.pack()

y = Button(root, text="Yes", font=("", 25), command=itsyes)
y.pack(side='left', expand=True, fill='x')

n = Button(root, text="No", font=("", 25), command=itsno)
n.pack(side='left', expand=True, fill='x')

root.mainloop()