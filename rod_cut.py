INT_MIN = -32767
def cut_rod(price):
    n = len(price)
    val = [0]*(n+1)
    for i in range(1, n+1):
        max_val = INT_MIN
        for j in range(i):
             max_val = max(max_val, price[j] + val[i-j-1])
        val[i] = max_val
    return val[n]