import tkinter as tk
from tkinter import filedialog, messagebox, ttk

# --------------------- Class Modification ---------------------- #
class Tk(tk.Tk):
	def __init__(self, *args, **kwargs):
		"""A modified version of Tk from tkinter"""
		super().__init__(*args, **kwargs)
		self.config(bg="#fbfbfb")

	def setTitle(self, title: str):
		self.title(title)

class Label(tk.Label):
	def __init__(self, master, *args, **kwargs):
		"""A modified version of Label from tkinter"""
		super().__init__(master=master, *args, **kwargs)
		self.config(bg="#fbfbfb", fg="#000000")

class Frame(tk.Frame):
	def __init__(self, master, *args, **kwargs):
		"""A modified version of Frame from tkinter"""
		super().__init__(master=master, *args, **kwargs)
		self.config(bg="#fbfbfb")

class Button(tk.Button):
	def __init__(self, master, *args, **kwargs):
		"""A modified version of Button from tkinter"""
		super().__init__(master=master, *args, **kwargs)
		self.config(bg="#fbfbfb", fg="#000000")

	def setText(self, text: str):
		self.config(text=text)

	def getText(self):
		return self.get()

	def setAction(self, action):
		self.config(command=action)

class LabelFrame(tk.LabelFrame):
	def __init__(self, master, *args, **kwargs):
		"""A modified version of LabelFrame from tkinter"""
		super().__init__(master=master, *args, **kwargs)
		self.config(bg="#fbfbfb", fg="#000000")

class Entry(tk.Entry):
	def __init__(self, master, *args, **kwargs):
		"""A modified version of Entry from tkinter"""
		super().__init__(master=master, *args, **kwargs)
		self.config(bg="#fbfbfb", fg="#000000")

	def getText(self):
		return self.get()

	def setText(self, text: str):
		self.insert(0, text)

	def setVariable(self, var):
		self.config(textvariable=var)

	def setReaction(self, seq: str, function):
		self.bind(seq, function)

class Text(tk.Text):
	def __init__(self, master, *args, **kwargs):
		"""A modified version of Text from tkinter"""
		super().__init__(master, *args, **kwargs)
		self.config(bg="#fbfbfb", fg="#000000")

	def getText(self):
		return self.get("1.0", "end-1c")

	def setText(self, text: str):
		return self.insert("1.0", text)

	def setVariable(self, var):
		self.insert("1.0", var.get())

	def setReaction(self, seq: str, function):
		self.bind(seq, function)

class Selection(Button):
	"""This class is used for Navigation of the project and make it special just for this project"""
	def setText(self, text: str):
		self.config(text=text, bd=0, relief='solid')
		self.pack(side='top', fill='x')

class LabelText(LabelFrame):
	def __init__(self, master, text: str):
		"""A mixed of Text and LabelFrame for looks like material css"""
		super().__init__(master=master)
		self.config(text=text)
		self.__text = Text(self, bd=0, borderwidth=0, border=0, relief="solid", wrap='word')
		self.__text.pack(side='top', fill='both')

	def getInside(self):
		return self.__text

	def setHeight(self, height: float):
		self.__text.config(height=height)

	def getText(self):
		return self.__text.getText()

	def setText(self, text: str):
		self.__text.setText(text=text)

	def setVariable(self, var):
		self.__text.setVariable(var)

	def setReaction(self, seq: str, function):
		self.__text.setReaction(seq, function)

class LabelEntry(LabelFrame):
	def __init__(self, master, text: str):
		"""A mixed of Entry and LabelFrame for looks like material css"""
		super().__init__(master=master)
		self.config(text=text)
		self.__entry = Entry(self, bd=0, borderwidth=0, border=0)
		self.__entry.pack(side="left", fill='both', expand=True)

	def getEntry(self):
		return self.__entry

	def getText(self):
		return self.__entry.getText()

	def setText(self, text: str):
		self.__entry.setText(text)

	def setVariable(self, var):
		self.__entry.setVariable(var)

	def setReaction(self, seq: str, function):
		self.__entry.setReaction(seq, function)

class LabelEntryButton(LabelFrame):
	def __init__(self, master):
		"""A special class to get the file directory with LabelFrame and Entry and Button"""
		super().__init__(master=master)

		self.__entry = Entry(self, bd=0, borderwidth=0, border=0)
		self.__entry.pack(side='left', fill='both', expand=True)
		self.__button = Button(self)
		self.__button.pack(side='left', fill='both')

	def setTitle(self, text: str):
		self.config(text=text)

	def getEntry(self):
		return self.__entry

	def getText(self):
		return self.__entry.get()

	def setText(self, text: str):
		self.__entry.setText(text)

	def clearText(self):
		self.__entry.delete(0, tk.END)

	def setVariable(self, var):
		self.__entry.setVariable(var)

	def setButtonAction(self, action):
		self.__button.config(command=action)

	def setButtonText(self, text: str):
		self.__button.config(text=text)

	def setReaction(self, seq: str, function):
		self.__entry.setReaction(seq, function)


class LabelFile(LabelEntryButton):
	def __init__(self, master):
		"""A special class to get the file directory with LabelFrame and Entry and Button"""
		super().__init__(master=master)
		self.pdf = ("PDF", "*.pdf")
		self.docx = ("Document", "*.docx")
		self.xlsx = ("Excel", "*.xlsx")
		self.all = ("All Files", "*.*")
		self.__types = []
		self.__titleFile = ""

	def setDataType(self, fileTypes: list = [(tuple)]):
		self.__types.append(fileTypes)

	def setDialogTitle(self, title: str = ""):
		if title != "":
			self.__titleFile = title

	def getFile(self):
		def getFile():
			file = filedialog.askopenfilename(title=self.__titleFile, filetypes=self.__types)
			self.clearText()
			self.setText(file)
		if self.__titleFile == "":
			self.__titleFile = "Select File"
		self.setButtonAction(lambda: getFile())
		self.setButtonText("🗎")

class Table(ttk.Treeview):
	"""A modified version of tk.Treeview of tkinter"""
	def __init__(self, master, columns: [str], width: [int]):
		super().__init__(master=master, show='headings')
		if len(columns) > len(width):
			for i in range(len(width) - 1, len(columns)):
				width.append(width[i - 1])
		self['columns'] = columns
		for i in range(len(columns)):
			self.heading(columns[i], text=columns[i])
			self.column(columns[i], width=width[i])

	def add(self, item: tuple):
		self.insert("", index=tk.END, values=item)

	def bulk(self, items: [tuple]):
		for i in items:
			self.add(i)

	def replaceBulk(self, items: [tuple]):
		self.delete(*self.get_children())
		self.bulk(items)

	def replace(self, items: [tuple]):
		self.delete(*self.get_children())
		self.insert("", index=tk.END, values=items)

	def remove(self):
		self.delete(*self.get_children())
# ------------------------------------------------------------------- #