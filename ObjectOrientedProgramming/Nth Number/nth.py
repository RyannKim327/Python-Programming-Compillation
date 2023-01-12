import math

class positions:
	def __init__(self, number):
		self.ones = [
			"th", "first", "second", "third", "fourth",
			"fifth", "sixth", "seventh", "eigth", "ninth",
			'tenth', "eleventh", "twelveth", "thirteenth", "fourteenth",
			"fifteenth", "sixteenth", "seventeenth", "eighteenth", "nineteenth"
		]
		self.tens = [
			"twenty", "thirty", "fourty", "fifty", 
			"sixty", "seventy", "eighty", "ninety"
		]
		self.more = [
			"hundread", "thousand"
		]
		self.digit = number
	
	def convert(self):
		output = ""

		if math.floor((self.digit % 100) / 10) - 2 >= 0:
			p = math.floor((self.digit % 100) / 10) - 2
			output += self.tens[p]
			if math.floor((self.digit % 10)) == 0:
				output += "th"
			output += " "
		
		if math.floor((self.digit % 100)) < 20:
			p = self.digit % 100
			output += self.ones[p] + " "
		elif math.floor((self.digit % 10)) <= 9 and math.floor((self.digit % 10)) != 0:
			p = self.digit % 10
			output += self.ones[p] + " "
		
		return output

num = int(input("Enter number: "))
a = positions(num)

print(a.convert())