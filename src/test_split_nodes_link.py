# TODO: tests could be more rigorous. Consider writing more.

import unittest
from textnode import TextNode
from textnode import TextType
from split_nodes_link import split_nodes_link

node_1 = TextNode('[to youtube](https://www.youtube.com/@bootdotdev)', TextType.TEXT)
node_2 = TextNode('[to boot dev](https://www.boot.dev) and', TextType.TEXT)
node_3 = TextNode('and [to youtube](https://www.youtube.com/@bootdotdev)', TextType.TEXT)
node_4 = TextNode('[to boot dev](https://www.boot.dev) [to youtube](https://www.youtube.com/@bootdotdev)', TextType.TEXT)
node_5 = TextNode('[to boot dev](https://www.boot.dev) <== Click this link for boot. Click this link for video ==> [to youtube](https://www.youtube.com/@bootdotdev)', TextType.TEXT)
node_6 = TextNode('[to youtube](https://www.youtube.com/@bootdotdev) Click this link', TextType.TEXT)
node_7 = TextNode('This is text with two links [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)', TextType.TEXT)
node_8 = TextNode('This is text with a link [to boot dev](https://www.boot.dev) and an image ![to youtube](https://www.youtube.com/@bootdotdev)', TextType.TEXT)

old_nodes = [
    node_1,
    node_2,
    node_3,
    node_4,
    node_5,
    node_6,
    node_7,
    node_8,
]

expected_node_1 = [TextNode('to youtube', TextType.LINK, 'https://www.youtube.com/@bootdotdev')]
expected_node_2 = [
    TextNode('to boot dev', TextType.LINK, 'https://www.boot.dev'), 
    TextNode(' and', TextType.TEXT)
    ]
expected_node_3 = [
    TextNode('and ', TextType.TEXT), 
    TextNode('to youtube', TextType.LINK, 'https://www.youtube.com/@bootdotdev')
    ]
expected_node_4 = [
    TextNode('to boot dev', TextType.LINK, 'https://www.boot.dev'), 
    TextNode('to youtube', TextType.LINK, 'https://www.youtube.com/@bootdotdev')
    ]
expected_node_5 = [
    TextNode('to boot dev', TextType.LINK, 'https://www.boot.dev'), 
    TextNode(' <== Click this link for boot. Click this link for video ==> ', TextType.TEXT), 
    TextNode('to youtube', TextType.LINK, 'https://www.youtube.com/@bootdotdev')
    ]
expected_node_6 = [
    TextNode('to youtube', TextType.LINK, 'https://www.youtube.com/@bootdotdev'),
    TextNode(' Click this link', TextType.TEXT), 

]
expected_node_7 = [
    TextNode('This is text with two links ', TextType.TEXT),
    TextNode('to boot dev', TextType.LINK, 'https://www.boot.dev'), 
    TextNode(' and ', TextType.TEXT),
    TextNode('to youtube', TextType.LINK, 'https://www.youtube.com/@bootdotdev')
]

expected_node_8 = [
    TextNode('This is text with a link ', TextType.TEXT), 
    TextNode('to boot dev', TextType.LINK, 'https://www.boot.dev'),
    TextNode(' and an image ![to youtube](https://www.youtube.com/@bootdotdev)', TextType.TEXT)
]

expected_nodes = expected_node_1 + expected_node_2 + expected_node_3 + expected_node_4 + expected_node_5 + expected_node_6 + expected_node_7 + expected_node_8



class TestExtractMarkdownLinks(unittest.TestCase):
    def test_isolated_split_nodes_link(self):
        resulting_node = split_nodes_link([node_1])
        self.assertEqual([resulting_node], [expected_node_1])
    def test_all_split_nodes_link(self):
        self.maxDiff = None
        resulting_nodes = split_nodes_link(old_nodes)
        self.assertEqual(resulting_nodes, expected_nodes)

