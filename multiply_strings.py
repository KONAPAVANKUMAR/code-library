

def multiply(num1: "str", num2: "str") -> "str":
    interm = []
    zero = ord('0')
    i_pos = 1
    for i in reversed(num1):
        j_pos = 1
        add = 0
        for j in reversed(num2):
            mult = (ord(i)-zero) * (ord(j)-zero) * j_pos * i_pos
            j_pos *= 10
            add += mult
        i_pos *= 10
        interm.append(add)
    return str(sum(interm))

