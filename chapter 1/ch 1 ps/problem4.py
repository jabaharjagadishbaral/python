import os

directory = "."

for root, dirs, files in os.walk(directory):
    print("Directory:", root)
    for d in dirs:
        print("  Folder:", d)
    for f in files:
        print("  File:", f)