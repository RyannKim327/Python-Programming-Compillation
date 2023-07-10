from tkinter import *
from tkinter import messagebox, simpledialog, ttk
import menu, setup, random


def exitConfirmation():
	if messagebox.askyesno("CONFIRMATION", "Are you sure, you want to close the app?"):
		root.destroy()


def refreshQuestions():
	quest_lists.delete(*quest_lists.get_children())
	q = setup.getAllQuestions()
	lists = []
	x = False
	for _q in q:
		p = 0
		l = []
		for c in list(_q):
			if x:
				if p >= 3:
					t = setup.getTeacher(int(c))
					l.append(t['fullname'])
				else:
					l.append(c)
				p += 1
		if x:
			lists.append(l)
		x = True
	for _q in lists:
		quest_lists.insert("", index=END, values=_q)


def addQuestion():
	e = []
	q = que.get()
	a = ans.get()
	cs = isCaseSensitive.get()
	t = userInfo['ID']

	if q == "" or not q.endswith("?") or not q.endswith("."):
		e.append("question")
	if a == "":
		e.append("answer")
	
	if len(e) > 0:
		messagebox.showerror(f"Please fill up with the valid data: {', '.join(e)}")
	if setup.addQuestion(q, a, cs, t):
		messagebox.showinfo("SUCCESS", "New Question Added")
		refreshQuestions()


def qCloseNav():
	global qtwidth
	if qtwidth >= 0:
		qtwidth -= 0.075
		navigation.place(x=-10, y=0, relheight=1, relwidth=qtwidth)
		navigation.after(10, qCloseNav)

def qShowNav():
	global qtwidth
	if qtwidth < 0.75:
		qtwidth += 0.075
		navigation.place(x=0, y=0, relheight=1, relwidth=qtwidth)
		navigation.after(10, qShowNav)

def nav():
	global nav_show
	if nav_show:
		qCloseNav()
	else:
		qShowNav()
	nav_show = not nav_show


def createQuestion():
	global que, ans, isCaseSensitive, navigation, quest_lists, nav_show, qtwidth
	qtwidth = 0
	nav_show = False

	question_root = Toplevel(bg=baseColor, padx=5)
	question_root.geometry("500x300")
	question_root.title("Project Q&A")
	question_root.resizable(False, False)

	Label(question_root, text="Create a Question", bg=baseColor, fg=txtColor, justify='center', font=("Times New Roman", 25)).pack(fill='x')
	
	lq = LabelFrame(question_root, bg=baseColor, fg=txtColor, text="Question", font=("Times New Roman", 15))
	que = Entry(lq, bg=baseColor, fg=txtColor, font=("Times New Roman", 15), bd=0)
	que.pack(fill='x')

	lq.pack(fill='x')

	ans_frame = LabelFrame(question_root, bg=baseColor, fg=txtColor, text="Answer", font=("Times New Roman", 15))
	ans = Entry(ans_frame, bg=baseColor, fg=txtColor, font=("Times New Roman", 15), bd=0)
	ans.pack(fill='x', side='left', expand=True)

	isCaseSensitive = BooleanVar()
	isCaseSensitive.set(True)
	Checkbutton(ans_frame, bg=baseColor, fg=txtColor, font=("Times New Roman", 15), activebackground=baseColor, activeforeground=txtColor, selectcolor=baseColor, text='Is Case Sensitive?', variable=isCaseSensitive).pack(side='left')
	
	ans_frame.pack(fill='x')

	Button(question_root, bg=baseColor, fg=txtColor  , text="Add question", font=("Times New Roman", 15), command=lambda: addQuestion()).pack(fill='x', pady=5)

	# m = Menu(question_root)
	men = menu.menuSetup(question_root)
	men.add_cascade(label="Navigation", command=lambda: nav())

	navigation = Frame(question_root)

	quest_lists = ttk.Treeview(navigation, show='headings')

	columns = (
		"Question",
		"Answer",
		"Case Sensitive",
		"Question By"
	)
	w = [
		10, 10, 5, 20
	]
	x = 0
	quest_lists['columns'] = columns
	for c in columns:
		quest_lists.heading(c, text=c)
		quest_lists.column(c, width=w[x])
		x += 1
	
	refreshQuestions()

	quest_lists.pack(fill='both')
	navigation.place(x=0, y=0, relheight=1, relwidth=qtwidth)

	question_root.protocol("WM_DELETE_WINDOW", lambda: exitConfirmation())
	question_root.mainloop()


