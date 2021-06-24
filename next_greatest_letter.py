import bisect
def next_greatest_letter(letters, target):
    index = bisect.bisect(letters, target)
    return letters[index % len(letters)]