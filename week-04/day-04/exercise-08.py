# 8. Given a string, compute recursively a new string where all the 'x' chars have been removed.

def replaceChar(inval, old, new):
    if inval == '':
        return ''
    if inval[0] == old:
        return new + replaceChar(inval[1:], old, new)
    
    return inval[0] + replaceChar(inval[1:], old, new)
x = replaceChar("xsalax","x", "")

print(x)
