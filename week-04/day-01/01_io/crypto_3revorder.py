# Create a method that decrypts texts/reversed_zen_order.txt
def decrypt(file_name):
    result = ""
    f = open(file_name,'r')
    for line in reversed(list(f.readlines())):
        result += line

    print( result)
    f.close()

decrypt("test.txt")
