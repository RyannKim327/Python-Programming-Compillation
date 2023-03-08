arr = []
i = int(input("Enter number: "))

while i != 0:
	arr.append(i)
	i = int(input("Enter number: "))

print(arr)

for i in range(len(arr)):
	for j in range(i):
		if arr[i] < arr[j]:
			arr[i], arr[j] = arr[j], arr[i]

print(arr)