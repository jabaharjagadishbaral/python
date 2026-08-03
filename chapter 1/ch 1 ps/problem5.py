import os

# Specify the directory path
directory = "."   # Current directory

# Print all files and folders in the directory
contents = os.listdir(directory)

print("Contents of the directory:")
for item in contents:
    print(item)