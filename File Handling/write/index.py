# open(filename, mode)
# w meaans write
# r means read
read = open("samplefile.txt", "r")

# to check the text inside
txt = read.read()
print(txt)


file = open("samplefile.txt", "w")

txt += input("Enter something: ") + "\n"

# to modify
file.write(txt)
file.close()

# to check again.
print(read.read())