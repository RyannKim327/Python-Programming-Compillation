import random
from tkinter import *
from tkinter import messagebox, simpledialog, ttk
# from playsound import playsound
import menu
import setup
from toPDF import toPDF


def logout(base):
	global userInfo
	userInfo = {
		"ID": 0,
		"type": ""
	}
	base.destroy()
	root.deiconify()

def exitConfirmation():
	if messagebox.askyesno("CONFIRMATION", "Are you sure, you want to close the app?"):
		root.destroy()

def cantClose():
	messagebox.showerror("ERROR", "You can't close this window while answering")

def extractPDF(filename, sheetname, pdfname):
	res = toPDF(filename, sheetname, pdfname)
	if res['done']:
		messagebox.showinfo("SUCCESS", res['msg'])
	else:
		messagebox.showerror("ERROR", res['msg'])

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

def archieveQuestion():
	data = setup.archieveQuestions(updateQPos)
	if data['done']:
		messagebox.showinfo("SUCCESS", data['msg'])
		refreshQuestions()

def refreshArchives():
	treeArchives.delete(*treeArchives.get_children())
	q = setup.getAllArchives()
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
		treeArchives.insert("", index=END, values=_q)

def questionVerifier():
	q = que.get()
	a = ans.get()
	x = []
	if len(q) <= 5:
		x.append("Question")
	if a == "":
		x.append("Answer")

	if len(x) >= 1:
		addQuestion()
	elif "Question" in x:
		que.focus()
	elif "Answer" in x:
		ans.focus()

def addQuestion():
	e = []
	q = que.get()
	a = ans.get()
	cs = isCaseSensitive.get()
	t = userInfo['ID']

	if not (len(q) > 5 or q.endswith("?") or q.endswith(".")):
		e.append("question")
	if a == "":
		e.append("answer")

	if len(e) >= 1:
		messagebox.showerror("ERROR", f"Please fill up with the valid data: {', '.join(e)}")
	else:
		if setup.addQuestion(q, a, cs, t):
			que.delete(0, END)
			ans.delete(0, END)
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
	if qtwidth < 0.85:
		qtwidth += 0.075
		navigation.place(x=0, y=0, relheight=1, relwidth=qtwidth)
		navigation.after(10, qShowNav)

def removeStudent(treeView):
	delete = False
	stud = ""
	if len(treeView.selection()) > 0:
		i = treeView.selection()[0]
		item = treeView.item(i)['values']
		pos = 1
		for j in setup.getAllUsers("students", False):
			if item[0] == j[1]:
				delete = True
				stud = item[0]
				break
			pos += 1
		if delete:
			if messagebox.askyesno("CONFIRMATION", f"Are you sure you want to remove this {stud}?"):
				if setup.removeStudent(pos)['done']:
					messagebox.showinfo("SUCCESS", "A student was removed")
					lists = setup.leaderboard()['lists']
					treeView.delete(*treeView.get_children())
					_l = []
					for l in range(len(lists)):
						__l = []
						for _i in range(len(lists[l])):
							if _i == 1 or _i == 3:
								d = lists[l][_i]
								__l.append(d)
						_l.append(__l)

				for l in _l:
					treeView.insert("", index=END, values=l)
		else:
			messagebox.showerror("ERROR", "We can't find this student to our data")

def closeStudents(l_root):
	l_root.destroy()
	createQuestion()

def showStudents():
	l_root = Toplevel()
	l_root.geometry("300x300")
	l_root.title("Students")
	l_root.config(bg=baseColor)

	l_style = ttk.Style()
	l_style.theme_use("default")
	l_style.configure("Treeview", background=baseColor, foreground=txtColor, fieldbackground=baseColor, fieldforeground=txtColor)

	l_tree = ttk.Treeview(l_root, show="headings")
	lys = Scrollbar(l_root, orient='vertical', command=l_tree.yview, bg=baseColor)
	l_tree.config(yscrollcommand=lys.set)

	widths = [
		50,50
	]
	cols = (
		"Name",
		"Score"
	)

	l_tree['columns'] = cols
	lists = setup.leaderboard()['lists']
	something = 0
	for c in cols:
		l_tree.heading(c, text=c)
		l_tree.column(c, width=widths[something])
		something += 1

	_l = []
	for l in range(len(lists)):
		__l = []
		for i in range(len(lists[l])):
			if i == 1 or i == 3:
				d = lists[l][i]
				__l.append(d)
		_l.append(__l)

	for l in _l:
		l_tree.insert("", index=END, values=l)

	l_tree.bind("<<TreeviewSelect>>", lambda e: removeStudent(l_tree))

	l_tree.pack(side='left', fill='both', expand=True)
	lys.pack(side='left', fill='y')
	question_root.destroy()
	l_root.protocol("WM_DELETE_WINDOW", lambda: closeStudents(l_root))
	l_root.mainloop()

