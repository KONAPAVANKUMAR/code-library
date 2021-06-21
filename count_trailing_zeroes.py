from math import log2


def binary_count_trailing_zeros(a: int):
    return 0 if (a == 0) else int(log2(a & -a))