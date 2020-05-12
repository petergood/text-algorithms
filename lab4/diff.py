import sys
from lcs import longest_common_subsequence

def read_file(file):
    with open(file, 'r') as content_file:
        return content_file.read()

def diff(file1, file2):
    lines1 = read_file(file1).split('\n')
    lines2 = read_file(file2).split('\n')
    
    l, sigma = longest_common_subsequence(lines1, lines2)

    def print_line(line, c, i):
        if line not in sigma:
            print(f"{c} ({i}) {line}")

    i, j = 0, 0
    while i < len(lines1) or j < len(lines2):
        if i < len(lines1):
            print_line(lines1[i], '>', i)
            i = i + 1
        if j < len(lines2):
            print_line(lines2[j], '<', j)
            j = j + 1

if __name__ == "__main__":
    args = list(sys.argv)

    if len(args) != 3:
        print("Usage: python diff.py file1 file2")
        exit(1)

    diff(args[1], args[2])