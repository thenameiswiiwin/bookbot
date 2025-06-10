def get_num_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    chars = {}
    for char in text:
        lowered = char.lower()
        chars[lowered] = chars.get(lowered, 0) + 1
    return chars

def sort_on(entry):
    return entry["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = [{"char": char, "num": count} for char, count in num_chars_dict.items()]
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
