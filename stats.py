def get_num_words(text):
    """Returns the number of words in the given text."""
    return len(text.split())

def get_chars_dict(text):
    """Returns a dictionary of character counts (case-insensitive)."""
    chars = {}
    for char in text:
        lowered = char.lower()
        chars[lowered] = chars.get(lowered, 0) + 1
    return chars

def sort_on(item):
    """Helper function for sorting character dictionaries."""
    return item["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    """Converts character dictionary to a sorted list of {char, num} dicts."""
    sorted_list = [{"char": char, "num": count} for char, count in num_chars_dict.items()]
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
