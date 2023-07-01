from tkinter import *
from tkinter import messagebox
import menu, setup

def credentials():
	global userID
	userID = None
	if user.get() == "":
		messagebox.showerror("ERROR", "Please enter your username first")
	elif len(password.get()) < 8:
		messagebox.showerror("ERROR", "Password must be 8 characters")
	else:
		data = setup.getTeacherId(user.get(), password.get())
		if data.done:
			userID = data.userID
		else:
			messagebox.showerror("ERROR", "Account not found")

def login():
	global user, password
	Label(root, text="Login", font=("Times New Roman", 25), justify='center', bg=baseColor, fg=txtColor).pack(fill='x')

	userFrame = LabelFrame(root, text="ID", font=("Times New Roman", 15), bg=baseColor, fg=txtColor)

	user = Entry(userFrame, bg=baseColor, fg=txtColor, bd=0, font=("", 15))
	user.pack(side="left", fill='x', expand=True)

	userFrame.pack(fill='x')

	passFrame = LabelFrame(root, text="Password", font=("Times New Roman", 15), bg=baseColor, fg=txtColor)

	password = Entry(passFrame, bg=baseColor, fg=txtColor, bd=0, font=("", 15), show="•")
	password.pack(side="left", fill='x', expand=True)

	passFrame.pack(fill='x')

	Button(root, bg=baseColor, fg=txtColor, text="Login", activebackground=baseColor, activeforeground=txtColor, command=lambda: credentials()).pack(fill='x', pady=5)


def start():
	global root, baseColor, txtColor
	root = Tk()
	root.geometry("500x200")
	root.title("Elementary product")

	baseColor = "#575D5E"
	txtColor = "#ffffff"
	root.config(bg=baseColor, padx=5)

	login()

	menu.menuSetup(root)

	root.mainloop()

if __name__ == "__main__":
	setup.createExcell()
	setup.createStudents()
	start()
