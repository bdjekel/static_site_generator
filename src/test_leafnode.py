import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_no_value(self):
        node = LeafNode("p")
        self.assertRaises(ValueError, lambda: node.to_html())
    
    def test_has_children(self):
        node = LeafNode("p","This is the value", ['child_x', 'child_y'])
        self.assertIsNone(node.children)

    def test_no_tag(self):
        node = LeafNode(value="no tag here.")
        self.assertEqual(node.tag, "")
        self.assertEqual(node.to_html(), node.value)
        
        

if __name__ == "__main__":
    unittest.main()