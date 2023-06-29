from tkinter import *
from tkinter import messagebox

def _b(a, b):
	if a.get() == "." and b.get() == '+':
		messagebox.showinfo("SUCCESS", "Yehey")
	else:
		messagebox.showerror("ERROR", "WOW")

def _a():
	a = Tk()
	a.geometry("300x100")
	a.title("Loginn Form")

	Button(a, text="Show nav").pack(fill="both", expand=True)

	b = Frame(a, bg="red", height=500, width=50)
	Label(b, text="Test", bg="red", fg="white").pack()
	b.place(x=0, y=x0)

	a.mainloop()

if __name__ == "__main__":
	_a()