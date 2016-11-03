filename = 'alma.txt'
# create a function that reads a file and prints it's
# lines, also it should prepend an 'A' character
# to each line

fname = "cv-anakin.txt"

num_lines = 0
num_words = 0
num_chars = 0

with open(fname, 'r') as f:
    for line in f:
        words = line.split()
        print(line.rstrip() + "A\n")
        num_lines += 1
        num_words += len(words)
        num_chars += len(line)
