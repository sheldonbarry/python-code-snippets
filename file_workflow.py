import os

# function to concatenate files
def file_append (infile, outfile):
    with open (infile, 'r') as a:
        with open (outfile, 'a') as b:
            for line in a.readlines():
                # only write non-blank lines and make line endings consistent
                if line.strip() != '':
                    b.write(line.strip() + '\n')

# function to count rows
def count_rows(filename):
    count = 0
    with open(filename, 'r') as a:
        for row in a:
            count += 1
    return count

# set current directory
currentdir = os.sys.path[0]

# blank lists to store files 
files = []

# name of output files
outfile = "heroes.csv"

# parse the current directory and add file names of type ".csv" to the list
for name in os.listdir(currentdir):
    if os.path.isfile(name):
        if name.endswith(".csv"):
            files.append(name)

# process files and concatenate
for filename in files:
    print (f"concatenating {filename}")
    file_append(filename, outfile)

print(count_rows(outfile))