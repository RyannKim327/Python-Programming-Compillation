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

def creaateTeachers():
	global wb, students
	teach = "students"
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