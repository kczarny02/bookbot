def count_words(text):
    splitted_content = text.split()
    return len(splitted_content)


def count_characters(text):
    char_count = {}
    for char in text:
        if char == "\n":
            continue
        char_in_lower = char.lower()
        if char_in_lower in char_count:
            char_count[char_in_lower] += 1
        else:
            char_count[char_in_lower] = 1
    return char_count
