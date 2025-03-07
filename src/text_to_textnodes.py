from textnode import TextNode, TextType
from split_nodes_delimiter import split_nodes_delimiter
from split_nodes_image import split_nodes_image
from split_nodes_link import split_nodes_link

def text_to_textnodes(text):
    original_node = [TextNode(text, TextType.TEXT)]
    # print(f"ORIGINAL_NODE ==>\n\n{original_node}\n\n")

    bold_nodes_split = split_nodes_delimiter(original_node, "**", TextType.BOLD)
    # print(f"BOLD_NODES_SPLIT ==>\n\n{bold_nodes_split}\n\n")
    italic_nodes_split = split_nodes_delimiter(bold_nodes_split, "_", TextType.ITALIC)
    # print(f"ITALIC_NODES_SPLIT ==>\n\n{italic_nodes_split}\n\n")
    strikethrough_nodes_split = split_nodes_delimiter(italic_nodes_split, "~~", TextType.STRIKETHROUGH)
    # print(f"STRIKETHROUGH_NODES_SPLIT ==>\n\n{strikethrough_nodes_split}\n\n")
    code_nodes_split = split_nodes_delimiter(strikethrough_nodes_split, "`", TextType.CODE)
    # print(f"CODE_NODES_SPLIT ==>\n\n{code_nodes_split}\n\n")

    image_nodes_split = split_nodes_image(code_nodes_split)
    # print(f"IMAGE_NODES_SPLIT ==>\n\n{image_nodes_split}\n\n")

    link_nodes_split = split_nodes_link(image_nodes_split)
    # print(f"LINK_NODES_SPLIT ==>\n\n{link_nodes_split}\n\n")


    return link_nodes_split