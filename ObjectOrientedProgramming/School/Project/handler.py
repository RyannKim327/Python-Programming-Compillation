import json
import hashlib
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
			data[name] = {}
			data.saveData(data)
			self.__error__ = "User Not Found, the system created the user automatically."
	
	def __str__(self):
		return self.__error__

class UserAuthentication:
	def __init__(self):
		self.__authenticate__ = False
		try:
			self.name = input("Please enter your name: ")
			self.password = input("Please enter your password: ")
			self.__authenticate__ = True
		except UserNotFound as e:
			print(e)

class Security:
	def __init__(self, password: str):
		self.__password = password
	
	def encrypt(self, data: str):
		result = ""
		password = self.__password
		for i in range(len(data)):
			result += str(ord(data[i]) + ord(password[i % len(password)])) + " "
		return result

	def decrypt(self, data: str):
		result = ""
		d = data.split(" ")
		password = self.__password
		for i in range(len(d)):
			result += chr(int(d[i]) - ord(password[i % len(password)]))
		return result
