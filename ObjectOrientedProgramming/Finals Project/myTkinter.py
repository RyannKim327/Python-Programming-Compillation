import tkinter as tk
from tkinter import filedialog, messagebox

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