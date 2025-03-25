from leafnode import LeafNode
from text_to_textnodes import text_to_textnodes
from textnode import TextType

def text_to_children(markdown):
    children = []
    text_nodes = text_to_textnodes(markdown)
    # print(f"text_nodes ==> {text_nodes}")
    
    for node in text_nodes:
        match node.text_type:
            case TextType.IMAGE:
                image_node = LeafNode(
                    tag = node.text_type.value,
                    value = "",
                    props = {"src" : node.url, "alt" : node.text})
                children.append(image_node)
                # print(f"IMAGE ADDED TO CHILDREN ==> {children}")
            case TextType.LINK:
                link_node = LeafNode(
                    tag = node.text_type.value,
                    value = node.text,
                    props = {"href" : node.url}
                )
                # print("\n\n--------LINK NODE--------\n\n")
                print(f"{link_node}")
                # print("\n\n--------LINK NODE--------\n\n")

                children.append(link_node)
                # print(f"LINK ADDED TO CHILDREN ==> {children}")
            case TextType.TEXT:
                plaintext_node = LeafNode(value = node.text)
                children.append(plaintext_node)
                # print(f"TEXT ADDED TO CHILDREN ==> {children}")
            case _:
                emphasized_node = LeafNode(
                    tag = node.text_type.value,
                    value = node.text
                )
                children.append(emphasized_node)
                # print(f"EMPHASIZED ADDED TO CHILDREN ==> {children}")
    # print(f"\n------------------\ntext_to_children RETURNS:\n{children}\n------------------\n")
    return children

#TODO: Move below to test file. Write more tests.


# markdown = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
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

# text_to_children(markdown)