from tkinter import *
from tkinter import messagebox, ttk
import setup

def refreshData():
	# for i in _right.winfo_children():
	# 	i.destroy()

	# data_set = setup.getData()
	
	# for i in range(len(data_set)):
	# 	_data = data_set[i]
	# 	for j in range(len(_data)):
	# 		if i == 0:
	# 			Label(_right, width=table_w[j], text=columns[j], bg=bg, fg=fg, justify='center').grid(row=i, column=j, sticky='n')
	# 		else:
	# 			Label(_right, width=table_w[j], text=_data[j], bg=bg, fg=fg, justify='center', borderwidth=table_b, relief=table_s).grid(row=i, column=j, sticky='n')

	# _right.pack(side='left', fill='x', expand=True, anchor='nw')
	
	for i in tree.get_children():
		tree.delete(i)

	data_set = setup.getData()

	for i in range(len(data_set)):
		tree.insert(parent='', index=END, values=data_set[i])

def closeapp():
	if messagebox.askyesno("Confirmation", "Are you sure you want to exit?"):
		root_login.destroy()

def addData():
	_ = setup.addData({
		"reference": _emp_ref.get().upper(),
		"name": _emp_name.get(),
		"email": _emp_email.get(),
		"gender": _emp_gender.get(),
		"destination": _emp_destination.get(),
		"contact": _emp_contact.get(),
		"salary": _emp_salary.get(),
		"address": _emp_addr.get("1.0", "end-1c")
	})
	if _['approve']:
		messagebox.showinfo("Done", "New Data added")
		_emp_ref.delete(0, END)
		_emp_name.delete(0, END)
		_emp_email.delete(0, END)
		_emp_gender.set("male")
		_emp_destination.delete(0, END)
		_emp_contact.delete(0, END)
		_emp_salary.delete(0, END)
		_emp_addr.delete("1.0", END)
		_emp_ref.insert(0, setup.lastID())
		refreshData()
	else:
		messagebox.showerror("Error", f"Please fix your {_['invalids']}")

def search(data):
	# for i in _right.winfo_children():
	# 	i.destroy()

	# data_set = setup.getData(data)
	
	# for i in range(len(data_set)):
	# 	_data = data_set[i]
	# 	for j in range(len(_data)):
	# 		if i == 0:
	# 			Label(_right, width=table_w[j], text=columns[j], bg=bg, fg=fg, justify='center').grid(row=i, column=j, sticky='n')
	# 		else:
	# 			Label(_right, width=table_w[j], text=_data[j], bg=bg, fg=fg, justify='center', borderwidth=table_b, relief=table_s).grid(row=i, column=j, sticky='n')

	# _right.pack(side='left', fill='x', expand=True, anchor='nw')
	for i in tree.get_children():
		tree.delete(i)

	data_set = setup.getData(data)
	
	for i in range(len(data_set)):
		tree.insert(parent='', index=END, values=data_set[i])

def search_close(search_root):
	if messagebox.askyesno("Confirmation", "Would you like to clear the search?"):
		refreshData()
	
	search_root.destroy()

def search_frame():
	root_search = Toplevel()
	root_search.geometry("200x100")
	root_search.title("Search a data")
	root_search.resizable(False, False)
	root_search.config(bg=bg)

	Label(root_search, bg=bg, fg=fg, text="Search a profile", justify='center').pack(fill='x', expand=True)

	_search = Entry(root_search, bg=bg, fg=fg)
	_search.pack(fill='x', expand=True)

	Button(root_search, bg=bg, fg=fg, text="Search Data", command=lambda: search(_search.get())).pack(fill='x', expand=True)

	root_search.protocol("WM_DELETE_WINDOW", lambda: search_close(root_search))
	root_search.mainloop()

def reset_all():
	_emp_name.delete(0, END)
	_emp_email.delete(0, END)
	_emp_gender.set("male")
	_emp_destination.configure(textvariable=destinations[0])
	_emp_contact.delete(0, END)
	_emp_salary.delete(0, END)
	_emp_addr.delete("1.0", END)

	refreshData()

def selectDelRecord(event):
	global dataDelete
	dataDelete = []
	for items in tree.selection():
		item = tree.item(items)
		dataDelete.append(item['values'][0])
	if len(dataDelete) > 0:
		_delete.config(state='active', bg=button_bg, fg=fg)
	else:
		_delete.config(state='disabled')
	

def deleteRecord():
	if len(dataDelete) > 0:
		setup.deleteData(dataDelete)
		messagebox.showinfo("SUCCESS", "Data deleted successfully")
		refreshData()
	else:
		messagebox.showerror("Error", "There is no data selected")

