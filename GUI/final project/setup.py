from openpyxl import load_workbook
from openpyxl.workbook import Workbook
import os, hashlib

# Encryption
def encrypt(password: str) -> str:
	return (hashlib.sha256(password.encode())).hexdigest()

# Save
def save():
	wb.save(filename)

# Questions
def createExcell():
	global wb, questions, filename, archieves
	filename = "data.xlsx"
	quest = "questions"
	archs = "archieves questions"
	if os.path.exists(filename):
		wb = load_workbook(filename)
	else:
		wb = Workbook()
	
	if quest in wb.sheetnames:
		questions = wb[quest]
	else:
		questions = wb.active
		questions.title = quest

		columns = (
			"question",
			"answer",
			"case sensitive",
			"question by"
		)
		questions.append(columns)
	
	if archs in wb.sheetnames:
		archieves = wb[archs]
	else:
		archieves = wb.create_sheet(archs)
		columns = (
			"question",
			"answer",
			"case sensitive",
			"question by"
		)
		archieves.append(columns)		
	
	save()

def addQuestion(q: str, a: str, cs: bool, t: str):
	questions.append((q, a, cs, t))
	save()
	return True

def getAllQuestions():
	lists = []
	for i in questions.iter_rows(values_only=True):
		lists.append(i)
	return lists

def editQuestion(pos: int, data: list):
	for i in range(len(data)):
		questions.cell(row=pos + 2, column=i + 1, value=data[i])
	save()
	return {
		"done": True,
		"msg": "Data modified successfully"
	}

def archieveQuestions(pos: int):
	x = 0

	for i in questions.iter_rows(values_only=True):
		if x == pos - 1:
			archieves.append(i)
			break
		x += 1

	questions.delete_rows(pos)
	save()
	return {
		"done": True,
		"msg": "Data deleted successfully"
	}

# Students
def createStudents():
	global students
	studs = "students"
	
	if studs in wb.sheetnames:
		students = wb[studs]
	else:
		students = wb.create_sheet(studs)

		columns = (
			"ID",
			"fullname",
			"password",
			"score"
		)
		students.append(columns)
	
	save()

def addStudent(randomID: str, fullname: str, password: str) -> dict:
	id = randomID
	n = fullname
	p = encrypt(password)
	exist = False

	for i in students.iter_rows(values_only=True):
		if id in i:
			exist = True
			break
	
	if not exist:
		students.append((
			id,
			n,
			p,
			0
		))
		save()
	
	return {
		"exists": exist
	}

def getStudentId(username: str, password: str) -> dict:
	userID = 1
	done = False
	for i in students.iter_rows(values_only=True):
		if i[0] == username and i[2] == encrypt(password):
			done = True
			break
		userID += 1
	return {
		"done": done,
		"userID": userID
	}


def updateScore(id: str, score: int):
	x = 0
	for i in students.iter_rows(values_only=True):
		if id == i[0]:
			break
		x += 1
	students.cell(row=x, column=4, valiue=score)


def deleteStudent(pos: int):
	students.delete_rows(pos + 2)
	save()
	return {
		"done": True,
		"mgs": "A student was deleted successfully"
	}


# Teachers
def createTeachers():
	global teachers
	teach = "teachers"
	
	if teach in wb.sheetnames:
		teachers = wb[teach]
	else:
		teachers = wb.create_sheet(teach)

		columns = (
			"ID",
			"fullname",
			"password"
		)
		teachers.append(columns)
	
	save()

def addTeacher(randomID: str, fullname: str, password: str) -> dict:
	id = randomID
	n = fullname
	p = encrypt(password)
	exist = False

	for i in teachers.iter_rows(values_only=True):
		if id in i:
			exist = True
			break
	
	if not exist:
		teachers.append((
			id,
			n,
			p
		))
		save()
	
	return {
		"exists": exist
	}

def getTeacherId(username: str, password: str) -> dict:
	userID = 1
	done = False
	for i in teachers.iter_rows(values_only=True):
		if i[0] == username and i[2] == encrypt(password):
			done = True
			break
		userID += 1
	return {
		"done": done,
		"userID": userID
	}

def getTeacher(id: int):
	teacher = {}
	for i in range(len(teachers[id])):
		teacher[teachers[1][i].value] = teachers[id][i].value
	return teacher

def deleteStudent(pos: int):
	teachers.delete_rows(pos + 2)
	save()
	return {
		"done": True,
		"mgs": "A teacher was deleted successfully"
	}



# All users
def getAllUsers(_type):
	lists = []
	if _type == 'teacher':
		x = False
		for i in teachers.iter_rows(values_only = True):
			l = []
			if x:
				for j in range(0, 2):
					l.append(i[j])
				lists.append(l)
			x = True
	else:
		x = False
		for i in students.iter_rows(values_only = True):
			l = []
			if x:
				for j in range(0, 2):
					l.append(i[j])
				lists.append(l)
			x = True
	return lists
