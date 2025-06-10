import unittest
from stats import (
    get_num_words,
    get_chars_dict,
    chars_dict_to_sorted_list
)

class TestStatsFunctions(unittest.TestCase):
    def test_get_num_words(self):
        text = "Hello world, this is a test."
        self.assertEqual(get_num_words(text), 6)

    def test_get_chars_dict(self):
        text = "AaBbCc!"
        expected = {
            'a': 2,
            'b': 2,
            'c': 2,
            '!': 1
        }
        self.assertEqual(get_chars_dict(text), expected)

    def test_chars_dict_to_sorted_list(self):
        char_dict = {'a': 3, 'b': 1, 'c': 2}
        sorted_list = chars_dict_to_sorted_list(char_dict)
        expected = [
            {'char': 'a', 'num': 3},
            {'char': 'c', 'num': 2},
            {'char': 'b', 'num': 1}
        ]
        self.assertEqual(sorted_list, expected)

if __name__ == "__main__":
    unittest.main()
