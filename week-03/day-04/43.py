filename = 'alma.txt'
# create a function that prints the content of the
# file given in the input

fname = "cv-anakin.txt"

num_lines = 0
num_words = 0
num_chars = 0

with open(fname, 'r') as f:
    for line in f:
        print(line)
        words = line.split()

        num_lines += 1
        num_words += len(words)
        num_chars += len(line)
