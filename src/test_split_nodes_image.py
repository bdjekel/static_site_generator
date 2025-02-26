# TODO: uncomment below code and complete testing for split nodes image.

import unittest
from textnode import TextNode
from textnode import TextType
from split_nodes_image import split_nodes_image
from extract_markdown_images import extract_markdown_images

node_1 = TextNode('![to youtube](https://www.youtube.com/@bootdotdev)', TextType.TEXT)
node_2 = TextNode('![to boot dev](https://www.boot.dev) and', TextType.TEXT)
node_3 = TextNode('and ![to youtube](https://www.youtube.com/@bootdotdev)', TextType.TEXT)
node_4 = TextNode('![to boot dev](https://www.boot.dev) ![to youtube](https://www.youtube.com/@bootdotdev)', TextType.TEXT)
node_5 = TextNode('![to boot dev](https://www.boot.dev) <== Click this link for boot. Click this link for video ==> ![to youtube](https://www.youtube.com/@bootdotdev)', TextType.TEXT)
node_6 = TextNode('![to youtube](https://www.youtube.com/@bootdotdev) Click this image', TextType.TEXT)
node_7 = TextNode('This is text with two images ![to boot dev](https://www.boot.dev) and ![to youtube](https://www.youtube.com/@bootdotdev)', TextType.TEXT)
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

expected_node_1 = [TextNode('to youtube', TextType.IMAGE, 'https://www.youtube.com/@bootdotdev')]
expected_node_2 = [
    TextNode('to boot dev', TextType.IMAGE, 'https://www.boot.dev'), 
    TextNode(' and', TextType.TEXT)
    ]
expected_node_3 = [
    TextNode('and ', TextType.TEXT), 
    TextNode('to youtube', TextType.IMAGE, 'https://www.youtube.com/@bootdotdev')
    ]
expected_node_4 = [
    TextNode('to boot dev', TextType.IMAGE, 'https://www.boot.dev'), 
    TextNode('to youtube', TextType.IMAGE, 'https://www.youtube.com/@bootdotdev')
    ]
expected_node_5 = [
    TextNode('to boot dev', TextType.IMAGE, 'https://www.boot.dev'), 
    TextNode(' <== Click this link for boot. Click this link for video ==> ', TextType.TEXT), 
    TextNode('to youtube', TextType.IMAGE, 'https://www.youtube.com/@bootdotdev')
    ]
expected_node_6 = [
    TextNode('to youtube', TextType.IMAGE, 'https://www.youtube.com/@bootdotdev'),
    TextNode(' Click this image', TextType.TEXT), 

]
expected_node_7 = [
    TextNode('This is text with two images ', TextType.TEXT),
    TextNode('to boot dev', TextType.IMAGE, 'https://www.boot.dev'), 
    TextNode(' and ', TextType.TEXT),
    TextNode('to youtube', TextType.IMAGE, 'https://www.youtube.com/@bootdotdev')
]

expected_node_8 = [
    TextNode('This is text with a link [to boot dev](https://www.boot.dev) and an image ', TextType.TEXT),
    TextNode('to youtube', TextType.IMAGE, 'https://www.youtube.com/@bootdotdev')
]

expected_nodes = expected_node_1 + expected_node_2 + expected_node_3 + expected_node_4 + expected_node_5 + expected_node_6 + expected_node_7 + expected_node_8



class TestExtractMarkdownImages(unittest.TestCase):
    def test_isolated_split_nodes_image(self):
        resulting_node = split_nodes_image([node_1])
        self.assertEqual([resulting_node], [expected_node_1])
    def test_all_split_nodes_image(self):
        resulting_nodes = split_nodes_image(old_nodes)
        self.assertEqual(resulting_nodes, expected_nodes)

