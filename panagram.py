
from string import ascii_lowercase

def panagram(string):
    letters = set(ascii_lowercase)
    for c in string:
        try:
            letters.remove(c.lower())
        except:
            pass
    return len(letters) == 0