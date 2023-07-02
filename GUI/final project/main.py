from tkinter import *
from tkinter import messagebox, simpledialog, ttk
import menu, setup, random

def exitConfirmation():
	if messagebox.askyesno("CONFIRMATION", "Are you sure, you want to close the app?"):
		root.destroy()

def createQuestion():
	question_root = Toplevel()
	question_root.geometry("300x500")
	if userInfo['type'] == 'teacher':
		Label(question_root, text="Create a Question", justify='center', font=("Times New Roman", 25)).pack(fill='x', expand=True)
	else:
		pass
	
	menu.menuSetup(question_root)

	question_root.protocol("WM_DELETE_WINDOW", lambda: exitConfirmation())
	question_root.mainloop()

def register():
	chars = "abcdefghijklmnopqrstuvwxyz0123456789"
	if setup.encrypt(simpledialog.askstring("Confirmation", f"Please enter your passcode here to confirm this {userType.get()}", show="•")) == "c3782c86d8099f3fb5b755ebc970322567aa3894923de8c9c5fc97456133471c":
		userID = ""
		for i in range(5):
			userID += chars[random.randint(0, len(chars) - 1)]
		if userType.get() == 'teacher':
			data = setup.addTeacher(userID, user.get(), password.get())

			print(data)

			while data['exists']:
				for i in range(5):
					userID += chars[random.randint(0, len(chars) - 1)]
					data = setup.addTeacher(userID, user.get(), password.get())
			
			messagebox.showinfo("SUCCESS", f"Teacher's account created successfully. Use this id: {userID} as ID pass")
		else:
			data = setup.addStudent(userID, user.get(), password.get())

			while data['exists']:
				for i in range(5):
					userID += chars[random.randint(0, len(chars) - 1)]
					data = setup.addStudent(userID, user.get(), password.get())
			
			messagebox.showinfo("SUCCESS", f"Student's account created successfully. Use this id: {userID} as ID pass")

def credentials():
	global userInfo
	userID = None
	userInfo = {}
	print(userType.get())
	if userType.get() == 'student':
		if user.get() == "":
			messagebox.showerror("ERROR", "Please enter your username first")
		elif len(password.get()) < 8:
			messagebox.showerror("ERROR", "Password must be 8 characters")
		else:
			data = setup.getStudentId(user.get(), password.get())
			if data['done']:
				messagebox.showinfo("SUCCESS", "You're now logged in as a student.")
				userID = data['userID']
				userInfo = {
					"ID": userID,
					"type": userType
				}
				root.withdraw()
				createQuestion()
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
				userInfo = {
					"ID": userID,
					"type": userType
				}
				root.withdraw()
				createQuestion()
			else:
				messagebox.showerror("ERROR", "Account not found")

def destroyLists():
	global h
	if h >= 200:
		root.geometry(f"{w}x{h}")
		h -= 10
		root.after(10, destroyLists)
	else:
		listsFrame.destroy()
		sy.destroy()
		listsBtn.config(text="Lists", command=lambda: userLists())

def userLists():
	global h, listsFrame, sy
	if h < 500:
		root.geometry(f"{w}x{h}")
		h += 10
		root.after(10, userLists)
	else:
		listsFrame = Frame(root, bg=baseColor)

		tree = ttk.Treeview(listsFrame)
		sx = Scrollbar(listsFrame, orient='vertical')
		sy = Scrollbar(root, orient='horizontal')

		tree.pack(side='left', fill='both', expand=True)
		sx.pack(side='left', fill='y')
		sy.pack(side='bottom', fill='x', anchor='n')
		listsFrame.pack(side='bottom', fill='x', expand=True)
		listsBtn.config(text="Lists", command=lambda: destroyLists())

def login():
	global user, password, userType, listsBtn
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
	listsBtn = Button(buttons, bg=baseColor, fg=txtColor, text="Lists", activebackground=baseColor, activeforeground=txtColor, command=lambda: userLists())
	listsBtn.pack(side='left', fill='x', expand=True,  pady=5)
	Button(buttons, bg=baseColor, fg=txtColor, text="Register", activebackground=baseColor, activeforeground=txtColor, command=lambda: register()).pack(side='left', fill='x', expand=True,  pady=5)
	buttons.pack(fill='x')

def start():
	global root, baseColor, txtColor, w, h
	w = 500
	h = 200
	root = Tk()
	root.geometry(f"{w}x{h}")
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
