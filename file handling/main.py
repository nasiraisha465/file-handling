# open file and store file object in a variable
file = open ('codingal.txt')
print(file.read())
file.close()
# cannot read a closed file
print(file.read())
