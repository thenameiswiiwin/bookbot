import sys
from report import (
    generate_report,
    save_report
)
from stats import (
    get_num_words,
    get_chars_dict,
    chars_dict_to_sorted_list
)

def main():
    if len(sys.argv) < 2 or len(sys.argv) > 4:
        print("Usage: python3 main.py <path_to_book> [top_n] [output_file]")
        sys.exit(1)

    book_path = sys.argv[1]

    # Parse top_n if provided and positive integer
    top_n = None
    if len(sys.argv) >= 3:
        if sys.argv[2].isdigit() and int(sys.argv[2]) > 0:
            top_n = int(sys.argv[2])
        else:
            print("Error: top_n must be a positive integer")
            sys.exit(1)

    output_file = sys.argv[3] if len(sys.argv) == 4 else None

    text = get_book_text(book_path)
    if not text.strip():
        print("Warning: The file appears to be empty or unreadable.")
        sys.exit(1)

    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)

    report = generate_report(book_path, num_words, chars_sorted_list, top_n)

    if output_file:
        if save_report(report, output_file):
            print(f"Report saved to {output_file}")
        else:
            print(f"Failed to save report to {output_file}")
            sys.exit(1)
    else:
        print(report)

def get_book_text(file_path):
    """Reads the text from a file and returns it as a string."""
    try:
        with open(file_path, encoding="utf-8") as f:
            text = f.read()
        print(f"Successfully read the book file: {file_path}")
        return text
    except FileNotFoundError:
        print(f"Error: File not found: {file_path}")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
