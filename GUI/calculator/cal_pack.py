from tkinter import *

def add(n):
	e.insert(END, n)

def sum_it_all():
	total = eval(e.get())
	e.delete(0, END)
	e.insert(0, total)

def delete_one():
	e.delete(len(e.get()) - 1)

def start():

	global e

	pads = 8
	main_bg = "#131320"

	root = Tk()
	root.geometry('600x800')
	root.title('Calculator')
	root.config(bg="#131320")
	
	wala_kaming = Label(root, text="Calculator", bg=main_bg, fg='#ffffff', font=('Times New Roman', 25))
	wala_kaming.pack(fill='x')

	e = Entry(root, bg=main_bg, fg='#ffffff', font=('Courier New', 25), justify='right')
	e.pack(fill='x', padx=5, pady=5)

	row1 = Frame(root, bg=main_bg)

	b1 = Button(row1, bg=main_bg, fg='#ffffff', text='1', command=lambda: add("1"))
	b1.pack(side='left', fill='both', expand=True, anchor='n', padx=pads, pady=pads)

	b2 = Button(row1, bg=main_bg, fg='#ffffff', text='2', command=lambda: add("2"))
	b2.pack(side='left', fill='both', expand=True, anchor='n', padx=pads, pady=pads)

	b3 = Button(row1, bg=main_bg, fg='#ffffff', text='3', command=lambda: add("3"))
	b3.pack(side='left', fill='both', expand=True, anchor='n', padx=pads, pady=pads)

	ba = Button(row1, bg=main_bg, fg='#ffffff', text='+', command=lambda: add("+"))
	ba.pack(side='left', fill='both', expand=True, anchor='n', padx=pads, pady=pads)

	bs = Button(row1, bg=main_bg, fg='#ffffff', text='-', command=lambda: add("-"))
	bs.pack(side='left', fill='both', expand=True, anchor='n', padx=pads, pady=pads)

	row1.pack(fill='both', expand=True)
	
	row2 = Frame(root, bg=main_bg)

	b4 = Button(row2, bg=main_bg, fg='#ffffff', text='4', command=lambda: add("4"))
	b4.pack(side='left', fill='both', expand=True, anchor='n', padx=pads, pady=pads)

	b5 = Button(row2, bg=main_bg, fg='#ffffff', text='5', command=lambda: add("5"))
	b5.pack(side='left', fill='both', expand=True, anchor='n', padx=pads, pady=pads)

	b6 = Button(row2, bg=main_bg, fg='#ffffff', text='6', command=lambda: add("6"))
	b6.pack(side='left', fill='both', expand=True, anchor='n', padx=pads, pady=pads)

	bm = Button(row2, bg=main_bg, fg='#ffffff', text='*', command=lambda: add("*"))
	bm.pack(side='left', fill='both', expand=True, anchor='n', padx=pads, pady=pads)

	bq = Button(row2, bg=main_bg, fg='#ffffff', text='/', command=lambda: add("/"))
	bq.pack(side='left', fill='both', expand=True, anchor='n', padx=pads, pady=pads)

	row2.pack(fill='both', expand=True)

	be = Button(root, bg=main_bg, fg='#ffffff', text='=', width=15, command=sum_it_all)
	be.pack(side='right', fill='both', anchor='n', padx=pads, pady=pads)

	row3 = Frame(root, bg=main_bg)

	b7 = Button(row3, bg=main_bg, fg='#ffffff', text='7', command=lambda: add("7"))
	b7.pack(side='left', fill='both', expand=True, anchor='n', padx=pads, pady=pads)

	b8 = Button(row3, bg=main_bg, fg='#ffffff', text='8', command=lambda: add("8"))
	b8.pack(side='left', fill='both', expand=True, anchor='n', padx=pads, pady=pads)

	b9 = Button(row3, bg=main_bg, fg='#ffffff', text='9', command=lambda: add("9"))
	b9.pack(side='left', fill='both', expand=True, anchor='n', padx=pads, pady=pads)

	row3.pack(fill='both', expand=True)

	row4 = Frame(root, bg=main_bg)

	bd = Button(row4, bg=main_bg, fg='#ffffff', text='.', command=lambda: add("."))
	bd.pack(side='left', fill='both', expand=True, anchor='n', padx=pads, pady=pads)

	b0 = Button(row4, bg=main_bg, fg='#ffffff', text='0', command=lambda: add("0"))
	b0.pack(side='left', fill='both', expand=True, anchor='n', padx=pads, pady=pads)
	
	bc = Button(row4, bg=main_bg, fg='#ffffff', text='CE', command=delete_one)
	bc.pack(side='left', fill='both', expand=True, anchor='n', padx=pads, pady=pads)

	row4.pack(fill='both', expand=True)

	root.mainloop()

start()