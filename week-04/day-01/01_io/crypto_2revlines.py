# Create a method that decrypts texts/reversed_zen_lines.txt
def decrypt(file_name):
    result = ""
    f = open(file_name,'r')
    for line in f.readlines():
        result += line[::-1]
    f.close()
    result = result[1:]
    result += "\n"
    return result
    # return result
# decrypt("texts/reversed_zen_lines.txt")
