# 9. Given a string, compute recursively a new string where all the
# adjacent chars are now separated by a "*".


def replaceChar(inval):
    if inval == '':
        return ''
    else :
        return  inval[0] + "*" + replaceChar(inval[1:])


x = replaceChar("xsalax")

print(x)
