import os
import shutil

# Create nested directories
os.makedirs("Folder/Test", exist_ok=True)

# List files and folders
print(os.listdir())

# Find .txt files
for file in os.listdir():
    if file.endswith(".txt"):
        print(file)

# Copy file
shutil.copy("text.txt", "Folder/text.txt")

# Move file
shutil.move("Folder/text.txt", "Folder/Test/text.txt")