def nav():
	global nav_show
	if nav_show:
		qCloseNav()
		refreshQuestions()
	else:
		qShowNav()
	nav_show = not nav_show

def updateQuestionAction():
	data = setup.updateQuestion(updateQPos, (eu.get(), ea.get(), uc.get()))
	if data['done']:
		messagebox.showinfo("SUCCESS", data['msg'])
		update_r.destroy()
		refreshQuestions()

def updateQuestion():
	global eu, ea, uc, update_r
	update_r = Toplevel()
	update_r.geometry("500x300")
	update_r.title("Update Question")
	update_r.resizable(False, False)
	update_r.config(bg=baseColor)

	uq = LabelFrame(update_r, bg=baseColor, fg=txtColor, text="Question", font=("Times New Roman", 15))
	eu = Entry(uq, bg=baseColor, fg=txtColor, bd=0, font=("Times New Roman", 15), insertbackground=txtColor)
	eu.delete(0, END)
	eu.insert(0, selected[len(selected) - 1][0])
	eu.pack(fill='x')
	uq.pack(fill='x', padx=5, pady=5)

	ua = LabelFrame(update_r, bg=baseColor, fg=txtColor, text="Answer", font=("Times New Roman", 15))
	ea = Entry(ua, bg=baseColor, fg=txtColor, bd=0, font=("Times New Roman", 15), insertbackground=txtColor)
	ea.delete(0, END)
	ea.insert(0, selected[len(selected) - 1][1])
	ea.pack(side='left', fill='x', expand=True)

	uc = BooleanVar()
	uc.set(selected[len(selected) - 1][2])
	Checkbutton(ua, bg=baseColor, fg=txtColor, bd=0, font=("Times New Roman", 15), activebackground=baseColor, activeforeground=txtColor, selectcolor=baseColor, text='Is Case Sensitive?', variable=uc).pack(side='left')

	ua.pack(fill='x', padx=5, pady=5)

	Button(update_r, text='Update Question', bg=baseColor, fg=txtColor, command=lambda: updateQuestionAction()).pack(fill='x', padx=5, pady=5)

	update_r.mainloop()

def activateButtons(event):
	global selected, updateQPos
	updateQPos = 1
	selected = []
	for items in quest_lists.selection():
		item = quest_lists.item(items)
		selected.append(item['values'])
	if len(selected) > 0:
		for i in setup.getAllQuestions():
			if i[0] == selected[len(selected) - 1][0] and i[1] == selected[len(selected) - 1][1]:
				break
			updateQPos += 1
		archieve_q.config(state='active')
		update_q.config(state='active')
	else:
		archieve_q.config(state='disabled')
		update_q.config(state='disabled')

def closePDF():
	pdf_root.destroy()
	createQuestion()

def exportPDF():
	global pdf_root, question_root

	pdf_root = Toplevel(bg=baseColor)
	pdf_root.geometry("500x150")
	pdf_root.resizable(False, False)
	sheets = setup.getAllSheets()	
	name = LabelFrame(pdf_root, bg=baseColor, fg=txtColor, text="Enter PDF Name")
	file = Entry(name, font=("", 15), bg=baseColor, fg=txtColor, insertbackground=txtColor, bd=0)
	file.pack(fill='x', expand=True)
	name.pack(fill='x', expand=True)
	title = LabelFrame(pdf_root, bg=baseColor, fg=txtColor, text="Choose Data to Extract")
	sheet = StringVar()
	sheet.set(sheets[0])
	s = ttk.Style()
	s.theme_use("clam")
	s.configure("TCombobox", fieldbackground=baseColor, background=baseColor, fieldforeground=txtColor, foreground=txtColor)
	ttk.Combobox(title, font=("", 15), background=baseColor, foreground=txtColor, textvariable=sheet, values=sheets).pack(fill='x', expand=True)
	title.pack(fill='x', expand=True)

	Button(pdf_root, text="Convert now", bg=baseColor, fg=txtColor, command=lambda: extractPDF("data.xlsx", sheet.get(), file.get() + ".pdf")).pack(fill="x", expand=True)

	pdf_root.protocol("WM_DELETE_WINDOW", lambda: closePDF())
	question_root.destroy()
	pdf_root.mainloop()

