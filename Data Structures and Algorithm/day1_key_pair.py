def check(arr: list, val: int) -> bool:
	for i in range(len(arr) - 1):
		for j in range(i, len(arr)):
			if arr[i] + arr[j] == val:
				return True
	return False

nums = [1, 2, 3, 4, 5]
x = 3

print(check(nums, x))