students_data = [
	["Alice", [85, 90, 92], ["Math", "English", "Science"]],
	["Bob", [78, 88, 80], ["Math", "English", "Science"]],
	["Charlie", [92, 94, 89], ["Math", "English", "Science"]],
	["David", [80, 85, 88], ["Math", "English", "Science"]],
]

student = []

for i in students_data:
	ave = 0
	for j in i[1]:
		ave += j
	ave /= len(i[1])
	ave *= 100
	ave //= 1
	ave /= 100
	student.append([f"Name: {i[0]}", ave])

for i in range(len(student)):
	for j in range(len(student)):
		if i < j:
			student[i], student[j] = student[j], student[i]