from tkinter import *

def start():

	root = Tk()
	root.geometry('300x300')
	root.title('Calculator')
	root.config(bg="#131320")

	e = Entry(root, bg='#131320', fg='#ffffff')
	e.pack(fill='x', padx=5, pady=5)

	b1 = Button(root, text="1", width=5, height=2)
	b1.pack(side='left', anchor='n', padx=5, pady=5)

	b2 = Button(root, text="2", width=5, height=2)
	b2.pack(side='left', anchor='n', padx=5, pady=5)
	
	b3 = Button(root, text="3", width=5, height=2)
	b3.pack(side='left', anchor='n', padx=5, pady=5)
	
	b4 = Button(root, text="4", width=5, height=2)
	b4.pack(side='left', anchor='n', padx=5, pady=5)
	
	b5 = Button(root, text="5", width=5, height=2)
	b5.pack(side='left', anchor='n', padx=5, pady=5)

	b6 = Button(root, text="6", width=5, height=2)
	b6.pack(side='left', padx=5, pady=5)

	b7 = Button(root, text="7", width=5, height=2)
	b7.pack(side='left', padx=5, pady=5)
	
	b8 = Button(root, text="8", width=5, height=2)
	b8.pack(side='left', padx=5, pady=5)
	
	b9 = Button(root, text="9", width=5, height=2)
	b9.pack(side='left', padx=5, pady=5)
	
	b0 = Button(root, text="0", width=5, height=2)
	b0.pack(side='left', padx=5, pady=5)


	root.mainloop()

start()