attendance = 0

def getInfo(name, section, subject):
	msg = f"Name: {name}\nSection: {section}\nSubject: {subject}"
	print(msg)

def present():
	global attendance
	attendance += 1

def absent():
	global attendance
	attendance -= 1

def totalGrade():
	print(attendance)