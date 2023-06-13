from tkinter import *

def start():

	pads = 8
	main_bg = "#131320"

	root = Tk()
	root.geometry('300x300')
	root.title('Calculator')
	root.config(bg="#131320")
	root.resizable(False, False)

	wala_kaming = Label(root, text="Calculator", bg=main_bg, fg='#ffffff', font=('Times New Roman', 25))
	wala_kaming.pack(fill='x')

	e = Entry(root, bg=main_bg, fg='#ffffff', font=('Courier New', 25), justify='right')
	e.pack(fill='x', padx=5, pady=5)

	row1 = Frame(root, bg=main_bg)

	b1 = Button(row1, bg=main_bg, fg='#ffffff', text='1', width=5)
	b1.pack(side='left', anchor='n', padx=pads, pady=pads)

	b2 = Button(row1, bg=main_bg, fg='#ffffff', text='2', width=5)
	b2.pack(side='left', anchor='n', padx=pads, pady=pads)

	b3 = Button(row1, bg=main_bg, fg='#ffffff', text='3', width=5)
	b3.pack(side='left', anchor='n', padx=pads, pady=pads)

	ba = Button(row1, bg=main_bg, fg='#ffffff', text='+', width=5)
	ba.pack(side='left', anchor='n', padx=pads, pady=pads)

	bs = Button(row1, bg=main_bg, fg='#ffffff', text='-', width=5)
	bs.pack(side='left', anchor='n', padx=pads, pady=pads)

	row1.pack(fill='x')
	
	row2 = Frame(root, bg=main_bg)

	b4 = Button(row2, bg=main_bg, fg='#ffffff', text='4', width=5)
	b4.pack(side='left', anchor='n', padx=pads, pady=pads)

	b5 = Button(row2, bg=main_bg, fg='#ffffff', text='5', width=5)
	b5.pack(side='left', anchor='n', padx=pads, pady=pads)

	b6 = Button(row2, bg=main_bg, fg='#ffffff', text='6', width=5)
	b6.pack(side='left', anchor='n', padx=pads, pady=pads)

	bm = Button(row2, bg=main_bg, fg='#ffffff', text='*', width=5)
	bm.pack(side='left', anchor='n', padx=pads, pady=pads)

	bq = Button(row2, bg=main_bg, fg='#ffffff', text='/', width=5)
	bq.pack(side='left', anchor='n', padx=pads, pady=pads)

	row2.pack(fill='x')

	be = Button(root, bg=main_bg, fg='#ffffff', text='=', width=13, height=4)
	be.pack(side='right', anchor='n', padx=pads, pady=pads)

	row3 = Frame(root, bg=main_bg)

	b7 = Button(row3, bg=main_bg, fg='#ffffff', text='7', width=5)
	b7.pack(side='left', anchor='n', padx=pads, pady=pads)

	b8 = Button(row3, bg=main_bg, fg='#ffffff', text='8', width=5)
	b8.pack(side='left', anchor='n', padx=pads, pady=pads)

	b9 = Button(row3, bg=main_bg, fg='#ffffff', text='9', width=5)
	b9.pack(side='left', anchor='n', padx=pads, pady=pads)

	row3.pack(fill='x')

	row4 = Frame(root, bg=main_bg)

	bd = Button(row4, bg=main_bg, fg='#ffffff', text='.', width=5)
	bd.pack(side='left', anchor='n', padx=pads, pady=pads)

	b0 = Button(row4, bg=main_bg, fg='#ffffff', text='0', width=5)
	b0.pack(side='left', anchor='n', padx=pads, pady=pads)
	
	bc = Button(row4, bg=main_bg, fg='#ffffff', text='CE', width=5)
	bc.pack(side='left', anchor='n', padx=pads, pady=pads)

	row4.pack(fill='x')

	root.mainloop()

start()