def employee_frame():

	global _emp_ref, _emp_name, _emp_email, _emp_gender, _emp_destination, _emp_contact, _emp_salary, _emp_addr, _right, columns, table_b, table_s, table_w, bg, button_bg, fg, destinations, tree, _delete
	setup.createDatabase()

	bg = "#212529"
	fg = "#e9ecef"

	def_size = 15
	font = ""

	padxb = 5
	padyb = 5
	
	b_size = 25
	button_bg = "#495057"
	button_bw = 1
	button_style = 'solid'
	
	entry_bg = bg # "#495057"
	entry_bw = 0
	entry_style = 'solid'

	table_b= 1
	table_s = 'solid'

	columns = (
		"Reference No.",
		"Name",
		"Email",
		"Gender",
		"Destination",
		"Contact No.",
		"Salary",
		"Address"
	)
	table_w = [
		25, 100, 50,
		8, 55, 50,
		10, 100
	]

	destinations = [
		"Finance Department",
		"Chief Executive Officer",
		"Chief Operating Officer",
		"Programmer",
		"Data Analysis",
		"Department Head",
		"Marketing Strategy"
	]

	employee_root = Toplevel()
	employee_root.geometry("1200x760")
	employee_root.title("Employee")
	employee_root.config(bg=bg)

	Label(employee_root, bg=bg, fg=fg, text="Employee Record System", justify='center', font=("", 24)).pack(side='top', anchor='n')

	_bottom = Frame(employee_root, bg=bg)

	Button(_bottom, font=(font, b_size), borderwidth=button_bw, relief=button_style, text="Add Record", bg=button_bg, fg=fg, command=lambda: addData()).pack(side='left', padx=padxb, pady=padyb, fill='x', expand=True)
	Button(_bottom, font=(font, b_size), borderwidth=button_bw, relief=button_style, text="Search", bg=button_bg, fg=fg, command=lambda: search_frame()).pack(side='left', padx=padxb, pady=padyb, fill='x', expand=True)
	Button(_bottom, font=(font, b_size), borderwidth=button_bw, relief=button_style, text="Update Record", bg=button_bg, fg=fg).pack(side='left', padx=padxb, pady=padyb, fill='x', expand=True)
	_delete = Button(_bottom, font=(font, b_size), borderwidth=button_bw, relief=button_style, text="Delete Record", bg=button_bg, fg=fg, state='disabled', command=lambda: deleteRecord())
	_delete.pack(side='left', padx=padxb, pady=padyb, fill='x', expand=True)
	Button(_bottom, font=(font, b_size), borderwidth=button_bw, relief=button_style, text="Reset", bg=button_bg, fg=fg, command=lambda: reset_all()).pack(side='left', padx=padxb, pady=padyb, fill='x', expand=True)
	Button(_bottom, font=(font, b_size), borderwidth=button_bw, relief=button_style, text="Exit", bg=button_bg, fg=fg, command=lambda: closeapp()).pack(side='left', padx=padxb, pady=padyb, fill='x', expand=True)

	_bottom.pack(side='bottom', fill='x', expand=True)

	_left = Frame(employee_root, bg=bg, padx=5)

	emp_ref = LabelFrame(_left, bg=bg, fg=fg, text="Employee Ref:", labelanchor='nw')

	_emp_ref = Entry(emp_ref, font=(font, def_size), bg=entry_bg, fg=fg, borderwidth=entry_bw, relief=entry_style)
	_emp_ref.insert(0, setup.lastID())
	_emp_ref.pack(side='left', fill='x', expand=True)

	emp_ref.pack(side='top', fill='x', expand=True)

	emp_name = LabelFrame(_left, bg=bg, fg=fg, text="Full name:", labelanchor='nw')

	_emp_name = Entry(emp_name, font=(font, def_size), bg=entry_bg, fg=fg, borderwidth=entry_bw, relief=entry_style)
	_emp_name.pack(side='left', fill='x', expand=True)

	emp_name.pack(side='top', fill='x', expand=True)
	
	emp_email = LabelFrame(_left, bg=bg, fg=fg, text="Email:", labelanchor='nw')

	_emp_email = Entry(emp_email, font=(font, def_size), bg=entry_bg, fg=fg, borderwidth=entry_bw, relief=entry_style)
	_emp_email.pack(side='left', fill='x', expand=True)

	emp_email.pack(side='top', fill='x', expand=True)
	
	emp_gender = LabelFrame(_left, bg=bg, fg=fg, text="Gender:", labelanchor='nw')
	
	_emp_gender = StringVar()
	_emp_gender.set("male")
	
	Radiobutton(emp_gender, bg=bg, fg=fg, selectcolor=bg, text="Male", value='male', variable=_emp_gender, font=(font, def_size)).pack(side='left', fill='x', expand=True)
	Radiobutton(emp_gender, bg=bg, fg=fg, selectcolor=bg, text="Female", value='female', variable=_emp_gender, font=(font, def_size)).pack(side='left', fill='x', expand=True)
	
	emp_gender.pack(side='top', fill='x', expand=True)
	
	emp_destination = LabelFrame(_left, bg=bg, fg=fg, text="Destination:", labelanchor='nw')

	s = ttk.Style()
	s.theme_use("clam")
	s.configure("TCombobox", fieldbackground=bg, background=bg, fieldforeground=fg, foreground=fg)
	
	_emp_destination = ttk.Combobox(emp_destination, values=destinations, textvariable= destinations[0], font=(font, def_size))
	_emp_destination.pack(side='left', fill='x', expand=True)

	emp_destination.pack(side='top', fill='x', expand=True)
	
	emp_contact = LabelFrame(_left, bg=bg, fg=fg, text="Contact No.:", labelanchor='nw')

	_emp_contact = Entry(emp_contact, font=(font, def_size), bg=entry_bg, fg=fg, borderwidth=entry_bw, relief=entry_style)
	_emp_contact.pack(side='left', fill='x', expand=True)

	emp_contact.pack(side='top', fill='x', expand=True)
	
	emp_salary = LabelFrame(_left, bg=bg, fg=fg, text="Salary:", labelanchor='nw')

	_emp_salary = Entry(emp_salary, font=(font, def_size), bg=entry_bg, fg=fg, borderwidth=entry_bw, relief=entry_style)
	_emp_salary.pack(side='left', fill='x', expand=True)

	emp_salary.pack(side='top', fill='x', expand=True)
	
	emp_addr = LabelFrame(_left, bg=bg, fg=fg, text="Address:", labelanchor='nw')

	_emp_addr = Text(emp_addr, height=5, width=20, font=(font, def_size), bg=entry_bg, fg=fg, borderwidth=entry_bw, relief=entry_style, wrap='word')
	_emp_addr.pack(side='left', fill='x', expand=True)

	emp_addr.pack(side='top', fill='x', expand=True)

	_left.pack(side='left', fill='x', expand=True, anchor='ne')

	_right = Frame(employee_root, bg=bg, padx=5)

	# data_set = setup.getData()

	# for i in range(len(data_set)):
	# 	_rows = Frame(_right)
	# 	for j in range(len(data_set[i])):
	# 		if j == 0:
	# 			Label(_rows, text=columns[i], bg=bg, fg=fg, justify='center').pack(side='top', fill='x', expand=True)
	# 		else:
	# 			Label(_rows, text=data_set[i][j], bg=bg, fg=fg, justify='center', borderwidth=table_w, relief=table_s).pack(side='top', fill='x', expand=True)
	# 	_rows.pack(side='left', fill='x', expand=True)

	# for i in range(len(data_set)):
	# 	_data = data_set[i]
	# 	for j in range(len(_data)):
	# 		if i == 0:
	# 			Label(_right, width=table_w[j], text=columns[j], bg=bg, fg=fg, justify='center').grid(row=i, column=j, sticky='n')
	# 		else:
	# 			Label(_right, width=table_w[j], text=_data[j], bg=bg, fg=fg, justify='center', borderwidth=table_b, relief=table_s).grid(row=i, column=j, sticky='n')

	tree = ttk.Treeview(_right, show='headings')

	_x = Scrollbar(_right, orient='horizontal', command=tree.xview)
	_y = Scrollbar(_right, orient='vertical', command=tree.yview)

	tree.configure(xscrollcommand=_x.set, yscrollcommand=_y.set)

	tree['columns'] = columns
	for i in range(len(columns)):
		tree.heading(columns[i], text=columns[i])
		tree.column(columns[i], width=table_w[i])

	# for i in range(1, len(data_set)):
	# 	tree.insert(parent='', index=END, values=data_set[i])

	refreshData()

	tree.bind("<<TreeviewSelect>>", selectDelRecord)

	_x.pack(side="bottom", fill='x')
	_y.pack(side="right", fill='y')

	tree.pack(fill="both", expand=True)

	_right.pack(side='right', fill='both', expand=True, anchor='ne')

	employee_root.protocol("WM_DELETE_WINDOW", lambda: closeapp())
	employee_root.mainloop()

