from tkinter import *

def add(n):
	global equation

	lists_of_etc = [
		'+',
		'-',
		'*',
		'/'
	]
	
	if e.get() == "Error sya Tiger, ERROR!!!":
		e.delete(0, END)
	if len(e.get()) > 0:
		last_char = e.get()[len(e.get()) - 1]
		# if not last_char in lists_of_etc:
		# 	e.insert(END, n)
		# elif not n in lists_of_etc:
		# 	e.insert(END, n)
		if n == ".":
			if not n in e.get():
				e.insert(END, n)
		if n in lists_of_etc:
			equation += e.get() + n
			e.delete(0, END)
		
	else:
		if(not n in lists_of_etc and e.get() == ""):
			e.insert(END, n)

def sum_it_all():
	print(equation + e.get())
	try:
		total = eval(equation + e.get())
		e.delete(0, END)
		e.insert(0, total)
	except:
		e.delete(0, END)
		e.insert(0, "Error sya Tiger, ERROR!!!")

def delete_one():
	if e.get() == "Error sya Tiger, ERROR!!!":
		e.delete(0, END)
	e.delete(len(e.get()) - 1)

def start():

	global e, equation
	equation = ""

	pads = 8
	main_bg = "#B1B4BF"
	k_bg = ""
	main_fg = "#293041"
	

	root = Tk()
	root.geometry('600x800')
	root.title('Calculator')
	root.config(bg=main_bg)
	
	wala_kaming = Label(root, text="Calculator", bg=main_bg, fg=main_fg, font=('Times New Roman', 25))
	wala_kaming.pack(fill='x')

	e = Entry(root, bg=main_bg, fg=main_fg, font=('Times New Roman', 35), justify='right', borderwidth=5, relief="sunken")
	e.pack(fill='x', padx=5, pady=5)

	row1 = Frame(root, bg=main_bg)

	b1 = Button(row1, bg=main_bg, fg=main_fg, text='1', font=("Times New Roman", 25), borderwidth=5, relief="raised", command=lambda: add("1"))
	b1.pack(side='left', fill='both', expand=True, anchor='n', padx=pads, pady=pads)

	b2 = Button(row1, bg=main_bg, fg=main_fg, text='2', font=("Times New Roman", 25), borderwidth=5, relief="raised", command=lambda: add("2"))
	b2.pack(side='left', fill='both', expand=True, anchor='n', padx=pads, pady=pads)

	b3 = Button(row1, bg=main_bg, fg=main_fg, text='3', font=("Times New Roman", 25), borderwidth=5, relief="raised", command=lambda: add("3"))
	b3.pack(side='left', fill='both', expand=True, anchor='n', padx=pads, pady=pads)

	ba = Button(row1, bg=main_bg, fg=main_fg, text='+', font=("Times New Roman", 25), borderwidth=5, relief="raised", command=lambda: add("+"))
	ba.pack(side='left', fill='both', expand=True, anchor='n', padx=pads, pady=pads)

	bs = Button(row1, bg=main_bg, fg=main_fg, text='-', font=("Times New Roman", 25), borderwidth=5, relief="raised", command=lambda: add("-"))
	bs.pack(side='left', fill='both', expand=True, anchor='n', padx=pads, pady=pads)

	row1.pack(fill='both', expand=True)
	
	row2 = Frame(root, bg=main_bg)

	b4 = Button(row2, bg=main_bg, fg=main_fg, text='4', font=("Times New Roman", 25), borderwidth=5, relief="raised", command=lambda: add("4"))
	b4.pack(side='left', fill='both', expand=True, anchor='n', padx=pads, pady=pads)

	b5 = Button(row2, bg=main_bg, fg=main_fg, text='5', font=("Times New Roman", 25), borderwidth=5, relief="raised", command=lambda: add("5"))
	b5.pack(side='left', fill='both', expand=True, anchor='n', padx=pads, pady=pads)

	b6 = Button(row2, bg=main_bg, fg=main_fg, text='6', font=("Times New Roman", 25), borderwidth=5, relief="raised", command=lambda: add("6"))
	b6.pack(side='left', fill='both', expand=True, anchor='n', padx=pads, pady=pads)

	bm = Button(row2, bg=main_bg, fg=main_fg, text='*', font=("Times New Roman", 25), borderwidth=5, relief="raised", command=lambda: add("*"))
	bm.pack(side='left', fill='both', expand=True, anchor='n', padx=pads, pady=pads)

	bq = Button(row2, bg=main_bg, fg=main_fg, text='/', font=("Times New Roman", 25), borderwidth=5, relief="raised", command=lambda: add("/"))
	bq.pack(side='left', fill='both', expand=True, anchor='n', padx=pads, pady=pads)

	row2.pack(fill='both', expand=True)

	be = Button(root, bg=main_bg, fg=main_fg, text='=', font=("Times New Roman", 30), borderwidth=5, relief="raised", width=8, command=sum_it_all)
	be.pack(side='right', fill='both', anchor='n', padx=pads, pady=pads)

	row3 = Frame(root, bg=main_bg)

	b7 = Button(row3, bg=main_bg, fg=main_fg, text='7', font=("Times New Roman", 25), borderwidth=5, relief="raised", command=lambda: add("7"))
	b7.pack(side='left', fill='both', expand=True, anchor='n', padx=pads, pady=pads)

	b8 = Button(row3, bg=main_bg, fg=main_fg, text='8', font=("Times New Roman", 25), borderwidth=5, relief="raised", command=lambda: add("8"))
	b8.pack(side='left', fill='both', expand=True, anchor='n', padx=pads, pady=pads)

	b9 = Button(row3, bg=main_bg, fg=main_fg, text='9', font=("Times New Roman", 25), borderwidth=5, relief="raised", command=lambda: add("9"))
	b9.pack(side='left', fill='both', expand=True, anchor='n', padx=pads, pady=pads)

	row3.pack(fill='both', expand=True)

	row4 = Frame(root, bg=main_bg)

	bd = Button(row4, bg=main_bg, fg=main_fg, text='.', font=("Times New Roman", 25), borderwidth=5, relief="raised", command=lambda: add("."))
	bd.pack(side='left', fill='both', expand=True, anchor='n', padx=pads, pady=pads)

	b0 = Button(row4, bg=main_bg, fg=main_fg, text='0', font=("Times New Roman", 25), borderwidth=5, relief="raised", command=lambda: add("0"))
	b0.pack(side='left', fill='both', expand=True, anchor='n', padx=pads, pady=pads)
	
	bc = Button(row4, bg=main_bg, fg=main_fg, text='CE', font=("Times New Roman", 25), borderwidth=5, relief="raised", command=delete_one)
	bc.pack(side='left', fill='both', expand=True, anchor='n', padx=pads, pady=pads)

	row4.pack(fill='both', expand=True)

	root.mainloop()

if __name__ == "__main__":
	start()