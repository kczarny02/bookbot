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


def sort_characters_count(char_count):
    list_of_dicts = []
    for key in char_count:
        if key.isalpha():
            char_dict = {
                "char": key,
                "num": char_count[key]
            }
            list_of_dicts.append(char_dict)

    def sort_on(items):
        return items["num"]

    sorted_list = sorted(list_of_dicts, reverse=True, key=sort_on)
    for item in sorted_list:
        char = item["char"]
        num = item["num"]
        print(f"{char}: {num}")
