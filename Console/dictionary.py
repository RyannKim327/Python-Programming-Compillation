# Simple Create and Read using dictionary

# Create a dictionary
data = {}

# Read the current data
print(data)

# Create a new data
key = input("Enter key name: ")
value = input("Enter data: ")
data[key] = value

# Read the data again
print(data)

# Update
key = input("Enter the name: ")
if data.get(key) == None:
	# Not existed
	print("Not Existed key")
else:
	# Rewrite method
	value = input("Enter the new data: ")
	data[key] = value

# Print the data to see the result
print(data)

# Delete Data
key = input("Enter the key: ")
if data.get(key) == None:
	# Not existed
	print("Not Existed key")
else:
	# Deleting process
	data.pop(key)

# Print the data to see the result
print(data)
