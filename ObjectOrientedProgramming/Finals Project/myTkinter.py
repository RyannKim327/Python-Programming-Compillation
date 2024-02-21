import tkinter as tk
from tkinter import filedialog, messagebox

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

class Text(tk.Text):
	def __init__(self, master, *args, **kwargs):
		"""A modified version of Text from tkinter"""
		super().__init__(master, *args, **kwargs)
		self.config(bg="#fbfbfb", fg="#000000")

	def getText(self):
		return self.get("1.0", "end-1c")

	def setText(self, text: str):
		return self.insert("1.0", text)

	# def setVariable(self, var):
	# 	self.config(variable=var)

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
		self.__text = Text(self, bd=0, borderwidth=0, border=0, relief="solid")
		self.__text.pack(side="left", fill='x', expand=True)

	def getInside(self):
		return self.__text

	def setHeight(self, height: float):
		self.__text.config(height=height)

	def getText(self):
		return self.__text.getText()

	def setText(self, text: str):
		self.__text.setText(text=text)

	# def setVariable(self, var):
	# 	self.__text.setVariable(var)

class LabelEntry(LabelFrame):
	def __init__(self, master, text: str):
		"""A mixed of Entry and LabelFrame for looks like material css"""
		super().__init__(master=master)
		self.config(text=text)
		self.__entry = Entry(self, bd=0, borderwidth=0, border=0)
		self.__entry.pack(side="left", fill='x', expand=True)

	def getEntry(self):
		return self.__entry

	def getText(self):
		return self.__entry.getText()

	def setText(self, text: str):
		self.__entry.setText(text)

	def setVariable(self, var):
		self.__entry.setVariable(var)

class LabelFile(LabelFrame):
	def __init__(self, master, text: str, fileTitle: str = "", fileTypes: list = []):
		"""A special class to get the file directory with LabelFrame and Entry and Button"""
		super().__init__(master=master)

		def getFile():
			file = filedialog.askopenfilename(title=self.__titleFile, filetypes=self.__types)
			self.__entry.delete(0, tk.END)
			self.__entry.insert(0, file)

		self.__titleFile = "Select File"
		if fileTitle != "":
			self.__titleFile = fileTitle
		self.__types = fileTypes
		self.config(text=text)
		self.__entry = Entry(self, bd=0, borderwidth=0, border=0)
		self.__entry.pack(side='left', fill='both', expand=True)
		self.__button = Button(self, text="🗎")
		self.__button.config(command=lambda: getFile())
		self.__button.pack(side='left')

	def getEntry(self):
		return self.__entry

	def getText(self):
		return self.__entry.get()

	def setText(self, text: str):
		self.__entry.setText(text)

	def setVariable(self, var):
		self.__entry.setVariable(var)
# ------------------------------------------------------------------- #