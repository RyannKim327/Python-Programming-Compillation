import json

class Database:
	def __init__(self):
		try:
			with open("passwords.json", "r") as file:
				self.__data__ = json.loads(file.read())
		except:
			print("JSON File not found, the system generated.")
			self.__data__ = {}
			with open("passwords.json", "w") as file:
				file.write(json.dumps(self.__data__, indent=4))
		
	def getData(self):
		return self.__data__
	
	def saveData(self, data: json):
		with open("passwords.json", "w") as file:
				file.write(json.dumps(data, indent=4))

class UserNotFound(Exception):
	def __init__(self, name):
		data = Database()
		if name == "":
			self.__error__ = "The name is blank"
		elif data.getData().get(name) == None:
			self.__error__ = "User Not Found"
	
	def __str__(self):
		return self.__error__

class UserAuthentication:
	def __init__(self):
		self.name = input("Please enter your name: ")