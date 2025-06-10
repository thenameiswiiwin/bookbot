import sys
from stats import (
    get_num_words,
    get_chars_dict,
    chars_dict_to_sorted_list
)

def main():
    if len(sys.argv) < 2 or len(sys.argv) > 4:
        print("Usage: python3 main.py <path_to_book> [top_n] [output_flle]")
        sys.exit(1)

    book_path = sys.argv[1]
    top_n = int(sys.argv[2]) if len(sys.argv) >= 3 and sys.argv[2].isdigit() else None
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
        save_report(report, output_file)
        print(f"Report saved to {output_file}")
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

def generate_report(file_path, num_words, chars_sorted_list, top_n=None):
    """Generates and returns the analysis report as a string."""
    report_lines = []
    report_lines.append("============ BOOKBOT ============")
    report_lines.append(f"Analyzing book found at {file_path}...")
    report_lines.append("----------- Word Count ----------")
    report_lines.append(f"Found {num_words} total words")
    report_lines.append("--------- Character Count -------")

    alpha_chars = [c for c in chars_sorted_list if c["char"].isalpha()]
    total_alpha = sum(c["num"] for c in alpha_chars)
    chars_to_show = alpha_chars[:top_n] if top_n else alpha_chars

    for item in chars_to_show:
        percent = (item["num"] / total_alpha * 100)
        report_lines.append(f"{item['char']}: {item['num']} ({percent:.2f}%)")

    report_lines.append("============= END ===============")
    return "\n".join(report_lines)

def save_report(report, output_file):
    """Saves the report to a file."""
    try:
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(report)
    except Exception as e:
        print(f"Error saving report to {output_file}: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