def verifArchieve():
	if messagebox.askyesno("CONFIRMATION", "Are you sure you want to unarchive this question?"):
		lists = list(treeArchives.selection())
		last = len(lists) - 1
		setup.retrieveQuestion(last)

def closeArchives():
	arRoot.destroy()
	createQuestion()

def archives():
	global treeArchives, arRoot
	arRoot = Toplevel(bg=baseColor)
	arRoot.geometry("500x500")
	arRoot.title("Archives Questions")
	treeArchives = ttk.Treeview(arRoot, show="headings")
	columns = (
		"Question",
		"Answer",
		"Case Sensitive",
		"Question By"
	)
	w = [
		10, 10, 5, 20
	]	
	treeArchives['columns'] = columns
	colx = 0
	for i in columns:
		treeArchives.heading(i, text=i)
		treeArchives.column(i, width=w[colx])
		colx +=1
	
	treeArchives.bind("<<TreeviewSelect>>", lambda e: verifArchieve())
	treeArchives.pack(side='left', fill='x', expand=True)
	refreshArchives()
	question_root.destroy()
	arRoot.protocol("WM_DELETE_WINDOW", lambda: closeArchives())
	arRoot.mainloop()

def createQuestion():
	global que, ans, isCaseSensitive, navigation, quest_lists, nav_show, qtwidth, update_q, archieve_q, q_scroll, treeArchives, question_root
	qtwidth = 0
	nav_show = False

	question_root = Toplevel(bg=baseColor, padx=5)
	question_root.geometry("500x300")
	question_root.title("Project Q&A")
	question_root.resizable(False, False)

	Label(question_root, text="Create a Question", bg=baseColor, fg=txtColor, justify='center', font=("Times New Roman", 25)).pack(fill='x')

	lq = LabelFrame(question_root, bg=baseColor, fg=txtColor, text="Question", font=("Times New Roman", 15))
	que = Entry(lq, bg=baseColor, fg=txtColor, font=("Times New Roman", 15), bd=0, insertbackground=txtColor)
	que.bind("<Return>", lambda e: questionVerifier())
	que.pack(fill='x', ipadx=10)

	lq.pack(fill='x', pady=3)

	ans_frame = LabelFrame(question_root, bg=baseColor, fg=txtColor, text="Answer", font=("Times New Roman", 15))
	ans = Entry(ans_frame, bg=baseColor, fg=txtColor, font=("Times New Roman", 15), bd=0, insertbackground=txtColor)
	ans.bind("<Return>", lambda e: questionVerifier())
	ans.pack(fill='x', side='left', expand=True)

	isCaseSensitive = BooleanVar()
	isCaseSensitive.set(True)
	Checkbutton(ans_frame, bg=baseColor, fg=txtColor, font=("Times New Roman", 15), activebackground=baseColor, activeforeground=txtColor, selectcolor=baseColor, text='Is Case Sensitive?', variable=isCaseSensitive).pack(side='left')

	ans_frame.pack(fill='x', pady=3)

	Button(question_root, bg=baseColor, fg=txtColor, text="Add question", font=("Times New Roman", 15), command=lambda: addQuestion()).pack(fill='x', pady=5)

	men = menu.menuSetup(question_root)
	totalQ = len(setup.getAllQuestions())
	totalArcs = len(setup.getAllArchives())
	menus = Menu(men, tearoff=False, background=baseColor, foreground=txtColor)
	menus.add_command(label=f"Questions ({totalQ - 1})", command=lambda: nav())
	menus.add_command(label=f"Show Archives ({totalArcs - 1})", command=lambda: archives())
	menus.add_command(label=f"Save as PDF File", command=lambda: exportPDF())
	menus.add_command(label="Students", command=lambda: showStudents())
	menus.add_command(label="Logout", command=lambda: logout(question_root))
	men.add_cascade(label="Actions", menu=menus)

	navigation = Frame(question_root, bg=baseColor, bd=0, highlightcolor=txtColor, highlightthickness=3)

	q_base = Frame(navigation, bg=baseColor)

	quest_lists = ttk.Treeview(q_base, show='headings')
	q_scroll = Scrollbar(q_base, orient='vertical', command=quest_lists.yview)
	quest_lists.configure(yscrollcommand=q_scroll.set)

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

	quest_lists.bind("<<TreeviewSelect>>", activateButtons)

	quest_lists.pack(side='left', fill='both', expand=True)
	q_scroll.pack(side='left', fill='y')

	buttons = Frame(navigation, bg=baseColor)

	update_q = Button(buttons, bg=baseColor, fg=txtColor, activebackground=baseColor, activeforeground=txtColor, disabledforeground=txtColor, text="Update", state='disabled', command=updateQuestion)
	update_q.pack(side='left', fill='x', expand=True)
	archieve_q = Button(buttons, bg=baseColor, fg=txtColor, activebackground=baseColor, activeforeground=txtColor, disabledforeground=txtColor,  text="Archieve", state='disabled', command=archieveQuestion)
	archieve_q.pack(side='left', fill='x', expand=True)

	q_base.pack(side='top', fill='both', expand=True)
	buttons.pack(side='top', fill='x')

	question_root.protocol("WM_DELETE_WINDOW", lambda: exitConfirmation())
	question_root.mainloop()

