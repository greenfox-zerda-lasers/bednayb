# Create a method that decrypts texts/encoded_zen_lines.txt
def decrypt(file_name):
    result = ""
    #open the file
    f = open(file_name,'r')
    for line in f.readlines():
        result += line
    result = list(result)
    result2 = []
# convert to ascii
    for i in range(len(result)):
        result2.append(ord(result[i]))
# ascii -1
    for i in range(len(result)):
        if result2[i] != 32 and result2[i] !=10:
            result2[i] = result2[i] -1
# convert back
    result3 = ''.join(chr(i) for i in result2)
    f.close()
    return result3

# decrypt('texts/encoded_zen_lines.txt')
