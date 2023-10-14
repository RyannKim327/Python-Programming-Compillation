from tkinter import *
from tkinter import messagebox

def login():
	if usr.get() == "user" and password.get() == "admin":
		messagebox.showinfo("Done", "Done")
	else:
		messagebox.showerror("Error", "Error")

def showpass():
	global _show
	if _show:
		password.config(show="•")
		_show = False
	else:
		password.config(show="")
		_show = True

def start():
	global usr, password, _show
	
	_show = True
	root = Tk()
	root.geometry("300x100")

	Label(root, text="Username:\t", font=("Arial", 13)).grid(row=0, column=0)
	Label(root, text="Password:\t", font=("Arial", 13)).grid(row=1, column=0)

	usr = Entry(root, font=("Arial", 13))
	usr.grid(row=0, column=1)

	password = Entry(root, font=("Arial", 13), show="•")
	password.grid(row=1, column=1)

	_login = Button(root, text="Login", command=lambda:login())
	_login.grid(row=2, column=0, columnspan=2)

	Button(root, text="Show password", command=lambda:showpass()).grid(row=3, column=0, columnspan=2)

	root.mainloop()


if __name__ == "__main__":
	start()