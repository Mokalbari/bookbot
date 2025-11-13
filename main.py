from typing import Literal

from stats import Char_Count_Dict, get_character_count, get_words_count, sort_dict

FRANKENSTEIN_BOOK_PATH = "books/frankenstein.txt"

Decoration = Literal["bookbot", "word-count", "char-count"]


def get_book_text(file_path: str) -> str:
    with open(file_path) as file:
        file_contents = file.read()
        return file_contents


def get_text_decorate(decoration: Decoration):
    print_message: dict[Decoration, str] = {
        "bookbot": "============ BOOKBOT ============",
        "word-count": "----------- Word Count ----------",
        "char-count": "--------- Character Count -------",
    }

    return print_message[decoration]


def print_logs(count: int, char_count: Char_Count_Dict):
    print(get_text_decorate("bookbot"))
    print(f"Analyzing book found at {FRANKENSTEIN_BOOK_PATH}")
    print(get_text_decorate("word-count"))
    print(f"Found {count} total words")
    print(get_text_decorate("char-count"))


def main() -> None:
    file = get_book_text(FRANKENSTEIN_BOOK_PATH)
    count = get_words_count(file)
    char_count = get_character_count(file)
    sorted = sort_dict(char_count)

    print_logs(count, sorted)


main()
