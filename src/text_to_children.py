from htmlnode import HTMLNode
from text_to_textnodes import text_to_textnodes
from textnode import TextType

def text_to_children(markdown):
    children = []
    text_nodes = text_to_textnodes(markdown)
    print(f"text_nodes ==> {text_nodes}")
    
    for node in text_nodes:
        if node.text_type is TextType.IMAGE:
            image_node = HTMLNode(
                tag = node.text_type.value, 
                props = {"src" : node.url, "alt" : node.text})
            children.append(image_node)
            print(f"IMAGE ADDED TO CHILDREN ==> {children}")
        elif node.text_type is TextType.LINK:
            link_node = HTMLNode(
                tag = node.text_type.value,
                value = node.text,
                props = {"href" : node.url}
            )
            children.append(link_node)
            print(f"LINK ADDED TO CHILDREN ==> {children}")
        elif node.text_type is TextType.TEXT:
            plaintext_node = HTMLNode(value = node.text)
            children.append(plaintext_node)
            print(f"TEXT ADDED TO CHILDREN ==> {children}")
        else:
            emphasized_node = HTMLNode(
                tag = node.text_type.value,
                value = node.text
            )
            children.append(emphasized_node)
            print(f"EMPHASIZED ADDED TO CHILDREN ==> {children}")
    return children

#TODO: Move below to test file. Write more tests.
markdown = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
# expected_nodes_all = [
#     TextNode("This is ", TextType.TEXT),
#     TextNode("text", TextType.BOLD),
#     TextNode(" with an ", TextType.TEXT),
#     TextNode("italic", TextType.ITALIC),
#     TextNode(" word and a ", TextType.TEXT),
#     TextNode("code block", TextType.CODE),
#     TextNode(" and an ", TextType.TEXT),
#     TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
#     TextNode(" and a ", TextType.TEXT),
#     TextNode("link", TextType.LINK, "https://boot.dev"),
# ]

text_to_children(markdown)