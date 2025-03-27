from textnode import TextNode, TextType
from split_nodes_delimiter import split_nodes_delimiter
from split_nodes_image import split_nodes_image
from split_nodes_link import split_nodes_link

#TODO: add type hinting to entire file

def text_to_textnodes(text):
    original_node = [TextNode(text, TextType.TEXT)]

    bold_nodes_split = split_nodes_delimiter(original_node, "**", TextType.BOLD)
    italic_nodes_split = split_nodes_delimiter(bold_nodes_split, "_", TextType.ITALIC)
    strikethrough_nodes_split = split_nodes_delimiter(italic_nodes_split, "~~", TextType.STRIKETHROUGH)
    code_nodes_split = split_nodes_delimiter(strikethrough_nodes_split, "`", TextType.CODE)
    image_nodes_split = split_nodes_image(code_nodes_split)
    link_nodes_split = split_nodes_link(image_nodes_split)

    return link_nodes_split