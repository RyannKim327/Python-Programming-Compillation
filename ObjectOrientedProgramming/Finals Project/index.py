from tkinter import *
from tkinter import ttk, messagebox
import json

class Database:
	def __init__(self):
		self.__file = "data.json"

	def getData(self):
		try:
			with open(self.__file, "r") as file:
				self.__data = json.load(file)
		except Exception as e:
			messagebox.showwarning("Warning", e) #"The database is not existed, so the system automatically generates it.")
			self.__data = {
				"data": []
			}
			with open(self.__file, "w") as file:
				file.write(json.dumps(self.__data, indent=4))
		return self.__data
	
	def deleteData(self, key: str):
		if messagebox.askyesno("Confirmation", "Are you sure you want to remove this data?"):
			self.__data.pop(key)
			messagebox.showinfo("Success", "Data Removed Successfully")
	
	def removeAllData(self):
		if messagebox.askyesno("Confirmation", "All data will never be retribed once you proceed to this action."):
			self.__data.clear()

	def saveData(self):
		with open(self.__file, "w") as file:
			file.write(json.dumps(self.__data, indent=4))
		messagebox.showinfo("Success", "The data was saved.")

class Selection(Button):
	"""This class is used for Navigation of the project"""
	def setText(self, text: str):
		self.config(text=text, bd=0, relief='solid')
		self.pack(side='top', fill='x')

	def setAction(self, action):
		self.config(command=action)

# ----------------------- Clear Current UI ---------------------- #
def cls():
	for i in layout.winfo_children():
		i.destroy()
	pass
# -------------------------------------------------------------------#

# -------------------------- Homepage -------------------------- #
def homepage():
	global nav
	cls()
	if not hasNav:
		sec.pack(side='left', anchor='n', expand=True)
		nav.pack_forget()
	title.config(text="Grade Management and Monitoring System")
# -------------------------------------------------------------------#

# ------------------------- Add Student ------------------------- #
def add_student():
	global nav
	cls()
	if not hasNav:
		sec.pack(side='left', anchor='n', expand=True)
		nav.pack_forget()
	title.config(text="Add Student")
# -------------------------------------------------------------------#

# ------------------------ Grade Student ------------------------ #
def grade_student():
	global nav
	cls()
	if not hasNav:
		sec.pack(side='left', anchor='n', expand=True)
		nav.pack_forget()
	title.config(text="Add Grade to the student")
# ------------------------------------------------------------------- #
	
# ------------------------ Navigate Me -------------------------- #
def navigateMe():
	global nav
	cls()
	nav = Frame(base, width=base.winfo_width())

	home = Selection(nav)
	home.setText("Home")
	home.setAction(lambda: homepage())

	addStudent = Selection(nav)
	addStudent.setText("Add Student")
	addStudent.setAction(lambda: add_student())

	gradeStudent = Selection(nav)
	gradeStudent.setText("Grade Student")
	gradeStudent.setAction(lambda: grade_student())

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
			nav = Frame(base, width=width * 0.15)
			hasNav = True
		if width >= 600:
			nav = Frame(base, width=width * 0.18)
			hasNav = True
		if width >= 750:
			nav = Frame(base, width=width * 0.20)
			hasNav = True
		if width >= 1000:
			nav = Frame(base, width=width * 0.25)
			hasNav = True

		home = Selection(nav)
		home.setText("Home")
		home.setAction(lambda: homepage())

		addStudent = Selection(nav)
		addStudent.setText("Add Student")
		addStudent.setAction(lambda: add_student())

		gradeStudent = Selection(nav)
		gradeStudent.setText("Grade Student")
		gradeStudent.setAction(lambda: grade_student())

		nav.pack(side='left', anchor="n", fill='y')
		nav.pack_propagate(0)

		titleSide = Frame(sec)

		back = Selection(titleSide)
		back.setText("←")
		back.setAction(lambda: navigateMe())
		back.pack_forget()
		if not hasNav:
			back.pack(side="left", anchor='w')

		title = Label(titleSide, text="Grade Management and Monitoring System", font=('Times New Roman', 20), justify='center', wraplength=titleWidth)
		title.pack(fill='x', side='left', expand=True)
		titleSide.pack(fill='x', side='top')

		layout = Frame(sec)

		layout.pack(side='top', expand=True)		
		sec.pack(side='left', anchor='n', expand=True)
# -------------------------------------------------------------------#

# ------------------------ Main Layout ------------------------- #
def main():

	# Globalizing the data
	global base, bwidth

	base = Tk()
	base.title("")
	base.geometry("300x300")
	base.minsize(300, 300)
	bwidth = base.winfo_width()

	# This is just to initiate the responsiveness of the UI
	ui(True)

	# To detect the changes of the UI
	base.bind("<Configure>", lambda e: ui(False))
	base.mainloop()
# -------------------------------------------------------------------#

if __name__ == "__main__":
	main()