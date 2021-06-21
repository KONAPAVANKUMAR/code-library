def get_reverse_bit_string(number: int) -> str:
    bit_string = ""
    for _ in range(0, 32):
        bit_string += str(number % 2)
        number = number >> 1
    return bit_string


def reverse_bit(number):
    result = 0
    for _ in range(1, 33):
        result = result << 1
        end_bit = number % 2
        number = number >> 1
        result = result | end_bit
    return get_reverse_bit_string(result)