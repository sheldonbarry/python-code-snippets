import sys
from hashlib import sha256
 
def sha256_checksum(file):
    with open(file, 'rb') as f:
        return sha256(f.read()).hexdigest() 
 
if __name__ == "__main__":
    print(sha256_checksum(sys.argv[1]))