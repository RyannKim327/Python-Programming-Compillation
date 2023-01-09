# open(filename, mode)
# w meaans write
# r means read
file = open("samplefile.txt", "w")
read = open("samplefile.txt", "r")

# to check the text inside
print(read.read())

txt = input("Enter something: ")

# to modify
file.write(txt)
file.close()

# to check again.
print(read.read())