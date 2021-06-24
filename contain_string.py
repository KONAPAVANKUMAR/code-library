
def contain_string(haystack, needle):
    if len(needle) == 0:
        return 0
    if len(needle) > len(haystack):
        return -1
    for i in range(len(haystack)):
        if len(haystack) - i < len(needle):
            return -1
        if haystack[i:i+len(needle)] == needle:
            return i
    return -1
