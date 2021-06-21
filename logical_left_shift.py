def logical_left_shift(number: int, shift_amount: int):
    binary_number = str(bin(number))
    binary_number += "0" * shift_amount
    return binary_number