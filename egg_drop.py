INT_MAX = 32767

def egg_drop(n, k):
    egg_floor = [[0 for x in range(k+1)] for x in range(n+1)]

    for i in range(1, n+1):
        egg_floor[i][1] = 1
        egg_floor[i][0] = 0

    for j in range(1, k+1):
        egg_floor[1][j] = j
    for i in range(2, n+1):
        for j in range(2, k+1):
            egg_floor[i][j] = INT_MAX
            for x in range(1, j+1):
                res = 1 + max(egg_floor[i-1][x-1], egg_floor[i][j-x])
                if res < egg_floor[i][j]:
                    egg_floor[i][j] = res
    return egg_floor[n][k]