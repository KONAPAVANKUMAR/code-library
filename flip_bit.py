def flip_bit(number: int, position: int) -> int:
    return number ^ (1 << position)