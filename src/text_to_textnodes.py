from textnode import TextNode, TextType
from split_nodes_delimiter import split_nodes_delimiter
from split_nodes_image import split_nodes_image
from split_nodes_link import split_nodes_link

#TODO: add type hinting to entire file

def text_to_textnodes(text):
    text_nodes = [TextNode(text, TextType.TEXT)]

    text_nodes = split_nodes_image(text_nodes)
    text_nodes = split_nodes_link(text_nodes)
    text_nodes = split_nodes_delimiter(text_nodes, "**", TextType.BOLD)
    text_nodes = split_nodes_delimiter(text_nodes, "_", TextType.ITALIC)
    text_nodes = split_nodes_delimiter(text_nodes, "~~", TextType.STRIKETHROUGH)
    text_nodes = split_nodes_delimiter(text_nodes, "`", TextType.CODE)

    return text_nodes