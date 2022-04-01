# script to concatenate text files into a new file

# name of output files
outfile = 'heroes.csv'

# list of files to concatenate in order of concat
infiles = ["file-1.csv",
           "file-2.csv",
           "file-3.csv"]

# function to concatenate files
def file_append (infile, outfile):
    with open (infile, 'r') as a:
        with open (outfile, 'a') as b:
            for line in a.readlines():
                # only write non-blank lines and make line endings consistent
                if line.strip() != '':
                    b.write(line.strip() + '\n')

# process files and concatenate
for filename in infiles:
    print (f"concatenating {filename}")
    file_append(filename, outfile)






    
        
