import unittest
from markdown_to_blocks import markdown_to_blocks

#TODO: write more tests
#TODO: add type hinting to entire file

class TestMarkdownToBlocks(unittest.TestCase):
    def test_v1(self):
        pass
    def test_markdown_to_blocks(self):
        self.maxDiff == None
        md = """
            This is **bolded** paragraph

            This is another paragraph with _italic_ text and `code` here
            This is the same paragraph on a new line

            - This is a list
            - with items
            """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

if __name__ == "__main__":
    unittest.main()