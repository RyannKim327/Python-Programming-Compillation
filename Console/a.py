students_data = [
	["Alice", [85, 90, 92], ["Math", "English", "Science"]],
	["Bob", [78, 88, 80], ["Math", "English", "Science"]],
	["Charlie", [92, 94, 89], ["Math", "English", "Science"]],
	["David", [80, 85, 88], ["Math", "English", "Science"]],
]

student = []

for i in students_data:
	print(f"Name: " + i[0])
	ave = 0
	for j in i[1]:
		ave += j
	ave /= len(i[1])
	print((ave * 10) % 10)