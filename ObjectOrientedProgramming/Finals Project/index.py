from tkinter import *
from tkinter import ttk, messagebox
import json

class Database:
	def __init__(self):
		"""This class is used to create a database which is a json file to store data from the application."""
		self.__file = "data.json"

	def getData(self):
		try:
			with open(self.__file, "r") as file:
				self.__data = json.load(file)
		except Exception as e:
			messagebox.showwarning("Warning", "The database is not existed, so the system automatically generates it.")
			self.__data = {
				"data": []
			}
			with open(self.__file, "w") as file:
				file.write(json.dumps(self.__data, indent=4))
		return self.__data

	def deleteData(self, key: str):
		if messagebox.askyesno("Confirmation", "Are you sure you want to remove this document?"):
			self.__data.pop(key)
			messagebox.showinfo("Success", "Data Removed Successfully")

	def removeAllData(self):
		if messagebox.askyesno("Confirmation", "All data will never be retribed once you proceed to this action."):
			self.__data.clear()

	def saveData(self):
		with open(self.__file, "w") as file:
			file.write(json.dumps(self.__data, indent=4))
		messagebox.showinfo("Success", "The data was saved.")

class Document(Database):
	def checkDocument(self, title: str, author: str):
		return self.__data[f"{title.lower()}_{author.lower()}"]

	def addDocument(self, title: str, author: str, content: str):
		self.__data[f"{title.lower()}_{author.lower()}"] = {
			"title": title.capitalize(),
			"author": author.capitalize(),
			"content": content
		}
		with open(self.__file, "w") as file:
			file.write(json.dumps(self.__data, indent=4))

class Selection(Button):
	"""This class is used for Navigation of the project"""
	def setText(self, text: str):
		self.config(text=text, bd=0, relief='solid')
		self.pack(side='top', fill='x')

	def setAction(self, action):
		self.config(command=action)

class Insert(LabelFrame):
	def __init__(self, master, text: str):
		super().__init__(master=master)
		self.config(text=text)
		self.__entry = Entry(self, bd=0, borderwidth=0)
		self.__entry.pack(fill='x')

	def setBackground(self, bg: str):
		self.__entry.config(bg=bg)
		self.config(bg=bg)

	def setTextColor(self, fg: str):
		self.__entry.config(fg=fg)
		self.config(fg=fg)

	def get(self):
		return self.__entry.get()

# ----------------------- Clear Current UI ---------------------- #
def cls():
	for i in layout.winfo_children():
		i.destroy()
# -------------------------------------------------------------------#

# -------------------------- Homepage -------------------------- #
def homepage():
	global nav, layout
	cls()

	if not hasNav:
		sec.pack(side='left', anchor='n', expand=True)
		nav.pack_forget()
	Label(layout, text="Test mode").pack()
	title.config(text="Document Management System")
# -------------------------------------------------------------------#

# ------------------------ Add Document ----------------------- #
def addDocument():
	global nav, layout
	cls()

	if not hasNav:
		sec.pack(side='left', anchor='n', expand=True)
		nav.pack_forget()

	title_ = Insert(layout, text="Sample")
	title_.setBackground(bg)
	title_.setTextColor(fg)
	title_.pack(side="top")
	title.config(text="New Document")
# -------------------------------------------------------------------#

# ---------------------- Check Document ---------------------- #
def checkDocument():
	global nav, layout
	cls()

	if not hasNav:
		sec.pack(side='left', anchor='n', expand=True)
		nav.pack_forget()
	title.config(text="Check Document")
# ------------------------------------------------------------------- #

# ------------------------ Navigate Me -------------------------- #
def navigateMe():
	global nav
	cls()
	nav = Frame(base, width=base.winfo_width())

	home = Selection(nav, bg=bg, fg=fg)
	home.setText("Home")
	home.setAction(lambda: homepage())

	newDocument = Selection(nav, bg=bg, fg=fg)
	newDocument.setText("New Document")
	newDocument.setAction(lambda: addDocument())

	checkDocu = Selection(nav, bg=bg, fg=fg)
	checkDocu.setText("Check Document")
	checkDocu.setAction(lambda: checkDocument())

	sec.pack_forget()
	nav.pack(anchor='n', fill='x')
# ------------------------------------------------------------------- #

# ------------------------ User Interface ------------------------ #
def ui(a):
	"""This function makes the interface more responsive"""
	global bwidth, layout, title, nav, sec, hasNav

	width = base.winfo_width()
	if bwidth != width or a:
		# The changes happens
		bwidth = width

		for i in base.winfo_children():
			i.destroy()

		sec = Frame(base, bg=bg)
		nav = Frame(base, bg=bg, width=0)
		hasNav = False

		titleWidth = width
		if width >= 500:
			nav = Frame(base, bg=bg, width=width * 0.25)
			hasNav = True

		home = Selection(nav, bg=bg, fg=fg)
		home.setText("Home")
		home.setAction(lambda: homepage())

		newDocument = Selection(nav, bg=bg, fg=fg)
		newDocument.setText("New Document")
		newDocument.setAction(lambda: addDocument())

		checkDocu = Selection(nav, bg=bg, fg=fg)
		checkDocu.setText("Check Document")
		checkDocu.setAction(lambda: checkDocument())

		nav.pack(side='left', anchor="n", fill='y')
		nav.pack_propagate(0)

		titleSide = Frame(sec, bg=bg)

		back = Selection(titleSide, bg=bg, fg=fg)
		back.setText("←")
		back.setAction(lambda: navigateMe())
		back.pack_forget()
		if not hasNav:
			back.pack(side="left", anchor='nw')

		title = Label(titleSide, text="Document Management System", bg=bg, fg=fg, font=('Times New Roman', 20), justify='left', wraplength=titleWidth * 0.9, width=base.winfo_width())
		title.pack(fill='x', side='left')
		titleSide.pack(fill='x', side='top')

		layout = Frame(sec, bg=bg)
		layout.pack(side='top', expand=True)
		homepage()
		sec.pack(side='left', anchor='n', expand=True)
# -------------------------------------------------------------------#

# ------------------------ Main Layout ------------------------- #
def main():
	# Globalizing the data
	global base, bwidth, db, bg, fg

	bg = "#fbfbfb"
	fg = "#000000"
	# Database setup for one time call
	db = Database()

	base = Tk()
	base.title("Document Management System")
	base.geometry("350x300")
	base.minsize(350, 300)
	base.config(background=bg)
	bwidth = base.winfo_width()

	# This is just to initiate the responsiveness of the UI
	ui(True)

	# To detect the changes of the UI
	base.bind("<Configure>", lambda e: ui(False))
	base.mainloop()
# -------------------------------------------------------------------#

if __name__ == "__main__":
	main()