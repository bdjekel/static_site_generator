import re
from textnode import TextNode
from textnode import TextType
from extract_markdown_images import extract_markdown_images


def split_nodes_image(old_nodes: list):
    new_nodes = []
    for node in old_nodes:
        sub_nodes = []
        sub_nodes_text = re.split(r"(!\[[^\[\]]*\]\([^\(\)]*\))", node.text)
        sub_nodes_text = [s for s in sub_nodes_text if s != ""]
        for s in sub_nodes_text:
            if "![" in s:
                image_data = extract_markdown_images(s)
                print(f"IMAGE DATA ==> {image_data}")
                sub_nodes.extend([TextNode(image_data[0][0], TextType.IMAGE, image_data[0][1])])
            else:
                sub_nodes.extend([TextNode(s, TextType.TEXT)])
        print(f"SUB_NODES ==> {sub_nodes}")
        new_nodes.extend(sub_nodes)



            

    print("new_nodes)
    return new_nodes


