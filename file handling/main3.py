file = open("codingal.txt","r")
counter = 0
# reading from file
content = file.read()
# splitting content into lines
# and storing them in a list 
colist = content.split("\n")
for i in colist:
    if i:
        counter += 1
print("This is the number of list in the file")
print(counter)

