def get_num_words(words):
    individual_words = words.split()
    number = len(individual_words)
    return number
def letter_count(text):
    chars = {}
    for letter in text:
        lowered = letter.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars
def sorted_count_on(character_count):
    return character_count["num"]
def sorted_count(character_count):
    sorted_list = []
    for ch in character_count:
        sorted_list.append({"char": ch, "num": character_count[ch]})
    sorted_list.sort(reverse=True, key=sorted_count_on)
    return sorted_list
