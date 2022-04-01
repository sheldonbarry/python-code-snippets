

filename = "input_data.txt"
output = "output_data.txt"

with open(filename, 'r') as infile:
    with open(output, 'w') as outfile:
        for line in infile.readlines():
            outfile.write(line.strip()+'\n')

            
