from tkinter import *
from tkinter import messagebox, ttk

def register():
	name = entry_name.get()
	age = entry_age.get()
	gender = str_gender.get()
	description = text_description.get("1.0", "end-1c")
	skills = text_skills.get("1.0", "end-1c")
	phone = entry_phone.get()
	educ = str_educ.get()

	if name == "" or not " " in name:
		messagebox.showerror("Error", "Please fix your name")
	elif not age.isdigit():
		messagebox.showerror("Error", "Please fix your age")
	elif not phone.isdigit() or len(phone) != 11:
		messagebox.showerror("Error", "This is not a phone number")
	else:
		hobbies = []
		for x in hobby_lists:
			if not x.get() == "":
				hobbies.append(x.get())
		if len(hobbies) == 0:
			hobbies.append("No hobbies")
		
		message = f"Name: {name}\nAge: {age}\nGender: {gender}\nDescription: {description}\nSkills: {skills}\nPhone: {phone}\nEducation: {educ}\nHobbies: {', '.join(hobbies)}"
		messagebox.showinfo("Congrats", message)

def start():

	global entry_name, entry_age, str_gender, text_description, text_skills, entry_phone, str_educ, hobby_lists

	text_height = 3
	text_width = 30

	root = Tk()
	root.geometry("350x500")
	root.title("Biodata")

	label_name = Label(root, text="Name: ")
	label_name.grid(row=0, column=0, sticky='e')

	entry_name = Entry(root)
	entry_name.grid(row=0, column=2)

	label_age = Label(root, text="Age: ")
	label_age.grid(row=1, column=0, sticky='e')

	entry_age = Entry(root)
	entry_age.grid(row=1, column=2)

	label_gender = Label(root, text="Gender: ")
	label_gender.grid(row=2, column=0, sticky='e')

	str_gender = StringVar()
	str_gender.set('male')

	gender_male = Radiobutton(root, text="Male", value="male", variable=str_gender)
	gender_male.grid(row=2, column=1)

	gender_female = Radiobutton(root, text="Female", value="female", variable=str_gender)
	gender_female.grid(row=2, column=3)

	label_description = Label(root, text="Description: ")
	label_description.grid(row=3, column=0, sticky='e')

	text_description = Text(root, height=text_height, width=text_width)
	text_description.grid(row=3, column=1, columnspan=3, sticky='w')

	label_skills = Label(root, text="Skills: ")
	label_skills.grid(row=4, column=0, sticky='e')

	text_skills = Text(root, height=text_height, width=text_width)
	text_skills.grid(row=4, column=1, columnspan=3, sticky='w')

	label_phone = Label(root, text="Phone: ")
	label_phone.grid(row=5, column=0, sticky='e')

	entry_phone = Entry(root)
	entry_phone.grid(row=5, column=2)

	label_educ = Label(root, text="Education: ")
	label_educ.grid(row=6, column=0, sticky='e')

	education = [
		"High School",
		"Bachelor's Degree",
		"Master's Degree",
		"Ph.D"
	]

	str_educ = StringVar()
	str_educ.set(education[0])

	entry_educ = ttk.Combobox(root, values=education, textvariable=str_educ)
	entry_educ.grid(row=6, column=2)

	label_hobby = Label(root, text="Hobbies: ")
	label_hobby.grid(row=7, column=0, sticky='e')


	hobby_lists = []
	hobbies = [
		"Programming",
		"Sleeping",
		"Music",
		"Sipping Coffee"
	]
	position = 0
	for i in hobbies:
		str_hobby = StringVar()
		check_hobby = Checkbutton(root, text=i, onvalue=i, offvalue="", textvariable=i, variable=str_hobby)
		check_hobby.grid(row=8 + position, column=1, columnspan=3, sticky='w')
		hobby_lists.append(str_hobby)
		position += 1

	reg = Button(root, text="Register", command=lambda: register())
	reg.grid(row=position + 9, column=1, columnspan=2)

	root.mainloop()

if __name__ == "__main__":
	start()