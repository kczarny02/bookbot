from stats import count_words, count_characters


def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()


def main():
    text = get_book_text("./books/frankenstein.txt")
    words_count = count_words(text)
    characters_count = count_characters(text)
    print(f"{words_count} words found in the document")
    print(characters_count)


main()
