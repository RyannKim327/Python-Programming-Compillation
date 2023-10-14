def toBytes(text):
	result = []
	for i in range(len(text)):
		result.append(ord(text))	
	return result