def go_answer(n, totalQ):
	global score
	q = totalQ[n]
	if q[2]:
		if s_ans.get() == q[1]:
			score += 1
	else:
		if s_ans.get().lower() == q[1].lower():
			score += 1
	s_ans.delete(0, END)
	go_ask()


def go_ask():
	global l_question, its_time
	totalQ = setup.getAllQuestions()
	n = random.randint(1, len(totalQ) - 1)
	while n in l_questions and len(l_questions) < len(totalQ) - 2:
		n = random.randint(1, len(totalQ) - 1)
	if len(l_questions) < len(totalQ) - 2:
		s_f.config(text=totalQ[n][0])
		l_questions.append(n)
		s_ans.bind("<Return>", lambda e: go_answer(n, totalQ))
	else:
		s_ans.config(state='disabled')
		its_time = 0


def go_time():
	global its_time
	if its_time > 0:
		its_time -= 1
		timer.config(text=round(its_time))
		s_root.after(1000, go_time)
	else:
		s_ans.config(state='disabled')
		messagebox.showwarning("WARNING", "Time is up")
		

def students_portal():
	global timer, its_time, s_root, s_ans, s_f, score, l_questions
	l_questions = []
	score = 0
	its_time = 60
	s_root = Toplevel(bg=baseColor)
	s_root.geometry("500x300")
	s_root.title("Project Q&A")
	s_root.resizable(False, False)

	timer = Label(s_root, bg=baseColor, fg=txtColor, font=("", 25))
	timer.pack()

	s_f = LabelFrame(s_root, bg=baseColor, fg=txtColor, font=("", 10))
	s_ans = Entry(s_f, bg=baseColor, fg=txtColor, bd=0, font=("", 15))
	s_ans.pack(fill='x')

	s_f.pack(fill='x')
	go_ask()
	go_time()

	s_root.protocol("WM_DELETE_WINDOW", exitConfirmation)
	s_root.mainloop()


def register():
	chars = "abcdefghijklmnopqrstuvwxyz0123456789"
	if setup.encrypt(simpledialog.askstring("Confirmation", f"Please enter your passcode here to confirm this {userType.get()}", show="•")) == "c3782c86d8099f3fb5b755ebc970322567aa3894923de8c9c5fc97456133471c":
		userID = ""
		for i in range(5):
			userID += chars[random.randint(0, len(chars) - 1)]
		if userType.get() == 'teacher':
			data = setup.addTeacher(userID, user.get(), password.get())
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
		setType()
	else:
		messagebox.showerror("NOTICE", "Invalid Verification")


def credentials():
	global userInfo
	userID = None
	userInfo = {}
	if userType.get() == 'student':
		if user.get().lower() == "":
			messagebox.showerror("ERROR", "Please enter your username first")
		elif len(password.get()) < 8:
			messagebox.showerror("ERROR", "Password must be 8 characters")
		else:
			data = setup.getStudentId(user.get().lower(), password.get())
			if data['done']:
				messagebox.showinfo("SUCCESS", "You're now logged in as a student.")
				userID = data['userID']
				userInfo = {
					"ID": userID,
					"type": userType
				}
				root.withdraw()
				students_portal()
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


def accounts():
	for i in tree.get_children():
		tree.delete(i)
	lists = setup.getAllUsers(_type)
	for i in lists:
		tree.insert('', index=END, values=i)


def destroyLists():
	global h, isShow
	isShow = False
	if h >= 200:
		root.geometry(f"{w}x{h}")
		h -= 10
		root.after(10, destroyLists)
	else:
		listsBtn.config(text="Lists", command=lambda: userLists())


def userLists():
	global h, isShow
	isShow = True
	if h < 500:
		root.geometry(f"{w}x{h}")
		h += 10
		root.after(10, userLists)
		setType()
	else:
		listsBtn.config(text="Lists", command=lambda: destroyLists())


def setType():
	global _type
	if isShow:
		_type = userType.get()
		accounts()


