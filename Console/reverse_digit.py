multiplier = 1

n = int(input("Enter numbers: "))
result = 0

print(f"You entered: {n}")

while n > 0:
    result = (n % 10) + (result * multiplier)
    multiplier = 10
    n //= 10

print(f"The reversed digits are: {result}")
