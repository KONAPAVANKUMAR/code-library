import math

def _l2_distance(vec):
    norm = 0.
    for e in vec:
        norm += e * e
    norm = math.sqrt(norm)
    return norm


def cosine_similarity(a, b):
    norm_a = _l2_distance(a)
    norm_b = _l2_distance(b)
    similarity = 0.
    for ae, be in zip(a, b):
        similarity += ae * be
    similarity /= (norm_a * norm_b)
    return similarity