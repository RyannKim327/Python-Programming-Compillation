from tkinter import *
from tkinter import messagebox, filedialog

def saveIt():
	if filename.get() == "":
		filename_ = filedialog.askopenfilename(initialdir="/", title="Open a file", filetypes=(("Text Files", "*.txt"), ("All files", "*.*")))
		file = open(filename_, "r")
		file_ = filename_.split("/")[len(filename_.split("/")) - 1].split(".")[0]
		text.insert(1.0, file.read())
		filename.insert(0, file_)
	else:
		file = open(filename.get() + ".txt", "w")
		file.write(text.get(1.0, "end-1c"))
		messagebox.showinfo("Notice", "File Created/Updated Successfully")

def check(event):
	if event.widget.get() == "":
		save.config(text="Open")
	else:
		save.config(text="Save")

base = Tk()
base.title("Notepad Application")
base.geometry("500x500")
base.resizable(False, False)

frame = Frame(base)

filename = Entry(frame)
filename.config(width=65)
filename.bind("<FocusOut>", check)
filename.pack(side='left')

save = Button(frame, text="Open")
save.config(command=saveIt)
save.pack(fill=X)

frame.pack(fill=X)

text = Text()
text.pack(fill=BOTH)

base.mainloop()