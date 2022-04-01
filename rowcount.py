import sys

def count_rows(filename):
    count = 0
    with open(filename, 'r') as a:
        for row in a:
            count += 1
    print(count)

if __name__ == "__main__":
    count_rows(sys.argv[1])