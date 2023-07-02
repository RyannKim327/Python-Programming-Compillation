from openpyxl import load_workbook
from openpyxl.workbook import Workbook
import os, hashlib

def encrypt(password: str) -> str:
	return (hashlib.sha256(password.encode())).hexdigest()

def save():
	wb.save(filename)

def createExcell():
	global wb, questions, filename
	filename = "data.xlsx"
	quest = "questions"
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
			"question by"
		)
		questions.append(columns)
	
	save()

def createStudents():
	global wb, students
	studs = "students"
	if os.path.exists(filename):
		wb = load_workbook(filename)
	else:
		wb = Workbook()
	
	if studs in wb.sheetnames:
		students = wb[studs]
	else:
		students = wb.create_sheet(studs)

		columns = (
			"ID",
			"fullname",
			"password"
		)
		students.append(columns)
	
	save()

def createTeachers():
	global wb, teachers
	teach = "teachers"
	if os.path.exists(filename):
		wb = load_workbook(filename)
	else:
		wb = Workbook()
	
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
			p
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