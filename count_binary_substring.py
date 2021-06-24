
def count_binary_substring(s):
    cur = 1
    pre = 0
    count = 0
    for i in range(1, len(s)):
        if s[i] != s[i - 1]:
            count = count + min(pre, cur)
            pre = cur
            cur = 1
        else:
            cur = cur + 1
    count = count + min(pre, cur)
    return count
