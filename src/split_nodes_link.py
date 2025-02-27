import re
from textnode import TextNode
from textnode import TextType
from extract_markdown_links import extract_markdown_links


def split_nodes_image(old_nodes: list):
    new_nodes = []
    for node in old_nodes:
        sub_nodes = []
        sub_nodes_text = re.split(r"(?<!!)\[[^\[\]]*\]\([^\(\)]*\)", node.text)
        print(f"SUB_NODES_TEXT ==> {sub_nodes_text}")
        sub_nodes_text = [s for s in sub_nodes_text if len(s) > 0 and s != " "]
        for s in sub_nodes_text:
            if "![" in s:
                link_data = extract_markdown_links(s)
                sub_nodes.extend([TextNode(link_data[0][0], TextType.LINK, link_data[0][1])])
            else:
                sub_nodes.extend([TextNode(s, TextType.TEXT)])
        new_nodes.extend(sub_nodes)
    return new_nodes

