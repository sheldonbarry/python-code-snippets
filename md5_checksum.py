import sys
from hashlib import md5
 
def md5_checksum(file):
    with open(file, 'rb') as f:
        return md5(f.read()).hexdigest() 
 
if __name__ == "__main__":
    print(md5_checksum(sys.argv[1]))