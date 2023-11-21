students_data = [
	["Alice", [85, 90, 92], ["Math", "English", "Science"]],
	["Bob", [78, 88, 80], ["Math", "English", "Science"]],
	["Charlie", [92, 94, 89], ["Math", "English", "Science"]],
	["David", [80, 85, 88], ["Math", "English", "Science"]],
]

def getStudents(arr: list):
	student = arr

	# Traversal
	for i in student:
		ave = 0
		for j in i[1]:
			ave += j
		ave /= len(i[1])
		ave *= 100
		ave //= 1
		ave /= 100
		student.append(ave)

	# Sort
	for i in range(len(student)):
		for j in range(len(student)):
			if student[i][-1] < student[j][-1]:
				student[i], student[j] = student[j], student[i]

	return student

students_data = getStudents(students_data)
print(f"Sorted by Average: {students_data}")

print()

students_data.append(["Eva", [95, 91, 88], ["Math", "English", "Science"]])
print(f"Added Eva: {students_data}")

print()

students_data = getStudents(students_data)
print(f"New sort with Eva: {students_data}")

print()

students_data.pop(0)
print(f"Remove lowest average: {students_data}")

print()

english_scores = []
for i in range(len(students_data)):
	english_scores.append(students_data[i][1][1])
print(english_scores)

print()

maths = [i for i in students_data]
for i in range(len(maths)):
	for j in range(len(maths)):
		if maths[i] > maths[j]:
			maths[i], maths[j] = maths[j], maths[i]

print(maths)