
def factorial(n, mod=None):
    result = 1
    if n == 0:
        return 1
    for i in range(2, n+1):
        result *= i
        if mod:
            result %= mod
    return result