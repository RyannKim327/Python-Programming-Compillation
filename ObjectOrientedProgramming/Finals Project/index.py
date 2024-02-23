# from tkinter import *
from tkinter import messagebox, StringVar
from myTkinter import *
from data import *
import os

# ----------------------- Clear Current UI ---------------------- #
def cls():
	for i in layout.winfo_children():
		i.destroy()
# ------------------------------------------------------------------- #

# -------------------------- Homepage -------------------------- #
def homepage():
	global nav, layout, window
	cls()
	window = "home"

	if not hasNav:
		sec.pack(side='left', anchor='n', expand=True, pady=3, padx=3)
		nav.pack_forget()

	Label(layout, text="This is Document Manage System, a simple GUI Project developed to store documents from PDF to normal text/raw information. This may help you to check whether the data you gathered is already published by someone or not.", justify='center', wraplength=bwidth * 0.65).pack()
	title.config(text="Document Management System")
# ------------------------------------------------------------------- #

# ------------------------ Add Document ----------------------- #
def addDocument():
	global nav, layout, window, content, db
	global strTitle, strAuthor, strContent, strFile

	cls()
	window = "add"

	if not hasNav:
		sec.pack(side='left', anchor='n', expand=True, pady=3, padx=3)
		nav.pack_forget()

	def changeContent():
		global content
		if content.getText() == "":
			print("title")
			reader = PDFExtractor(document.getText())
			content.setText(reader)

	def saveData():
		global db
		error = []
		if title_.getText() == "":
			error.append("No title")
		if author_.getText() == "":
			error.append("No author")
		if content.getText() == "" and not os.path.exists(document.getText()):
			error.append("No content")

		if len(error) > 0:
			messagebox.showerror("Empty Requirements", ", ".join(error))
		else:
			_data = content.getText()
			if os.path.exists(document.getText()):
				result = PDFExtractor(document.getText())
				_data = str(result)
			db.addDocument(title_.getText(), author_.getText(), _data)
			db.saveData()

	def changedTitle(*args):
		try:
			newTitle = title_.getText()
			strTitle.set(newTitle)
		except:
			pass

	def changedFile(*args):
		try:
			newFile = document.getText()
			strFile.set(newFile)
		except:
			pass

	def changedContent():
		try:
			newContent = content.getText()
			strContent.set(newContent)
		except:
			pass

	def changedAuthor(*args):
		try:
			newAuthor = author_.getText()
			strAuthor.set(newAuthor)
		except:
			pass

	strTitle.trace_add("write", changedTitle)
	strFile.trace_add("write", changedFile)
	strAuthor.trace_add("write", changedAuthor)

	title_ = LabelEntry(layout, text="Title")
	title_.setVariable(strTitle)
	title_.pack(side="top", fill='x')

	author_ = LabelEntry(layout, text="Author")
	author_.setVariable(strAuthor)
	author_.pack(side="top", fill='x')

	document = LabelFile(layout)
	document.setTitle("Import file")
	document.setVariable(strFile)
	document.pack(side="top", fill='x')

	content = LabelText(layout, text="Content")
	content.setText(strContent.get())
	content.setVariable(strContent)
	content.setReaction("<KeyRelease>", lambda e: changedContent())
	print(base.winfo_height() * (layout.winfo_height() * 0.015))
	content.setHeight(base.winfo_height() * (layout.winfo_height() * 0.015))
	content.pack(side="top", fill='both', expand=True)

	save = Button(layout)
	save.setText("Save")
	save.setAction(lambda: saveData())
	save.pack(side='top', fill='both', pady=3)

	title.config(text="New Document")
# ------------------------------------------------------------------- #

# ---------------------- Check Document ---------------------- #
def checkDocument():
	global nav, layout, window, strSearch
	cls()
	window = "check"

	if not hasNav:
		sec.pack(side='left', anchor='n', expand=True, pady=3, padx=3)
		nav.pack_forget()

	def searchEvent():
		global strSearch
		tree.remove()
		docu = db.getDocument(search.getText())
		if len(docu) > 0:
			for j in docu:
				tree.add((i.capitalize(), j['author'], j['content']))
		else:
			messagebox.showwarning("WARNING", "No data found.")

	def changedSearch(*args):
		global strSearch
		try:
			newSearch = search.getText()
			strSearch.set(newSearch)
		except:
			pass

	search = LabelEntry(layout, text="Search")
	search.setVariable(strSearch)

	strAuthor.trace_add("write", changedSearch)

	search.getEntry().bind("<Return>", lambda e: searchEvent())
	search.pack(side="top", fill='x')

	tree = Table(layout, ["Title", "Author", "Content"], [33])
	if len(db.getAllTitles()) > 0:
		for i in db.getAllTitles():
			docu = db.getDocument(i)
			for j in docu:
				content = j['content']
				if len(content) > 15:
					content = f"{j['content'][:15]}..."
				tree.add((i.capitalize(), j['author'], content))
	tree.pack(side="top", fill='both', expand=True)
