Char_Count_Dict = dict[str, int]


def get_words_count(text: str):
    return len(text.split())


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
