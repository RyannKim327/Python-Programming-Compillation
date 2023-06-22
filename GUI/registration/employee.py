from tkinter import *
from tkinter import messagebox



def employee_frame():

	global _emp_ref, _emp_name, _emp_email, _emp_gender, emp_destination, _emp_contact, _emp_salary, _emp_addr

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
	
	entry_bg = "#495057"
	entry_bw = 1
	entry_style = 'solid'

	employee_root = Tk()
	employee_root.geometry("1200x760")
	employee_root.title("Employee")
	employee_root.config(bg=bg)

	Label(employee_root, bg=bg, fg=fg, text="Employee Record System", justify='center', font=("", 24)).pack(side='top', anchor='n')

	_bottom = Frame(employee_root, bg=bg)

	Button(_bottom, font=(font, b_size), borderwidth=button_bw, relief=button_style, text="Add Record", bg=button_bg, fg=fg).pack(side='left', padx=padxb, pady=padyb, fill='x', expand=True)
	Button(_bottom, font=(font, b_size), borderwidth=button_bw, relief=button_style, text="Save", bg=button_bg, fg=fg).pack(side='left', padx=padxb, pady=padyb, fill='x', expand=True)
	Button(_bottom, font=(font, b_size), borderwidth=button_bw, relief=button_style, text="Print", bg=button_bg, fg=fg).pack(side='left', padx=padxb, pady=padyb, fill='x', expand=True)
	Button(_bottom, font=(font, b_size), borderwidth=button_bw, relief=button_style, text="Reset", bg=button_bg, fg=fg).pack(side='left', padx=padxb, pady=padyb, fill='x', expand=True)
	Button(_bottom, font=(font, b_size), borderwidth=button_bw, relief=button_style, text="Exit", bg=button_bg, fg=fg).pack(side='left', padx=padxb, pady=padyb, fill='x', expand=True)

	_bottom.pack(side='bottom', fill='x', expand=True)

	_left = Frame(employee_root, bg=bg)

	emp_ref = Frame(_left, bg=bg)

	Label(emp_ref, bg=bg, fg=fg, text="Employee Ref:\t", font=(font, def_size)).pack(side='left')
	_emp_ref = Entry(emp_ref, font=(font, def_size), bg=entry_bg, fg=fg, borderwidth=entry_bw, relief=entry_style)
	_emp_ref.pack(side='left')

	emp_ref.pack(side='top', fill='x', expand=True)

	emp_name = Frame(_left, bg=bg)

	Label(emp_name, bg=bg, fg=fg, text="Full name:\t", font=(font, def_size)).pack(side='left')
	_emp_name = Entry(emp_name, font=(font, def_size), bg=entry_bg, fg=fg, borderwidth=entry_bw, relief=entry_style)
	_emp_name.pack(side='left')

	emp_name.pack(side='top', fill='x', expand=True)
	
	emp_email = Frame(_left, bg=bg)

	Label(emp_email, bg=bg, fg=fg, text="Email:\t\t", font=(font, def_size)).pack(side='left')
	_emp_email = Entry(emp_email, font=(font, def_size), bg=entry_bg, fg=fg, borderwidth=entry_bw, relief=entry_style)
	_emp_email.pack(side='left')

	emp_email.pack(side='top', fill='x', expand=True)
	
	emp_gender = Frame(_left, bg=bg)

	Label(emp_gender, bg=bg, fg=fg, text="Gender:\t\t", font=(font, def_size)).pack(side='left')
	_emp_gender = Entry(emp_gender, font=(font, def_size), bg=entry_bg, fg=fg, borderwidth=entry_bw, relief=entry_style)
	_emp_gender.pack(side='left')

	emp_gender.pack(side='top', fill='x', expand=True)
	
	emp_destination = Frame(_left, bg=bg)

	Label(emp_destination, bg=bg, fg=fg, text="Destination:\t", font=(font, def_size)).pack(side='left')
	_emp_destination = Entry(emp_destination, font=(font, def_size), bg=entry_bg, fg=fg, borderwidth=entry_bw, relief=entry_style)
	_emp_destination.pack(side='left')

	emp_destination.pack(side='top', fill='x', expand=True)
	
	emp_contact = Frame(_left, bg=bg)

	Label(emp_contact, bg=bg, fg=fg, text="Contact No.:\t", font=(font, def_size)).pack(side='left')
	_emp_contact = Entry(emp_contact, font=(font, def_size), bg=entry_bg, fg=fg, borderwidth=entry_bw, relief=entry_style)
	_emp_contact.pack(side='left')

	emp_contact.pack(side='top', fill='x', expand=True)
	
	emp_salary = Frame(_left, bg=bg)

	Label(emp_salary, bg=bg, fg=fg, text="Salary:\t\t", font=(font, def_size)).pack(side='left')
	_emp_salary = Entry(emp_salary, font=(font, def_size), bg=entry_bg, fg=fg, borderwidth=entry_bw, relief=entry_style)
	_emp_salary.pack(side='left')

	emp_salary.pack(side='top', fill='x', expand=True)
	
	emp_addr = Frame(_left, bg=bg)

	Label(emp_addr, bg=bg, fg=fg, text="Address:\t\t", font=(font, def_size)).pack(side='left')
	_emp_addr = Entry(emp_addr, font=(font, def_size), bg=entry_bg, fg=fg, borderwidth=entry_bw, relief=entry_style)
	_emp_addr.pack(side='left')

	emp_addr.pack(side='top', fill='x', expand=True)

	_left.pack(side='left', fill='x', expand=True, anchor='ne')

	_right = Frame(employee_root, bg=bg)

	_right.pack(side='right', fill='x', expand=True, anchor='nw')

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

	root_login = Tk()
	root_login.geometry("300x100")
	root_login.title("Login Panel")

	username = Frame(root_login)

	Label(username, text="Username:\t", font=("", 13)).pack(side='left', fill='x')
	username_entry = Entry(username, font=("", 13))
	username_entry.pack(side='left', fill='x', expand=True, padx=padx, pady=pady)

	password = Frame(root_login)

	Label(password, text="Password:\t", font=("", 13)).pack(side='left', fill='x')
	password_entry = Entry(password, font=("", 13), show="•")
	password_entry.pack(side='left', fill='x', expand=True, padx=padx, pady=pady)

	username.pack(fill='x', expand=True)
	password.pack(fill='x', expand=True)

	Button(root_login, text="Login", command=login).pack(side='left', fill='x', expand=True, padx=padx, pady=pady)

	root_login.mainloop()

if __name__ == "__main__":
	employee_frame()