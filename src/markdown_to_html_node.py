from block_to_block_type import block_to_block_type, BlockType
from htmlnode import HTMLNode
from leafnode import LeafNode
from markdown_to_blocks import markdown_to_blocks
from parentnode import ParentNode
from text_to_children import text_to_children

#TODO: add type hinting to entire file

def markdown_to_html_node(markdown: str) -> ParentNode:
    
    wrapper_div: ParentNode = ParentNode("div", children=[])
    markdown_blocks: list[str] = markdown_to_blocks(markdown)
    print("----------------------------------")
    for i, block in enumerate(markdown_blocks):
        print(f"\nvvBlock #{i}vv\n{block}\n")
    print("----------------------------------")
    
    for block in markdown_blocks:

        block_type: BlockType = block_to_block_type(block)


        match block_type:

#TODO: Add feature to allow for markdown within headings?
            case BlockType.HEADING1 | BlockType.HEADING2 | BlockType.HEADING3 | BlockType.HEADING4 | BlockType.HEADING5 | BlockType.HEADING6:
                block: str = block.strip("#")
                block: str = block.strip()
                heading_node: HTMLNode = LeafNode(block_type.value, block)
                wrapper_div.children.append(heading_node)

            case BlockType.CODE:
                block: str = block.strip("`")
                block: str = block.strip()
                code_node: LeafNode = LeafNode(block_type.value, block)
                wrapper_div.children.append(code_node)

#TODO: Add feature to allow for markdown within blockquotes?
            case BlockType.QUOTE:
                block: str = block.strip("> ")
                quote_node: HTMLNode = LeafNode(block_type.value, block)
                wrapper_div.children.append(quote_node)

            case BlockType.UNORDERED_LIST:
                ul_node: HTMLNode = list_to_nodes(block, block_type.value)
                wrapper_div.children.append(ul_node)

            case BlockType.ORDERED_LIST:
                ol_node: HTMLNode = list_to_nodes(block, block_type.value)
                wrapper_div.children.append(ol_node)

            case _:
                other_node: HTMLNode = ParentNode(block_type.value, children=[])
                children: list[HTMLNode] = text_to_children(block)
                other_node.children = children
                wrapper_div.children.append(other_node)


    return wrapper_div

def list_to_nodes(block: str, tag: str) -> HTMLNode | ValueError:
    if block == "":
        raise ValueError("Empty list not allowed.")    
    list_node: ParentNode = ParentNode(tag, children=[])
    leaf_nodes: list[HTMLNode] = []
    list_items: list[str] = block.splitlines()
    for item in list_items:
        children: list[LeafNode] = text_to_children(item)
        if len(children) == 0:
            leaf_nodes.append(LeafNode("li", item))
        else:
            leaf_nodes.append(ParentNode("li", children))
    list_node.children = leaf_nodes
    return list_node





















