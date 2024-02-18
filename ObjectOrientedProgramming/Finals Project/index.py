# from tkinter import *
from tkinter import ttk, messagebox, filedialog
from myTkinter import *
from data import *

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

	Label(layout, text="Test mode").pack()
	title.config(text="Document Management System")
# ------------------------------------------------------------------- #

# ------------------------ Add Document ----------------------- #
def addDocument():
	global nav, layout, window
	cls()
	window = "add"

	if not hasNav:
		sec.pack(side='left', anchor='n', expand=True, pady=3, padx=3)
		nav.pack_forget()

	def changeContent():
		print("test")
		reader = PDFExtractor(document.getText())
		content.getInside().insert(tk.END, reader)

	title_ = LabelEntry(layout, text="Sample")
	title_.pack(side="top", fill='x', expand=True)
	document = LabelFile(layout, text="Import file")
	document.pack(fill='x')
	document.getEntry().bind("<Return>", lambda e: changeContent())
	content = LabelText(layout, text="Sample2")
	content.pack()
	title.config(text="New Document")
# ------------------------------------------------------------------- #

# ---------------------- Check Document ---------------------- #
def checkDocument():
	global nav, layout, window
	cls()
	window = "check"

	if not hasNav:
		sec.pack(side='left', anchor='n', expand=True, pady=3, padx=3)
		nav.pack_forget()
	title.config(text="Check Document")
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
	global bwidth, layout, title, nav, sec, hasNav, window

	# UI Detection
	width = base.winfo_width()
	if bwidth != width or a:

		# The changes happens
		bwidth = width

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
		layout.pack(side='top', expand=True, pady=3, padx=3)

		sec.pack(side='left', anchor='n', expand=True, pady=3, padx=3)

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
	global base, bwidth, db, window
	window = "home"

	# Database setup for one time call
	db = Database()

	base = Tk()
	base.setTitle("Document Management System")
	base.geometry("350x300")
	base.minsize(350, 300)
	bwidth = base.winfo_width()

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