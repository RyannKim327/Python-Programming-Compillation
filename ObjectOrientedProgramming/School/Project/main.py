from handler import *
import hashlib

# security = Security("RySes")

# print(security.encrypt("Hello World"))
# print(security.decrypt("154 222 191 209 226 114 208 194 215 223 182"))

try:
	user = UserAuthentication()
	print(user.checkUser())
except Exception as e:
	print("Error:", e)