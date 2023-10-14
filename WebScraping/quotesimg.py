import requests as req

def getData():
	data = req.get("https://zenquotes.io/api/image")
	return data

print(getData())