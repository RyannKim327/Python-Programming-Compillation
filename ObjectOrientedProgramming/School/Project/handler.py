import json, hashlib, getpass
class Database:
	def __init__(self):
		try:
			with open("passwords.json", "r") as file:
				self.__data__ = json.loads(file.read())
			print(self.__data__)
		except:
			self.__data__ = {}
			self.saveData(self.__data__)
		
	def getData(self):
		return self.__data__
	
	def saveData(self, data: json):
		with open("passwords.json", "w") as file:
				file.write(json.dumps(data, indent=4))

class AuthenticationError(Exception):
	def __init__(self, name: str, password: str):
		self.__error__ = []
		if name == "":
			self.__error__.append("User's name is empty")
		if password == "":
			self.__error__.append("User's password is empty")
		elif len(password) < 8:
			self.__error__.append("User's password is too short")
	
	def __str__(self):
		return " and ".join(self.__error__)

class UserNotFound(AuthenticationError):
	def __init__(self, name, password):
		super().__init__(name, password)
		data = Database()
		if name == "":
			self.__error__ = "The name is blank"
		elif data.getData().get(name) == None:
			data.getData()[name][name] = hashlib.md5(password.encode()).hexdigest()
			data.saveData(data)
			self.__error__ = "User Not Found, the system created the user automatically."
	
	def __str__(self):
		return self.__error__

class UserAuthentication:
	def __init__(self):
		self.name = input("Please enter your name: ")
		self.password = getpass.getpass("Please enter your password: ")
		raise UserNotFound(self.name, self.password)

	def checkUser(self):
		db = Database()
		print(db.getData())
		try:
			if db.getData().get(self.name) != None:
				if db.getData()[self.name] == hashlib.md5(self.password.encode()).hexdigest():
					return {
						"message": "We've found it",
						"name": self.name,
						"password": self.password
					}
				else:
					return {
						"message": "Wrong username or password"
					}
			else:
				return {
					"message": "There's no user found"
				}
		except Exception as e:
			return {
				"message": e
			}

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
