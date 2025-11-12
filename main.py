from stats import get_character_count, get_words_count

FRANKENSTEIN_BOOK_PATH = "books/frankenstein.txt"


def get_book_text(file_path: str) -> str:
    with open(file_path) as file:
        file_contents = file.read()
        return file_contents


def main() -> None:
    file = get_book_text(FRANKENSTEIN_BOOK_PATH)
    count = get_words_count(file)
    char_count = get_character_count(file)
    print(f"Found {count} total words")
    print(char_count)


main()
