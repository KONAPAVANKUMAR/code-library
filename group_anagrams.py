

def group_anagrams(strs):
    d = {}
    ans = []
    k = 0
    for str in strs:
        sstr = ''.join(sorted(str))
        if sstr not in d:
            d[sstr] = k
            k += 1
            ans.append([])
            ans[-1].append(str)
        else:
            ans[d[sstr]].append(str)
    return ans
