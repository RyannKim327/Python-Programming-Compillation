from tkinter import *
from tkinter import ttk
import datetime
import data as dt

def execute():
	"Name:        "
	"Age:         "
	"Sex:         "
	"Course:      "
	"Year:        "
	"Address:     "
	"Phone:       "
	"Description: "
	data = []
	data.append(name_entry.get())
	data.append(age_entry.get())
	data.append(str_sex.get())
	course = ""
	for x in course_lists:
		course += x.get() + ", "
	data.append(course)
	data.append(year_entry.get())
	data.append(addr_entry.get())
	data.append(phone_entry.get())
	data.append(desc_entry.get("1.0", "end-1c"))

	dt.addData(data)

def changeAge():
	if year_entry.get().isdigit():
		a = datetime.date.today().year - int(yrs.get())
		if a >= 15:
			age_entry.delete(0, END)
			age_entry.insert(0, a)
		else:
			age_entry.delete(0, END)
			age_entry.insert(0, 15)
			year_entry.delete(0, END)
			year_entry.insert(0, datetime.date.today().year - a)
		return True
	else:
		age_entry.delete(0, END)
		age_entry.insert(0, 0)
		return False

def start():

	global name_entry, age_entry, str_sex, str_course, year_entry, addr_entry, phone_entry, desc_entry, course_lists, yrs

	root = Tk()
	root.geometry("600x600")
	root.title("Registration Panel")

	font_size = 17
	padh = 5
	padv = 5

	"Name:        "
	"Age:         "
	"Sex:         "
	"Course:      "
	"Year:        "
	"Address:     "
	"Phone:       "
	"Description: "

	title = Label(root, text="Registration Form", font=("Times New Roman", font_size), justify=CENTER)
	title.pack()

	name_frame = Frame(root)

	name_label = Label(name_frame, text="Name:\t", font=("", font_size))
	name_label.pack(side='left')

	name_entry = Entry(name_frame, font=("", font_size))
	name_entry.pack(side='right', fill='x', expand=True)

	name_frame.pack(fill="x", expand=True, padx=padh, pady=padv, anchor='n')
	
	age_frame = Frame(root)

	age_label = Label(age_frame, text="Age:\t", font=("", font_size))
	age_label.pack(side='left')

	int_age = IntVar()
	age = []
	for i in range(15, 71):
		age.append(i)

	age_entry = ttk.Combobox(age_frame, font=("", font_size), values=age, textvariable=int_age)
	age_entry.pack(side='right', fill='x', expand=True)

	age_frame.pack(fill="x", expand=True, padx=padh, pady=padv, anchor='n')
	
	sex_frame = Frame(root)

	sex_label = Label(sex_frame, text="Sex:\t", font=("", font_size))
	sex_label.pack(side='left')

	str_sex = StringVar()

	sex_radio_1 = Radiobutton(sex_frame, text="Female", font=("", font_size), variable=str_sex, value="female")
	sex_radio_1.pack(side='right', fill='x', expand=True)

	sex_radio_2 = Radiobutton(sex_frame, text="Male", font=("", font_size), variable=str_sex, value="male")
	sex_radio_2.pack(side='right', fill='x', expand=True)

	sex_frame.pack(fill="x", expand=True, padx=padh, pady=padv, anchor='n')

	course_frame = Frame(root)

	course_label = Label(course_frame, text="Course:\t", font=("", font_size))
	course_label.pack(side='left', anchor='n')

	courses_frame = Frame(course_frame)

	course_lists = []
	courses = [
		"Mathematics",
		"Physics",
		"Programming"
	]

	for x in courses:
		str_course = StringVar()
		str_course.set(x)
		course_ = Checkbutton(courses_frame, font=("", font_size), justify='left', onvalue=x, offvalue="", text=x, variable=str_course)
		course_lists.append(str_course)
		course_.pack(side='top', fill='x', expand=True)

	courses_frame.pack(side='top', fill="x", expand=True, padx=padh, pady=padv, anchor='ne')

	course_frame.pack(fill='x', expand=True, padx=padh, pady=padv)

	year_frame = Frame(root)

	year_label = Label(year_frame, text="Year:\t", font=("", font_size))
	year_label.pack(side='left')

	yrs = IntVar()
	yr = []
	for i in range(1903, datetime.date.today().year - 14):
		yr.append(i)

	year_entry = ttk.Combobox(year_frame, font=("", font_size), values=yr, textvariable=yrs, validate="focusout", validatecommand=changeAge)
	year_entry.pack(side='right', fill='x', expand=True)

	year_frame.pack(fill="x", expand=True, padx=padh, pady=padv, anchor='n')
	
	addr_frame = Frame(root)

	addr_label = Label(addr_frame, text="Address:\t", font=("", font_size))
	addr_label.pack(side='left')

	addr_entry = Entry(addr_frame, font=("", font_size))
	addr_entry.pack(side='right', fill='x', expand=True)

	addr_frame.pack(fill="x", expand=True, padx=padh, pady=padv, anchor='n')
	
	phone_frame = Frame(root)

	phone_label = Label(phone_frame, text="Phone:\t", font=("", font_size))
	phone_label.pack(side='left')

	phone_entry = Entry(phone_frame, font=("", font_size))
	phone_entry.pack(side='right', fill='x', expand=True)

	phone_frame.pack(fill="x", expand=True, padx=padh, pady=padv, anchor='n')
	
	desc_frame = Frame(root)

	desc_label = Label(desc_frame, text="Description: ", font=("", font_size))
	desc_label.pack(side='left', anchor="n")

	desc_entry = Text(desc_frame, font=("", font_size), height=2)
	desc_entry.pack(side='right', fill='x', expand=True)

	desc_frame.pack(fill="x", expand=True, padx=padh, pady=padv, anchor='n')

	register = Button(root, text="Register", font=("Times New Roman", font_size), command=execute)
	register.pack(fill='x', expand=True, padx=padh, pady=padv)

	root.mainloop()

if __name__ == "__main__":
	data = [
		"name",
		"age",
		"sex",
		"course",
		"year",
		"address",
		"phone",
		"description"
	]
	dt.createDatabase(data)
	start()