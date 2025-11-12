FRANKENSTEIN_BOOK_PATH = "books/frankenstein.txt"


def get_book_text(file_path: str) -> str:
    with open(file_path) as file:
        file_contents = file.read()
        return file_contents


def get_words_count(text: str) -> int:
    return len(text.split())


def main() -> None:
    file = get_book_text(FRANKENSTEIN_BOOK_PATH)
    count = get_words_count(file)
    print(f"Found {count} total words")


main()
