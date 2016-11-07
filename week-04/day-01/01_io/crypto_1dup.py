# Create a method that decrypts the texts/duplicated_chars.txt

def decrypt(file_name):
    result = ""
    f = open(file_name,'r')
    for line in f.readlines():
        # if line[x] == "/n":
        #    result += "/n"
          result += (line[::2])
        # else:
        #     print(line[::2])
    f.close()
    return result
