from tkinter import *

def start():

	pads = 8

	root = Tk()
	root.geometry('300x300')
	root.title('Calculator')
	root.config(bg="#131320")

	wala_kaming = Label(root, text="Calculator", bg="#131320", fg='#ffffff', font=('Times New Roman', 25))
	wala_kaming.pack(fill='x')

	e = Entry(root, bg='#131320', fg='#ffffff', font=('Courier New', 25), justify='right')
	e.pack(fill='x', padx=5, pady=5)

	row1 = Frame(root, bg='#131320')

	b1 = Button(row1, bg='#131320', fg='#ffffff', text='1', width=5)
	b1.pack(side='left', padx=pads, pady=pads)

	b2 = Button(row1, bg='#131320', fg='#ffffff', text='2', width=5)
	b2.pack(side='left', padx=pads, pady=pads)

	b3 = Button(row1, bg='#131320', fg='#ffffff', text='3', width=5)
	b3.pack(side='left', padx=pads, pady=pads)

	b4 = Button(row1, bg='#131320', fg='#ffffff', text='4', width=5)
	b4.pack(side='left', padx=pads, pady=pads)

	ba = Button(row1, bg='#131320', fg='#ffffff', text='+', width=5)
	ba.pack(side='left', padx=pads, pady=pads)


	row1.pack(fill='x')
	
	row2 = Frame(root, bg='#131320')

	b5 = Button(row2, bg='#131320', fg='#ffffff', text='5', width=5)
	b5.pack(side='left', padx=pads, pady=pads)

	b6 = Button(row2, bg='#131320', fg='#ffffff', text='6', width=5)
	b6.pack(side='left', padx=pads, pady=pads)

	b7 = Button(row2, bg='#131320', fg='#ffffff', text='7', width=5)
	b7.pack(side='left', padx=pads, pady=pads)

	b8 = Button(row2, bg='#131320', fg='#ffffff', text='8', width=5)
	b8.pack(side='left', padx=pads, pady=pads)

	bs = Button(row2, bg='#131320', fg='#ffffff', text='-', width=5)
	bs.pack(side='left', padx=pads, pady=pads)

	row2.pack(fill='x')

	row3 = Frame(root, bg='#131320')

	b9 = Button(row3, bg='#131320', fg='#ffffff', text='9', width=5)
	b9.pack(side='left', padx=pads, pady=pads)

	b0 = Button(row3, bg='#131320', fg='#ffffff', text='0', width=5)
	b0.pack(side='left', padx=pads, pady=pads)

	bm = Button(row3, bg='#131320', fg='#ffffff', text='*', width=5)
	bm.pack(side='left', padx=pads, pady=pads)

	bq = Button(row3, bg='#131320', fg='#ffffff', text='/', width=5)
	bq.pack(side='left', padx=pads, pady=pads)

	be = Button(row3, bg='#131320', fg='#ffffff', text='=', width=5)
	be.pack(side='left', padx=pads, pady=pads)

	row3.pack(fill='x')

	root.mainloop()

start()