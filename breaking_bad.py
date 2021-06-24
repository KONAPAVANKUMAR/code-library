
from functools import reduce


def match_symbol(words, symbols):
    import re
    combined = []
    for s in symbols:
        for c in words:
            r = re.search(s, c)
            if r:
                combined.append(re.sub(s, "[{}]".format(s), c))
    return combined

def match_symbol_1(words, symbols):
    res = []
    symbols = sorted(symbols, key=lambda _: len(_), reverse=True)
    for word in words:
        for symbol in symbols:
            word_replaced = ''
            if word.find(symbol) != -1:
                word_replaced = word.replace(symbol, '[' + symbol + ']')
                res.append(word_replaced)
                break
        if word_replaced == '':
            res.append(word)
    return res


class TreeNode:
    def __init__(self):
        self.c = dict()
        self.sym = None


def bracket(words, symbols):
    root = TreeNode()
    for s in symbols:
        t = root
        for char in s:
            if char not in t.c:
                t.c[char] = TreeNode()
            t = t.c[char]
        t.sym = s
    result = dict()
    for word in words:
        i = 0
        symlist = list()
        while i < len(word):
            j, t = i, root
            while j < len(word) and word[j] in t.c:
                t = t.c[word[j]]
                if t.sym is not None:
                    symlist.append((j + 1 - len(t.sym), j + 1, t.sym))
                j += 1
            i += 1
        if len(symlist) > 0:
            sym = reduce(lambda x, y: x if x[1] - x[0] >= y[1] - y[0] else y,
                         symlist)
            result[word] = "{}[{}]{}".format(word[:sym[0]], sym[2],
                                             word[sym[1]:])
    return tuple(word if word not in result else result[word] for word in words)
