from tkinter import *
from tkinter import ttk

if __name__ == "__main__":
	root = Tk()
	root.geometry("500x500")

	t = ttk.Treeview(root, show='headings')

	columns = (
		"p",
		"q",
		"p ^ q",
		"p V q",
		"~p",
		"~q"
	)

	datas = [
		{
			"p": True,
			"q": True
		},
		{
			"p": True,
			"q": False
		},
		{
			"p": False,
			"q": True
		},
		{
			"p": False,
			"q": False
		}
	]

	t['columns'] = columns
	for i in columns:
		t.heading(i, text=i)
		t.column(i, width=50)
	
	for i in datas:
		k = []
		for j in columns:
			k.append(eval(j.replace("p",str( i["p"])).replace("q", str(i["q"])).replace("^", "and").replace("V", "or").replace("~", "not ")))
		t.insert("", index=END, values=k)

	t.pack()

	root.mainloop()