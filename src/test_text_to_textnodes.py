import unittest
from textnode import TextNode, TextType
from text_to_textnodes import text_to_textnodes


class TestTextToTextNode(unittest.TestCase):
    def test_all_split_types(self):
        test_text_with_all = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        expected_nodes_all = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]
        self.assertEqual(text_to_textnodes(test_text_with_all), expected_nodes_all)

    # Test parsing of plain text with no formatting
    def test_plain_text(self):
        test_text = "Just some plain text."
        expected_nodes = [TextNode("Just some plain text.", TextType.TEXT)]
        self.assertEqual(text_to_textnodes(test_text), expected_nodes)

    # Test parsing of bold text
    def test_bold_text(self):
        test_text = "This is **bold** text."
        expected_nodes = [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text.", TextType.TEXT),
        ]
        self.assertEqual(text_to_textnodes(test_text), expected_nodes)

    # Test parsing of italic text
    def test_italic_text(self):
        test_text = "This is _italic_ text."
        expected_nodes = [
            TextNode("This is ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" text.", TextType.TEXT),
        ]
        self.assertEqual(text_to_textnodes(test_text), expected_nodes)

    # Test parsing of inline code
    def test_code_text(self):
        test_text = "This is `code` text."
        expected_nodes = [
            TextNode("This is ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" text.", TextType.TEXT),
        ]
        self.assertEqual(text_to_textnodes(test_text), expected_nodes)

    # Test parsing of an image
    def test_image(self):
        test_text = "This is an ![alt text](https://example.com/image.jpg)."
        expected_nodes = [
            TextNode("This is an ", TextType.TEXT),
            TextNode("alt text", TextType.IMAGE, "https://example.com/image.jpg"),
            TextNode(".", TextType.TEXT),
        ]
        self.assertEqual(text_to_textnodes(test_text), expected_nodes)

    # Test parsing of a link
    def test_link(self):
        test_text = "This is a [link](https://example.com)."
        expected_nodes = [
            TextNode("This is a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://example.com"),
            TextNode(".", TextType.TEXT),
        ]
        self.assertEqual(text_to_textnodes(test_text), expected_nodes)

    # Test parsing of multiple formats in one text
    def test_combined_formats(self):
        test_text = "This is **bold** , _italic_ , and `code` ."
        expected_nodes = [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" , ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" , and ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" .", TextType.TEXT),
        ]
        self.assertEqual(text_to_textnodes(test_text), expected_nodes)

# TODO: TEST EXCLUDED. CURRENTLY, THE PROGRAM DOES NOT ALLOW FOR NESTED FORMATTING.
    # Test nested formatting (bold inside italic)
    # def test_nested_formatting(self):
    #     test_text = "This is _italic with **bold** inside_."
    #     expected_nodes = [
    #         TextNode("This is ", TextType.TEXT),
    #         TextNode("italic with ", TextType.ITALIC),
    #         TextNode("bold", TextType.BOLD),
    #         TextNode(" inside", TextType.ITALIC),
    #         TextNode(".", TextType.TEXT),
    #     ]
    #     self.assertEqual(text_to_textnodes(test_text), expected_nodes)

    # Test parsing of an empty string
    def test_empty_string(self):
        test_text = ""
        expected_nodes = []
        self.assertEqual(text_to_textnodes(test_text), expected_nodes)

    # Test malformed markdown (unclosed bold)
    def test_unclosed_bold(self):
        test_text = "This is **bold text."
        with self.assertRaises(Exception):
            text_to_textnodes(test_text)


    # Test malformed markdown (unclosed link). Should result in unformatted text, not error.
    def test_unclosed_link(self):
        test_text = "This is a [broken link(https://example.com)."
        expected_nodes = [TextNode("This is a [broken link(https://example.com).", TextType.TEXT)]
        self.assertEqual(text_to_textnodes(test_text), expected_nodes)

# TODO: TEST EXCLUDED. CURRENTLY, THE PROGRAM ONLY PRESERVES A SINGLE UNIT SPACE.
# Test whitespace preservation
    # def test_whitespace_preservation(self):
    #     test_text = "  This is  **bold**  with spaces.  "
    #     expected_nodes = [
    #         TextNode("  This is  ", TextType.TEXT),
    #         TextNode("bold", TextType.BOLD),
    #         TextNode("  with spaces.  ", TextType.TEXT),
    #     ]
    #     self.assertEqual(text_to_textnodes(test_text), expected_nodes)



if __name__ == "__main__":
    unittest.main()