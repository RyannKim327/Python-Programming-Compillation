students_data = [
	["Alice", [85, 90, 92], ["Math", "English", "Science"]],
	["Bob", [78, 88, 80], ["Math", "English", "Science"]],
	["Charlie", [92, 94, 89], ["Math", "English", "Science"]],
	["David", [80, 85, 88], ["Math", "English", "Science"]],
]

def getStudents(arr: list):
	student = []

	# Traversal
	for i in arr:
		ave = 0
		for j in i[1]:
			ave += j
		ave /= len(i[1])
		ave *= 100
		ave //= 1
		ave /= 100
		student.append([f"Name: {i[0]}", ave])

	# Sort
	for i in range(len(student)):
		for j in range(len(student)):
			if student[i][1] < student[j][1]:
				student[i], student[j] = student[j], student[i]

	return student

new_students = getStudents(students_data)
print(f"Sorted by Average: {new_students}")

students_data.append(["Eva", [95, 91, 88], ["Math", "English", "Science"]])
print(f"Added Eva: {students_data}")

new_students = getStudents(students_data)
print(f"New sort with Eva: {new_students}")
new_students.shift()
print(new_students)