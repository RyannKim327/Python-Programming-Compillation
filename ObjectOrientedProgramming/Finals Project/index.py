# from tkinter import *
from tkinter import ttk, messagebox, filedialog
import tkinter as tk
import json

# --------------------- Class Modification ---------------------- #
class Tk(tk.Tk):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.config(bg="#fbfbfb")

	def setTitle(self, title: str):
		self.title(title)

class Label(tk.Label):
	def __init__(self, master, *args, **kwargs):
		super().__init__(master=master, *args, **kwargs)
		self.config(bg="#fbfbfb", fg="#000000")

class Frame(tk.Frame):
	def __init__(self, master, *args, **kwargs):
		super().__init__(master=master, *args, **kwargs)
		self.config(bg="#fbfbfb")

class Button(tk.Button):
	def __init__(self, master, *args, **kwargs):
		super().__init__(master=master, *args, **kwargs)
		self.config(bg="#fbfbfb", fg="#000000")

class LabelFrame(tk.LabelFrame):
	def __init__(self, master, *args, **kwargs):
		super().__init__(master=master, *args, **kwargs)
		self.config(bg="#fbfbfb", fg="#000000")

class Entry(tk.Entry):
	def __init__(self, master, *args, **kwargs):
		super().__init__(master=master, *args, **kwargs)
		self.config(bg="#fbfbfb", fg="#000000")

class Text(tk.Text):
	def __init__(self, master, *args, **kwargs):
		super().__init__(master, *args, **kwargs)
		self.config(bg="#fbfbfb", fg="#000000")

class Selection(Button):
	"""This class is used for Navigation of the project"""
	def setText(self, text: str):
		self.config(text=text, bd=0, relief='solid')
		self.pack(side='top', fill='x')

	def setAction(self, action):
		self.config(command=action)

class LabelEntry(LabelFrame):
	def __init__(self, master, text: str):
		super().__init__(master=master)
		self.config(text=text)
		self.__entry = Entry(self, bd=0, borderwidth=0, border=0)
		self.__entry.pack(fill='x')

class LabelText(LabelFrame):
	def __init__(self, master, text: str):
		super().__init__(master=master)
		self.config(text=text)
		self.__text = Text(self, bd=0, borderwidth=0, border=0)
		self.__text.pack(fill='x')

	def get(self):
		return self.__text.get()

class LabelEntry(LabelFrame):
	def __init__(self, master, text: str):
		super().__init__(master=master)
		self.config(text=text)
		self.__entry = Entry(self, bd=0, borderwidth=0, border=0)
		self.__entry.pack(fill='x')

	def get(self):
		return self.__entry.get()

class LabelFile(LabelFrame):
	def __init__(self, master, text: str, fileTitle: str = "", fileTypes: list = []):
		super().__init__(master=master)
		self.__titleFile = "Select File"
		if fileTitle != "":
			self.__titleFile = fileTitle
		self.__types = fileTypes
		self.config(text=text)
		self.__entry = Entry(self, bd=0, borderwidth=0, border=0)
		self.__entry.pack(side='left', fill='x', expand=True)
		button = Button(self, text="🗎")
		button.config(command=lambda: self.getFile())
		button.pack(side='left')

	def getFile(self):
		file = filedialog.askopenfilename(title=self.__titleFile, filetypes=self.__types)
		self.__entry.delete(0, tk.END)
		self.__entry.insert(0, file)
# ------------------------------------------------------------------- #

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

	title_ = LabelEntry(layout, text="Sample")
	title_.pack(side="top", fill='x', expand=True)
	document = LabelFile(layout, text="Import file")
	document.pack(fill='x')
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

	# To detect the changes of the UI
	base.bind("<Configure>", lambda e: ui(False))
	base.mainloop()
# ------------------------------------------------------------------- #

if __name__ == "__main__":
	main()