from tkinter import *


def start():

	pads = 5
	bgc = "#131320"
	fgc = "#ffffff"

	root = Tk()
	root.config(bg=bgc)
	root.geometry("300x300")
	root.title("Calculator")
	root.resizable(False, False)

	wala_kaming = Label(root, text="Calculator", font=('Times New Roman', 25), justify='center', bg=bgc, fg=fgc)
	wala_kaming.grid(row=0, column=0, columnspan=5)

	entry = Entry(root, width=28, font=('Times New Roman', 15), bg=bgc, fg=fgc)
	entry.grid(row=1, column=0, columnspan=5, padx=pads, pady=pads)

	b1 = Button(root, text="1", width=5, bg=bgc, fg=fgc)
	b1.grid(row=2, column=0, padx=pads, pady=pads)

	b2 = Button(root, text="2", width=5, bg=bgc, fg=fgc)
	b2.grid(row=2, column=1, padx=pads, pady=pads)

	b3 = Button(root, text="3", width=5, bg=bgc, fg=fgc)
	b3.grid(row=2, column=2, padx=pads, pady=pads)

	ba = Button(root, text="+", width=5, bg=bgc, fg=fgc)
	ba.grid(row=2, column=3, padx=pads, pady=pads)

	bs = Button(root, text="-", width=5, bg=bgc, fg=fgc)
	bs.grid(row=2, column=4, padx=pads, pady=pads)
	
	b4 = Button(root, text="4", width=5, bg=bgc, fg=fgc)
	b4.grid(row=3, column=0, padx=pads, pady=pads)

	b5 = Button(root, text="5", width=5, bg=bgc, fg=fgc)
	b5.grid(row=3, column=1, padx=pads, pady=pads)

	b6 = Button(root, text="6", width=5, bg=bgc, fg=fgc)
	b6.grid(row=3, column=2, padx=pads, pady=pads)

	bp = Button(root, text="+", width=5, bg=bgc, fg=fgc)
	bp.grid(row=3, column=3, padx=pads, pady=pads)

	bq = Button(root, text="-", width=5, bg=bgc, fg=fgc)
	bq.grid(row=3, column=4, padx=pads, pady=pads)

	b7 = Button(root, text="7", width=5, bg=bgc, fg=fgc)
	b7.grid(row=4, column=0, padx=pads, pady=pads)

	b8 = Button(root, text="8", width=5, bg=bgc, fg=fgc)
	b8.grid(row=4, column=1, padx=pads, pady=pads)

	b9 = Button(root, text="9", width=5, bg=bgc, fg=fgc)
	b9.grid(row=4, column=2, padx=pads, pady=pads)

	be = Button(root, text="=", width=13, height=3, bg=bgc, fg=fgc)
	be.grid(row=4, column=3, columnspan=2, rowspan=2, padx=pads, pady=pads)

	bd = Button(root, text=".", width=5, bg=bgc, fg=fgc)
	bd.grid(row=5, column=0, padx=pads, pady=pads)

	b0 = Button(root, text="0", width=5, bg=bgc, fg=fgc)
	b0.grid(row=5, column=1, padx=pads, pady=pads)

	bc = Button(root, text="CE", width=5, bg=bgc, fg=fgc)
	bc.grid(row=5, column=2, padx=pads, pady=pads)


	root.mainloop()

start()