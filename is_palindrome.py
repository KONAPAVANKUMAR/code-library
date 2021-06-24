
from string import ascii_letters


def is_palindrome(s):
    i = 0
    j = len(s)-1
    while i < j:
        while not s[i].isalnum():
            i += 1
        while not s[j].isalnum():
            j -= 1
        if s[i].lower() != s[j].lower():
            return False
        i, j = i+1, j-1
    return True


def remove_punctuation(s):
    return "".join(i.lower() for i in s if i in ascii_letters)

def string_reverse(s):
	return s[::-1]

def is_palindrome_reverse(s):
	s = remove_punctuation(s)
	if (s == string_reverse(s)): 
		return True
	return False	

