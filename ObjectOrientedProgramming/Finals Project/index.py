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

class Input(Entry):
	def __init__(self, master, *args, **kwargs):
		super().__init__(self, master, *args, **kwargs)
		self.config(bd=0)

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

	title_ = LabelFrame(layout, text="Title")
	title__ = Input(title_)
	title__.pack()
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

		nav.pack(side='left', anchor="n", fill='y')
		nav.pack_propagate(0)

		titleSide = Frame(sec)

		back = Selection(titleSide)
		back.setText("←")
		back.setAction(lambda: navigateMe())
		back.pack_forget()
		if not hasNav:
			back.pack(side="left", anchor='nw')

		title = Label(titleSide, text="Document Management System", font=('Times New Roman', 20), justify='left', wraplength=titleWidth * 0.9, width=base.winfo_width())
		title.pack(fill='x', side='left')
		titleSide.pack(fill='x', side='top')

		layout = Frame(sec)
		layout.pack(side='top', expand=True)
		homepage()
		sec.pack(side='left', anchor='n', expand=True)
# -------------------------------------------------------------------#

# ------------------------ Main Layout ------------------------- #
def main():
	# Globalizing the data
	global base, bwidth, db

	# Database setup for one time call
	db = Database()

	base = Tk()
	base.title("")
	base.geometry("350x300")
	base.minsize(350, 300)
	bwidth = base.winfo_width()

	# This is just to initiate the responsiveness of the UI
	ui(True)

	# To detect the changes of the UI
	base.bind("<Configure>", lambda e: ui(False))
	base.mainloop()
# -------------------------------------------------------------------#

if __name__ == "__main__":
	main()