# ------------------------------------------------------------------- #

# ------------------------ Navigate Me -------------------------- #
def navigateMe():
	global nav
	cls()
	nav = Frame(base, width=base.winfo_width())

	home = Selection(nav)
	home.setText("Home")
	home.setAction(lambda: homepage())

	newDocument = Selection(nav)
	newDocument.setText("New Document")
	newDocument.setAction(lambda: addDocument())

	checkDocu = Selection(nav)
	checkDocu.setText("Check Document")
	checkDocu.setAction(lambda: checkDocument())

	sec.pack_forget()
	nav.pack(anchor='n', fill='x', pady=3, padx=3)
# ------------------------------------------------------------------- #

# ------------------------ User Interface ------------------------ #
def ui(a):
	"""This function makes the interface more responsive"""
	global bwidth, bheight, layout, title, nav, sec, hasNav, window

	# UI Detection
	width = base.winfo_width()
	height = base.winfo_height()
	if bwidth != width or a or bheight != height:

		# The changes happens
		bwidth = width
		bheight = height

		for i in base.winfo_children():
			i.destroy()

		sec = Frame(base)
		nav = Frame(base, width=0)
		hasNav = False

		titleWidth = width
		if width >= 500:
			nav = Frame(base, width=width * 0.25)
			hasNav = True

		home = Selection(nav)
		home.setText("Home")
		home.setAction(lambda: homepage())

		newDocument = Selection(nav)
		newDocument.setText("New Document")
		newDocument.setAction(lambda: addDocument())

		checkDocu = Selection(nav)
		checkDocu.setText("Check Document")
		checkDocu.setAction(lambda: checkDocument())

		nav.pack(side='left', anchor="n", fill='y', pady=3, padx=3)
		nav.pack_propagate(0)

		titleSide = Frame(sec)

		back = Selection(titleSide)
		back.setText("←")
		back.setAction(lambda: navigateMe())
		back.pack_forget()
		if not hasNav:
			back.pack(side="left", anchor='nw', pady=3, padx=3)

		title = Label(titleSide, text="Document Management System", font=('Times New Roman', 20), justify='left', wraplength=titleWidth * 0.9, width=base.winfo_width())
		title.pack(fill='x', side='left')
		titleSide.pack(fill='x', side='top')

		layout = Frame(sec)
		layout.pack(side='top', fill="both", expand=True, pady=3, padx=3)

		sec.pack(side='left', fill='both', anchor='n', expand=True, pady=3, padx=3)

		match window:
			case "home":
				homepage()
			case "add":
				addDocument()
			case "check":
				checkDocument()
# ------------------------------------------------------------------- #

# ------------------------ Main Layout ------------------------- #
def main():
	# Globalizing the data
	global base, bwidth, bheight, db, window
	global strTitle, strAuthor, strContent, strFile, strSearch
	window = "home"

	# Database setup for one time call
	db = Document()

	base = Tk()
	base.setTitle("Document Management System")
	base.geometry("350x300")
	base.minsize(350, 300)
	bwidth = base.winfo_width()
	bheight = base.winfo_height()

	strTitle = StringVar(base)
	strAuthor = StringVar(base)
	strContent = StringVar(base)
	strFile = StringVar(base)
	strSearch = StringVar(base)

	# This is just to initiate the responsiveness of the UI
	ui(True)
	
	def closeWindow():
		if messagebox.askyesno("Confirmation", "Are you sure you want to close this application?"):
			base.destroy()

	# To detect the changes of the UI
	base.bind("<Configure>", lambda e: ui(False))
	base.protocol("WM_DELETE_WINDOW", lambda: closeWindow())
	base.mainloop()
# ------------------------------------------------------------------- #

if __name__ == "__main__":
	main()