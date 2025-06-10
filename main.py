def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    print(text)

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()
