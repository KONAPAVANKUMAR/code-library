

def binary_and(a: int, b: int) -> str:

    a = str(bin(a))[2:]
    a = str(bin(b))[2:]

    max_len = max(len(a), len(b))

    return "0b" + "".join(
        str(int(char_a == "1" and char_b == "1"))
        for char_a, char_b in zip(a.zfill(max_len), b.zfill(max_len))
    )
