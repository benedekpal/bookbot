def get_num_words(text):
    return len(text.split())

def get_num_chars(text):
    text = text.lower()
    character_count = {}

    for c in text:
        if c in character_count.keys():
            character_count[c] += 1
        else:
            character_count[c] = 1

    sorted_character_count = sorted(character_count.items(), key=lambda kv: kv[1], reverse=True)

    return sorted_character_count
