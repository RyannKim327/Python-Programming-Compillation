from tkinter import *


def start():

	root = Tk()
	root.geometry("300x300")
	root.title("Calculator")
	root.resizable(False, False)

	wala_kaming = Label(root, text="Calculator", font=('Times New Roman', 25), justify='center')
	wala_kaming.grid(row=0, column=0, columnspan=5)

	entry = Entry(root, width=40)
	entry.grid(row=1, column=1, columnspan=5)

	b1 = Button(root, text="1", width=5)
	b1.grid(row=2, column=0)

	b2 = Button(root, text="2", width=5)
	b2.grid(row=2, column=1)

	b3 = Button(root, text="3", width=5)
	b3.grid(row=2, column=3)

	b4 = Button(root, text="4", width=5)
	b4.grid(row=2, column=4)

	b5 = Button(root, text="5", width=5)
	b5.grid(row=2, column=5)

	root.mainloop()

start()