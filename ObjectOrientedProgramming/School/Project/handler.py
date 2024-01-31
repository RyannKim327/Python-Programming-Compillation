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
	def __init__(self, name, password):
		data = Database()
		if name == "":
			self.__error__ = "The name is blank"
		elif data.getData().get(name) == None:
			data[name][name] = password
			data.saveData(data)
			self.__error__ = "User Not Found, the system created the user automatically."
	
	def __str__(self):
		return self.__error__

def AuthenticationError(Exception):
	def __init__(self, name, password):
		self.__error__ = []
		if name == "":
			self.__error__.append("User's name is empty")
		if password == "":
			self.__error__.append("User's password is empty")
		elif len(password) < 8:
			self.__error__.append("User's password is too short")
	
	def __str__(self):
		return self.__error__.join(" and ")

class UserAuthentication:
	def __init__(self):
		self.name = input("Please enter your name: ")
		self.password = input("Please enter your password: ")
		raise AuthenticationError(self.name, self.password)
	
	def UserInformation(self):
		try:
			return {
				"name": self.name,
				"password": self.password
			}
		except AuthenticationError as e:
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
