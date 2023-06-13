from tkinter import *

def start():

	pads = 8

	root = Tk()
	root.geometry('300x300')
	root.title('Calculator')
	root.config(bg="#131320")

	e = Entry(root, bg='#131320', fg='#ffffff')
	e.pack(fill='x', padx=5, pady=5)

	b1 = Button(root, bg='#131320', fg='#ffffff', text='1', width=5)
	b1.pack(side='left', anchor='n', padx=pads, pady=pads)

	b2 = Button(root, bg='#131320', fg='#ffffff', text='2', width=5)
	b2.pack(fill='x', side='left', anchor='n', padx=pads, pady=pads)

	b3 = Button(root, bg='#131320', fg='#ffffff', text='3', width=5)
	b3.pack(fill='x', side='left', anchor='n', padx=pads, pady=pads)

	b4 = Button(root, bg='#131320', fg='#ffffff', text='4', width=5)
	b4.pack(fill='x', side='left', anchor='n', padx=pads, pady=pads)

	b5 = Button(root, bg='#131320', fg='#ffffff', text='5', width=5)
	b5.pack(fill='x', side='left', anchor='n', padx=pads, pady=pads)

	b6 = Button(root, bg='#131320', fg='#ffffff', text='1', width=5)
	b6.pack(fill='x', side='bottom', padx=pads, pady=pads)

	b7 = Button(root, bg='#131320', fg='#ffffff', text='2', width=5)
	b7.pack(fill='x', side='left', anchor='n', padx=pads, pady=pads)

	b8 = Button(root, bg='#131320', fg='#ffffff', text='3', width=5)
	b8.pack(fill='x', side='left', anchor='n', padx=pads, pady=pads)

	b9 = Button(root, bg='#131320', fg='#ffffff', text='4', width=5)
	b9.pack(fill='x', side='left', anchor='n', padx=pads, pady=pads)

	b0 = Button(root, bg='#131320', fg='#ffffff', text='5', width=5)
	b0.pack(fill='x', side='left', anchor='n', padx=pads, pady=pads)

	root.mainloop()

start()