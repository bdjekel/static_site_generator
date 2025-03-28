import unittest
from extract_title import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_correct_title_only(self):
        title = "# Hello"
        expected_title = "Hello"
        self.assertEqual(extract_title(title), expected_title)

    def test_incorrect_title_only(self):
        title = "## Hell0000o"
        self.assertRaises(ValueError, extract_title, title)

    def test_correct_title_multiline(self):
        title = """
        # Hello
        LMNOP
        Seventy eight twenty two
        More words
        """
        expected_title = "Hello"
        self.assertEqual(extract_title(title), expected_title)