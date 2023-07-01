from tkinter import *
from tkinter import messagebox
import menu, setup


def start():
	global root, baseColor, txtColor
	root = Tk()
	root.geometry("500x200")
	root.title("Elementary product")

	baseColor = "#575D5E"
	txtColor = "#ffffff"
	root.config(bg=baseColor, padx=5)

	

	menu.menuSetup(root)

	root.mainloop()

if __name__ == "__main__":
	setup.createExcell()
	setup.createStudents()
	start()
