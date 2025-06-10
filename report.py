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
        return True
    except Exception as e:
        print(f"Error saving report to {output_file}: {e}")
        return False
