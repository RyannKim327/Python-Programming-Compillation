from tkinter import *
from tkinter import messagebox

def saveIt():
	file = open(filename.get() + ".txt", "w")
	file.write(text.get(1.0, "end-1c"))
	messagebox.showinfo("Notice", "File Created/Updated Successfully")

base = Tk()
base.title("Notepad Application")
base.geometry("500x500")
base.resizable(False, False)

frame = Frame(base)

filename = Entry(frame)
filename.config(width=65)
filename.pack(side='left')

save = Button(frame, text="Save")
save.config(command=saveIt)
save.pack(fill=X)

frame.pack(fill=X)

text = Text()
text.pack(fill=BOTH)

base.mainloop()