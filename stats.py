def get_num_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    chars = {}
    for char in text:
        lowered = char.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_on(dict):
    return dict["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for item in num_chars_dict:
        sorted_list.append({"char": item, "num": num_chars_dict[item]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
