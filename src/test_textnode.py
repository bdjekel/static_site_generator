import unittest

from textnode import TextNode
from htmlnode import HTMLNode
from leafnode import LeafNode

class TestTextNode(unittest.TestCase):

# Constructor Unit Tests

    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_diff_text_type(self):
        node = TextNode("This is a text node", "italic")
        node2 = TextNode("This is a text node", "bold")
        self.assertNotEqual(node, node2)

    def test_diff_url(self):
        node = TextNode("This is a text node", "bold","www.node.com")
        node2 = TextNode("This is a text node", "bold", "www.node2.com")
        self.assertNotEqual(node, node2)

# TextNode to HTMLNode Unit Tests
    def test_type_text(self):
        node = TextNode("text test", "text")
        node2 = LeafNode(None, node.text)
        self.assertEqual(node.text, node2.value)
        self.assertIsNone(node2.tag)
    def test_type_bold(self):
        node = TextNode("bold test", "bold")
        node2 = LeafNode("b", node.text)
        self.assertEqual(node.text, node2.value)
        self.assertEqual(node2.tag, "b")
    def test_type_italic(self):
        node = TextNode("italic test", "italic")
        node2 = LeafNode("i", node.text)
        self.assertEqual(node.text, node2.value)
        self.assertEqual(node2.tag, "i")
    def test_type_code(self):
        node = TextNode("code test", "code")
        node2 = HTMLNode("code", node.text)
        self.assertEqual(node.text, node2.value)
    def test_type_link(self):
        node = TextNode("link test", "link", "www.testlink.com")
        node2 = HTMLNode("link", node.text, None, {"href": f"{node.url}"})
        self.assertEqual(node2.tag, "link")
        self.assertEqual(node.text, node2.value)
        self.assertEqual(node.url, node2.props["href"])
    def test_type_image(self):
        node = TextNode("img test", "image", "www.testpicture.com")
        node2 = HTMLNode("img", "", None, {"src": f"{node.url}", "alt": f"{node.text}"})
        self.assertEqual(node2.tag, "img")
        self.assertEqual(node.text, node2.props["alt"])
        self.assertEqual(node.url, node2.props["src"])
        


if __name__ == "__main__":
    unittest.main()