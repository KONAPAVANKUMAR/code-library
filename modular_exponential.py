def modular_exponential(base, exponent, mod):

    base %= mod
    result = 1

    while exponent > 0:
        if exponent & 1:
            result = (result * base) % mod
        exponent = exponent >> 1
        base = (base * base) % mod

    return result