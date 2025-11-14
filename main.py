import sys
from typing import Literal

from stats import get_character_count, get_words_count, sort_dict

MIN_SYS_ARG = 2

Decoration = Literal["bookbot", "word-count", "char-count", "end"]


def check_sys_argv():
    if len(sys.argv) < MIN_SYS_ARG:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


def get_book_text(file_path: str) -> str:
    with open(file_path) as file:
        file_contents = file.read()
        return file_contents


def get_text_decorate(decoration: Decoration):
    print_message: dict[Decoration, str] = {
        "bookbot": "============ BOOKBOT ============",
        "word-count": "----------- Word Count ----------",
        "char-count": "--------- Character Count -------",
        "end": "============= END ===============",
    }

    return print_message[decoration]


def print_logs(count: int, book_path: str, char_count: list[tuple[str, int]]):
    print(get_text_decorate("bookbot"))
    print(f"Analyzing book found at {book_path}")
    print(get_text_decorate("word-count"))
    print(f"Found {count} total words")
    print(get_text_decorate("char-count"))

    for char in char_count:
        if not char[0].isalpha():
            continue

        print(f"{char[0]}: {char[1]}")

    print(get_text_decorate("end"))


def main() -> None:
    check_sys_argv()
    book_path = sys.argv[1]
    file = get_book_text(book_path)
    count = get_words_count(file)
    char_count = get_character_count(file)
    sorted = sort_dict(char_count)

    print_logs(count, book_path, sorted)


main()
