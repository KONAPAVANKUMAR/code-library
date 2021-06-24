from gcd import gcd

def lcm(a, b):
    return abs(a) * abs(b) / gcd(a, b)