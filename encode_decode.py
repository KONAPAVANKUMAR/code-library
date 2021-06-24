
def encode(strs):
    res = ''
    for string in strs.split():
        res += str(len(string)) + ":" + string
    return res

def decode(s):
    strs = []
    i = 0
    while i < len(s):
        index = s.find(":", i)
        size = int(s[i:index])
        strs.append(s[index+1: index+1+size])
        i = index+1+size
    return strs