def go_answer(n, totalQ):
	global score
	q = totalQ[n]
	if q[2]:
		if s_ans.get() == q[1]:
			score += 1
		elif s_ans.get().lower() == q[1].lower():
			score += 0.5
	else:
		if s_ans.get().lower() == q[1].lower():
			score += 1
	s_ans.delete(0, END)
	go_ask()

def go_ask():
	global l_question, its_time, question_starts
	s_ans.focus()
	totalQ = setup.getAllQuestions()
	n = random.randint(1, len(totalQ) - 1)
	while n in l_questions and len(l_questions) < len(totalQ) - 2:
		n = random.randint(1, len(totalQ) - 1)
	if len(l_questions) < len(totalQ) - 2:
		s_f.config(text=totalQ[n][0])
		l_questions.append(n)
		s_ans.bind("<Return>", lambda e: go_answer(n, totalQ))
		if not question_starts:
			go_time()
			question_starts = True
	else:
		s_ans.config(state='disabled')
		its_time = 0

def go_time():
	global its_time
	if its_time > 0:
		its_time -= 1
		timer.config(text=round(its_time))
		s_root.after(1000, go_time)
	elif its_time == 0:
		timer.config(text="Time's up!!!")
		s_ans.config(state='disabled')
		setup.updateScore(userInfo['ID'], score)
		its_time -= 1
		s_root.after(10, go_time)
	else:
		# try:
		# 	playsound("gover.mp3")
		# except:
		# 	pass
		logout(s_root)
		accounts()

def students_portal():
	global timer, its_time, s_root, s_ans, s_f, score, l_questions, question_starts
	question_starts = False
	l_questions = []
	score = 0
	its_time = 60
	s_root = Toplevel(bg=baseColor)
	s_root.geometry("500x300")
	s_root.title("Project Q&A")
	s_root.resizable(False, False)
	s_root.grab_set()
	s_root.focus_force()
	s_root.grab_release()

	timer = Label(s_root, bg=baseColor, fg=txtColor, font=("", 25))
	timer.pack()

	s_f = LabelFrame(s_root, bg=baseColor, fg=txtColor, font=("", 10), relief='solid')
	s_ans = Entry(s_f, bg=baseColor, fg=txtColor, bd=0, font=("", 15), justify='center', insertbackground=txtColor)
	s_ans.pack(fill='x')

	s_f.pack(fill='x')
	go_ask()

	s_root.protocol("WM_DELETE_WINDOW", cantClose)
	s_root.mainloop()

def register():
	chars = "abcdefghijklmnopqrstuvwxyz0123456789"
	if len(password.get()) >= 8:
		if setup.encrypt(simpledialog.askstring("CONFIRMATION", f"Please enter your passcode here to confirm this {userType.get()}", show="•")) == adminMasterKey:
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
			messagebox.showwarning("NOTICE", "Invalid Verification")
	else:
		messagebox.showwarning("NOTICE", "Password must least 8 characters")

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
					"pos": data['pos'],
					"type": userType
				}
				root.withdraw()
				user.delete(0, END)
				password.delete(0, END)
				students_portal()
			else:
				messagebox.showerror("ERROR", "Account not found")
	else:
		if user.get() == "":
			messagebox.showerror("ERROR", "Please enter your username first")
			user.delete(0, END)
			password.delete(0, END)
		elif len(password.get()) < 8:
			messagebox.showerror("ERROR", "Password must be 8 characters")
			user.delete(0, END)
			password.delete(0, END)
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
				user.delete(0, END)
				password.delete(0, END)
				createQuestion()
			else:
				messagebox.showerror("ERROR", "Account not found")
				user.delete(0, END)
				password.delete(0, END)

