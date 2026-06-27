with open("demofile.txt", "a") as f:
  f.write("Now the file has more content!")

#open and read the file after the appending:
with open("demofile.txt") as f:
  print(f.read())

#Overwrite Existing Content

with open("demofile.txt", "w") as f:
  f.write("Woops! I have deleted the content!")

#open and read the file after the overwriting:
with open("demofile.txt") as f:
  print(f.read())


#"x" - Create - will create a file, returns an error if the file exists
#"a" - Append - will create a file if the specified file does not exists
#"w" - Write - will create a file if the specified file does not exists
