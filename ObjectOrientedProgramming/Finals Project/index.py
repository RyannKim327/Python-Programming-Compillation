from tkinter import *

class Selection(Button):
	"""This class is used for Navigation of the project"""
	def setText(self, text: str):
		self.config(text=text)
		self.pack(side='top', fill='x')
	
	def setAction(self, action):
		self.config(command=action)

# ----------------------- Clear Current UI ---------------------- #
def cls():
	pass
# -------------------------------------------------------------------#

# -------------------------- Homepage -------------------------- #
def homepage():
	pass
# -------------------------------------------------------------------#

# ------------------------- Add Student ------------------------- #
def add_student():
	pass
# -------------------------------------------------------------------#

# ------------------------ Grade Student ------------------------ #
def grade_student():
	pass
# -------------------------------------------------------------------#

# ------------------------ User Interface ------------------------ #
def ui(a):
	"""This function makes the interface more responsive"""

	global bwidth, layout, title

	width = base.winfo_width()
	if bwidth != width or a:
		# The changes happens
		bwidth = width
		
		for i in base.winfo_children():
			i.destroy()
			
		sec = Frame(base)
		nav = Frame(base, width=0)
		titleWidth = width
		if width >= 500:
			nav = Frame(base, width=width * 0.15)
			titleWidth = width * 0.85
		if width >= 750:
			nav = Frame(base, width=width * 0.20)
			titleWidth = width * 0.80
		if width >= 1000:
			nav = Frame(base, width=width * 0.25)
			titleWidth = width * 0.75

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
	
		title = Label(sec, text="Grade Management and Monitoring System", font=('Times New Roman', 25), justify='center', wraplength=titleWidth)
		title.pack(fill='x', side='top')

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