def accounts():
	tree.delete(*tree.get_children())
	lists = setup.getAllUsers(_type)
	for i in lists:
		tree.insert('', index=END, values=i)

def destroyLists():
	global h, isShow
	isShow = False
	if h >= 225:
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
		_bpass.config(text="•_-")
	isPass = not isPass

def checker():
	if user.get() == "":
		user.focus()
	elif password.get() == "":
		password.focus()
	else:
		credentials()

def searchUser():
	utype = userType.get()
	data = setup.getAllUsers(utype)
	lists = []
	for i in data:
		if search.get().lower() in i[1].lower() or search.get().lower() in i[0].lower():
			lists.append(i)

	tree.delete(*tree.get_children())
	for i in lists:
		tree.insert("", index=END, values=i)

def inserAsID():
	user.delete(0, END)
	lists = []
	for i in tree.selection():
		item = tree.item(i)
		lists.append(item['values'][0])
		password.focus()
	if len(lists) > 0:
		user.insert(0, lists[len(lists) - 1])

def login():
	global user, password, userType, listsBtn, isShow, tree, _type, _bpass, isPass, search
	isPass = True
	isShow = False
	Label(root, text="Project Q&A", font=("Times New Roman", 25), justify='center', bg=baseColor, fg=txtColor).pack(fill='x')

	userType = StringVar()
	userType.set("student")
	typeFrame = Frame(root, bg=baseColor)
	Radiobutton(typeFrame, bg=baseColor, fg=txtColor, text="Student", selectcolor=baseColor, variable=userType, textvariable="student", value='student', command=lambda: setType()).pack(side='left', fill='x', expand=True)
	Radiobutton(typeFrame, bg=baseColor, fg=txtColor, text="Teacher", selectcolor=baseColor, variable=userType, textvariable="teacher", value='teacher', command=lambda: setType()).pack(side='left', fill='x', expand=True)
	typeFrame.pack(fill='x')

	userFrame = LabelFrame(root, text="ID to login | Fullname to register", font=("Times New Roman", 15), bg=baseColor, fg=txtColor)

	user = Entry(userFrame, bg=baseColor, fg=txtColor, bd=0, font=("", 15), insertbackground=txtColor)
	user.bind("<Return>", lambda e: checker())
	user.focus()
	user.pack(side="left", fill='x', expand=True)

	userFrame.pack(fill='x', pady=3)

	passFrame = LabelFrame(root, text="Password", font=("Times New Roman", 15), bg=baseColor, fg=txtColor)

	password = Entry(passFrame, bg=baseColor, fg=txtColor, bd=0, font=("", 15), show="•", insertbackground=txtColor)
	password.bind("<Return>", lambda e: checker())
	password.pack(side="left", fill='x', expand=True)

	_bpass = Button(passFrame, text="•_-", command=lambda: showPassword(), bg=baseColor, fg=txtColor, bd=0)
	_bpass.pack(side='left')

	passFrame.pack(fill='x', pady=3)

	buttons = Frame(root, bg=baseColor)
	Button(buttons, bg=baseColor, fg=txtColor, text="Login", bd=1, relief="raised", activebackground=baseColor, activeforeground=txtColor, command=lambda: credentials()).pack(side='left', fill='x', expand=True, padx=5, pady=5)
	listsBtn = Button(buttons, bg=baseColor, fg=txtColor, text="Lists", bd=1, relief="raised", activebackground=baseColor, activeforeground=txtColor, command=lambda: userLists())
	listsBtn.pack(side='left', fill='x', expand=True, padx=5, pady=5)
	Button(buttons, bg=baseColor, fg=txtColor, text="Register", bd=1, relief="raised", activebackground=baseColor, activeforeground=txtColor, command=lambda: register()).pack(side='left', fill='x', expand=True, padx=5, pady=5)
	buttons.pack(fill='x')

	listsFrame = Frame(root, bg=baseColor)

	style = ttk.Style()
	style.theme_use("default")
	style.configure("Treeview", background=baseColor, foreground=txtColor, fieldbackground=baseColor, fieldforeground=txtColor)
	style.configure("Menu", background=baseColor, foreground=txtColor, fieldbackground=baseColor, fieldforeground=txtColor)
	style.configure("Treeview.Heading", background=baseColor, foreground=txtColor, fieldbackground=baseColor, fieldforeground=txtColor)

	s = LabelFrame(listsFrame, text="Search your name", font=("Times New Roman", 15), bg=baseColor, fg=txtColor)

	search = Entry(s, font=("", 15), bg=baseColor, fg=txtColor, bd=0, insertbackground=txtColor)
	search.bind("<Return>", lambda e: searchUser())
	search.pack(fill='x')

	s.pack(fill='x')

	tree = ttk.Treeview(listsFrame, show='headings')
	sx = Scrollbar(listsFrame, orient='vertical', command=tree.xview)
	tree.configure(xscrollcommand=sx.set)

	columns = ("ID", "Fullname", "Score")
	tree['columns'] = columns
	widths = [
		10, 50, 10
	]
	w = 0
	for i in columns:
		tree.heading(i, text=i)
		tree.column(i, width=widths[w])
		w += 1

	_type = userType.get()
	accounts()

	tree.bind("<<TreeviewSelect>>", lambda e: inserAsID())
	tree.pack(side='left', fill='both', expand=True)
	sx.pack(side='left', fill='y')
	listsFrame.pack(side='top', fill='x', expand=True, pady=5)

