from block_to_block_type import block_to_block_type, BlockType
from htmlnode import HTMLNode
from leafnode import LeafNode
from markdown_to_blocks import markdown_to_blocks
from parentnode import ParentNode
from text_to_children import text_to_children

import re

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

#BUG: code blocks are stripping new lines. Fix using helper function defined below.
            case BlockType.CODE:
                block: str = block.strip("`")
                block: str = block.strip()
                code_node: LeafNode = LeafNode(block_type.value, block)
                wrapper_div.children.append(code_node)

#BUG: fix formatting on quotes. Needs to maintain new lines and remove ">" chars. Fix using helper function defined below.
#TODO: proposed feature: allow for formatting within blockquotes.
            case BlockType.QUOTE:
                block: str = block.strip("> ")
                quote_node: LeafNode = LeafNode(block_type.value, block)
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


def block_to_node(block: str) -> LeafNode | ValueError:
    pass


def list_to_nodes(block: str, tag: str) -> HTMLNode | ValueError:
    if block == "":
        raise ValueError("Empty list not allowed.")    
    
    list_node: ParentNode = ParentNode(tag, children=[])
    leaf_nodes: list[HTMLNode] = []
    list_items: list[str] = block.splitlines()
    

    for item in list_items:
        match tag:
            case "ol":
                item = re.sub(r"\d.\s", "", item)
            case "ul":
                item = re.sub(r"- ", "", item)
        
        children: list[LeafNode] = text_to_children(item)
    
        if len(children) == 0:
            leaf_nodes.append(LeafNode("li", item))
    
        else:
            leaf_nodes.append(ParentNode("li", children))
    
    list_node.children = leaf_nodes
    
    return list_node





















