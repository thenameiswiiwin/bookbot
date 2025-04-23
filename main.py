import sys
from stats import (
        get_num_words, 
        get_num_chars,
        sorted_list,
)

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    text = get_book_text(path)
    num_words = get_num_words(text)
    num_chars = get_num_chars(text)
    sorted = sorted_list(num_chars)
    print_report(path, num_words, sorted)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def print_report(path, num_words, sorted):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")


main()
