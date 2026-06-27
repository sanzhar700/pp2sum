#To open a file for reading it is enough to specify the name of the file:
f = open("demofile.txt")

#The code above is the same as:
f = open("demofile.txt", "rt")

#read
f = open("demofile.txt")
print(f.read())

#with
with open("demofile.txt") as f:
  print(f.read())

#close statement
f = open("demofile.txt")
print(f.readline())
f.close()


#readline
with open("demofile.txt") as f:
  print(f.readline())


#Loop through the file line by line:
with open("demofile.txt") as f:
  for x in f:
    print(x)

    