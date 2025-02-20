# import unittest
# from textnode import TextNode
# from split_nodes_image import split_nodes_image
# from extract_markdown_images import extract_markdown_images

# node_1 = TextNode('![to youtube](https://www.youtube.com/@bootdotdev)', 'text')
# node_2 = TextNode('![to boot dev](https://www.boot.dev) and', 'text')
# node_3 = TextNode('and ![to youtube](https://www.youtube.com/@bootdotdev)', 'text')
# node_4 = TextNode('![to boot dev](https://www.boot.dev) ![to youtube](https://www.youtube.com/@bootdotdev)', 'text')
# node_5 = TextNode('![to boot dev](https://www.boot.dev) <== Click this link for boot. Click this link for video ==> ![to youtube](https://www.youtube.com/@bootdotdev)', 'text')
# node_6 = TextNode('![to youtube](https://www.youtube.com/@bootdotdev) Click this image', 'text')
# node_7 = TextNode('This is text with a link ![to boot dev](https://www.boot.dev) and ![to youtube](https://www.youtube.com/@bootdotdev)', 'text')
# node_8 = TextNode('This is text with a link [to boot dev](https://www.boot.dev) and an image ![to youtube](https://www.youtube.com/@bootdotdev)', 'text')

# old_nodes = [
#     node_1,
#     node_2,
#     node_3,
#     node_4,
#     node_5,
#     node_6,
#     node_7,
#     node_8,
# ]

# expected_nodes_1 = [TextNode('to youtube', 'image', 'https://www.youtube.com/@bootdotdev)')]
# expected_nodes_2 = [
#     TextNode('to boot dev', 'image', 'https://www.boot.dev'), 
#     TextNode('and', 'text')
#     ]
# expected_nodes_3 = [
#     TextNode('and', 'text'), 
#     TextNode('to youtube', 'image', 'https://www.youtube.com/@bootdotdev)')
#     ]
# expected_nodes_4 = [
#     TextNode('to boot dev', 'image', 'https://www.boot.dev'), 
#     TextNode('to youtube', 'image', 'https://www.youtube.com/@bootdotdev)')
#     ]
# expected_nodes_5 = [
#     TextNode('to boot dev', 'image', 'https://www.boot.dev'), 
#     TextNode('<== Click this link for boot. Click this link for video ==>', 'text'), 
#     TextNode('to youtube', 'image', 'https://www.youtube.com/@bootdotdev)')
#     ]
# expected_nodes_6 = [
#     TextNode('to youtube', 'image', 'https://www.youtube.com/@bootdotdev)'),
#     TextNode('Click this image', 'text'), 

# ]


# class TestExtractMarkdownImages(unittest.TestCase):
#     def test_split_nodes_image(self):
        