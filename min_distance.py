
def min_distance(word1, word2):
    return len(word1) + len(word2) - 2 * lcs(word1, word2, len(word1), len(word2))

def lcs(s1, s2, i, j):
    if i == 0 or j == 0:
        return 0
    elif s1[i - 1] == s2[j - 1]:
        return 1 + lcs(s1, s2, i - 1, j - 1)
    else:
        return max(lcs(s1, s2, i - 1, j), lcs(s1, s2, i, j - 1))

