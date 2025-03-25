# TODO: tests could be more rigorous. Consider writing more.

import unittest
from extract_markdown_links import extract_markdown_links

sb_meme = '../assets/tired_spongebob.webp'
raw_md_link_string = f'Spongebob Squarepants is a show about enjoying the [little things]({sb_meme}) in life.'
raw_md_image_string = f'Spongebob Squarepants is a show about enjoying the ![little things]({sb_meme}) in life.'

expected_result_1 = [('little things', sb_meme)]
expected_result_2 = []

class TestExtractMarkdownLinks(unittest.TestCase):
    def test_single_link_string_normal(self):
        acutal_result = extract_markdown_links(raw_md_link_string)
        self.assertEqual(acutal_result, expected_result_1)

    def test_single_image_string_normal(self):
        acutal_result = extract_markdown_links(raw_md_image_string)
        self.assertEqual(acutal_result, expected_result_2)

if __name__ == "__main__":
    unittest.main()