def teacherRemoveConfirmation(id):
	t_lists = []
	for i in setup.getAllUsers("teacher"):
		t_lists.append(i[0])
	print(t_lists)
	if id in t_lists:
		pos = 1
		for i in t_lists:
			if i == id:
				break
			pos += 1
		setup.removeTeacher(pos)
	else:
		messagebox.showerror("ERROR", "Teacher not found")

def removeTeacher():
	ask =simpledialog.askstring("Verification", "Enter the master's password: ")
	if ask:
		if setup.encrypt(ask) == adminMasterKey:
			admin_root = Toplevel(bg =baseColor)
			admin_root.geometry("500x150")
			frame = LabelFrame(admin_root, font=("", 15), bg=baseColor, fg=txtColor, text="Enter teacher's ID")
			t_id = Entry(frame, font=("", 15), bg=baseColor, fg=txtColor, bd=0, insertbackground=txtColor)
			t_id.pack(fill='x', expand=True)
			t_id.bind("<Return>", lambda e: teacherRemoveConfirmation(t_id.get()))
			frame.pack(fill='x', expand=True)
			admin_root.mainloop()
		else:
			messagebox.showwarning("DENIED", "You're not allowed here")

def start():
	global root, w, h, adminMasterKey
	adminMasterKey = "c3782c86d8099f3fb5b755ebc970322567aa3894923de8c9c5fc97456133471c"
	w = 500
	h = 225
	root = Tk()
	root.geometry(f"{w}x{h}")
	root.title("Project Q&A")
	root.resizable(False, False)
	root.config(bg=baseColor, padx=5)

	login()

	men = menu.menuSetup(root)
	men.add_command(label="Remove teacher", command=lambda: removeTeacher())

	root.mainloop()

def setTheme(theme='light'):
	global  baseColor, txtColor
	if theme == DARK:
		baseColor = "#16161d"
		txtColor = "#ffffff"
	else:
		baseColor = "#9DE0F5"
		txtColor = "#004A8A"

def change(load_root):
	load_root.destroy()
	start()

def loading():
	load_root = Tk()
	load_root.geometry("300x150")
	load_root.config(bg=baseColor)
	load_root.eval("tk::PlaceWindow . center")
	load_root.overrideredirect(True)

	Label(load_root, text="Developed by",  bg=baseColor, fg=txtColor, font=("Times New Roman", 25)).pack(fill='x')
	Label(load_root, text="Ryann Kim Sesgundo", bg=baseColor, fg=txtColor, font=("Times New Roman", 15)).pack(fill='x')

	f = LabelFrame(load_root, text="Please Wait", bg=baseColor, fg=txtColor)

	progress = ttk.Progressbar(f, orient='horizontal', maximum=101, mode="determinate")
	progress.pack(fill='x', expand=True)

	def loadit(i=0):
		if i < 100:
			x =  (random.randint(0, 10))
			if x + i > 90:
				x = (100 -  i) 
			progress.step(x)
			i += x
			load_root.after(random.randint(0, 1000), lambda: loadit(i))
		else:
			change(load_root)
	
	loadit()

	f.pack(fill='x', expand=True)
	load_root.config(padx=5, pady=5)
	load_root.mainloop()

if __name__ == "__main__":
	DARK = 'dark'
	LIGHT = 'light'
	setup.createExcell()
	setup.createStudents()
	setup.createTeachers()
	setTheme(DARK)
	loading()