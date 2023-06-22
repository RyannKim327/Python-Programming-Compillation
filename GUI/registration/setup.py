from openpyxl import *
import os

def createDatabase():
	if os.path.exists("employees.xlsx"):
		wb = load_workbook("employees.xlsx")
		ws = wb['employees']
	else:
		wb = Workbook()
		ws = wb.active
		ws.title = "employees"
	ws.cell(row = 1, column = 1, value = "reference")

def addData(data: dict):
	proceed = True
	invalids = []
	if data.get("reference") == None:
		invalids.append("reference")
		proceed = False

	if data.get("name") == None:
		invalids.append("name")
		proceed = False
		
	if data.get("email") == None:
		invalids.append("email")
		proceed = False

	if data.get("gender") == None:
		invalids.append("gender")
		proceed = False

	if data.get("destination") == None:
		invalids.append("destination")
		proceed = False

	if data.get("contact") == None:
		invalids.append("contact")
		proceed = False

	if data.get("salary") == None:
		invalids.append("salary")
		proceed = False

	if data.get("address") == None:
		invalids.append("address")
		proceed = False
	
	return {
		"approve": proceed,
		"invalids": ", ".join(invalids)
	}
