from tkinter import *
import json

class myfile:
	def __init__(self):
		self.data = json.loads(open("a.json", "r").read())
	
	def read(self):
		return self.data
	
	def write(self, data: dict):
		_file = open("a.json", "w")
		_file.write(json.dumps(data))

def add(x, _value):
	insert[x] += 1
	r['available'][x] += 1
	amt = int(total.cget("text").split(": ")[1])
	amt -= int(_value)
	total.config(text=f"Your total cost was: {amt}")

	_1k_.config(text=f"{r['money'][0]}: {insert[0]}")
	_5h_.config(text=f"{r['money'][1]}: {insert[1]}")
	_2h_.config(text=f"{r['money'][2]}: {insert[2]}")
	_1h_.config(text=f"{r['money'][3]}: {insert[3]}")
	_50p_.config(text=f"{r['money'][4]}: {insert[4]}")
	_20p_.config(text=f"{r['money'][5]}: {insert[5]}")
	_10p_.config(text=f"{r['money'][6]}: {insert[6]}")
	_5p_.config(text=f"{r['money'][7]}: {insert[7]}")
	_1p_.config(text=f"{r['money'][8]}: {insert[8]}")
	_25c_.config(text=f"{r['money'][9]}: {insert[9]}")
	_05c_.config(text=f"{r['money'][10]}: {insert[10]}")

	data.write(r)

def start():
	global total, insert, r, data
	global _1k_, _5h_, _2h_, _1h_, _50p_, _20p_, _10p_, _5p_, _1p_, _25c_, _05c_
	
	amt = 1234

	data = myfile()
	insert = [
		0, 0, 0,
		0, 0, 0, 0,
		0, 0, 0, 0
	]
	r = data.read()

	_padx = 5
	_pady = 5

	base = Tk()
	base.title("Monetary System")
	base.geometry("500x500")

	total = Label()
	total.config(text=f"Your total cost was: {amt}", font=('Times New Roman', 25))
	total.pack(side="top", fill="x", expand=True)

	table1 = Frame(base)

	_1k_ = Label(table1, text=f"{r['money'][0]}: {insert[0]}", font=("Times New Roman", 15))
	_1k_.pack(side="left", expand=True, padx=_padx)

	_5h_ = Label(table1, text=f"{r['money'][1]}: {insert[1]}", font=("Times New Roman", 15))
	_5h_.pack(side="left", expand=True, padx=_padx)

	_2h_ = Label(table1, text=f"{r['money'][2]}: {insert[2]}", font=("Times New Roman", 15))
	_2h_.pack(side="left", expand=True, padx=_padx)

	_1h_ = Label(table1, text=f"{r['money'][3]}: {insert[3]}", font=("Times New Roman", 15))
	_1h_.pack(side="left", expand=True, padx=_padx)

	table1.pack(side="top", expand=False, anchor=N)

	table2 = Frame(base)

	_50p_ = Label(table2, text=f"{r['money'][4]}: {insert[4]}", font=("Times New Roman", 15))
	_50p_.pack(side="left", expand=True, padx=_padx)

	_20p_ = Label(table2, text=f"{r['money'][5]}: {insert[5]}", font=("Times New Roman", 15))
	_20p_.pack(side="left", expand=True, padx=_padx)

	_10p_ = Label(table2, text=f"{r['money'][6]}: {insert[6]}", font=("Times New Roman", 15))
	_10p_.pack(side="left", expand=True, padx=_padx)

	_5p_ = Label(table2, text=f"{r['money'][7]}: {insert[7]}", font=("Times New Roman", 15))
	_5p_.pack(side="left", expand=True, padx=_padx)

	table2.pack(side="top", expand=False, anchor=N)
	
	table3 = Frame(base)

	_1p_ = Label(table3, text=f"{r['money'][7]}: {insert[7]}", font=("Times New Roman", 15))
	_1p_.pack(side="left", expand=True, padx=_padx)

	_25c_ = Label(table3, text=f"{r['money'][9]}: {insert[9]}", font=("Times New Roman", 15))
	_25c_.pack(side="left", expand=True, padx=_padx)

	_05c_ = Label(table3, text=f"{r['money'][10]}: {insert[10]}", font=("Times New Roman", 15))
	_05c_.pack(side="left", expand=True, padx=_padx)

	table3.pack(side="top", expand=False, anchor=N)

	_line_1 = Frame(base)

	_1k = Button(_line_1)
	_1k.config(text=f"{r['money'][0]} pesos", command=lambda: add(0, r['money'][0]))
	_1k.pack(side="left", fill="x", expand=True, padx=_padx)

	_5h = Button(_line_1)
	_5h.config(text=f"{r['money'][1]} pesos", command=lambda: add(1, r['money'][1]))
	_5h.pack(side="left", fill="x", expand=True, padx=_padx)

	_2h = Button(_line_1)
	_2h.config(text=f"{r['money'][2]} pesos", command=lambda: add(2, r['money'][2]))
	_2h.pack(side="left", fill="x", expand=True, padx=_padx)

	_line_1.pack(fill="x", expand=False, anchor=N, pady=_pady)

	_line_2 = Frame(base)

	_1h = Button(_line_2)
	_1h.config(text=f"{r['money'][3]} pesos", command=lambda: add(3, r['money'][3]))
	_1h.pack(side="left", fill="x", expand=True, padx=_padx)

	_5t = Button(_line_2)
	_5t.config(text=f"{r['money'][4]} pesos", command=lambda: add(4, r['money'][4]))
	_5t.pack(side="left", fill="x", expand=True, padx=_padx)

	_2t = Button(_line_2)
	_2t.config(text=f"{r['money'][5]} pesos", command=lambda: add(5, r['money'][5]))
	_2t.pack(side="left", fill="x", expand=True, padx=_padx)

	_line_2.pack(fill="x", expand=False, anchor=N, pady=_pady)
	
	_line_3 = Frame(base)

	_1t = Button(_line_3)
	_1t.config(text=f"{r['money'][6]} pesos", command=lambda: add(6, r['money'][6]))
	_1t.pack(side="left", fill="x", expand=True, padx=_padx)

	_5p = Button(_line_3)
	_5p.config(text=f"{r['money'][7]} pesos", command=lambda: add(7, r['money'][7]))
	_5p.pack(side="left", fill="x", expand=True, padx=_padx)

	_1p = Button(_line_3)
	_1p.config(text=f"{r['money'][8]} pesos", command=lambda: add(8, r['money'][8]))
	_1p.pack(side="left", fill="x", expand=True, padx=_padx)

	_line_3.pack(fill="x", expand=False, anchor=N, pady=_pady)
	
	_line_4 = Frame(base)

	_p25 = Button(_line_4)
	_p25.config(text=f"{r['money'][9]} pesos", command=lambda: add(9, r['money'][9]))
	_p25.pack(side="left", fill="x", expand=True, padx=_padx)

	_p05 = Button(_line_4)
	_p05.config(text=f"{r['money'][10]} pesos", command=lambda: add(10, r['money'][10]))
	_p05.pack(side="left", fill="x", expand=True, padx=_padx)

	_done = Button(_line_4)
	_done.config(text=f"    Done   ")
	_done.pack(side="left", fill="x", expand=True, padx=_padx)

	_line_4.pack(fill="x", expand=False, anchor=N, pady=_pady)


	base.mainloop()

if __name__ == "__main__":
	start()