filename = 'alma.txt'
# write a function that reads a file and prints how many
# lines and characters in it


fname = "cv-anakin.txt"

num_lines = 0
num_words = 0
num_chars = 0

with open(fname, 'r') as myfile:
    for line in myfile:

        words = line.split()

        num_lines += 1
        num_words += len(words)
        num_chars += len(line)

print(num_lines)
