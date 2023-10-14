import time

def check(arr: list, val: int) -> bool:
	for i in range(len(arr) - 1):
		for j in range(i, len(arr)):
			if arr[i] + arr[j] == val:
				return True
	return False

start = time.time()

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
x = 38

print(str(nums) + " " + str(x) + " " + str(check(nums, x)))
print(time.time() - start)