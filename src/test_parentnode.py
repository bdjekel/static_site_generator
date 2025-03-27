import unittest
from leafnode import LeafNode
from parentnode import ParentNode

#TODO: write more tests
#TODO: add type hinting to entire file

class TestParentNode(unittest.TestCase):
    def test_no_children(self):
        node = ParentNode("p")
        self.assertRaises(ValueError, lambda: node.to_html())
    
    def test_no_tag(self):
        node = ParentNode(children=['child_x', 'child_y'])
        self.assertRaises(ValueError, lambda: node.to_html())

    def test_norm_with_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertIsNotNone(lambda: node.to_html())      
                

if __name__ == "__main__":
    unittest.main()

