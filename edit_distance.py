def edit_distance(A, B):
    m, n = len(A) + 1, len(B) + 1

    edit = [[0 for _ in range(n)] for _ in range(m)]

    for i in range(1, m):
        edit[i][0] = i

    for j in range(1, n):
        edit[0][j] = j

    for i in range(1, m):
        for j in range(1, n):
            cost = 0 if A[i - 1] == B[j - 1] else 1
            edit[i][j] = min(edit[i - 1][j] + 1, edit[i][j - 1] + 1, edit[i - 1][j - 1] + cost)

    return edit[-1][-1]