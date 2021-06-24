
def common_prefix(s1, s2):
    if not s1 or not s2:
        return ""
    k = 0
    while s1[k] == s2[k]:
        k = k + 1
        if k >= len(s1) or k >= len(s2):
            return s1[0:k]
    return s1[0:k]

def longest_common_prefix_v1(strs):
    if not strs:
        return ""
    result = strs[0]
    for i in range(len(strs)):
        result = common_prefix(result, strs[i])
    return result

