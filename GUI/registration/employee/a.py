from tkinter import *

def _b():
	global x
	if x < 0:
		x += 0.005
		b.place(x=0, y=0, relx=x, rely=0, relheight=1, relwidth=0.3)
		print(x)
		b.after(10, _b)
	else:
		x = 0

def _c():
	global x
	if x >= 0:
		x -= 0.005
		b.place(x=0, y=0, relx=x, rely=0, relheight=1, relwidth=0.3)
		print(x)
		b.after(10, _b)

def _a():
	global a, b, x
	a = Tk()
	a.geometry("300x100")
	a.title("Loginn Form")

	x = -1

	Button(a, text="Show nav", command=_b).pack(fill="both", expand=True)

	b = Frame(a, bg="red", padx=10, pady=10)
	Button(b, text="x", command=_c).place(x=0, y=0, relx=1, rely=0, relheight=0.1, relwidth=0.1)
	Label(b, text="This is a header", bg="red", fg="white").pack(side='top', fill='x', expand=True, anchor='n')
	Label(b, text="This is a Content", bg="red", fg="white").pack(side='left', fill='x', expand=True)
	b.place(x=0, y=0, relx=x, rely=0, relheight=1, relwidth=0.3)

	a.mainloop()

if __name__ == "__main__":
	_a()