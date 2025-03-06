import unittest
from textnode import TextNode, TextType
from text_to_textnodes import text_to_textnodes

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

class TestTextToTextNode(unittest.TestCase):
    def test_all_split_types(self):
        resulting_nodes_all = text_to_textnodes(test_text_with_all)
        self.assertEqual(resulting_nodes_all, expected_nodes_all)

