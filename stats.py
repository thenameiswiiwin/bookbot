def get_num_words(text):
    return len(text.split())

def get_num_chars(text):
    chars = {}
    for char in text.lower():
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars

def sort_on(d):
    return d["num"]

def sorted_list(dict):
    list = []
    for char in dict:
        list.append({"char": char, "num": dict[char]})
    list.sort(reverse=True, key=sort_on)
    return list
