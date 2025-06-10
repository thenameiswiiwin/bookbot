from stats import (
    get_num_words,
    get_chars_dict,
    chars_dict_to_sorted_list
)

def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()
