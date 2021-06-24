
def delete_reoccurring_characters(string):
    seen_characters = set()
    output_string = ''
    for char in string:
        if char not in seen_characters:
            seen_characters.add(char)
            output_string += char
    return output_string

    