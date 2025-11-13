import re

REGEX_LETER = "a-zA-ZäöüßÄÖÜ]"
Char_Count_Dict = dict[str, int]


def get_words_count(text: str):
    return len(text.split())


def sort_dict(dict: Char_Count_Dict):
    return sorted(dict.items(), key=lambda x: x[1], reverse=True)


def get_character_count(text: str):
    words = text.split()
    character_count: Char_Count_Dict = {}

    for word in words:
        for character in word:
            normalized = character.lower()

            if normalized in character_count:
                character_count[normalized] += 1
            else:
                character_count[normalized] = 1

    return character_count
