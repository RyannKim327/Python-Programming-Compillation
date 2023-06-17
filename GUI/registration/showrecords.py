from tkinter import *
from data import *

root = Tk()
root.geometry("600x600")
root.title("Information:")

createDatabase([])

x = 0
for i in getData():
	y = 0
	for j in i:
		z = Label(root, text=j)
		z.grid(row=x, column=y)
		y += 1
	x += 1

root.mainloop()