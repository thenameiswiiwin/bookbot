# BookBot

**BookBot** is a simple Python tool that analyzes text files (books) and generates a report with:

- Total word count
- Frequency and percentage of each alphabetic character

It can also save the report to a file.

---

## Features

- Reads a book text file (`.txt`)
- Counts total words
- Counts and sorts character frequencies (alphabetic only)
- Generates a detailed analysis report with percentages
- Saves the report to a file
- Includes unit tests for core functions

---

## Requirements

- Python 3.6+
- No external dependencies

---

## Usage

Run the script from the command line, providing the path to your book file:

```bash
python3 main.py path/to/book.txt
````

Example output:

```
============ BOOKBOT ============
Analyzing book found at path/to/book.txt...
----------- Word Count ----------
Found 35000 total words
--------- Character Count -------
e: 4000 (12.00%)
t: 3000 (9.00%)
a: 2800 (8.40%)
...
============= END ===============
```

---

## Saving the Report

You can modify the script to save the generated report to a file using the `save_report` function in `report.py`. Example:

```python
report = generate_report(book_path, num_words, chars_sorted_list)
save_report(report, "report.txt")
```

---

## Running Tests

Unit tests are provided to verify core functionality.

Run tests with:

```bash
python3 -m unittest discover tests
```

---

## Project Structure

```
bookbot/
├── main.py          # Main entry point
├── stats.py         # Text analysis functions
├── report.py        # Report generation and saving
├── tests/           # Unit tests
│   └── test_report.py
└── README.md
```
