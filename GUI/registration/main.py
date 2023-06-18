from tkinter import *

def regis():
	import registration
	registration.show()
	

def read():
	import showrecords
	showrecords.show()


def start():

	root = Tk()
	root.geometry("600x850")
	root.title("My Sample Project")

	Label(root, text="Welcome kapatid", justify=CENTER, font=("Times New Roman", 50)).pack(fill='x', expand=True)

	r1 = Frame(root)

	reg = Button(r1, text="Registration", font=("Times new Roman", 25), command=regis)
	reg.pack(side='left', fill='both', expand=True)
	
	sr = Button(r1, text="Show Records", font=("Times new Roman", 25), command=read)
	sr.pack(side='left', fill='both', expand=True)

	r1.pack(fill='both', expand=True)
	
	r2 = Frame(root)

	up = Button(r2, text="Update a record", font=("Times new Roman", 25))
	up.pack(side='left', fill='both', expand=True)
	
	delete = Button(r2, text="Delete a record", font=("Times new Roman", 25))
	delete.pack(side='left', fill='both', expand=True)

	r2.pack(fill='both', expand=True)

	root.mainloop()

if __name__ == "__main__":
	start()