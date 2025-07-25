import sys
from stats import count_words, count_characters, sort_characters_count


def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    words_count = count_words(text)
    characters_count = count_characters(text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {words_count} total words")
    print("--------- Character Count -------")
    sort_characters_count(characters_count)
    print("============= END ===============")


main()