def login():
	if username_entry.get() == 'user' and password_entry.get() == 'admin':
		messagebox.showinfo("Please proceed", "Start now")
		root_login.withdraw()
		employee_frame()
	else:
		messagebox.showerror("Error", "Invalid Credentials")

def start():
	# Login

	global root_login, username_entry, password_entry

	padx = 5
	pady = 5

	bg = "#212529"
	fg = "#e9ecef"

	root_login = Tk()
	root_login.geometry("300x150")
	root_login.title("Login Panel")
	root_login.config(bg=bg)

	username = LabelFrame(root_login, bg=bg, fg=fg, text="Username:", labelanchor='nw')

	# Label(username, text="Username:\t", font=("", 13), bg=bg, fg=fg).pack(side='left', fill='x')
	username_entry = Entry(username, font=("", 13), bg=bg, fg=fg, borderwidth=0)
	username_entry.pack(side='left', fill='x', expand=True, padx=padx, pady=pady)

	password = LabelFrame(root_login, bg=bg, fg=fg, text="Password:", labelanchor='nw')

	# Label(password, text="Password:\t", font=("", 13), bg=bg, fg=fg).pack(side='left', fill='x')
	password_entry = Entry(password, font=("", 13), show="•", bg=bg, fg=fg, borderwidth=0)
	password_entry.pack(side='left', fill='x', expand=True, padx=padx, pady=pady)

	username.pack(fill='x', expand=True)
	password.pack(fill='x', expand=True)

	Button(root_login, text="Login", command=login, bg=bg, fg=fg).pack(side='left', fill='x', expand=True, padx=padx, pady=pady)

	root_login.mainloop()

if __name__ == "__main__":
	start()