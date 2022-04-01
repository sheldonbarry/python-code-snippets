import os

# set current directory
currentdir = os.sys.path[0]

# blank lists to store files and directories    
files = []
directories = []

# parse the current directory and add file names to the list
for name in os.listdir(currentdir):
    if os.path.isfile(name):
        files.append(name)
    elif os.path.isdir(name):
        directories.append(name)

print(files)
print(directories)        