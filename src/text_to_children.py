from leafnode import LeafNode
from text_to_textnodes import text_to_textnodes
from textnode import TextType, TextNode

#TODO: add type hinting to entire file

def text_to_children(markdown: str) -> list[LeafNode]:
    children: list[LeafNode] = []
    text_nodes: list[TextNode] = text_to_textnodes(markdown)
    
    for node in text_nodes:
        match node.text_type:
            case TextType.IMAGE:
                image_node: LeafNode = LeafNode(
                    tag = node.text_type.value,
                    value = "",
                    props = {"src" : node.url, "alt" : node.text})
                children.append(image_node)
            case TextType.LINK:
                link_node: LeafNode = LeafNode(
                    tag = node.text_type.value,
                    value = node.text,
                    props = {"href" : node.url}
                )

                children.append(link_node)
            case TextType.TEXT:
                plaintext_node: LeafNode = LeafNode(value = node.text)
                children.append(plaintext_node)
            case _:
                emphasized_node: LeafNode = LeafNode(
                    tag = node.text_type.value,
                    value = node.text
                )
                children.append(emphasized_node)
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