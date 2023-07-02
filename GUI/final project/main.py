from tkinter import *
from tkinter import messagebox
import menu, setup, random

def register():
	chars = "abcdefghijklmnopqrstuvwxyz0123456789"
	userID = ""
	for i in range(5):
		userID += chars[random.randint(0, len(chars) - 1)]
	
	data = setup.addTeacher(userID, user.get(), password.get())

	print(data)

	while data['exists']:
		for i in range(5):
			userID += chars[random.randint(0, len(chars) - 1)]
			data = setup.addTeacher(userID, user.get(), password.get())
	
	messagebox.showinfo("SUCCESS", f"Teacher's account created successfully. Use this id: {userID} as ID pass")

def credentials():
	global userID
	userID = None
	print(userType.get())
	if userType.get() == 'student':
		if user.get() == "":
			messagebox.showerror("ERROR", "Please enter your username first")
		elif len(password.get()) < 8:
			messagebox.showerror("ERROR", "Password must be 8 characters")
		else:
			data = setup.getTeacherId(user.get(), password.get())
			if data['done']:
				messagebox.showinfo("SUCCESS", "You're now logged in as a student.")
				userID = data['userID']
			else:
				messagebox.showerror("ERROR", "Account not found")
	else:
		if user.get() == "":
			messagebox.showerror("ERROR", "Please enter your username first")
		elif len(password.get()) < 8:
			messagebox.showerror("ERROR", "Password must be 8 characters")
		else:
			data = setup.getTeacherId(user.get(), password.get())
			if data['done']:
				messagebox.showinfo("SUCCESS", "You're now logged in as a teacher.")
				userID = data['userID']
			else:
				messagebox.showerror("ERROR", "Account not found")

def login():
	global user, password, userType
	Label(root, text="Login", font=("Times New Roman", 25), justify='center', bg=baseColor, fg=txtColor).pack(fill='x')

	userType = StringVar()
	userType.set("student")
	typeFrame = Frame(root, bg=baseColor)
	Radiobutton(typeFrame, bg=baseColor, fg=txtColor, text="Student", selectcolor=baseColor, variable=userType, textvariable="student", value='student').pack(side='left', fill='x', expand=True)
	Radiobutton(typeFrame, bg=baseColor, fg=txtColor, text="Teacher", selectcolor=baseColor, variable=userType, textvariable="teacher", value='teacher').pack(side='left', fill='x', expand=True)
	typeFrame.pack(fill='x')


	userFrame = LabelFrame(root, text="ID", font=("Times New Roman", 15), bg=baseColor, fg=txtColor)

	user = Entry(userFrame, bg=baseColor, fg=txtColor, bd=0, font=("", 15))
	user.pack(side="left", fill='x', expand=True)

	userFrame.pack(fill='x')

	passFrame = LabelFrame(root, text="Password", font=("Times New Roman", 15), bg=baseColor, fg=txtColor)

	password = Entry(passFrame, bg=baseColor, fg=txtColor, bd=0, font=("", 15), show="•")
	password.pack(side="left", fill='x', expand=True)

	passFrame.pack(fill='x')

	buttons = Frame(root, bg=baseColor)
	Button(buttons, bg=baseColor, fg=txtColor, text="Login", activebackground=baseColor, activeforeground=txtColor, command=lambda: credentials()).pack(side='left', fill='x', expand=True, pady=5)
	Button(buttons, bg=baseColor, fg=txtColor, text="Register", activebackground=baseColor, activeforeground=txtColor, command=lambda: register()).pack(side='left', fill='x', expand=True,  pady=5)
	buttons.pack(fill='x')

def start():
	global root, baseColor, txtColor
	root = Tk()
	root.geometry("500x200")
	root.title("Project Q&A")

	baseColor = "#575D5E"
	txtColor = "#ffffff"
	root.config(bg=baseColor, padx=5)

	login()

	menu.menuSetup(root)

	root.mainloop()

if __name__ == "__main__":
	setup.createExcell()
	setup.createStudents()
	setup.createTeachers()
	start()
