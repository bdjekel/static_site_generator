import unittest

from htmlnode import HTMLNode

#TODO: write more tests
#TODO: add type hinting to entire file

class TestHTMLNode(unittest.TestCase):
    def test_norm_no_children(self):
        node_props = {"class": "tester", "style":"color:red;"}
        node = HTMLNode("h1","Testing, testing, 1, 2, 3", props=node_props)
        self.assertIsNone(node.children)

    def test_no_tag(self):
        node_props = {"class": "tester", "style":"color:red;"}
        node = HTMLNode(value="Testing, testing, 1, 2, 3", children=["<p></p>","<a><a/>"], props=node_props)
        self.assertIsNone(node.tag)

    def test_no_props(self):
        node = HTMLNode("h1", "Testing, testing, 1, 2, 3", ["<p></p>","<a><a/>"])
        self.assertIsNone(node.props)
    
# TODO: Add test condition for multiple props.


if __name__ == "__main__":
    unittest.main()