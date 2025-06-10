import unittest
import os
from report import generate_report, save_report

class TestReport(unittest.TestCase):
    def test_generate_report_basic(self):
        book_path = "sample.txt"
        num_words = 100
        char_data = [
            {'char': 'e', 'num': 30},
            {'char': 't', 'num': 20},
            {'char': 'a', 'num': 10},
            {'char': '.', 'num': 10}
        ]

        expected_substring = [
            "Analyzing book found at sample.txt",
            "Found 100 total words",
            "e: 30 (50.00%)",
            "t: 20 (33.33%)",
            "a: 10 (16.67%)"
        ]

        report = generate_report(book_path, num_words, char_data)

        for line in expected_substring:
            self.assertIn(line, report)

    def test_generate_report_top_n(self):
        book_path = "topn.txt"
        num_words = 200
        char_data = [
            {'char': 'z', 'num': 50},
            {'char': 'y', 'num': 30},
            {'char': 'x', 'num': 20}
        ]

        report = generate_report(book_path, num_words, char_data, top_n=2)
        self.assertIn("z: 50", report)
        self.assertIn("y: 30", report)
        self.assertNotIn("x: 20", report)

    def test_save_report(self):
        content = "This is a test report"
        output_path = "tests/temp_report.txt"

        success = save_report(content, output_path)
        self.assertTrue(success)
        self.assertTrue(os.path.exists(output_path))

        with open(output_path, "r", encoding="utf-8") as f:
            read_content = f.read()
        self.assertEqual(read_content, content)

        # Cleanup
        os.remove(output_path)

if __name__ == "__main__":
    unittest.main()
