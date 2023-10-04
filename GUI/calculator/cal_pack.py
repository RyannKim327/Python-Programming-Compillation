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
	
	title = Label(root, text="Calculator", bg=main_bg, fg=main_fg, font=('Times New Roman', 25))
	title.grid(row=0, column=0, columnspan=5)

	e = Entry(root, bg=main_bg, fg=main_fg, font=('Times New Roman', 35), justify='right', borderwidth=5, relief="sunken")
	e.grid(row=1, column=0, columnspan=5)

	b1 = Button(root, bg=main_bg, fg=main_fg, text='1', font=("Times New Roman", 25), borderwidth=5, relief="raised", command=lambda: add("1"))
	b1.grid(row=2, column=0)

	b2 = Button(root, bg=main_bg, fg=main_fg, text='2', font=("Times New Roman", 25), borderwidth=5, relief="raised", command=lambda: add("2"))
	b2.grid(row=2, column=1)

	b3 = Button(root, bg=main_bg, fg=main_fg, text='3', font=("Times New Roman", 25), borderwidth=5, relief="raised", command=lambda: add("3"))
	b3.grid(row=2, column=2)

	ba = Button(root, bg=main_bg, fg=main_fg, text='+', font=("Times New Roman", 25), borderwidth=5, relief="raised", command=lambda: add("+"))
	ba.grid(row=2, column=3)

	bs = Button(root, bg=main_bg, fg=main_fg, text='-', font=("Times New Roman", 25), borderwidth=5, relief="raised", command=lambda: add("-"))
	bs.grid(row=2, column=4)

	b4 = Button(root, bg=main_bg, fg=main_fg, text='4', font=("Times New Roman", 25), borderwidth=5, relief="raised", command=lambda: add("4"))
	b4.grid(row=3, column=0)

	b5 = Button(root, bg=main_bg, fg=main_fg, text='5', font=("Times New Roman", 25), borderwidth=5, relief="raised", command=lambda: add("5"))
	b5.grid(row=3, column=1)

	b6 = Button(root, bg=main_bg, fg=main_fg, text='6', font=("Times New Roman", 25), borderwidth=5, relief="raised", command=lambda: add("6"))
	b6.grid(row=3, column=2)

	bm = Button(root, bg=main_bg, fg=main_fg, text='*', font=("Times New Roman", 25), borderwidth=5, relief="raised", command=lambda: add("*"))
	bm.grid(row=3, column=3)

	bq = Button(root, bg=main_bg, fg=main_fg, text='/', font=("Times New Roman", 25), borderwidth=5, relief="raised", command=lambda: add("/"))
	bq.grid(row=3, column=4)

	be = Button(root, bg=main_bg, fg=main_fg, text='=', font=("Times New Roman", 30), borderwidth=5, relief="raised", command=sum_it_all)
	be.grid(row=4, column=4, columnspan=2, rowspan=2)

	b7 = Button(root, bg=main_bg, fg=main_fg, text='7', font=("Times New Roman", 25), borderwidth=5, relief="raised", command=lambda: add("7"))
	b7.grid(row=4, column=0)

	b8 = Button(root, bg=main_bg, fg=main_fg, text='8', font=("Times New Roman", 25), borderwidth=5, relief="raised", command=lambda: add("8"))
	b8.grid(row=4, column=1)

	b9 = Button(root, bg=main_bg, fg=main_fg, text='9', font=("Times New Roman", 25), borderwidth=5, relief="raised", command=lambda: add("9"))
	b9.grid(row=4, column=2)

	bd = Button(root, bg=main_bg, fg=main_fg, text='.', font=("Times New Roman", 25), borderwidth=5, relief="raised", command=lambda: add("."))
	bd.grid(row=5, column=0)

	b0 = Button(root, bg=main_bg, fg=main_fg, text='0', font=("Times New Roman", 25), borderwidth=5, relief="raised", command=lambda: add("0"))
	b0.grid(row=5, column=1)	
	bc = Button(root, bg=main_bg, fg=main_fg, text='CE', font=("Times New Roman", 25), borderwidth=5, relief="raised", command=delete_one)
	bc.grid(row=5, column=2)


	root.mainloop()

if __name__ == "__main__":
	start()