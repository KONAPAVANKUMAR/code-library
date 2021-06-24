def is_rotated(s1, s2):
    if len(s1) == len(s2):
        return s2 in s1 + s1
    else:
        return False


def is_rotated_v1(s1, s2):
    if len(s1) != len(s2):
        return False
    if len(s1) == 0:
        return True

    for c in range(len(s1)):
        if all(s1[(c + i) % len(s1)] == s2[i] for i in range(len(s1))):
            return True
    return False