def showPassword():
	global isPass
	if isPass:
		password.config(show="")
		_bpass.config(text="•_•")
	else:
		password.config(show="•")
		_bpass.config(text="-_-")
	isPass = not isPass


def checker():
	print("Checked")
	if user.get() == "":
		user.focus()
	elif password.get() == "":
		password.focus()
	else:
		credentials()


def login():
	global user, password, userType, listsBtn, isShow, tree, _type, _bpass, isPass

	isPass = True
	isShow = False
	Label(root, text="Project Q&A", font=("Times New Roman", 25), justify='center', bg=baseColor, fg=txtColor).pack(fill='x')

	userType = StringVar()
	userType.set("student")
	typeFrame = Frame(root, bg=baseColor)
	Radiobutton(typeFrame, bg=baseColor, fg=txtColor, text="Student", selectcolor=baseColor, variable=userType, textvariable="student", value='student', command=lambda: setType()).pack(side='left', fill='x', expand=True)
	Radiobutton(typeFrame, bg=baseColor, fg=txtColor, text="Teacher", selectcolor=baseColor, variable=userType, textvariable="teacher", value='teacher', command=lambda: setType()).pack(side='left', fill='x', expand=True)
	typeFrame.pack(fill='x')

	userFrame = LabelFrame(root, text="ID", font=("Times New Roman", 15), bg=baseColor, fg=txtColor)

	user = Entry(userFrame, bg=baseColor, fg=txtColor, bd=0, font=("", 15))
	user.bind("<Return>", lambda e: checker())
	user.pack(side="left", fill='x', expand=True)

	userFrame.pack(fill='x')

	passFrame = LabelFrame(root, text="Password", font=("Times New Roman", 15), bg=baseColor, fg=txtColor)

	password = Entry(passFrame, bg=baseColor, fg=txtColor, bd=0, font=("", 15), show="•")
	password.bind("<Return>", lambda e: checker())
	password.pack(side="left", fill='x', expand=True)

	_bpass = Button(passFrame, text="-_-", command=lambda: showPassword(), bg=baseColor, fg=txtColor, bd=0)
	_bpass.pack(side='left')

	passFrame.pack(fill='x')

	buttons = Frame(root, bg=baseColor)
	Button(buttons, bg=baseColor, fg=txtColor, text="Login", activebackground=baseColor, activeforeground=txtColor, command=lambda: credentials()).pack(side='left', fill='x', expand=True, pady=5)
	listsBtn = Button(buttons, bg=baseColor, fg=txtColor, text="Lists", activebackground=baseColor, activeforeground=txtColor, command=lambda: userLists())
	listsBtn.pack(side='left', fill='x', expand=True,  pady=5)
	Button(buttons, bg=baseColor, fg=txtColor, text="Register", activebackground=baseColor, activeforeground=txtColor, command=lambda: register()).pack(side='left', fill='x', expand=True,  pady=5)
	buttons.pack(fill='x')

	listsFrame = Frame(root, bg=baseColor)

	style = ttk.Style()
	style.theme_use("clam")
	style.configure("Treeview", background=baseColor, foreground=txtColor, fieldbackground=baseColor, fieldforeground=txtColor)

	s = LabelFrame(listsFrame, text="Search your name", font=("Times New Roman", 15), bg=baseColor, fg=txtColor)

	search = Entry(s, font=("", 15), bg=baseColor, fg=txtColor, bd=0)
	search.pack(fill='x')

	s.pack(fill='x')

	tree = ttk.Treeview(listsFrame, show='headings')
	sx = Scrollbar(listsFrame, orient='vertical', command=tree.xview)
	tree.configure(xscrollcommand=sx.set)

	columns = ("ID", "Fullname")
	tree['columns'] = columns
	for i in columns:
		tree.heading(i, text=i)
		tree.column(i)

	_type = userType.get()
	accounts()

	tree.pack(side='left', fill='both', expand=True)
	sx.pack(side='left', fill='y')
	listsFrame.pack(side='top', fill='x', expand=True)


def start():
	global root, baseColor, txtColor, w, h
	w = 500
	h = 200
	root = Tk()
	root.geometry(f"{w}x{h}")
	root.title("Project Q&A")
	root.resizable(False, False)

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