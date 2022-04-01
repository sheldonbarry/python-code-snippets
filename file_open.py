
file = "file-1.csv"

# basic file open and close
f = open(file, 'r')
print(f.read())
f.close()

# better way using context manager
with open(file, 'r') as f:
    print(f.read()) 